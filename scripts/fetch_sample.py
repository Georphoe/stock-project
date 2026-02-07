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
os.makedirs(DATA_DIR, exist_ok=True)
# 生成這路徑, 如果有不存在的資料夾就生成他
# 建立一個叫 data 的資料夾（如果已存在 不會報錯）。用來放 stocks.db
# 結果：/project-root/data
db_path = os.path.join(DATA_DIR, "stocks.db")
# 組合完整資料庫檔案路徑
# 只是在「組路徑字串」
# 完全不會建立 stocks.db 檔案


symbol = "AAPL" # 直觀表示「證券代號 / ticker symbol」
df = yf.download( symbol, start = "2020-01-01", end = "2025-01-01", progress = False) 
# 回傳的是一個 Pandas DataFrame, （也就是一個「表格型」資料結構）
# progress=False：停止顯示下載進度條（若在腳本或自動化環境中，通常把它設為 False 以避免 CLI 進度列污染日誌）。
# yfinance 回傳的 index 預設常是 DatetimeIndex（日期為索引）[ 是Time Series（時間序列）就是「一組依照時間順序排列的數據」 ]
print(df.head())

# 修正：如果回傳的是多層欄位，先把它壓平
# 下載後的 df 欄位長這樣：[('Close', 'AAPL'), ('Open', 'AAPL')...] 需要壓平
if isinstance(df.columns, pd.MultiIndex):
    df.columns = df.columns.get_level_values(0)

df = df.reset_index() # date becomes a column
# 很多情況你要把資料寫入關聯式資料庫（如 SQLite）或做欄位命名/選取時，把日期當成欄位比當成 index 更方便（SQL table 都是以欄位為單位）
df = df.rename(columns={"Date":"date", "Open":"open", "High":"high", "Low":"low", "Close":"close", "Volume":"volume"})
# 重新命名 DataFrame 的欄位: 一致性 PEP8, 可讀性：date、open 等小寫欄位在 SQL 或 JSON 中更常見


conn = sqlite3.connect(db_path) # database connection
# 使用 Python 內建的 sqlite3 模組建立（或打開）一個到檔案 data/stocks.db 的 SQLite 連線（connection），並把連線物件存在變數 conn
# 如果 stocks.db 不存在
# SQLite 會自動建立 stocks.db 檔案

c = conn.cursor() # cursor
# 從 conn（資料庫連線）建立一個 cursor（游標）物件，並指派給變數 c。這個 cursor 用來執行 SQL 語句（SELECT、INSERT、CREATE TABLE 等）以及取得查詢結果。


# 嘗試把一支股票加入 stocks 表；如果這支股票已經存在（symbol 重複），就什麼都不做、也不報錯。
# 使用 cursor 執行一條 SQL 語句（支援參數化，安全防 SQL Injection）
c.execute(
    "INSERT OR IGNORE INTO stocks(symbol, name) VALUES (?, ?)", 
    (symbol, symbol)
)
# "INSERT OR IGNORE INTO stocks(symbol, name) VALUES (?, ?)",
# INSERT：新增一筆資料到 stocks 表
# OR IGNORE：如果違反約束（例如 UNIQUE(symbol) 重複），就忽略這次插入，不報錯
# INTO stocks(symbol, name)：指定要插入的表與欄位
# VALUES (?, ?)：使用參數佔位符（?），實際值由下面的 tuple 傳入
conn.commit()

# 用股票代碼 symbol 去 stocks 表，查出它對應的 id（主鍵）
c.execute("SELECT id FROM stocks WHERE symbol=?", (symbol,))
# 為什麼一定要 (symbol,) 而不是 symbol？
# 因為 execute() 的規則是： execute(sql, parameters), 第二個參數 必須是「可迭代物件」

# 從資料庫查詢結果中，拿出第一筆資料的第一個欄位，存成 stock_id
# 回傳型態是 tuple, 因為我們只選了 id 所以回傳 (id, )
result = c.fetchone()
if result:
    stock_id = result[0]
else:
    # 處理找不到 id 的情況 (雖然 INSERT OR IGNORE 後通常會有，但這是好習慣)
    raise ValueError(f"Cannot find stock id for symbol: {symbol}")


# 把 DataFrame 的選定欄位寫進 SQLite 的一個暫存 table temp_prices。if_exists="replace" 表示若 temp_prices 已存在就先刪掉再建立。
df[["date", "open", "high", "low", "close", "volume"]].to_sql("temp_prices", conn, if_exists="replace", index=False)
# 指定資料庫內的資料表名稱為 'temp_prices'
#  指定要寫入的資料庫連線物件（sqlite3 連線）
#  若表格已存在則「先刪除再重建」，確保裡面只有本次寫入的新資料
#  不要將 Pandas 自動生成的 0, 1, 2... 索引列存入資料庫

c.execute("""
INSERT OR REPLACE INTO prices(stock_id, date, open, high, low, close, volume)
SELECT ?, date, open, high, low, close, volume FROM temp_prices
""", (stock_id,))
conn.commit()
# 這段會把 temp_prices 的資料插到 prices：
# INSERT OR REPLACE：若遇到 UNIQUE(stock_id, date) 衝突（同一天已存在資料），
# REPLACE 會把舊 row 刪掉再插入新的（等同於 update）。這是實現簡單 upsert 的方式。
# SELECT ?, date, ... FROM temp_prices：第一個 ? 被替換成 stock_id，把所有資料加上這個 stock_id 再寫入。

# --- Good Practice: 過河拆橋，刪除暫存表 ---
c.execute("DROP TABLE IF EXISTS temp_prices")
print("temp_prices table deleted")

conn.close()
# 為什麼要 conn.close():
# 1. 釋放資料庫連線資源（連線數、記憶體、socket）
# 2. 避免連線佔住導致 "too many connections"
# 3. 防止 transaction / lock 沒結束，影響其他操作
# 4. 確保程式行為穩定、可預期
# ⚠️ 尤其在 long-running 程式（API / Server / CI）中一定要關
print("Saved", len(df), "rows to data/stocks.db")
