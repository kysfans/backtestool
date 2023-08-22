import tkinter as tk
import time
from tkinter import filedialog, ttk
import pandas as pd
import matplotlib.pyplot as plt
import requests
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from ui_helpers import create_widgets
import yfinance as yf
import os
import strategy


class BacktestApp:
    def __init__(self, root):

        self.root = root
        self.root.title("Stock Trading Strategy Backtest Tool")
        self.root.geometry("800x600")
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.data = None
        self.leverage_var = tk.StringVar()
        self.symbol_var = tk.StringVar()
        self.start_date_var = tk.StringVar()
        self.end_date_var = tk.StringVar()
        self.strategy_var = tk.StringVar()
        self.strategy = ["Long_Term_Holding", "Moving_Average", "Moving_Average_Crossover", "Gil_Blake_Trading"]
        self.plot_canvas = None
        self.strategy_menu = None
        self.strategy_params_frame = None
        self.strategy_params = {}
        self.trade_history_df = {}

        create_widgets(self)

        self.create_plot_canvas()

    def on_closing(self):
        # 在視窗關閉時執行的操作，例如停止線程或任務
        # 這裡可以添加需要停止的背景任務或線程的代碼
        # 然後使用 self.root.destroy() 關閉視窗
        self.root.destroy()

    """
    def plot_selected_strategy(self, trade_history_df):
        if self.plot_canvas:
            self.plot_canvas.get_tk_widget().destroy()

        if self.data is not None:
            fig, ax = plt.subplots(figsize=(10, 6))
            # trade_history_df['Cumulative_Income'] = trade_history_df['Income'].cumsum()
            # ax.plot(trade_history_df['Date'], trade_history_df['Cumulative_Income'], label='Income')
            ax.plot(trade_history_df['Date'], trade_history_df['Income'], label='Income')
            ax.set_xlabel('Date')
            ax.set_ylabel('Income')
            ax.set_title('Long Hold Strategy Backtest Results')
            self.plot_canvas = FigureCanvasTkAgg(fig, master=self.root)
            self.plot_canvas.get_tk_widget().pack()
    """

    def plot_selected_strategy(self, trade_history_df):
        if self.plot_canvas:
            self.plot_canvas.get_tk_widget().destroy()

        if self.data is not None:
            fig, ax = plt.subplots(figsize=(10, 6))

            # Filter trade history where income >= 50
            valid_trade_history_df = trade_history_df[trade_history_df['Income'] >= 50]

            if not valid_trade_history_df.empty:
                ax.plot(valid_trade_history_df['Date'], valid_trade_history_df['Income'], label='Income')
                ax.set_xlabel('Date')
                ax.set_ylabel('Income')
                ax.set_title('Long Hold Strategy Backtest Results')
                self.plot_canvas = FigureCanvasTkAgg(fig, master=self.root)
                self.plot_canvas.get_tk_widget().pack()
            else:
                print("No valid trade history with income >= 50.")

    def backtest_strategy(self):

        leverage_value = self.leverage_var.get()
        if leverage_value:
            select_strategy = self.strategy_var.get()
            self.trade_history_df = strategy.investment_strategy(self.data, 100, leverage_value, select_strategy)
            self.plot_selected_strategy(self.trade_history_df)
        else:
            print("Please enter a valid leverage value.")

    def download_stock_data(self):
        # 定義股票代號列表
        stock_symbols = {'AAPL': 'AAPL_data.csv', 'MSFT': 'MSFT_data.csv', 'GOOGL': 'GOOGL_data.csv',
                         'AMZN': 'AMZN_data.csv', 'META': 'META_data.csv', '^NDX': '^NDX_data.csv'}

        # 設定儲存路徑
        save_path = "historical_stock_data"

        # 創建儲存路徑文件夾（如果不存在）
        if not os.path.exists(save_path):
            os.makedirs(save_path)

        # 下載歷史數據並保存為不同的CSV檔案
        for symbol, filename in stock_symbols.items():
            data = yf.Ticker(symbol)
            df = data.history(period="max")
            file_path = os.path.join(save_path, filename)  # 指定檔案的完整路徑
            df.index.name = 'Date'  # 將日期設定為索引名稱
            df.reset_index(inplace=True)  # 重設索引，將日期列恢復為數據列
            df.to_csv(file_path, index=False)
            print(f"已保存 {symbol} 的歷史數據為 {file_path}")
            time.sleep(0.5)  # 增加延遲

    def create_plot_canvas(self):
        fig, ax = plt.subplots(figsize=(10, 6))
        self.plot_canvas = FigureCanvasTkAgg(fig, master=self.root)
        self.plot_canvas.get_tk_widget().pack()

    def plot_stock_prices(self):
        if self.plot_canvas:
            self.plot_canvas.get_tk_widget().destroy()  # 刪除舊的圖表部件
        if self.data is not None:
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.plot(self.data['Date'], self.data['Close'])  # 假設 'Date' 和 'Close' 是您的數據框的列名
            ax.set_xlabel('Date')
            ax.set_ylabel('Stock Price')
            ax.set_title('Stock Price Chart')
            self.plot_canvas = FigureCanvasTkAgg(fig, master=self.root)
            self.plot_canvas.get_tk_widget().pack()

    def load_data(self, file_path):
        self.data = pd.read_csv(file_path)
        self.plot_stock_prices()

    def open_file_dialog(self):
        file_path = filedialog.askopenfilename(filetypes=[('CSV Files', '*.csv')])
        if file_path:
            self.load_data(file_path)
