🧭 06_api_routing_and_db_encapsulation.md  
📅 日期：2026-03-10  
💡 主題：API 路由設計、DB 封裝、FastAPI 工程慣例、測試  

---

# 🚧 一、本週核心工作

- 設計簡單 REST 路由概念
- 封裝 DB 查詢函數 `query_prices`
- 建立 FastAPI endpoint  
  `GET /stocks/{symbol}/prices`
- 梳理專案結構並理解 `__init__.py` 作用
- 更新專案，為 watchlist / 指標計算預留擴展
- 撰寫簡單測試程式 `test_query.py` 確認 DB 與函數運作

---

# 🌐 二、API 路由設計要點

📌 **REST 設計理念**

- REST 直覺、學習成本低
- MVP 階段非常適合
- URL 應該表達「資源」

---

📌 **同步 vs 非同步**

- `sync` → 一般請求
- `async` → 適合大量 request / IO 操作

FastAPI 原生支援：

```python
async def endpoint():

📌 建議 API 設計（示意）

/api/stocks?symbol=XXX
→ 股票基本資訊

/api/stocks/{symbol}/prices?start=&end=
→ 區間價格查詢

/api/watchlist
→ 使用者股票清單（未來擴展）

/api/indicators
→ 技術指標計算（未來擴展）
📦 三、DB 封裝與工程思維

📌 為什麼要封裝 DB

將 API layer 與 Data layer 分離

優點：

易維護

易測試

邏輯清楚

📌 Single Responsibility Principle

不同檔案負責不同任務：

init_db.py
→ 建立資料表

ingest_data.py
→ 寫入資料

db.py
→ 查詢資料

📌 典型資料流程

API endpoint
      ↓
query_prices()
      ↓
Database
      ↓
Return JSON
📂 四、Python 專案結構與 __init__.py

📌 __init__.py 的作用

1️⃣ 將資料夾標記為 Python package

2️⃣ 允許 import：

from backend.db import query_prices

📌 建議專案結構

backend/
    __init__.py
    main.py          # FastAPI endpoint
    db.py            # DB 封裝函數

data/
    stocks.db

scripts/
    init_db.py
    ingest_data.py

test/
    test_query.py
🧪 五、測試程式 test_query.py

📌 範例程式

from backend.src.main import query_prices

try:
    data = query_prices("AAPL")

    print("success")
    print(data[0])

except Exception as e:
    print("Error:", e)
🎯 功能與工程觀念
1️⃣ 確認封裝函數運作正常

測試：

query_prices()
是否能正確連接 DB
2️⃣ 捕捉例外

使用：

try / except

避免程式崩潰。

可以快速定位問題：

DB 連線問題

SQL 錯誤

欄位錯誤

3️⃣ 簡單 Smoke Test

只印第一筆資料：

print(data[0])

就能確認功能是否正常。

📌 工程思維

每個模組完成後都應該：

先寫簡單測試

優點：

快速 debug

避免影響主程式

方便未來加入 CI/CD

🛠 六、建立 Python 檔案（PowerShell 指令）

在 Windows PowerShell 可以快速建立檔案：

New-Item main.py -ItemType File

📌 作用：

建立一個新的 Python 檔案

等同於：

右鍵 → New File → main.py

⚠️ 重要

這個指令：

不會執行 Python

不會啟動 API

只是建立檔案

建立檔案後才可以在 main.py 裡寫 FastAPI 程式。

🚀 七、啟動與測試 API
⚙️ 1. 啟動 FastAPI
# 進入專案目錄
cd backend

# 安裝依賴
pip install fastapi uvicorn

# 啟動 API
uvicorn main:app --reload

📌 指令解析

uvicorn
→ 啟動 Web Server

main
→ main.py

app
→ app = FastAPI()

--reload
→ 程式碼變更自動重啟

📌 API 會啟動在：

http://127.0.0.1:8000
🌐 2. 測試 API

使用瀏覽器或 API 工具：

GET http://127.0.0.1:8000/stocks/AAPL/prices

成功會返回：

JSON 格式資料
📑 3. Swagger UI（FastAPI 自動生成）

FastAPI 會自動生成 API 文件：

http://127.0.0.1:8000/docs

可以：

查看 API

發送 request

檢查 response

🧪 4. API 測試策略

測試順序：

1️⃣ 先測 DB function
2️⃣ 再測 API endpoint

未來可使用：

pytest
httpx

進行自動化測試。

⚙️ 八、uvicorn 與 ASGI Server
🧠 uvicorn 是什麼

uvicorn 是一個 ASGI Web Server

它的工作是：

1️⃣ 啟動 Web server
2️⃣ 接收 HTTP request
3️⃣ 呼叫 FastAPI
4️⃣ 回傳 response

📌 資料流程

Browser
   ↓
Uvicorn
   ↓
FastAPI
   ↓
Python function
   ↓
Database
   ↓
Response JSON
🧠 ASGI Server 是什麼

ASGI =

Asynchronous Server Gateway Interface

它是一個 Web Server 與 Python Web Framework 之間的標準介面。

📌 架構

Browser
   ↓
HTTP Request
   ↓
ASGI Server (uvicorn)
   ↓
FastAPI
   ↓
Python 程式邏輯
   ↓
Response

📌 ASGI 的特點

支援 async

高併發

支援 WebSocket

適合高效能 API

🧠 為什麼 FastAPI 使用 ASGI

FastAPI 是設計給 非同步架構 的 framework。

因此需要：

ASGI Server

而不是舊的：

WSGI Server

📌 常見 ASGI server：

uvicorn
hypercorn
daphne

其中 uvicorn 最常見。