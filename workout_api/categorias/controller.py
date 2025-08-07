from uuid import uuid4

from fastapi import APIRouter, Body, HTTPException, Query, status
from fastapi_pagination import Page, paginate
from pydantic import UUID4
from sqlalchemy import and_
from sqlalchemy.exc import IntegrityError
from sqlalchemy.future import select
from workout_api.categorias.models import CategoriaModel
from workout_api.categorias.schemas import CategoriaIn, CategoriaOut
from workout_api.contrib.dependencies import DatabaseDependency

router = APIRouter()


@router.post(
    "/",
    summary="Criar uma nova categoria",
    status_code=status.HTTP_201_CREATED,
    response_model=CategoriaOut,
    tags=["Categoria"],
)
async def post(
    db_session: DatabaseDependency, categoria_in: CategoriaIn = Body(...)
) -> CategoriaOut:
    categoria_out = CategoriaOut(id=uuid4(), **categoria_in.model_dump())
    categoria_model = CategoriaModel(**categoria_out.model_dump())

    try:
        db_session.add(categoria_model)
        await db_session.commit()
    except IntegrityError:
        await db_session.rollback()
        raise HTTPException(
            status_code=status.HTTP_303_SEE_OTHER,
            detail=f"Já existe uma categoria cadastrada com o nome: {categoria_model.nome}",
        )
    except Exception:
        await db_session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Erro ao criar categoria",
        )

    return categoria_out


@router.get(
    "/",
    summary="Consultar todas as categorias",
    status_code=status.HTTP_200_OK,
    response_model=Page[CategoriaOut],
    tags=["Categoria"],
)
async def get(
    db_session: DatabaseDependency, nome: str = Query(default=None)
) -> Page[CategoriaOut]:
    query_stmt = select(CategoriaModel)
    if nome:
        query_stmt = query_stmt.filter(CategoriaModel.nome.ilike(f"%{nome}%"))

    result = (await db_session.execute(query_stmt)).scalars().all()

    return paginate([CategoriaOut.model_validate(c) for c in result])


@router.get(
    "/{id}",
    summary="Consultar uma categoria pelo id",
    status_code=status.HTTP_200_OK,
    response_model=CategoriaOut,
    tags=["Categoria"],
)
async def query(id: UUID4, db_session: DatabaseDependency) -> CategoriaOut:
    categoria = (
        (await db_session.execute(select(CategoriaModel).filter_by(id=id)))
        .scalars()
        .first()
    )

    if not categoria:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Categoria não encontrada"
        )

    return CategoriaOut.model_validate(categoria)
