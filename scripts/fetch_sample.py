# scripts/fetch_sample.py
import yfinance as yf # 從 Yahoo Finance 下載股價資料的套件（非官方 API，但簡單好用） 
import pandas as pd # 處理表格資料的主力庫。
import sqlite3 # 連接 SQLite 資料庫的標準庫。
import os # 處理檔案路徑與目錄。

os.makedirs("data", exist_ok=True)
# 建立一個叫 data 的資料夾（如果已存在就不會報錯）。用來放 stocks.db

symbol = "AAPL"
df = yf.download( symbol, start = "2020-01-01", end = "2025-01-01", progress = False)
print(df.head())