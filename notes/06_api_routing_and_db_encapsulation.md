🧭 06_api_routing_and_db_encapsulation.md
📅 日期：2026-03-10
💡 主題：API 路由設計、DB 封裝、FastAPI 工程慣例、測試

一、本週核心工作

設計簡單 REST 路由概念

封裝 DB 查詢函數 (query_prices)

建立 FastAPI endpoint （GET /stocks/{symbol}/prices）

梳理專案結構並理解 __init__.py 作用

更新專案，為 watchlist / 指標計算預留擴展

撰寫簡單測試程式 test_query.py 確認 DB 與函數運作

二、API 路由設計要點

REST 直覺、學習成本低，MVP 推薦使用

路由設計應清楚表達資源與操作

同步 vs 非同步：async 適合大量或即時請求

建議路由概念（示意，不需全部實作）：

/api/stocks?symbol=XXX → 股票基本資訊

/api/stocks/{symbol}/prices?start=&end= → 區間價格查詢

/api/watchlist、/api/indicators → 未來擴展

三、DB 封裝與工程思維

封裝 DB 查詢讓 API 層與資料層分離

優點：清楚責任分層、易測試、易維護

Single Responsibility Principle：init_db.py（建表） vs ingest_data.py（寫資料）

四、Python 專案結構與 init.py

__init__.py：

將資料夾標記為 package

可初始化或暴露函數給上層使用

建議結構：

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
五、測試程式 test_query.py

範例程式：

from backend.src.main import query_prices

try:
    data = query_prices("AAPL")
    print('success')
    print(data[0])
except Exception as e:
    print("Error:", e)
功能與工程觀念

1️⃣ 確認封裝函數運作正常

測試 query_prices 是否能正確連 DB 並回傳資料

2️⃣ 捕捉例外

用 try/except 避免程式崩潰

可以快速定位問題（DB 連線、SQL 語法、欄位錯誤）

3️⃣ 簡單可讀

只印第一筆資料即可確認結果

適合快速 smoke test

📌 工程思維

每個模組封裝完成後都應有簡單測試

測試與主程式分層，避免測試程式干擾主程式運行

這也是後續導入 pytest 或 CI/CD 的基礎

六、工程慣例重點

REST API route 命名直覺

DB 操作封裝集中管理

專案分層清楚，利於維護與測試

README.md 說明架構和執行流程

PowerShell 可快速初始化檔案（New-Item main.py -ItemType File）

七、本週學習重點（面試可用）

REST API 設計思維

DB 層封裝與責任分離

專案結構規劃

__init__.py 的角色

撰寫簡單測試程式確認函數運作

為未來 watchlist / 指標計算保留擴展空間