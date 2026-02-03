 FastAPI ML API

API backend desenvolvida com FastAPI, SQLAlchemy e MySQL, seguindo boas práticas de arquitetura para aplicações reais de mercado.

Tecnologias
- Python 3.11+
- FastAPI
- SQLAlchemy
- MySQL
- Uvicorn
- Pydantic
- Docker (em breve)

 Arquitetura
bash
app/
 ├── main.py
 ├── database/
 │   ├── connection.py
 │   └── base.py
 ├── models/
 │   ├── user.py
 │   └── user_profile.py
⚙️ Funcionalidades
Health check da API

Health check de conexão com banco

Conexão segura com MySQL via SQLAlchemy

Estrutura preparada para CRUD e Machine Learning

▶️ Como executar o projeto
1. Criar ambiente virtual
bash
Copiar código
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
2. Instalar dependências
bash
Copiar código
pip install -r requirements.txt
3. Configurar variáveis de ambiente
Crie um arquivo .env:

env
Copiar código
DB_HOST=localhost
DB_PORT=3306
DB_NAME=ml_api
DB_USER=root
DB_PASSWORD=senha
4. Rodar a aplicação
bash
Copiar código
uvicorn app.main:app --reload
Acesse:

http://127.0.0.1:8000/health

http://127.0.0.1:8000/docs

📈 Próximos passos
CRUD de usuários

Autenticação JWT

Deploy em cloud

Integração com modelos de Machine Learning

👨‍💻 Desenvolvido por Christian Binda
