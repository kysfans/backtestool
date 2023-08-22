import tkinter as tk
from tkinter import filedialog, ttk


def create_widgets(app):
    create_user_inputs(app)
    create_strategy_menu(app)


def create_user_inputs(app):
    frame = tk.Frame(app.root)
    frame.pack(side=tk.TOP, padx=10, pady=10, anchor="w")

    symbol_label = tk.Label(frame, text="Stock Symbol:")
    symbol_label.pack(side=tk.LEFT, padx=5)

    symbol_entry = tk.Entry(frame, textvariable=app.symbol_var)
    symbol_entry.pack(side=tk.LEFT, padx=5)

    start_date_label = tk.Label(frame, text="Start Date:")
    start_date_label.pack(side=tk.LEFT, padx=5)

    start_date_entry = tk.Entry(frame, textvariable=app.start_date_var)
    start_date_entry.pack(side=tk.LEFT, padx=5)

    end_date_label = tk.Label(frame, text="End Date:")
    end_date_label.pack(side=tk.LEFT, padx=5)

    end_date_entry = tk.Entry(frame, textvariable=app.end_date_var)
    end_date_entry.pack(side=tk.LEFT, padx=5)

    download_button = tk.Button(frame, text="Download Stock Data", command=app.download_stock_data)
    download_button.pack(side=tk.LEFT, padx=5)

    load_button = tk.Button(frame, text="Load Data", command=app.open_file_dialog)
    load_button.pack(side=tk.LEFT, padx=5)

    leverage_label = tk.Label(frame, text="Leverage:")
    leverage_label.pack(side=tk.LEFT, padx=5)

    leverage_entry = tk.Entry(frame, textvariable=app.leverage_var)
    leverage_entry.pack(side=tk.LEFT, padx=5)

    backtest_button = tk.Button(frame, text="Run Backtest", command=app.backtest_strategy)
    backtest_button.pack(side=tk.LEFT, padx=5)

    strategy_label = tk.Label(frame, text="Select Strategy:")
    strategy_label.pack(side=tk.LEFT, padx=5)

    strategy_menu = ttk.OptionMenu(frame, app.strategy_var, " ", *app.strategy)
    strategy_menu.pack(side=tk.LEFT, padx=5)


def create_strategy_menu(app):
    frame = tk.Frame(app.root)
    frame.pack(side=tk.TOP, padx=10, pady=10, anchor="w")

    app.strategy_params_frame = tk.Frame(app.root)
    app.strategy_params_frame.pack(side=tk.TOP, padx=10, pady=10, anchor="w")

    selected_strategy = app.strategy_var.get()
    app.strategy_params = {}
    if selected_strategy == 'Moving_Average_Crossover':
        app.strategy_params['ma1'] = tk.StringVar()
        ma1_label = tk.Label(app.strategy_params_frame, text="MA1:")
        ma1_label.pack(side=tk.LEFT, padx=5)

        ma1_entry = tk.Entry(app.strategy_params_frame, textvariable=app.strategy_params['ma1'])
        ma1_entry.pack(side=tk.LEFT, padx=5)

        app.strategy_params['ma2'] = tk.StringVar()
        ma2_label = tk.Label(app.strategy_params_frame, text="MA2:")
        ma2_label.pack(side=tk.LEFT, padx=5)

        ma2_entry = tk.Entry(app.strategy_params_frame, textvariable=app.strategy_params['ma2'])
        ma2_entry.pack(side=tk.LEFT, padx=5)
