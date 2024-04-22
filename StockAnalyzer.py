import stockanalyzer as sa
stock_code = 'AAPL'
start_date = '2020-01-01'
end_date = '2021-12-31'
df = sa.get_stock_data(stock_code, start_date, end_date)
df['SMA'] = sa.calculate_sma(df['Close'], window=20)
df['RSI'] = sa.calculate_rsi(df['Close'], window=14)
df['Upper Band'], df['Lower Band'] = sa.calculate_bollinger_bands(df['Close'], window=20, std_dev=2)
sa.plot_stock_data(df, indicators=['SMA', 'RSI'], signals=True)
sa.plot_bollinger_bands(df, window=20, std_dev=2)
sa.plot_returns(df['Returns'])
sa.plot_stock_data(df, indicators=['SMA', 'RSI'], signals=True)
sa.plot_bollinger_bands(df, window=20, std_dev=2)
sa.plot_returns(df['Returns'])
