🧭 01_project_setup.md
📅 日期：2025-10-15
💡 主題：專案初始化（Stock Project）
一、目標

建立一個新的 Python 專案環境，並準備好基本目錄結構與 Git 版本控制。

二、步驟紀錄
1️⃣ 建立專案資料夾並初始化 Git
mkdir stock-project
cd stock-project
git init


建立一個新資料夾並初始化 Git 儲存庫。

2️⃣ 建立 README 檔案
echo "# Stock Project" > README.md


新增一個簡單的 README 作為專案說明文件。

3️⃣ 建立 Python 虛擬環境

（使用 Windows PowerShell）

python -m venv .venv


建立一個名為 .venv 的虛擬環境，確保專案依賴與系統環境分離。

4️⃣ 啟用虛擬環境
.venv\Scripts\Activate.ps1


啟用後，PowerShell 會顯示虛擬環境名稱，表示目前的 Python 環境已切換成功。

5️⃣ 安裝必要套件, 保證用的 pip 對應當前這個 venv Python 版本
python3 -m pip install --upgrade pip
python3 -m pip install yfinance pandas sqlalchemy sqlite3


更新 pip，並安裝未來會用到的主要套件：

yfinance：抓取股票資料

pandas：資料處理

sqlalchemy：資料庫 ORM 工具

sqlite3：輕量資料庫（Python 內建，但這裡一起列出）

6️⃣ 建立專案基本結構
mkdir backend frontend data scripts


建立四個主要資料夾：

backend/：後端程式（API、資料庫邏輯）

frontend/：前端頁面（未來用 React/Next.js）

data/：資料存放（例如 CSV、SQLite DB）

scripts/：輔助腳本（如自動抓取資料、初始化設定）

7️⃣ 建立 .gitignore
echo "venv/" > .gitignore


忽略虛擬環境資料夾，避免將 .venv 推上 GitHub。

8️⃣ 提交初始版本
git add .
git commit -m "init project"


把目前所有檔案加入版本控制並建立第一個 commit。

✅ 結果

至此，專案結構如下：

stock-project/
├── backend/
├── frontend/
├── data/
├── scripts/
├── .venv/
├── .gitignore
├── README.md
└── requirements.txt (可日後新增)


專案已完成初始化，接下來可以：

在 backend/ 撰寫抓取股票資料的 Python 程式

在 scripts/ 新增 fetch_sample.py 測試 yfinance
