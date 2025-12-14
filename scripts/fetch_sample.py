# scripts/fetch_sample.py
import yfinance as yf # 從 Yahoo Finance 下載股價資料的套件（非官方 API，但簡單好用） 
import pandas as pd # 處理表格資料的主力庫。
import sqlite3 # 連接 SQLite 資料庫的標準庫。
import os # 處理檔案路徑與目錄。


abs_path = os.path.abspath(__file__)
# 取得 fetch_data.py 的絕對路徑
# __file__ 是 Python 內建變數，代表目前這支程式檔案的位置
BASE_DIR = os.path.dirname(os.path.dirname(abs_path))
# 取得專案根目錄 :/ STOCK-PROJECT
DATA_DIR = os.path.join(BASE_DIR, "data")
# 這一行「只會組路徑，不會生成資料夾」
os.mkdir(DATA_DIR, exist_ok=True)
# 在專案根目錄下生成 data 資料夾
# 結果：/project-root/data
db_path = os.path.join(DATA_DIR, "stocks.db")
# 組合完整資料庫檔案路徑
# 只是在「組路徑字串」
# 完全不會建立 stocks.db 檔案

os.makedirs("data", exist_ok=True)
# 在「目前執行程式時的工作目錄」底下建立 data
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


conn = sqlite3.connect("data/stocks.db") # database connection
# 使用 Python 內建的 sqlite3 模組建立（或打開）一個到檔案 data/stocks.db 的 SQLite 連線（connection），並把連線物件存在變數 conn
# 如果 stocks.db 不存在
# SQLite 會自動建立 stocks.db 檔案

c = conn.cursor() # cursor
# 從 conn（資料庫連線）建立一個 cursor（游標）物件，並指派給變數 c。這個 cursor 用來執行 SQL 語句（SELECT、INSERT、CREATE TABLE 等）以及取得查詢結果。

c.executescript('''
CREAT
''')

