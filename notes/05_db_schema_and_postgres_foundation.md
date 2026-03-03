🧭 05_db_schema_and_postgres_foundation.md
📅 日期：2025-02-15
💡 主題：Database Schema 設計思維、PostgreSQL DDL、Time-Series 概念、Partitioning、專案結構重構

一、本週目標與進度

本週重點從「資料寫入流程」往前推進一層：

在任何資料進來之前，先把「容器的形狀」決定好。

完成內容包含：

理解並撰寫 PostgreSQL DDL

設計正式版 DB Schema

學習 time-series 資料模型

初步理解 partitioning 的概念

新增 scripts/init_db.py（專責 schema 初始化）

重構專案結構（拆分責任）

更新 README.md 說明架構

規劃未來支援「可輸入股票代碼」

二、DB Schema 思維：為什麼要先設計容器？
1️⃣ 什麼是 Schema？

Schema 就是：

資料庫中「表的形狀與規則」

包含：

Table 結構

欄位型別

PRIMARY KEY

UNIQUE constraint

Foreign Key

Index

📌 工程觀念

Schema 是「資料的合約（contract）」。

一旦 schema 設計好：

API 會依賴它

資料 pipeline 會依賴它

查詢效能會依賴它

Schema 設計錯誤 → 後面全部都痛苦。

三、PostgreSQL DDL 是什麼？
1️⃣ DDL = Data Definition Language

SQL 分三類：

類型	用途
DDL	定義資料結構
DML	操作資料
DQL	查詢資料

DDL 包含：

CREATE TABLE
DROP TABLE
ALTER TABLE
CREATE INDEX

📌 為什麼這週改用 PostgreSQL？

之前使用 SQLite 的優點：

輕量

無需 server

適合本地 prototype

但缺點：

不適合 production

不支援高階 partition

並發能力有限

PostgreSQL 的優點：

強型別系統

支援 partition

支援 JSONB

適合真實 production

這是從「學習專案」往「工程系統」轉型的第一步。

四、Time-Series 資料是什麼？

股票價格屬於：

Time-Series Data（時間序列資料）

特徵：

有明確時間欄位（date / timestamp）

資料量隨時間線性成長

查詢多為：

最近 N 天

某段時間區間

這種資料和一般 CRUD 系統不同。

一般系統（例如使用者表）

主要查 id

更新頻繁

Time-series 系統

主要查時間範圍

append-only 為主

很少 update

📌 設計差異

Time-series DB 更重視：

Index on date

Partition by date

壓縮與歸檔策略

五、什麼是 Partition？

Partition = 把一張大表拆成很多小表。

例如：

prices_2024
prices_2025
prices_2026

而對外仍然是一張 prices 表。

為什麼要 partition？

優點：

查詢只掃描部分資料

提升效能

易於刪除舊資料（直接 drop partition）

缺點：

結構變複雜

管理成本增加

小專案可能過度設計

📌 Trade-off

目前只是理解概念，尚未實作。

工程思維是：

先設計好可以擴展，而不是一開始就優化。

六、新增 scripts/init_db.py

本週最大結構變動：

scripts/
    init_db.py
    ingest_data.py
為什麼拆開？

init_db.py：

只負責 DDL

建立 tables

建立 index

ingest_data.py：

只負責抓資料

寫入資料

📌 設計原則

Single Responsibility Principle（單一職責原則）

優點：

清晰

易測試

易維護

缺點：

檔案變多

初學者會覺得分太細

但在大型系統中，這種分離是必要的。

七、README.md 修改

本週同步更新 README：

說明 DB 初始化流程

加入架構說明

新增執行順序：

python scripts/init_db.py
python scripts/ingest_data.py

📌 工程觀念

README 是：

專案的第一個 API

寫得清楚，未來面試官 clone 你的 repo 就能跑。

八、為什麼不讓 ingest 自動建表？

這是一個設計取捨問題。

方案 A：自動建表
優點：方便
缺點：模糊責任

方案 B：手動 init_db
優點：清楚分層
缺點：多一步操作

我選擇 B，因為：

Schema 是系統層級決策，不應該由資料流決定。

這是「工程化」與「腳本化」的差別。

九、未來規劃：支援輸入股票代碼

目前 symbol 是寫死在程式中。

未來改為：

python ingest_data.py AAPL

或

python ingest_data.py --symbol AAPL
為什麼這很重要？

這代表：

系統開始變成工具

支援動態輸入

可擴展成 API

未來甚至可以：

接 CLI 參數

接 FastAPI

做成 Web UI

這是從「學習專案」往「產品雛形」進化。

十、本週工程成長重點

1️⃣ 理解 DDL 與 DML 的本質差異
2️⃣ 學習 time-series 設計思維
3️⃣ 理解 partition 是效能策略而非語法炫技
4️⃣ 開始使用 PostgreSQL（往 production 靠攏）
5️⃣ 學會專案責任拆分

十一、小結（面試可用）

本週我將專案資料庫從 SQLite 過渡到 PostgreSQL，
重新設計 schema 並實作 DDL 初始化腳本。

我開始用 time-series 的角度思考股票資料的儲存方式，
理解 partition 與索引在成長型資料系統中的重要性。

同時透過拆分 init_db 與 ingestion 腳本，
讓專案結構更符合工程實務與可維護性原則。