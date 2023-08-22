程式名稱：股票交易策略回測工具

程式簡介：
這款股票交易策略回測工具是一個基於Python的桌面應用程式，利用Tkinter圖形用戶界面和pandas數據處理庫，旨在模擬和測試股票交易策略的效能。它通過使用yfinance獲取歷史股價數據，讓使用者能夠載入股票數據、選擇交易策略，設定初始投資金額和槓桿倍數，並獲取交易回測結果和相關的交易圖表。

功能介紹：
1. 資料載入： 使用者可以通過CSV文件載入歷史股價數據，並使用pandas庫進行數據處理，將數據顯示在Tkinter交易圖表上。
2. 不同策略選擇： 使用者可以從預設的交易策略中選擇，例如累積收益策略、單一移動平均線策略，甚至是用戶自定義的 "Gil_Blake_Trading" 策略。
3. 初始參數設定： 使用者可以在Tkinter界面中設定初始投資金額和槓桿倍數，方便進行回測。
4. 交易策略回測： 使用者可以在應用程式中選擇不同的交易策略，並觀察每日交易的相關數據，包括持倉、買賣信號、成本、收益等。
5. 交易圖表繪製： 使用Matplotlib庫，將回測結果以交易圖表的形式展示，幫助使用者直觀理解不同策略的收益走勢和交易點。
6. GUI界面： 使用Tkinter實現的GUI界面，提供了友好的操作方式，並使交易回測更加視覺化。

未來想更新的功能：
1. 更多交易策略： 在增加更多預設交易策略的基礎上，允許用戶通過介面自定義交易策略。
2. 回測結果分析： 提供更多的統計分析和評估指標，幫助使用者更全面地評估策略的效能。
3. 即時數據支援： 增加即時股價數據的獲取功能，讓回測更加貼近實際交易情況。
4. 多檔案支援： 允許同時載入並比較多個股票的歷史數據，進行跨股票的回測比較。
5. 用戶自定義設置： 提供更多的用戶自定義設置，例如外觀設置、交易參數調整等。

這個更新的程式簡介突出了您使用的技術，希望這份文檔更符合您的需求！
