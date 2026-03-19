"use client"; 
// 👉 Next.js App Router 的標記
// 表示這個元件是在「瀏覽器端（Client Component）」執行
// 因為我們用到了 useState（只能在 client 用）

import { useState } from "react"; 
// 👉 從 React 引入 useState（Hook）
// 用來在函式元件中管理「狀態」

export default function Home() {
  // 👉 定義一個 React 元件（頁面）

  const [ticker, setTicker] = useState("");
  // 👉 ticker：儲存使用者輸入的股票代號（例如 AAPL）
  // 👉 setTicker：用來更新 ticker 的函式
  // 👉 useState("")：初始值是空字串

  const [stock, setStock] = useState<any>(null);
  // 👉 stock：存放查詢到的股票資料（目前先用假資料）
  // 👉 初始值是 null（代表還沒查詢）
  // 👉 any：暫時不限制型別（之後可以改成 interface）

  const handleSearch = () => {
    // 👉 當使用者點擊 Search 按鈕時會執行這個函式

    // 👉 目前用「假資料」模擬 API 回傳
    // 👉 之後會改成 fetch / axios 去呼叫後端 API
    const fakeData = {
      symbol: ticker.toUpperCase(), 
      // 👉 把輸入的 ticker 轉成大寫（例如 aapl → AAPL）

      price: (Math.random() * 100 + 100).toFixed(2),
      // 👉 產生隨機股價（100 ~ 200）
      // 👉 toFixed(2) → 保留小數點 2 位

      change: (Math.random() * 10 - 5).toFixed(2),
      // 👉 產生漲跌幅（-5% ~ +5%）
      // 👉 負數 = 下跌，正數 = 上漲
    };

    setStock(fakeData);
    // 👉 把假資料存進 state
    // 👉 React 會自動重新 render 畫面
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center gap-6">
      {/* 👉 外層容器
          - min-h-screen：至少滿版高度
          - flex：使用 flex 排版
          - flex-col：直向排列
          - items-center：水平置中
          - justify-center：垂直置中
          - gap-6：元素之間間距 */}

      <h1 className="text-4xl font-bold">
        Stock Search 📈
      </h1>
      {/* 👉 標題 */}

      <input
        type="text"
        // 👉 輸入框類型

        placeholder="Enter ticker (e.g. AAPL)"
        // 👉 提示文字

        className="border px-4 py-2 rounded w-64"
        // 👉 Tailwind CSS：
        // border：邊框
        // px-4 py-2：內距
        // rounded：圓角
        // w-64：寬度

        value={ticker}
        // 👉 綁定 state（controlled component）
        // 👉 input 的值來自 ticker

        onChange={(e) => setTicker(e.target.value)}
        // 👉 當使用者輸入時：
        // 👉 把輸入值更新到 ticker state
      />

      <button 
        className="bg-blue-500 text-white px-4 py-2 rounded"
        // 👉 按鈕樣式

        onClick={() => {
          console.log(ticker);
          // 👉 在 console 印出目前輸入的 ticker（debug 用）

          handleSearch();
          // 👉 呼叫查詢函式
        }}
      >
        Search
      </button>

      {/* 👇 股票卡片 */}
      {stock && (
        // 👉 只有當 stock 有值時才會顯示
        // 👉 null / undefined 不會 render

        <div className="mt-6 p-6 border rounded shadow w-64 text-center">
          {/* 👉 卡片容器 */}

          <h2 className="text-2xl font-bold">
            {stock.symbol}
            {/* 👉 顯示股票代號 */}
          </h2>

          <p className="text-lg">
            Price: ${stock.price}
            {/* 👉 顯示股價 */}
          </p>

          <p className={stock.change >= 0 ? "text-green-500" : "text-red-500"}>
            {/* 👉 根據漲跌決定顏色
                - >= 0 → 綠色（上漲）
                - < 0 → 紅色（下跌）
            */}

            Change: {stock.change}%
            {/* 👉 顯示漲跌幅 */}
          </p>
        </div>
      )}
    </div>
  );
}