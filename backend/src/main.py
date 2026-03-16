from fastapi import FastAPI   # 從 fastapi module 拿 FastAPI class, 用來建立 API server，支援 HTTP GET/POST 等方法。
import sqlite3                # 載入 sqlite module, Python 內建模組，用來操作 SQLite 資料庫（輕量級 DB，不需額外安裝服務）。
import pandas as pd           # 載入 pandas 並命名 pd, 強大的資料處理工具，方便把 SQL query 結果轉成 DataFrame，再轉成 JSON。
from pathlib import Path      # 載入 pathlib module, Python 內建模組，用來處理檔案路徑。 pathlib 是 比較新的 Python 路徑工具 比起 os.path，程式更乾淨、更安全。

# 建立一個 FastAPI 實例，它是整個 web server 的入口，負責接收 HTTP 請求、回傳 response。
# 可以加 metadata（title, version）方便 Swagger UI 自動生成 API 文件：
app = FastAPI(title="Stock API", version="0.1") 

BASE_DIR = Path(__file__).resolve().parent.parent.parent # resolve() 把相對路徑轉成絕對路徑。 parent.parent 跳兩層找到專案根目錄。
db_path = BASE_DIR / "data" / "stocks.db" # pathlib.Path 這個 class 提供的功能, 當左邊是 Path 物件時，/ 不再代表除法，而代表 拼接路徑。 operator overloading


# 封裝 DB 操作，不要把 SQL 寫在 API route 裡。
# 每次 query 都新建連線，避免長時間佔用 DB。
# 每次建立連線有微小開銷，若非常頻繁 query 可以考慮 connection pool。
def query_prices(symbol, start = None, end = None):
    conn = sqlite3.connect(db_path)
    sql = """
    SELECT p.date, p.open, p.high, p.low, p.close, p.volume
    FROM prices p JOIN stocks s ON p.stock_id = s.id
    WHERE s.symbol = ?
    """

    params = [symbol] # SQLite 需要 params 列表傳入 pd.read_sql_query 或 cursor。

    if start: # 如果使用者提供 start 或 end 日期，就加上條件過濾。
        sql += " AND p.date >= ?" 
        params.append(start) # params.append(...) 確保 query 的 ? 有對應的值。
    if end:
        sql += " AND p.date <= ?"
        params.append(end)
    
    df = pd.read_sql_query(sql, conn, params= params) # pandas 可以直接讀 SQL query，返回一個 DataFrame。

    conn.close() # 用完就關，避免長時間佔用。

    return df.to_dict(orient="records") # 轉成 JSON 格式。 orient="records" 表示轉成 list of dicts。 API 回傳 JSON 用
    # list 裡面每一個元素是 row 的 dict
    # [
    # {"date": "2026-03-06", "open": 100, "close": 105},
    # {"date": "2026-03-05", "open": 102, "close": 103}
    # ]

# API endpoint: 取得某支股票的歷史價格
@app.get("/api/stocks/{symbol}/prices")
def get_prices(symbol: str, start: str = None, end: str = None):
    return query_prices(symbol.upper(), start, end) #  symbol.upper() 確保股票代碼統一為大寫

# API endpoint: 測試 API 是否運行
@app.get("/")
def root():
    return {"message": "Stock API running"}   