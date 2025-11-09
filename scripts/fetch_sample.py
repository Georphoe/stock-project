# scripts/fetch_sample.py
import yfinance as yf # 從 Yahoo Finance 下載股價資料的套件（非官方 API，但簡單好用） 
import pandas as pd # 處理表格資料的主力庫。
import sqlite3 # 連接 SQLite 資料庫的標準庫。
import os # 處理檔案路徑與目錄。

os.makedirs("data", exist_ok=True)
# 建立一個叫 data 的資料夾（如果已存在就不會報錯）。用來放 stocks.db

symbol = "AAPL" # 直觀表示「證券代號 / ticker symbol」
df = yf.download( symbol, start = "2020-01-01", end = "2025-01-01", progress = False) 
# 回傳的是一個 Pandas DataFrame, （也就是一個「表格型」資料結構）
# progress=False：停止顯示下載進度條（若在腳本或自動化環境中，通常把它設為 False 以避免 CLI 進度列污染日誌）。
# yfinance 回傳的 index 預設常是 DatetimeIndex（日期為索引）[ 是Time Series（時間序列）就是「一組依照時間順序排列的數據」 ]
print(df.head())

df = df.reset_index() # date becomes a column
# 很多情況你要把資料寫入關聯式資料庫（如 SQLite）或做欄位命名/選取時，把日期當成欄位比當成 index 更方便（SQL table 都是以欄位為單位）
df = df.rename(columns={"Date":"date", "Open":"open", "High":"high", "Low":"low", "Close":"close", "Volume":"volume"})
# 重新命名 DataFrame 的欄位: 一致性 PEP8, 可讀性：date、open 等小寫欄位在 SQL 或 JSON 中更常見


conn = sqlite3.connect("data/stocks.db")