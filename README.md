# SQL + Python Stock Analytics Pipeline

This project builds an ETL pipeline using Python and PostgreSQL to ingest, clean, store, and analyze stock market data for multiple companies.

## Tech Stack
- Python
- pandas
- PostgreSQL
- SQLAlchemy
- matplotlib

## Project Goals
- Clean and transform raw stock data
- Store normalized data in PostgreSQL
- Analyze returns, volatility, and trading volume using SQL
- Visualize trends with Python

## Tables
- companies
- daily_prices
- earnings

## How to Run
1. Run `extract.py`
2. Run `transform.py`
3. Run `load.py`
4. Run SQL queries from `analysis_queries.sql`

## Example Analyses
- 7-day moving average
- highest-volume trading days
- stock return comparisons
- volatility rankings