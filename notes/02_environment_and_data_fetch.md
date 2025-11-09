🧭 02_environment_and_data_fetch.md
📅 日期：2025-10-27
💡 主題：環境變數、Python 執行原理與資料抓取練習
一、這週進度

建立了 notes/ 資料夾，並完成第一週筆記。

使用 pip freeze > requirements.txt 將目前環境的套件版本輸出。

學習了 python 與 python3 命令的差異。

了解了系統環境變數的概念與其如何影響 Python 執行。

理解了 PowerShell 與 IDE 內建 Terminal 執行 Python 時的環境差異。

撰寫程式抓取 Yahoo Finance 股票資料並建立本地資料夾。

二、指令與環境概念
1️⃣ pip freeze > requirements.txt

將目前虛擬環境中已安裝的所有套件與版本輸出到 requirements.txt。
之後可以用 pip install -r requirements.txt 讓別人重建相同環境。

2️⃣ python vs python3
指令	常見於	說明
python	Windows、部分 macOS	指向系統預設的 Python 解譯器。可能是 Python 3 或 Python 2。
python3	macOS、Linux	明確指定使用 Python 3。部分系統同時保留 Python 2，因此必須用 python3 呼叫。

🧩 關鍵點：

命令其實只是「執行檔名稱的別名」。

系統會根據「環境變數 PATH」去尋找實際的 Python 可執行檔。

不同系統或 IDE 的設定可能導致 python 與 python3 指向不同版本。

3️⃣ 系統環境變數的概念

環境變數（Environment Variables）是作業系統在啟動程式時提供的「全域設定」。

常見變數：

PATH：定義可執行檔搜尋路徑

PYTHONPATH：定義 Python 模組搜尋路徑

VIRTUAL_ENV：虛擬環境啟用時設定的路徑

💡 重點理解：
當你在終端執行 python 時，系統會：

根據 PATH 找到實際 Python 執行檔的位置。

根據 PYTHONPATH 決定去哪裡找 modules。

4️⃣ PowerShell 與 IDE 內建 Terminal 差異
項目	             PowerShell	              IDE Terminal (ex. VS Code)
啟動環境	         系統全域環境	            通常會自動啟用虛擬環境 (.venv)
Python 版本	         可能使用全域 Python	   使用專案設定內的 Python 直譯器
Module 搜尋路徑	      取決於環境變數與全域設定	 IDE 會自動加入虛擬環境路徑

🧠 問題現象：
有時在 PowerShell 執行會找不到某些 module，但在 IDE 裡卻能執行成功。
➡️ 因為 PowerShell 沒有啟用專案的虛擬環境，導致載入的是全域 Python。

三、程式練習 — 抓取股票資料
📄 程式碼
import yfinance as yf  # 從 Yahoo Finance 下載股價資料的套件（非官方 API，但簡單好用）
import pandas as pd    # 處理表格資料的主力庫
import sqlite3         # 連接 SQLite 資料庫的標準庫
import os              # 處理檔案路徑與目錄

# 建立資料夾 (若已存在則不報錯)
os.makedirs("data", exist_ok=True)

# 定義股票代號與下載區間
symbol = "AAPL"
df = yf.download(symbol, start="2020-01-01", end="2025-01-01", progress=False)

# 顯示前 5 筆資料
print(df.head())

🧩 說明

os.makedirs()：建立 data/ 資料夾，作為儲存資料的地方。

yf.download()：從 Yahoo Finance 下載指定股票的歷史價格。

df.head()：預覽資料前幾列，用來確認下載是否成功。

四、學習重點回顧

理解虛擬環境與系統環境的分工。

能判斷 python 指令實際指向的版本。

熟悉如何用 pip freeze 管理套件版本。

實際使用 yfinance 下載並查看股票資料。