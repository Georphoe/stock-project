🧭 07_frontend_mvp_and_nextjs_fundamentals.md
📅 日期：2026-03-21
💡 主題：前端 MVP、Node/NPM 基礎、DOM、JSX、Next.js App Router、Server/Client Components、React Hooks

一、本週目標與進度

本週從「後端 API」延伸到「前端 MVP」，建立基本的使用者介面能力：

建立前端開發環境（Node / npm / npx）
理解 DOM 與瀏覽器運作方式
學習 JSX 語法與 React 基本概念
理解 Next.js App Router 架構
區分 Server Component vs Client Component
使用 React Hook（useState）管理狀態
初步建立「可與 API 串接」的前端思維

二、Node / npm / npx 基礎
1️⃣ Node.js 是什麼？

Node.js 是一個：

讓 JavaScript 可以在「瀏覽器外」執行的環境

📌 為什麼重要？

React / Next.js 都需要 Node 來運行與打包
讓 JS 能做後端、CLI 工具、build system
2️⃣ npm（套件管理工具）

npm = Node Package Manager

用途：

安裝套件（react, next）
管理 dependencies
執行 script（dev, build）

📌 優點：

生態系最大
安裝方便

📌 缺點：

node_modules 很大（常見痛點）
3️⃣ npx（執行工具）

npx = 直接執行套件，不需全域安裝

例如：

npx create-next-app

📌 差別：

工具	用途
npm	安裝套件
npx	執行套件

三、DOM（Document Object Model）

DOM 是：

瀏覽器將 HTML 轉換成「樹狀結構」

例如：

<div>
  <p>Hello</p>
</div>

會變成：

div
 └── p

📌 React 為什麼重要？

React 不直接操作 DOM，而是：

操作「虛擬 DOM（Virtual DOM）」

優點：

減少直接操作 DOM 的成本
提升效能
讓 UI 更新更可控

四、JSX 概念

JSX = JavaScript + HTML-like 語法

例如：

const element = <h1>Hello</h1>;

📌 本質：

JSX 會被轉成：

React.createElement("h1", null, "Hello");

📌 為什麼使用 JSX？

優點：

可讀性高
UI 結構清楚
和 JavaScript 結合方便

缺點：

需要編譯（Babel / Next.js 幫你處理）

五、Container vs Void Element
1️⃣ Container Element（有結尾標籤）

例如：

<div>Hello</div>

📌 特性：

可以包裹其他元素
有開始與結束 tag
2️⃣ Void Element（自閉合）

例如：

<img src="..." />
<input />

📌 特性：

沒有 children
必須 self-closing

📌 為什麼重要？

JSX 規則比 HTML 嚴格：

所有 void element 必須加 /

六、Next.js App Router 概念

App Router 是 Next.js 的新架構：

app/
  page.tsx
  layout.tsx

📌 核心概念：

基於「檔案系統的 routing」
每個資料夾 = 一個 route
page.tsx = 頁面
layout.tsx = 共用版面
📌 傳統 vs App Router
架構	特點
Pages Router	舊架構
App Router	新架構（推薦）
📌 App Router 優點
支援 Server Components
更好的效能
更好的資料取得方式

七、Server Component vs Client Component

這是 Next.js 的核心概念之一：

1️⃣ Server Component（預設）
在 server 執行
不會送到瀏覽器
無法使用 useState / useEffect

📌 優點：

更快（少 JS）
SEO 好
可直接存取 DB
2️⃣ Client Component

需要加：

"use client";

📌 特性：

在瀏覽器執行
可以用 hook
有互動性

📌 使用場景：

按鈕點擊
表單
即時 UI

📌 工程思維

預設用 Server Component，只有需要互動時才用 Client Component

這是效能最佳化關鍵。

八、React Hook（useState）
1️⃣ 什麼是 Hook？

Hook 是：

讓 function component 擁有狀態與生命週期的機制

2️⃣ useState
const [count, setCount] = useState(0);

📌 意義：

count = 當前狀態
setCount = 更新狀態的方法

📌 為什麼需要 Hook？

在 React 之前：

class component 才能有 state

現在：

function component + hooks = 主流

📌 工程思維

UI = function(state)
state 改變 → UI 更新

這是 React 的核心哲學。

九、本週 MVP 架構理解

本週已具備：

前端 UI 基礎概念
API 串接能力
React 狀態管理
Next.js 架構理解

👉 可以開始做：

股票查詢 UI
圖表顯示
API fetch 串接

十、本週學習重點（面試可用）
理解 Node / npm / npx 工具鏈
掌握 DOM 與 React 的關係
理解 JSX 本質（非原生 JS）
區分 container vs void element
理解 Next.js App Router 架構
Server / Client Component 的取捨
使用 useState 管理 UI 狀態
十一、小結

本週完成前端 MVP 的基礎概念建立：

從底層（DOM）到框架（React / Next.js），
理解前端如何與後端 API 串接，並建立可互動 UI。

系統架構已從：

資料抓取 → 資料庫 → API → 前端 UI

逐步形成完整流程，為下一步「圖表與互動功能」奠定基礎。