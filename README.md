# Bar API

REST API and terminal application for managing a bar's categories, products, tables and orders, built with FastAPI, PostgreSQL and explicit SQL queries.

## Tech Stack

- **Python 3.11+** - application language
- **FastAPI** - web framework for building the API
- **psycopg2** - PostgreSQL driver with explicit SQL queries
- **PostgreSQL 15** - relational database
- **Docker / Docker Compose** - database container
- **python-dotenv** - loads environment variables from `.env`

## Project Structure

```text
project-bar/
|-- docker-compose.yml       # spins up the PostgreSQL container
|-- .env                     # database credentials (do not commit)
|-- .env.example             # template for teammates
|-- requirements.txt         # Python dependencies
|-- sql/
|   |-- init.sql             # creates all tables on first run
|-- app/
    |-- cli.py               # terminal menu for CRUD operations
    |-- database.py          # PostgreSQL connection helpers
    |-- main.py              # API entry point
    |-- queries/             # explicit SQL queries by entity
    |-- routers/             # FastAPI routes
    |-- schemas.py           # request/response validation
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
python -m venv venv
venv\Scripts\activate       # Windows
# source venv/bin/activate  # Linux / Mac

pip install -r requirements.txt
```

### 4. Run the API

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`.

### 5. Run in terminal

```bash
python -m app.cli
```

This opens a text menu for CRUD operations without needing `uvicorn`.

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

The product queries already use `LEFT JOIN` to return the category description together with each product.

### Tables

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/mesas/` | List all tables |
| GET | `/mesas/{id}` | Get table by ID |
| POST | `/mesas/` | Create a new table |
| PUT | `/mesas/{id}` | Update a table |
| DELETE | `/mesas/{id}` | Delete a table |

### Orders

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/pedidos/` | List all orders |
| GET | `/pedidos/{id}` | Get order by ID |
| POST | `/pedidos/` | Create a new order |
| PUT | `/pedidos/{id}` | Update an order |
| DELETE | `/pedidos/{id}` | Delete an order |

### Example requests

**Create a category**

```bash
curl -X POST http://localhost:8000/categorias/ \
  -H "Content-Type: application/json" \
  -d "{\"descricao\": \"Bebidas\"}"
```

**Create a product linked to category 1**

```bash
curl -X POST http://localhost:8000/produtos/ \
  -H "Content-Type: application/json" \
  -d "{\"nome\": \"Cerveja Heineken\", \"preco_unitario\": 9.50, \"fk_categoria\": 1}"
```

**List all products**

```bash
curl http://localhost:8000/produtos/
```

## Verifying data in the database

Connect directly to PostgreSQL inside the Docker container:

```bash
docker exec -it bar_postgres psql -U bar_user -d bar_db
```

Then run SQL queries:

```sql
SELECT * FROM categoria;
SELECT * FROM produto;

SELECT
    p.id_produto,
    p.nome,
    p.preco_unitario,
    c.descricao AS categoria
FROM produto p
LEFT JOIN categoria c ON c.id_categoria = p.fk_categoria;
```

## Docker commands reference

```bash
docker compose up -d
docker compose stop
docker compose down
docker compose down -v
```

## Using pgAdmin instead of Docker

If your team already has PostgreSQL installed locally with pgAdmin, skip Docker and update `.env` with your local credentials:

```env
DB_HOST=localhost
DB_PORT=5432
DB_USER=postgres
DB_PASSWORD=your_password
DB_NAME=bar_db
```

Then run the SQL script manually in pgAdmin:

1. Open pgAdmin and select your database
2. Click **Query Tool**
3. Paste the contents of `sql/init.sql`
4. Execute the script to create all tables

The API and terminal mode work the same way regardless of whether you use Docker or pgAdmin.
