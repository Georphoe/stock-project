import sqlite3 # 連接 SQLite 資料庫的標準庫。
import os # 處理檔案路徑與目錄。

abs_path = os.path.abspath(__file__)
# 取得 fetch_data.py 的絕對路徑
# __file__ 是 Python 內建變數，代表目前這支程式檔案的位置
BASE_DIR = os.path.dirname(os.path.dirname(abs_path))
# 取得專案根目錄 :/ STOCK-PROJECT
DATA_DIR = os.path.join(BASE_DIR, "data")
# 這一行「只會組路徑，不會生成資料夾」
os.makedirs(DATA_DIR, exist_ok=True)
# 生成這路徑, 如果有不存在的資料夾就生成他
# 建立一個叫 data 的資料夾（如果已存在 不會報錯）。用來放 stocks.db
# 結果：/project-root/data
db_path = os.path.join(DATA_DIR, "stocks.db")
# 組合完整資料庫檔案路徑
# 只是在「組路徑字串」
# 完全不會建立 stocks.db 檔案
conn = sqlite3.connect(db_path) # database connection
# 使用 Python 內建的 sqlite3 模組建立（或打開）一個到檔案 data/stocks.db 的 SQLite 連線（connection），並把連線物件存在變數 conn
# 如果 stocks.db 不存在
# SQLite 會自動建立 stocks.db 檔案
c = conn.cursor() # cursor
# 從 conn（資料庫連線）建立一個 cursor（游標）物件，並指派給變數 c。這個 cursor 用來執行 SQL 語句（SELECT、INSERT、CREATE TABLE 等）以及取得查詢結果。

c.executescript('''
-- ==============================
-- SQLite 註解說明
-- 1. 單行註解：用兩個減號 --，後面到行尾都是註解
-- 2. 多行註解：用 /* ... */，可以跨多行
-- 3. 注意：不要用 Python 的 # 註解在 SQL 字串裡，SQLite 會報錯
-- ==============================

-- 建立 stocks 表格（如果不存在）
CREATE TABLE IF NOT EXISTS stocks (
    id INTEGER PRIMARY KEY,      -- 主鍵，唯一且不可為 NULL
    symbol TEXT UNIQUE,          -- 股票代碼，唯一
    name TEXT                    -- 股票名稱
);

-- 建立 prices 表格（如果不存在）
CREATE TABLE IF NOT EXISTS prices (
    id INTEGER PRIMARY KEY,      -- 主鍵
    stock_id INTEGER,            -- 對應 stocks 表的 id
    date TEXT,                   -- 日期，格式可用 'YYYY-MM-DD'
    open REAL,                   -- 開盤價
    high REAL,                   -- 最高價
    low REAL,                    -- 最低價
    close REAL,                  -- 收盤價
    volume INTEGER,              -- 成交量
    UNIQUE(stock_id, date)       -- 同一股票同一天資料唯一
)
''')
# -- UNIQUE：約束（constraint），用來保證資料不重複

# -- 1️⃣ 單一欄位 UNIQUE
# -- 語法：column TYPE UNIQUE
# -- 意思：這個欄位的值在整張表中不能重複
# symbol TEXT UNIQUE

# -- 2️⃣ 多欄位（組合）UNIQUE
# -- 語法：UNIQUE(col1, col2)
# -- 意思：這「一組值」不能重複，但單一欄位可重複
# UNIQUE(stock_id, date)

conn.commit()
# conn.commit() 把 SQL 變更寫入檔案。

conn.close()
# 為什麼要 conn.close():
# 1. 釋放資料庫連線資源（連線數、記憶體、socket）
# 2. 避免連線佔住導致 "too many connections"
# 3. 防止 transaction / lock 沒結束，影響其他操作
# 4. 確保程式行為穩定、可預期
# ⚠️ 尤其在 long-running 程式（API / Server / CI）中一定要關
print("Database schema initialized.")