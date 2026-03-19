"use client";
import { useState } from "react";

export default function Home() {
  return (
    <div className="min-h-screen flex flex-col items-center justify-center gap-6">
      <h1 className="text-4xl font-bold"> 
        Stock Search 📈
      </h1>
      <input
        type = 'text'
        placeholder="Enter ticker (e.g. AAPL)"
        className="border px-4 py-2 rounded w-64"
      />

      <button className="bg-blue-500 text-white px-4 py-2 rounded">
        Search
      </button>
      

    </div>
  );
}
