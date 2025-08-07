# Workout API 🏋️‍♂️

API para gerenciamento de atletas, categorias e centros de treinamento. 
Desenvolvido com **FastAPI**, utilizando **Alembic** para versionamento de banco de dados, e **PostgreSQL** como banco de dados via Docker.

## 🧱 Estrutura do Projeto

workout_api/
├── atleta/
├── categorias/
├── centro_treinamento/
├── configs/
├── contrib/
├── main.py
├── routers.py
├── alembic.ini
├── docker-compose.yml
├── Makefile
├── requirements.txt



## 🚀 Tecnologias e Ferramentas

- [FastAPI](https://fastapi.tiangolo.com/)
- [Alembic](https://alembic.sqlalchemy.org/)
- [PostgreSQL](https://www.postgresql.org/) via Docker Compose
- [Makefile](https://www.gnu.org/software/make/) para comandos úteis
- Ambiente virtual com `venv`

## 🐳 Subindo o Projeto com Docker Compose

```bash
# Subir o banco de dados PostgreSQL
make run-docker

O banco ficará disponível em:

    host: localhost
    porta: 5432
    usuário: workout
    senha: workout
    banco: workout


🐍 Ambiente Virtual
# Criar ambiente virtual
python -m venv .venv

# Ativar o ambiente (Linux/macOS)
source .venv/bin/activate

# Ativar o ambiente (Windows)
.venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt



🔄 Alembic - Migrations

# Criar nova migration
make create-migrations d="init"
alembic revision --autogenerate -m "sua_mensagem"
# Aplicar migrations
alembic upgrade head


📂 Estrutura das Pastas

    atleta/, categorias/, centro_treinamento/: módulos principais da API.
    configs/: configurações gerais (banco de dados, variáveis, etc).
    contrib/: utilitários, helpers ou validações customizadas.
    alembic/: configurações de migrations do banco.


✅ Requisitos

    Python 3.10+
    Docker e Docker Compose
    Make