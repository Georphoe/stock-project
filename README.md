# Stock Data Ingestion & API Project

A full-stack project that fetches historical stock price data from **Yahoo Finance**, stores it in a local **SQLite** database, and exposes a **FastAPI REST API** for querying and analyzing stock data.

## 🚧 Status
This project is currently under active development (MVP stage). Core backend functionality (data ingestion + API) is implemented, and frontend visualization is in progress.

This project is designed as a hands-on introduction to:

- Data ingestion (fetching external data)
- Relational database schema design
- Basic *upsert* logic for time-series data
- REST API development with FastAPI

---

## ✨ Features (MVP)

- Fetch historical stock price data (OHLCV) using `yfinance`
- Store stock metadata and time-series data in SQLite
- Expose a FastAPI REST API for querying stock prices
- Support filtering by date range via API endpoints
- Prevent duplicate records using database constraints

## 🛠️ Developer Experience

- Interactive API docs via Swagger UI
- Simple, reproducible local setup (no external services required)

---

## Tech Stack

* Python 3
* SQLite
* pandas
* yfinance
* FastAPI
* Uvicorn

---

## Project Structure

```
stock-project/
│
├─ backend/
│  └─ src/
│      ├─ __init__.py   # 讓 src 成為 package
│      └─ main.py       # FastAPI REST API
│
├─ scripts/
│  ├─ init_db.py        # Initialize database schema
│  └─ fetch_sample.py   # Fetch stock data from Yahoo Finance
│
├─ data/
│  └─ stocks.db         # SQLite database
│
├─ test/
│  └─ test_query.py     # Simple function test
│
├─ README.md
└─ requirements.txt
```

---

## Database Schema (Simplified)

### stocks

| Column | Description           |
| ------ | --------------------- |
| id     | Primary key           |
| symbol | Stock ticker (unique) |
| name   | Stock name            |

### prices

| Column   | Description                         |
| -------- | ----------------------------------- |
| id       | Primary key                         |
| stock_id | Foreign key referencing `stocks.id` |
| date     | Trading date                        |
| open     | Open price                          |
| high     | High price                          |
| low      | Low price                           |
| close    | Close price                         |
| volume   | Trading volume                      |

**Constraint**:

* `UNIQUE(stock_id, date)` ensures one price record per stock per day

---

## How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Initialize database schema (run once)

```bash
python scripts/init_db.py
```

This will create the SQLite database file:

```text
data/stocks.db
```

### 3. Fetch sample stock data

```bash
python scripts/fetch_sample.py
```

Example output:

```text
Saved 1258 rows to data/stocks.db
```

### 4. Start the FastAPI server
```bash
# Navigate to project root
cd backend

# Install FastAPI and Uvicorn if not installed
pip install fastapi uvicorn

# Start API server
uvicorn main:app --reload
```
--reload → automatically reload on code changes

API available at: http://127.0.0.1:8000

---

REST API Endpoints
1️⃣ Root Endpoint

Check server is running:

GET /

Example response:

{"message": "Stock API running"}
2️⃣ Get Stock Prices
GET /api/stocks/{symbol}/prices

Query parameters (optional):

start=YYYY-MM-DD → start date

end=YYYY-MM-DD → end date

Example:

GET http://127.0.0.1:8000/api/stocks/AAPL/prices?start=2024-01-01&end=2024-12-31

Example JSON response:

[
  {"date": "2026-03-06", "open": 100, "high": 105, "low": 98, "close": 102, "volume": 1500000},
  {"date": "2026-03-05", "open": 102, "high": 106, "low": 101, "close": 104, "volume": 1200000}
]
3️⃣ Interactive API Docs (Swagger UI)

FastAPI auto-generates docs:

http://127.0.0.1:8000/docs

You can test API requests directly in the browser.

---

Testing DB Functions

Before testing the API, you can test DB query functions:

python test/test_query.py

Purpose:

Confirm query_prices connects to DB correctly

Ensure JSON output format

Quick smoke test before API deployment

---

## Notes

* This project currently uses SQLite for simplicity and ease of setup.
* Designed for learning, experimentation, and local development.
* The architecture can be extended to support more robust backends.

---

## Future Improvements

* Support multiple stock symbols
* Add adjusted close price
* Add data visualization
* Migrate to PostgreSQL
* Build a REST API

---

## Recommended Usage Flow

Follow this sequence whenever you set up the project in a new environment:

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Initialize the database (run once)
python scripts/init_db.py

# 3. Fetch stock data
python scripts/fetch_sample.py
```
