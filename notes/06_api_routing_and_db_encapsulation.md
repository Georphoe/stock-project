🧭 06_api_routing重點筆記
📅 日期：2026-03-10
💡 主題：API 路由設計、DB 封裝、FastAPI 工程慣例

一、本週核心工作

設計簡單 REST 路由概念

封裝 DB 查詢函數 (query_prices)

建立 FastAPI endpoint （GET /stocks/{symbol}/prices）

梳理專案結構並理解 __init__.py 作用

更新專案，為 watchlist / 指標計算預留擴展

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
五、工程慣例重點

REST API route 命名直覺

DB 操作封裝集中管理

專案分層清楚，利於維護與測試

README.md 說明架構和執行流程

PowerShell 可快速初始化檔案（New-Item main.py -ItemType File）

六、本週學習重點（面試可用）

REST API 設計思維

DB 層封裝與責任分離

專案結構規劃

__init__.py 的角色

為未來 watchlist / 指標計算保留擴展空間