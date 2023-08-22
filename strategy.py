import pandas as pd


def investment_strategy(data, initial_investment, leverage, select_strategy):
    if data is not None:
        # 初始化變數
        buy_signal = 0
        sell_signal = 0
        position = 0
        buy_price = 0
        cost = initial_investment
        income = cost
        total_income = 0
        trade_history = []

        if select_strategy == "Long_Term_Holding":
            buy_signal = 1
            # 創建交易歷史列表

            # 遍歷數據
            for index, row in data.iterrows():
                if buy_signal == 1:
                    # 進行買入
                    buy_price = row['Close']
                    cost = initial_investment
                    position = initial_investment / buy_price
                    buy_signal = 0
                    sell_signal = 1
                    income = cost
                elif sell_signal == 1:
                    # 進行賣出
                    income = (1 + ((row['Close'] - buy_price) / buy_price) * float(leverage)) * float(cost)
                    position = 0
                    print(income)

                # 將交易紀錄添加到列表中
                trade_history.append({
                    'Date': row['Date'],
                    'Position': position,
                    'Buy_Signal': buy_signal,
                    'Sell_Signal': sell_signal,
                    'Buy_Price': buy_price,
                    'Cost': cost,
                    'Income': income
                })

            # 將交易歷史列表轉換為DataFrame
            trade_history_df = pd.DataFrame(trade_history)

            return trade_history_df

        elif select_strategy == "Moving_Average":
            data['Moving_Average'] = data['Close'].rolling(window=20).mean()
            for index, row in data.iterrows():
                if not buy_signal and row['Close'] > row['Moving_Average']:
                    # 進行買入
                    buy_price = row['Close']
                    position = cost / buy_price
                    buy_signal = True
                    sell_signal = False
                    print("cost = ", cost)
                elif buy_signal and row['Close'] < row['Moving_Average']:
                    # 進行賣出
                    income = position * row['Close']
                    position = 0
                    buy_signal = False
                    sell_signal = True
                    cost = income
                    print ("income =", income)

                # 將交易紀錄添加到列表中
                trade_history.append({
                    'Date': row['Date'],
                    'Position': position,
                    'Buy_Signal': buy_signal,
                    'Sell_Signal': sell_signal,
                    'Buy_Price': buy_price,
                    'Cost': cost,
                    'Income': income
                })

                # 將交易歷史列表轉換為DataFrame
            trade_history_df = pd.DataFrame(trade_history)

            return trade_history_df

        elif select_strategy == "Moving_Average_Crossover":
            data['Short_Moving_Average'] = data['Close'].rolling(window=7).mean()
            data['Long_Moving_Average'] = data['Close'].rolling(window=20).mean()
            for index, row in data.iterrows():
                if not buy_signal and row['Short_Moving_Average'] > row['Long_Moving_Average']:
                    # 進行買入
                    buy_price = row['Close']
                    position = cost / buy_price
                    buy_signal = True
                    sell_signal = False
                    print("cost = ", cost)
                elif buy_signal and row['Long_Moving_Average'] < row['Short_Moving_Average']:
                    # 進行賣出
                    income = position * row['Close']
                    position = 0
                    buy_signal = False
                    sell_signal = True
                    cost = income
                    print ("income =", income)

                # 將交易紀錄添加到列表中
                trade_history.append({
                    'Date': row['Date'],
                    'Position': position,
                    'Buy_Signal': buy_signal,
                    'Sell_Signal': sell_signal,
                    'Buy_Price': buy_price,
                    'Cost': cost,
                    'Income': income
                })

                # 將交易歷史列表轉換為DataFrame
            trade_history_df = pd.DataFrame(trade_history)

            return trade_history_df

        elif select_strategy == "Gil_Blake_Trading":
            for index in range(1, len(data)):
                yesterday_close = data.loc[index - 1, 'Close']
                today_close = data.loc[index, 'Close']
                if not buy_signal and today_close > yesterday_close:
                    # 進行買入
                    buy_price = today_close
                    position = cost / buy_price
                    buy_signal = True
                    sell_signal = False
                    print("cost = ", cost)
                elif buy_signal:
                    # 進行賣出
                    income = position * today_close
                    position = 0
                    buy_signal = False
                    sell_signal = True
                    cost = income
                    print ("income =", income)

                # 將交易紀錄添加到列表中
                trade_history.append({
                    'Date': data.loc[index ,'Date'],
                    'Position': position,
                    'Buy_Signal': buy_signal,
                    'Sell_Signal': sell_signal,
                    'Buy_Price': buy_price,
                    'Cost': cost,
                    'Income': income
                })

                # 將交易歷史列表轉換為DataFrame
            trade_history_df = pd.DataFrame(trade_history)

            return trade_history_df