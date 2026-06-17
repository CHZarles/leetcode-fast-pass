---
layout: default
title: 28 天速通 LeetCode
nav_order: 1
description: 100 道算法题的 28 天面试冲刺路线
---

<style>
  :root {
    --fp-ink: #171513;
    --fp-muted: #635f58;
    --fp-paper: #fffdf7;
    --fp-card: #ffffff;
    --fp-line: #211d19;
    --fp-red: #e54b37;
    --fp-green: #0f8f72;
    --fp-yellow: #f6c84c;
    --fp-blue: #2f6fcb;
    --fp-black: #171513;
    --fp-shadow: 0 24px 70px rgba(23, 21, 19, 0.14);
  }

  .main-content-wrap,
  .main-content,
  .main-content .fastpass-page {
    max-width: none;
  }

  .fastpass-page {
    color: var(--fp-ink);
    font-family: "Noto Serif SC", "Source Han Serif SC", "Songti SC", Georgia, serif;
    line-height: 1.65;
  }

  .fastpass-page * {
    box-sizing: border-box;
  }

  .fastpass-page a {
    color: inherit;
    text-decoration: none;
  }

  .fp-shell {
    position: relative;
    overflow: hidden;
    margin: 0 auto;
    max-width: 1240px;
    border: 1px solid rgba(23, 21, 19, 0.16);
    border-radius: 8px;
    background:
      linear-gradient(90deg, rgba(23, 21, 19, 0.035) 1px, transparent 1px) 0 0 / 28px 28px,
      linear-gradient(rgba(23, 21, 19, 0.035) 1px, transparent 1px) 0 0 / 28px 28px,
      var(--fp-paper);
    box-shadow: var(--fp-shadow);
  }

  .fp-shell::before {
    position: absolute;
    inset: 0;
    pointer-events: none;
    content: "";
    background:
      repeating-linear-gradient(135deg, transparent 0 24px, rgba(246, 200, 76, 0.1) 24px 26px, transparent 26px 52px),
      linear-gradient(135deg, transparent 0 54%, rgba(229, 75, 55, 0.12) 54% 55%, transparent 55% 100%);
  }

  .fp-hero,
  .fp-section,
  .fp-footer {
    position: relative;
    z-index: 1;
  }

  .fp-hero {
    display: grid;
    grid-template-columns: minmax(0, 1.05fr) minmax(320px, 0.95fr);
    gap: clamp(28px, 5vw, 72px);
    align-items: center;
    min-height: 560px;
    padding: clamp(34px, 6vw, 76px);
  }

  .fp-kicker,
  .fp-label,
  .fp-chip,
  .fp-day-number,
  .fp-stat span,
  .fp-phase-days {
    font-family: "DIN Condensed", "Bahnschrift Condensed", "Avenir Next Condensed", sans-serif;
    letter-spacing: 0;
    text-transform: uppercase;
  }

  .fp-kicker {
    display: inline-flex;
    gap: 10px;
    align-items: center;
    margin-bottom: 18px;
    color: var(--fp-green);
    font-size: 0.92rem;
    font-weight: 800;
  }

  .fp-kicker::before {
    display: inline-block;
    width: 34px;
    height: 3px;
    background: var(--fp-green);
    content: "";
  }

  .fp-hero h1 {
    max-width: 860px;
    margin: 0;
    color: var(--fp-black);
    font-size: 6.6rem;
    font-weight: 900;
    line-height: 0.92;
  }

  .fp-hero h1 .fp-outline {
    display: block;
    color: transparent;
    -webkit-text-stroke: 1.35px var(--fp-black);
    text-stroke: 1.35px var(--fp-black);
  }

  .fp-hero-copy {
    max-width: 720px;
    margin: 28px 0 0;
    color: var(--fp-muted);
    font-size: 1.18rem;
  }

  .fp-actions {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
    margin-top: 28px;
  }

  .fp-button {
    display: inline-flex;
    gap: 10px;
    align-items: center;
    min-height: 46px;
    padding: 11px 16px;
    border: 1px solid var(--fp-black);
    border-radius: 6px;
    background: var(--fp-card);
    color: var(--fp-black);
    font-weight: 800;
    transition: transform 180ms ease, box-shadow 180ms ease, background 180ms ease;
  }

  .fp-button:first-child {
    background: var(--fp-black);
    color: #fff;
  }

  .fp-button:hover {
    transform: translateY(-2px);
    box-shadow: 6px 6px 0 rgba(23, 21, 19, 0.18);
  }

  .fp-button .fp-icon {
    display: inline-grid;
    width: 22px;
    height: 22px;
    place-items: center;
    border-radius: 4px;
    background: currentColor;
    color: var(--fp-card);
    font-family: "DIN Condensed", "Bahnschrift Condensed", sans-serif;
    line-height: 1;
  }

  .fp-button:first-child .fp-icon {
    color: var(--fp-black);
    background: #fff;
  }

  .fp-stats {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 12px;
    margin-top: 34px;
    max-width: 620px;
  }

  .fp-stat {
    min-height: 116px;
    padding: 17px;
    border: 1px solid rgba(23, 21, 19, 0.18);
    border-radius: 8px;
    background: rgba(255, 255, 255, 0.78);
    backdrop-filter: blur(8px);
  }

  .fp-stat strong {
    display: block;
    color: var(--fp-black);
    font-family: "DIN Condensed", "Bahnschrift Condensed", "Avenir Next Condensed", sans-serif;
    font-size: 3.2rem;
    line-height: 0.9;
  }

  .fp-stat span {
    display: block;
    margin-top: 11px;
    color: var(--fp-muted);
    font-size: 0.83rem;
    font-weight: 800;
  }

  .fp-visual {
    position: relative;
    min-height: 520px;
    overflow: hidden;
    padding: 26px;
    border: 1px solid rgba(255, 255, 255, 0.22);
    border-radius: 8px;
    background:
      linear-gradient(90deg, rgba(255, 255, 255, 0.08) 1px, transparent 1px) 0 0 / 34px 34px,
      linear-gradient(rgba(255, 255, 255, 0.08) 1px, transparent 1px) 0 0 / 34px 34px,
      #171513;
    color: #fff;
    box-shadow: 14px 14px 0 rgba(23, 21, 19, 0.14);
  }

  .fp-visual::after {
    position: absolute;
    right: -54px;
    bottom: 44px;
    width: 260px;
    height: 76px;
    border: 1px solid rgba(246, 200, 76, 0.72);
    content: "";
    transform: rotate(-18deg);
  }

  .fp-visual-head {
    display: flex;
    justify-content: space-between;
    gap: 16px;
    align-items: flex-start;
    margin-bottom: 28px;
  }

  .fp-visual-head strong {
    display: block;
    max-width: 250px;
    font-size: 1.1rem;
    line-height: 1.28;
  }

  .fp-pulse {
    display: inline-flex;
    gap: 6px;
    align-items: center;
    color: var(--fp-yellow);
    font-family: "DIN Condensed", "Bahnschrift Condensed", sans-serif;
    font-size: 0.82rem;
    font-weight: 800;
  }

  .fp-pulse::before {
    display: inline-block;
    width: 10px;
    height: 10px;
    background: var(--fp-yellow);
    box-shadow: 0 0 0 0 rgba(246, 200, 76, 0.7);
    content: "";
    animation: fpPulse 1.8s infinite;
  }

  .fp-map {
    display: grid;
    grid-template-columns: repeat(4, minmax(0, 1fr));
    gap: 12px;
    position: relative;
  }

  .fp-map::before {
    position: absolute;
    top: 50%;
    left: 3%;
    width: 94%;
    height: 3px;
    background: linear-gradient(90deg, var(--fp-red), var(--fp-yellow), var(--fp-green), var(--fp-blue));
    content: "";
    transform: translateY(-50%);
  }

  .fp-node {
    position: relative;
    z-index: 1;
    min-height: 104px;
    padding: 14px;
    border: 1px solid rgba(255, 255, 255, 0.2);
    border-radius: 8px;
    background: rgba(23, 21, 19, 0.82);
    transition: transform 180ms ease, border-color 180ms ease;
  }

  .fp-node:hover {
    transform: translateY(-4px);
    border-color: rgba(246, 200, 76, 0.86);
  }

  .fp-node b {
    display: block;
    color: var(--fp-yellow);
    font-family: "DIN Condensed", "Bahnschrift Condensed", sans-serif;
    font-size: 1.55rem;
    line-height: 1;
  }

  .fp-node span {
    display: block;
    margin-top: 12px;
    color: rgba(255, 255, 255, 0.78);
    font-size: 0.9rem;
    line-height: 1.35;
  }

  .fp-terminal {
    position: absolute;
    right: 26px;
    bottom: 28px;
    left: 26px;
    padding: 18px;
    border: 1px solid rgba(255, 255, 255, 0.2);
    border-radius: 8px;
    background: rgba(255, 255, 255, 0.08);
    backdrop-filter: blur(8px);
  }

  .fp-terminal code {
    display: block;
    color: rgba(255, 255, 255, 0.9);
    font-size: 0.92rem;
    white-space: normal;
  }

  .fp-section {
    padding: clamp(42px, 6vw, 78px) clamp(22px, 5vw, 70px);
    border-top: 1px solid rgba(23, 21, 19, 0.14);
  }

  .fp-section-head {
    display: grid;
    grid-template-columns: minmax(0, 0.7fr) minmax(260px, 0.3fr);
    gap: 24px;
    align-items: end;
    margin-bottom: 28px;
  }

  .fp-label {
    display: block;
    margin-bottom: 8px;
    color: var(--fp-red);
    font-size: 0.88rem;
    font-weight: 900;
  }

  .fp-section h2 {
    margin: 0;
    color: var(--fp-black);
    font-size: 3.6rem;
    font-weight: 900;
    line-height: 0.95;
  }

  .fp-section-head p {
    margin: 0;
    color: var(--fp-muted);
  }

  .fp-phase-grid {
    display: grid;
    grid-template-columns: repeat(5, minmax(0, 1fr));
    gap: 14px;
  }

  .fp-phase {
    display: flex;
    flex-direction: column;
    min-height: 220px;
    padding: 18px;
    border: 1px solid rgba(23, 21, 19, 0.16);
    border-top: 8px solid var(--phase);
    border-radius: 8px;
    background: rgba(255, 255, 255, 0.78);
    transition: transform 180ms ease, box-shadow 180ms ease;
  }

  .fp-phase:hover {
    transform: translateY(-4px);
    box-shadow: 8px 8px 0 rgba(23, 21, 19, 0.1);
  }

  .fp-phase-days {
    color: var(--phase);
    font-size: 0.88rem;
    font-weight: 900;
  }

  .fp-phase h3 {
    margin: 10px 0 8px;
    color: var(--fp-black);
    font-size: 1.22rem;
    line-height: 1.25;
  }

  .fp-phase p {
    margin: 0 0 16px;
    color: var(--fp-muted);
    font-size: 0.95rem;
  }

  .fp-mini-links {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-top: auto;
  }

  .fp-chip {
    display: inline-flex;
    min-height: 28px;
    align-items: center;
    padding: 4px 9px;
    border: 1px solid rgba(23, 21, 19, 0.2);
    border-radius: 5px;
    background: #fff;
    color: var(--fp-black);
    font-size: 0.75rem;
    font-weight: 900;
  }

  .fp-chip:hover {
    border-color: var(--phase);
    color: var(--phase);
  }

  .fp-day-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
    gap: 12px;
  }

  .fp-day-card {
    display: flex;
    flex-direction: column;
    min-height: 286px;
    padding: 16px;
    border: 1px solid rgba(23, 21, 19, 0.16);
    border-radius: 8px;
    background: var(--fp-card);
    box-shadow: 0 1px 0 rgba(23, 21, 19, 0.05);
    transition: transform 180ms ease, box-shadow 180ms ease, border-color 180ms ease;
  }

  .fp-day-card:hover {
    transform: translateY(-5px);
    border-color: var(--accent);
    box-shadow: 8px 8px 0 rgba(23, 21, 19, 0.12);
  }

  .fp-day-top {
    display: flex;
    justify-content: space-between;
    gap: 10px;
    align-items: center;
  }

  .fp-day-number {
    display: inline-flex;
    width: 46px;
    height: 34px;
    align-items: center;
    justify-content: center;
    border: 1px solid var(--accent);
    border-radius: 5px;
    color: var(--accent);
    font-weight: 900;
  }

  .fp-day-topic {
    color: var(--fp-muted);
    font-size: 0.82rem;
    font-weight: 800;
  }

  .fp-day-card h3 {
    margin: 18px 0 10px;
    color: var(--fp-black);
    font-size: 1.15rem;
    line-height: 1.3;
  }

  .fp-day-card p {
    margin: 0;
    color: var(--fp-muted);
    font-size: 0.92rem;
  }

  .fp-case-list {
    display: grid;
    gap: 6px;
    margin: 14px 0 0;
    padding: 0;
    color: var(--fp-muted);
    font-size: 0.86rem;
    line-height: 1.42;
    list-style: none;
  }

  .fp-case-list li {
    position: relative;
    padding-left: 14px;
  }

  .fp-case-list li::before {
    position: absolute;
    top: 0.64em;
    left: 0;
    width: 6px;
    height: 2px;
    background: var(--accent);
    content: "";
  }

  .fp-url {
    display: block;
    margin-top: 14px;
    padding: 8px;
    border: 1px solid rgba(23, 21, 19, 0.12);
    border-radius: 5px;
    background: rgba(23, 21, 19, 0.035);
    color: var(--fp-muted);
    font-family: "SFMono-Regular", Consolas, "Liberation Mono", monospace;
    font-size: 0.72rem;
    line-height: 1.35;
    word-break: break-word;
  }

  .fp-day-card .fp-open {
    display: inline-flex;
    gap: 8px;
    align-items: center;
    margin-top: auto;
    padding-top: 16px;
    color: var(--accent);
    font-weight: 900;
  }

  .fp-method {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 14px;
  }

  .fp-method-card {
    min-height: 190px;
    padding: 22px;
    border: 1px solid rgba(23, 21, 19, 0.16);
    border-radius: 8px;
    background: rgba(255, 255, 255, 0.8);
  }

  .fp-method-card b {
    display: block;
    color: var(--fp-black);
    font-size: 1.1rem;
  }

  .fp-method-card p {
    margin: 12px 0 0;
    color: var(--fp-muted);
  }

  .fp-poster {
    display: grid;
    grid-template-columns: minmax(0, 0.58fr) minmax(280px, 0.42fr);
    gap: 24px;
    align-items: center;
    padding: 24px;
    border: 1px solid rgba(23, 21, 19, 0.16);
    border-radius: 8px;
    background: #171513;
    color: #fff;
  }

  .fp-poster img {
    display: block;
    width: 100%;
    border-radius: 6px;
    background: #fff;
  }

  .fp-poster h2 {
    color: #fff;
  }

  .fp-poster p {
    margin: 18px 0 0;
    color: rgba(255, 255, 255, 0.76);
  }

  .fp-footer {
    padding: 26px clamp(22px, 5vw, 70px);
    border-top: 1px solid rgba(23, 21, 19, 0.14);
    color: var(--fp-muted);
    font-size: 0.95rem;
  }

  .fp-animate {
    opacity: 0;
    transform: translateY(18px);
    animation: fpRise 700ms cubic-bezier(0.22, 1, 0.36, 1) forwards;
    animation-delay: var(--delay, 0ms);
  }

  @keyframes fpRise {
    to {
      opacity: 1;
      transform: translateY(0);
    }
  }

  @keyframes fpPulse {
    70% {
      box-shadow: 0 0 0 10px rgba(246, 200, 76, 0);
    }
    100% {
      box-shadow: 0 0 0 0 rgba(246, 200, 76, 0);
    }
  }

  @media (max-width: 980px) {
    .fp-hero h1 {
      font-size: 4.8rem;
    }

    .fp-section h2 {
      font-size: 3rem;
    }

    .fp-hero,
    .fp-section-head,
    .fp-poster {
      grid-template-columns: 1fr;
    }

    .fp-visual {
      min-height: 470px;
    }

    .fp-phase-grid {
      grid-template-columns: repeat(2, minmax(0, 1fr));
    }

    .fp-method {
      grid-template-columns: 1fr;
    }
  }

  @media (max-width: 640px) {
    .fp-hero h1 {
      font-size: 3.2rem;
    }

    .fp-hero-copy {
      font-size: 1.02rem;
    }

    .fp-stat strong {
      font-size: 2.6rem;
    }

    .fp-section h2 {
      font-size: 2.28rem;
    }

    .fp-shell {
      border-radius: 0;
    }

    .fp-hero {
      min-height: auto;
      padding: 28px 18px 34px;
    }

    .fp-stats {
      grid-template-columns: 1fr;
    }

    .fp-visual {
      min-height: auto;
      padding: 18px;
    }

    .fp-map {
      grid-template-columns: repeat(2, minmax(0, 1fr));
    }

    .fp-terminal {
      position: static;
      margin-top: 18px;
    }

    .fp-visual::after {
      right: -70px;
      bottom: 22px;
      opacity: 0.55;
    }

    .fp-section {
      padding: 38px 18px;
    }

    .fp-phase-grid,
    .fp-day-grid {
      grid-template-columns: 1fr;
    }
  }

  @media (prefers-reduced-motion: reduce) {
    .fp-animate,
    .fp-pulse::before {
      animation: none;
      opacity: 1;
      transform: none;
    }

    .fp-button,
    .fp-phase,
    .fp-day-card,
    .fp-node {
      transition: none;
    }
  }
</style>

<div class="fastpass-page">
  <div class="fp-shell">
    <header class="fp-hero">
      <div class="fp-animate" style="--delay: 60ms">
        <span class="fp-kicker">Interview pattern map</span>
        <h1>28 天速通 <span class="fp-outline">LeetCode</span></h1>
        <p class="fp-hero-copy">
          从复杂度分析开始，把链表、数组、树、栈队列、堆、图、滑动窗口、回溯和动态规划串成一条面试训练路线。每天 3 到 4 题，先掌握套路，再追求熟练度。
        </p>
        <div class="fp-actions" aria-label="页面导航">
          <a class="fp-button" href="{{ '/docs/Day%200%20-%20算法复杂度分析.html' | relative_url }}"><span class="fp-icon">1</span>开始 Day 0</a>
          <a class="fp-button" href="#route-map"><span class="fp-icon">2</span>查看路线</a>
          <a class="fp-button" href="#daily-lessons"><span class="fp-icon">3</span>每日入口</a>
        </div>
        <div class="fp-stats" aria-label="课程统计">
          <div class="fp-stat"><strong>100</strong><span>道高频算法题</span></div>
          <div class="fp-stat"><strong>29</strong><span>篇教程含 Day 0</span></div>
          <div class="fp-stat"><strong>10</strong><span>个面试主题阶段</span></div>
        </div>
      </div>

      <div class="fp-visual fp-animate" style="--delay: 180ms" aria-label="算法路线视觉图">
        <div class="fp-visual-head">
          <strong>把题目按“可迁移的套路”组织，而不是按题号硬刷。</strong>
          <span class="fp-pulse">ACTIVE PLAN</span>
        </div>
        <div class="fp-map">
          <a class="fp-node" href="{{ '/docs/Day%200%20-%20算法复杂度分析.html' | relative_url }}"><b>00</b><span>复杂度和取舍</span></a>
          <a class="fp-node" href="{{ '/docs/Day%201%20-%20Linked%20List%20链表1.html' | relative_url }}"><b>01</b><span>链表指针操作</span></a>
          <a class="fp-node" href="{{ '/docs/Day%204%20-%20Array%20数组1.html' | relative_url }}"><b>04</b><span>数组扫描模式</span></a>
          <a class="fp-node" href="{{ '/docs/Day%208%20-%20BST%20二叉树1.html' | relative_url }}"><b>08</b><span>树搜索模板</span></a>
          <a class="fp-node" href="{{ '/docs/Day%2012%20-%20Stack%20栈.html' | relative_url }}"><b>12</b><span>栈和队列</span></a>
          <a class="fp-node" href="{{ '/docs/Day%2014%20-%20PriorityQueue%20优先队列%20%26%20Heap%20堆%201.html' | relative_url }}"><b>14</b><span>堆和 Top K</span></a>
          <a class="fp-node" href="{{ '/docs/Day%2017%20-%20Graph%20图%201.html' | relative_url }}"><b>17</b><span>图搜索</span></a>
          <a class="fp-node" href="{{ '/docs/Day%2027%20Dynamic%20Programming%20动态规划%201.html' | relative_url }}"><b>27</b><span>动态规划</span></a>
        </div>
        <div class="fp-terminal">
          <code>for each pattern: 读题意 -> 写状态/指针 -> 过边界 -> 复盘模板 -> 迁移到相邻题型</code>
        </div>
      </div>
    </header>

    <section class="fp-section" id="route-map">
      <div class="fp-section-head">
        <div>
          <span class="fp-label">Route Map</span>
          <h2>十段式学习轨道</h2>
        </div>
        <p>每一段都对应一个面试常见能力：从低层数据结构操作，到搜索空间剪枝，再到状态转移。</p>
      </div>

      <div class="fp-phase-grid">
        <article class="fp-phase" style="--phase: var(--fp-red)">
          <span class="fp-phase-days">Day 0</span>
          <h3>复杂度预热</h3>
          <p>用 Two Sum 把时间、空间和大 O 取舍讲透。</p>
          <div class="fp-mini-links"><a class="fp-chip" href="{{ '/docs/Day%200%20-%20算法复杂度分析.html' | relative_url }}">进入</a></div>
        </article>

        <article class="fp-phase" style="--phase: var(--fp-green)">
          <span class="fp-phase-days">Day 1-3</span>
          <h3>链表指针</h3>
          <p>dummy node、双指针、翻转、环检测、LRU 和重排链表。</p>
          <div class="fp-mini-links">
            <a class="fp-chip" href="{{ '/docs/Day%201%20-%20Linked%20List%20链表1.html' | relative_url }}">D1</a>
            <a class="fp-chip" href="{{ '/docs/Day%202%20-%20Linked%20List%20链表2.html' | relative_url }}">D2</a>
            <a class="fp-chip" href="{{ '/docs/Day%203%20-%20Linked%20List%20链表3.html' | relative_url }}">D3</a>
          </div>
        </article>

        <article class="fp-phase" style="--phase: var(--fp-blue)">
          <span class="fp-phase-days">Day 4-6</span>
          <h3>数组基础</h3>
          <p>单调性、山脉数组、双指针、三数之和、矩阵和贪心扫描。</p>
          <div class="fp-mini-links">
            <a class="fp-chip" href="{{ '/docs/Day%204%20-%20Array%20数组1.html' | relative_url }}">D4</a>
            <a class="fp-chip" href="{{ '/docs/Day%205%20-%20Array%20数组2.html' | relative_url }}">D5</a>
            <a class="fp-chip" href="{{ '/docs/Day%206%20-%20Array%20数组3.html' | relative_url }}">D6</a>
          </div>
        </article>

        <article class="fp-phase" style="--phase: var(--fp-yellow)">
          <span class="fp-phase-days">Day 7-11</span>
          <h3>递归和二叉树</h3>
          <p>递归模型、DFS、BFS、遍历顺序、深度、路径和完全二叉树。</p>
          <div class="fp-mini-links">
            <a class="fp-chip" href="{{ '/docs/Day%207%20-%20Tree%20树.html' | relative_url }}">D7</a>
            <a class="fp-chip" href="{{ '/docs/Day%208%20-%20BST%20二叉树1.html' | relative_url }}">D8</a>
            <a class="fp-chip" href="{{ '/docs/Day%209%20-%20BST%20二叉树2.html' | relative_url }}">D9</a>
            <a class="fp-chip" href="{{ '/docs/Day%2010%20-%20BST%20二叉树3.html' | relative_url }}">D10</a>
            <a class="fp-chip" href="{{ '/docs/Day%2011%20-%20BST%20二叉树4.html' | relative_url }}">D11</a>
          </div>
        </article>

        <article class="fp-phase" style="--phase: #7f55d6">
          <span class="fp-phase-days">Day 12-13</span>
          <h3>栈和队列</h3>
          <p>括号、单调栈、队列互转、滑动窗口平均值和路径简化。</p>
          <div class="fp-mini-links">
            <a class="fp-chip" href="{{ '/docs/Day%2012%20-%20Stack%20栈.html' | relative_url }}">D12</a>
            <a class="fp-chip" href="{{ '/docs/Day%2013%20-%20Queue%20队列.html' | relative_url }}">D13</a>
          </div>
        </article>

        <article class="fp-phase" style="--phase: #d66a20">
          <span class="fp-phase-days">Day 14-16</span>
          <h3>堆和优先队列</h3>
          <p>Top K、k 路合并、双堆、中位数和区间选择。</p>
          <div class="fp-mini-links">
            <a class="fp-chip" href="{{ '/docs/Day%2014%20-%20PriorityQueue%20优先队列%20%26%20Heap%20堆%201.html' | relative_url }}">D14</a>
            <a class="fp-chip" href="{{ '/docs/Day%2015%20-%20PriorityQueue%20优先队列%20%26%20Heap%20堆%202.html' | relative_url }}">D15</a>
            <a class="fp-chip" href="{{ '/docs/Day%2016%20-%20PriorityQueue%20优先队列%20%26%20Heap%20堆%203.html' | relative_url }}">D16</a>
          </div>
        </article>

        <article class="fp-phase" style="--phase: #0f8f72">
          <span class="fp-phase-days">Day 17-20</span>
          <h3>图算法</h3>
          <p>DFS、BFS、岛屿、单词接龙、拓扑排序和并查集。</p>
          <div class="fp-mini-links">
            <a class="fp-chip" href="{{ '/docs/Day%2017%20-%20Graph%20图%201.html' | relative_url }}">D17</a>
            <a class="fp-chip" href="{{ '/docs/Day%2018%20-%20Graph%20图%202.html' | relative_url }}">D18</a>
            <a class="fp-chip" href="{{ '/docs/Day%2019%20-%20Graph%20图%203.html' | relative_url }}">D19</a>
            <a class="fp-chip" href="{{ '/docs/Day%2020%20-%20Graph%20图%204.html' | relative_url }}">D20</a>
          </div>
        </article>

        <article class="fp-phase" style="--phase: #2f6fcb">
          <span class="fp-phase-days">Day 21-24</span>
          <h3>数组和字符串进阶</h3>
          <p>滑动窗口、区间合并、二分搜索、字符串匹配和回文。</p>
          <div class="fp-mini-links">
            <a class="fp-chip" href="{{ '/docs/Day%2021%20Array%20数组%20%26%20String%20字符串%201.html' | relative_url }}">D21</a>
            <a class="fp-chip" href="{{ '/docs/Day%2022%20Array%20数组%20%26%20String%20字符串%202.html' | relative_url }}">D22</a>
            <a class="fp-chip" href="{{ '/docs/Day%2023%20Array%20数组%20%26%20String%20字符串%203.html' | relative_url }}">D23</a>
            <a class="fp-chip" href="{{ '/docs/Day%2024%20String%20字符串%204.html' | relative_url }}">D24</a>
          </div>
        </article>

        <article class="fp-phase" style="--phase: #e54b37">
          <span class="fp-phase-days">Day 25-26</span>
          <h3>回溯搜索</h3>
          <p>组合、子集、电话号码字母组合、排列、括号生成和大小写转换。</p>
          <div class="fp-mini-links">
            <a class="fp-chip" href="{{ '/docs/Day%2025%20Combination%20组合问题.html' | relative_url }}">D25</a>
            <a class="fp-chip" href="{{ '/docs/Day%2026%20Permutation%20排列问题.html' | relative_url }}">D26</a>
          </div>
        </article>

        <article class="fp-phase" style="--phase: #171513">
          <span class="fp-phase-days">Day 27-28</span>
          <h3>动态规划收束</h3>
          <p>子集和、硬币、等和划分、LCS、编辑距离和 LIS。</p>
          <div class="fp-mini-links">
            <a class="fp-chip" href="{{ '/docs/Day%2027%20Dynamic%20Programming%20动态规划%201.html' | relative_url }}">D27</a>
            <a class="fp-chip" href="{{ '/docs/Day%2028%20Dynamic%20Programming%20动态规划%202.html' | relative_url }}">D28</a>
          </div>
        </article>
      </div>
    </section>

    <section class="fp-section" id="daily-path">
      <div class="fp-section-head">
        <div>
          <span class="fp-label">Practice Loop</span>
          <h2>每天只抓一个核心套路</h2>
        </div>
        <p>控制刷题范围，固定复盘格式，把解法从“看懂”推进到“能在面试里写出来”。</p>
      </div>

      <div class="fp-method">
        <article class="fp-method-card">
          <b>1. 先看模式</b>
          <p>每篇先读基础知识和案例思路，明确这类题的状态、指针、队列或递归边界。</p>
        </article>
        <article class="fp-method-card">
          <b>2. 再敲模板</b>
          <p>把核心代码自己写一遍，重点检查空输入、重复元素、越界和终止条件。</p>
        </article>
        <article class="fp-method-card">
          <b>3. 最后迁移</b>
          <p>做习题时只问一个问题：它和今天的案例差在哪，是否只是数据结构或约束变了。</p>
        </article>
      </div>
    </section>

    <section class="fp-section" id="daily-lessons">
      <div class="fp-section-head">
        <div>
          <span class="fp-label">Exact Page Index</span>
          <h2>精确到每个页面</h2>
        </div>
        <p>每张卡片都是一个实际教程页面，列出点击后的核心小节和目标路径。正式部署时链接会进入对应的 HTML 页面。</p>
      </div>

      <div class="fp-day-grid">
        <a class="fp-day-card" style="--accent: var(--fp-red)" href="{{ '/docs/Day%200%20-%20算法复杂度分析.html' | relative_url }}">
          <div class="fp-day-top"><span class="fp-day-number">00</span><span class="fp-day-topic">Complexity</span></div>
          <h3>Day 0 - 算法复杂度分析</h3><p>点击进入复杂度预热页。</p><ul class="fp-case-list"><li>时间复杂度 / 空间复杂度 / 大 O 符号</li><li>案例：Two Sum</li><li>Brute Force / HashSet / 排序三种解法</li></ul><span class="fp-url">docs/Day 0 - 算法复杂度分析.html</span><span class="fp-open">打开这个页面</span>
        </a>
        <a class="fp-day-card" style="--accent: var(--fp-green)" href="{{ '/docs/Day%201%20-%20Linked%20List%20链表1.html' | relative_url }}">
          <div class="fp-day-top"><span class="fp-day-number">01</span><span class="fp-day-topic">Linked List</span></div>
          <h3>Day 01 - Linked List 链表1</h3><p>点击进入链表基础操作页。</p><ul class="fp-case-list"><li>构造一个链表</li><li>dummy node 和 API 分析</li><li>删除倒数第 N 个节点</li></ul><span class="fp-url">docs/Day 1 - Linked List 链表1.html</span><span class="fp-open">打开这个页面</span>
        </a>
        <a class="fp-day-card" style="--accent: var(--fp-green)" href="{{ '/docs/Day%202%20-%20Linked%20List%20链表2.html' | relative_url }}">
          <div class="fp-day-top"><span class="fp-day-number">02</span><span class="fp-day-topic">Two Pointers</span></div>
          <h3>Day 02 - Linked List 链表2</h3><p>点击进入链表模式页。</p><ul class="fp-case-list"><li>链表翻转 / 快慢指针</li><li>翻转链表 / 合并链表</li><li>环检测算法 / 循环移动链表</li></ul><span class="fp-url">docs/Day 2 - Linked List 链表2.html</span><span class="fp-open">打开这个页面</span>
        </a>
        <a class="fp-day-card" style="--accent: var(--fp-green)" href="{{ '/docs/Day%203%20-%20Linked%20List%20链表3.html' | relative_url }}">
          <div class="fp-day-top"><span class="fp-day-number">03</span><span class="fp-day-topic">Cache</span></div>
          <h3>Day 03 - Linked List 链表3</h3><p>点击进入链表综合题页。</p><ul class="fp-case-list"><li>Google 面试题 LRU Cache</li><li>API 分析和代码实现</li><li>Facebook 面试题重排链表</li></ul><span class="fp-url">docs/Day 3 - Linked List 链表3.html</span><span class="fp-open">打开这个页面</span>
        </a>
        <a class="fp-day-card" style="--accent: var(--fp-blue)" href="{{ '/docs/Day%204%20-%20Array%20数组1.html' | relative_url }}">
          <div class="fp-day-top"><span class="fp-day-number">04</span><span class="fp-day-topic">Array Scan</span></div>
          <h3>Day 04 - Array 数组1</h3><p>点击进入数组扫描页。</p><ul class="fp-case-list"><li>单调数列</li><li>数组中的最长山脉 / 最小差</li><li>最短无序连续子数组</li></ul><span class="fp-url">docs/Day 4 - Array 数组1.html</span><span class="fp-open">打开这个页面</span>
        </a>
        <a class="fp-day-card" style="--accent: var(--fp-blue)" href="{{ '/docs/Day%205%20-%20Array%20数组2.html' | relative_url }}">
          <div class="fp-day-top"><span class="fp-day-number">05</span><span class="fp-day-topic">Two Pointers</span></div>
          <h3>Day 05 - Array 数组2</h3><p>点击进入双指针数组页。</p><ul class="fp-case-list"><li>核心算法：两根指针</li><li>Three Sum / 移动零</li><li>螺旋矩阵</li></ul><span class="fp-url">docs/Day 5 - Array 数组2.html</span><span class="fp-open">打开这个页面</span>
        </a>
        <a class="fp-day-card" style="--accent: var(--fp-blue)" href="{{ '/docs/Day%206%20-%20Array%20数组3.html' | relative_url }}">
          <div class="fp-day-top"><span class="fp-day-number">06</span><span class="fp-day-topic">Greedy</span></div>
          <h3>Day 06 - Array 数组3</h3><p>点击进入数组综合题页。</p><ul class="fp-case-list"><li>四数之和</li><li>最长连续序列 / 最小糖果奖励</li><li>对角遍历</li></ul><span class="fp-url">docs/Day 6 - Array 数组3.html</span><span class="fp-open">打开这个页面</span>
        </a>
        <a class="fp-day-card" style="--accent: var(--fp-yellow)" href="{{ '/docs/Day%207%20-%20Tree%20树.html' | relative_url }}">
          <div class="fp-day-top"><span class="fp-day-number">07</span><span class="fp-day-topic">Recursion</span></div>
          <h3>Day 07 - Tree 树</h3><p>点击进入递归和树预热页。</p><ul class="fp-case-list"><li>阶乘</li><li>斐波那契数</li><li>嵌套列表加权和</li></ul><span class="fp-url">docs/Day 7 - Tree 树.html</span><span class="fp-open">打开这个页面</span>
        </a>
        <a class="fp-day-card" style="--accent: var(--fp-yellow)" href="{{ '/docs/Day%208%20-%20BST%20二叉树1.html' | relative_url }}">
          <div class="fp-day-top"><span class="fp-day-number">08</span><span class="fp-day-topic">DFS</span></div>
          <h3>Day 08 - BST 二叉树1</h3><p>点击进入二叉树 DFS 页。</p><ul class="fp-case-list"><li>二叉树基础 / 深度优先搜索</li><li>前序 / 中序 / 后序遍历</li><li>二叉树迭代器</li></ul><span class="fp-url">docs/Day 8 - BST 二叉树1.html</span><span class="fp-open">打开这个页面</span>
        </a>
        <a class="fp-day-card" style="--accent: var(--fp-yellow)" href="{{ '/docs/Day%209%20-%20BST%20二叉树2.html' | relative_url }}">
          <div class="fp-day-top"><span class="fp-day-number">09</span><span class="fp-day-topic">Tree Path</span></div>
          <h3>Day 09 - BST 二叉树2</h3><p>点击进入二叉树路径页。</p><ul class="fp-case-list"><li>最大深度 / 路径和</li><li>二叉树最大路径和</li><li>翻转二叉树 / 将二叉树拆成链表</li></ul><span class="fp-url">docs/Day 9 - BST 二叉树2.html</span><span class="fp-open">打开这个页面</span>
        </a>
        <a class="fp-day-card" style="--accent: var(--fp-yellow)" href="{{ '/docs/Day%2010%20-%20BST%20二叉树3.html' | relative_url }}">
          <div class="fp-day-top"><span class="fp-day-number">10</span><span class="fp-day-topic">BFS</span></div>
          <h3>Day 10 - BST 二叉树3</h3><p>点击进入二叉树 BFS 页。</p><ul class="fp-case-list"><li>基础知识：广度优先搜索</li><li>层次遍历 / 最小深度</li><li>右侧最近节点 / right-sibling tree</li></ul><span class="fp-url">docs/Day 10 - BST 二叉树3.html</span><span class="fp-open">打开这个页面</span>
        </a>
        <a class="fp-day-card" style="--accent: var(--fp-yellow)" href="{{ '/docs/Day%2011%20-%20BST%20二叉树4.html' | relative_url }}">
          <div class="fp-day-top"><span class="fp-day-number">11</span><span class="fp-day-topic">Complete Tree</span></div>
          <h3>Day 11 - BST 二叉树4</h3><p>点击进入完全二叉树页。</p><ul class="fp-case-list"><li>统计完全二叉树的节点数</li><li>解法 1 / 解法 2 / 解法 3</li><li>习题</li></ul><span class="fp-url">docs/Day 11 - BST 二叉树4.html</span><span class="fp-open">打开这个页面</span>
        </a>
        <a class="fp-day-card" style="--accent: #7f55d6" href="{{ '/docs/Day%2012%20-%20Stack%20栈.html' | relative_url }}">
          <div class="fp-day-top"><span class="fp-day-number">12</span><span class="fp-day-topic">Stack</span></div>
          <h3>Day 12 - Stack 栈</h3><p>点击进入栈和单调栈页。</p><ul class="fp-case-list"><li>基础知识：栈</li><li>有效括号序列 / 最小值最大值操作栈</li><li>下一个更大的数</li></ul><span class="fp-url">docs/Day 12 - Stack 栈.html</span><span class="fp-open">打开这个页面</span>
        </a>
        <a class="fp-day-card" style="--accent: #7f55d6" href="{{ '/docs/Day%2013%20-%20Queue%20队列.html' | relative_url }}">
          <div class="fp-day-top"><span class="fp-day-number">13</span><span class="fp-day-topic">Queue</span></div>
          <h3>Day 13 - Queue 队列</h3><p>点击进入队列和双端队列页。</p><ul class="fp-case-list"><li>基础知识：队列</li><li>用栈实现队列 / 用队列实现栈</li><li>滑动窗口平均值 / 简化路径</li></ul><span class="fp-url">docs/Day 13 - Queue 队列.html</span><span class="fp-open">打开这个页面</span>
        </a>
        <a class="fp-day-card" style="--accent: #d66a20" href="{{ '/docs/Day%2014%20-%20PriorityQueue%20优先队列%20%26%20Heap%20堆%201.html' | relative_url }}">
          <div class="fp-day-top"><span class="fp-day-number">14</span><span class="fp-day-topic">Top K</span></div>
          <h3>Day 14 - PriorityQueue 优先队列</h3><p>点击进入堆和 Top K 页。</p><ul class="fp-case-list"><li>优先队列 / 二叉堆 / Top K</li><li>数组中的第 K 大元素</li><li>前 K 高频 / 最少不同元素 / 重排字符串</li></ul><span class="fp-url">docs/Day 14 - PriorityQueue 优先队列 &amp; Heap 堆 1.html</span><span class="fp-open">打开这个页面</span>
        </a>
        <a class="fp-day-card" style="--accent: #d66a20" href="{{ '/docs/Day%2015%20-%20PriorityQueue%20优先队列%20%26%20Heap%20堆%202.html' | relative_url }}">
          <div class="fp-day-top"><span class="fp-day-number">15</span><span class="fp-day-topic">K-way Merge</span></div>
          <h3>Day 15 - PriorityQueue 优先队列</h3><p>点击进入 k 路合并页。</p><ul class="fp-case-list"><li>核心算法：k 路合并</li><li>有序矩阵中的第 K 小元素</li><li>最小范围 / 查找和最小的 K 对数字</li></ul><span class="fp-url">docs/Day 15 - PriorityQueue 优先队列 &amp; Heap 堆 2.html</span><span class="fp-open">打开这个页面</span>
        </a>
        <a class="fp-day-card" style="--accent: #d66a20" href="{{ '/docs/Day%2016%20-%20PriorityQueue%20优先队列%20%26%20Heap%20堆%203.html' | relative_url }}">
          <div class="fp-day-top"><span class="fp-day-number">16</span><span class="fp-day-topic">Two Heaps</span></div>
          <h3>Day 16 - PriorityQueue 优先队列</h3><p>点击进入双堆页。</p><ul class="fp-case-list"><li>核心算法：双堆</li><li>数据流中位数 / 滑动窗口中位数</li><li>最大化资本 / 右侧下一个区间</li></ul><span class="fp-url">docs/Day 16 - PriorityQueue 优先队列 &amp; Heap 堆 3.html</span><span class="fp-open">打开这个页面</span>
        </a>
        <a class="fp-day-card" style="--accent: var(--fp-green)" href="{{ '/docs/Day%2017%20-%20Graph%20图%201.html' | relative_url }}">
          <div class="fp-day-top"><span class="fp-day-number">17</span><span class="fp-day-topic">Graph Search</span></div>
          <h3>Day 17 - Graph 图 1</h3><p>点击进入图搜索基础页。</p><ul class="fp-case-list"><li>图与树 / 树搜索 / 图搜索</li><li>DFS</li><li>BFS</li></ul><span class="fp-url">docs/Day 17 - Graph 图 1.html</span><span class="fp-open">打开这个页面</span>
        </a>
        <a class="fp-day-card" style="--accent: var(--fp-green)" href="{{ '/docs/Day%2018%20-%20Graph%20图%202.html' | relative_url }}">
          <div class="fp-day-top"><span class="fp-day-number">18</span><span class="fp-day-topic">Grid BFS</span></div>
          <h3>Day 18 - Graph 图 2</h3><p>点击进入网格和单词图页。</p><ul class="fp-case-list"><li>岛屿的个数</li><li>Boggle</li><li>单词接龙 1 / 单词接龙 2</li></ul><span class="fp-url">docs/Day 18 - Graph 图 2.html</span><span class="fp-open">打开这个页面</span>
        </a>
        <a class="fp-day-card" style="--accent: var(--fp-green)" href="{{ '/docs/Day%2019%20-%20Graph%20图%203.html' | relative_url }}">
          <div class="fp-day-top"><span class="fp-day-number">19</span><span class="fp-day-topic">Topo Sort</span></div>
          <h3>Day 19 - Graph 图 3</h3><p>点击进入拓扑排序页。</p><ul class="fp-case-list"><li>核心算法：Topological Sort</li><li>课程规划顺序 / 外星人词典</li><li>序列重构 / 最小高度树</li></ul><span class="fp-url">docs/Day 19 - Graph 图 3.html</span><span class="fp-open">打开这个页面</span>
        </a>
        <a class="fp-day-card" style="--accent: var(--fp-green)" href="{{ '/docs/Day%2020%20-%20Graph%20图%204.html' | relative_url }}">
          <div class="fp-day-top"><span class="fp-day-number">20</span><span class="fp-day-topic">Union Find</span></div>
          <h3>Day 20 - Graph 图 4</h3><p>点击进入并查集页。</p><ul class="fp-case-list"><li>并查集 / 并查集最优实现</li><li>冗余连接 / 岛屿的个数 2</li><li>账户合并 / 计算除法</li></ul><span class="fp-url">docs/Day 20 - Graph 图 4.html</span><span class="fp-open">打开这个页面</span>
        </a>
        <a class="fp-day-card" style="--accent: var(--fp-blue)" href="{{ '/docs/Day%2021%20Array%20数组%20%26%20String%20字符串%201.html' | relative_url }}">
          <div class="fp-day-top"><span class="fp-day-number">21</span><span class="fp-day-topic">Sliding Window</span></div>
          <h3>Day 21 Array 数组</h3><p>点击进入滑动窗口页。</p><ul class="fp-case-list"><li>核心算法：滑动窗口</li><li>和大于 S 的最小子数组</li><li>最多 k 个不同字符 / 字符串排列 / 最小覆盖</li></ul><span class="fp-url">docs/Day 21 Array 数组 &amp; String 字符串 1.html</span><span class="fp-open">打开这个页面</span>
        </a>
        <a class="fp-day-card" style="--accent: var(--fp-blue)" href="{{ '/docs/Day%2022%20Array%20数组%20%26%20String%20字符串%202.html' | relative_url }}">
          <div class="fp-day-top"><span class="fp-day-number">22</span><span class="fp-day-topic">Intervals</span></div>
          <h3>Day 22 Array 数组</h3><p>点击进入区间合并页。</p><ul class="fp-case-list"><li>核心算法：区间合并</li><li>合并区间 / 区间交集</li><li>最少会议室 / 空闲时间</li></ul><span class="fp-url">docs/Day 22 Array 数组 &amp; String 字符串 2.html</span><span class="fp-open">打开这个页面</span>
        </a>
        <a class="fp-day-card" style="--accent: var(--fp-blue)" href="{{ '/docs/Day%2023%20Array%20数组%20%26%20String%20字符串%203.html' | relative_url }}">
          <div class="fp-day-top"><span class="fp-day-number">23</span><span class="fp-day-topic">Binary Search</span></div>
          <h3>Day 23 Array 数组</h3><p>点击进入二分搜索页。</p><ul class="fp-case-list"><li>核心算法：二分搜索</li><li>二分搜索法 / 数字范围</li><li>无限长度升序数组 / 搜索旋转排序数组</li></ul><span class="fp-url">docs/Day 23 Array 数组 &amp; String 字符串 3.html</span><span class="fp-open">打开这个页面</span>
        </a>
        <a class="fp-day-card" style="--accent: var(--fp-blue)" href="{{ '/docs/Day%2024%20String%20字符串%204.html' | relative_url }}">
          <div class="fp-day-top"><span class="fp-day-number">24</span><span class="fp-day-topic">String</span></div>
          <h3>Day 24 String 字符串 4</h3><p>点击进入字符串专题页。</p><ul class="fp-case-list"><li>字符串查找</li><li>最长回文子串 / 异位词分组</li><li>最长有效括号</li></ul><span class="fp-url">docs/Day 24 String 字符串 4.html</span><span class="fp-open">打开这个页面</span>
        </a>
        <a class="fp-day-card" style="--accent: var(--fp-red)" href="{{ '/docs/Day%2025%20Combination%20组合问题.html' | relative_url }}">
          <div class="fp-day-top"><span class="fp-day-number">25</span><span class="fp-day-topic">Combination</span></div>
          <h3>Day 25 Combination 组合问题</h3><p>点击进入组合回溯页。</p><ul class="fp-case-list"><li>核心算法：组合问题</li><li>子集问题 / 子集问题 2</li><li>电话号码的字母组合</li></ul><span class="fp-url">docs/Day 25 Combination 组合问题.html</span><span class="fp-open">打开这个页面</span>
        </a>
        <a class="fp-day-card" style="--accent: var(--fp-red)" href="{{ '/docs/Day%2026%20Permutation%20排列问题.html' | relative_url }}">
          <div class="fp-day-top"><span class="fp-day-number">26</span><span class="fp-day-topic">Permutation</span></div>
          <h3>Day 26 Permutation 排列问题</h3><p>点击进入排列回溯页。</p><ul class="fp-case-list"><li>核心算法：排列问题</li><li>排列 / 排列 2 / 大小写转换</li><li>生成括号 / 通配缩写</li></ul><span class="fp-url">docs/Day 26 Permutation 排列问题.html</span><span class="fp-open">打开这个页面</span>
        </a>
        <a class="fp-day-card" style="--accent: var(--fp-black)" href="{{ '/docs/Day%2027%20Dynamic%20Programming%20动态规划%201.html' | relative_url }}">
          <div class="fp-day-top"><span class="fp-day-number">27</span><span class="fp-day-topic">DP Subset</span></div>
          <h3>Day 27 Dynamic Programming 动态规划 1</h3><p>点击进入子集和 DP 页。</p><ul class="fp-case-list"><li>核心算法：子集和</li><li>非相邻最大子集和 / 最少硬币交换</li><li>硬币交换方案 / 划分和相等的子集</li></ul><span class="fp-url">docs/Day 27 Dynamic Programming 动态规划 1.html</span><span class="fp-open">打开这个页面</span>
        </a>
        <a class="fp-day-card" style="--accent: var(--fp-black)" href="{{ '/docs/Day%2028%20Dynamic%20Programming%20动态规划%202.html' | relative_url }}">
          <div class="fp-day-top"><span class="fp-day-number">28</span><span class="fp-day-topic">DP Sequence</span></div>
          <h3>Day 28 Dynamic Programming 动态规划 2</h3><p>点击进入子序列 DP 页。</p><ul class="fp-case-list"><li>核心算法：子序列问题</li><li>最长公共子序列 / 最长回文序列</li><li>编辑距离 / 最长上升子序列</li></ul><span class="fp-url">docs/Day 28 Dynamic Programming 动态规划 2.html</span><span class="fp-open">打开这个页面</span>
        </a>
      </div>
    </section>

    <section class="fp-section" id="poster">
      <div class="fp-poster">
        <img src="{{ '/docs/海报.png' | relative_url }}" alt="系统设计面试攻略海报">
        <div>
          <span class="fp-label">Next Track</span>
          <h2>算法之后，补系统设计</h2>
          <p>这个站点先把算法面试的高频题型打通。需要继续准备系统设计时，可以顺着原项目里的进阶资源接上。</p>
          <div class="fp-actions">
            <a class="fp-button" href="{{ '/docs/海报.png' | relative_url }}"><span class="fp-icon">+</span>查看海报</a>
          </div>
        </div>
      </div>
    </section>

    <footer class="fp-footer">
      明确目标：刷题主要是为了面试，不需要追求完美，能够稳定写出可过的解法就够。
    </footer>
  </div>
</div>
