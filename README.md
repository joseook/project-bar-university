# Bar API

REST API for managing a bar's categories and products, built with FastAPI and PostgreSQL.

## Tech Stack

- **Python 3.11+** — application language
- **FastAPI** — web framework for building the API
- **SQLAlchemy** — ORM to interact with the database
- **PostgreSQL 15** — relational database
- **Docker / Docker Compose** — database container
- **python-dotenv** — loads environment variables from `.env`

## Project Structure

```
project-bar/
├── docker-compose.yml       # spins up the PostgreSQL container
├── .env                     # database credentials (do not commit)
├── .env.example             # template for teammates
├── requirements.txt         # Python dependencies
├── sql/
│   └── init.sql             # creates all tables on first run
└── app/
    ├── main.py              # API entry point
    ├── database.py          # database connection
    ├── models.py            # table definitions (SQLAlchemy)
    ├── schemas.py           # request/response validation (Pydantic)
    └── routers/
        ├── categoria.py     # category endpoints
        └── produto.py       # product endpoints
```

## Getting Started

### Prerequisites

- [Docker](https://docs.docker.com/get-docker/) and Docker Compose installed
- Python 3.11 or higher

### 1. Configure environment variables

Copy the example file and fill in your credentials:

```bash
cp .env.example .env
```

The default `.env` values work out of the box with Docker:

```env
DB_HOST=localhost
DB_PORT=5432
DB_USER=bar_user
DB_PASSWORD=bar123
DB_NAME=bar_db
```

### 2. Start the database

```bash
docker compose up -d
```

On the first run, Docker will:
- Download the PostgreSQL 15 image
- Create the database and user
- Execute `sql/init.sql`, which creates all tables automatically

### 3. Set up Python environment

```bash
python3 -m venv venv
source venv/bin/activate      # Linux / Mac
# venv\Scripts\activate       # Windows

pip install -r requirements.txt
```

### 4. Run the API

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`.

---

## API Endpoints

Interactive documentation (Swagger UI) is available at `http://localhost:8000/docs`.

### Categories

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/categorias/` | List all categories |
| GET | `/categorias/{id}` | Get category by ID |
| POST | `/categorias/` | Create a new category |
| PUT | `/categorias/{id}` | Update a category |
| DELETE | `/categorias/{id}` | Delete a category |

### Products

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/produtos/` | List all products |
| GET | `/produtos/{id}` | Get product by ID |
| POST | `/produtos/` | Create a new product |
| PUT | `/produtos/{id}` | Update a product |
| DELETE | `/produtos/{id}` | Delete a product |

### Example requests

**Create a category:**

```bash
curl -X POST http://localhost:8000/categorias/ \
  -H "Content-Type: application/json" \
  -d '{"descricao": "Bebidas"}'
```

**Create a product linked to category 1:**

```bash
curl -X POST http://localhost:8000/produtos/ \
  -H "Content-Type: application/json" \
  -d '{"nome": "Cerveja Heineken", "preco_unitario": 9.50, "fk_categoria": 1}'
```

**List all products:**

```bash
curl http://localhost:8000/produtos/
```

---

## Verifying data in the database

Connect directly to PostgreSQL inside the Docker container:

```bash
docker exec -it bar_postgres psql -U bar_user -d bar_db
```

Then run SQL queries:

```sql
SELECT * FROM categoria;
SELECT * FROM produto;

-- Exit
\q
```

---

## Docker commands reference

```bash
# Start the database in background
docker compose up -d

# Stop without removing data
docker compose stop

# Stop and remove containers (data is preserved in volume)
docker compose down

# Stop, remove containers AND delete all data
docker compose down -v
```

---

## Using pgAdmin instead of Docker

If your team already has PostgreSQL installed locally with pgAdmin, skip Docker and update `.env` with your local credentials:

```env
DB_HOST=localhost
DB_PORT=5432
DB_USER=postgres          # your pgAdmin user
DB_PASSWORD=your_password
DB_NAME=bar_db            # database name created in pgAdmin
```

Then run the SQL script manually in pgAdmin:
1. Open pgAdmin and select your database
2. Click **Query Tool**
3. Paste the contents of `sql/init.sql`
4. Execute — all tables will be created

The Python API works the same way regardless of whether you use Docker or pgAdmin.

---

## Database Schema

```
CATEGORIA (1) ──── (N) PRODUTO
MESA      (1) ──── (N) PEDIDO
PEDIDO    (N) ──── (N) PRODUTO  via ITENS_PEDIDO
```

| Table | Description |
|-------|-------------|
| `categoria` | Product categories (e.g. Drinks, Snacks) |
| `produto` | Products with price and category |
| `mesa` | Bar tables with availability status |
| `pedido` | Customer orders linked to a table |
| `itens_pedido` | Junction table: products per order with quantity |
