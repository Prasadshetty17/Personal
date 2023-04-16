import datetime as dt
import pandas as pd
import yfinance as si
import time

def Share_Market():
    def swing_trades():
        starttime = time.time()
        st = dt.datetime.now() - dt.timedelta(days=365)
        et = dt.datetime.now()

        tickers = pd.read_csv('../Codes/Data/Nifty_500.csv')
        symbols = tickers['Ticker'].tolist()
        final_df = pd.DataFrame(
            columns=['Ticker', 'CMP', '1W_return', '1M_return', '6M_return', 'Trend', '20_EMA', '50_EMA'])
        for symbol in symbols:
            try:
                ticker = symbol + '.NS'
                print(symbol)
                moving_averages = [9, 20, 50, 200]
                df = si.download(ticker, st, et)
                for ma in moving_averages:
                    df['SMA_' + str(ma)] = round(df['Close'].ewm(span=ma).mean(), 2)
                cmp = round(df['Close'][-1], 2)
                day_Change = round(((df['Close'][-1] - df['Close'][-2]) / df['Close'][-2]) * 100, 2)
                week_Change = round(((df['Close'][-1] - df['Close'][-5]) / df['Close'][-5]) * 100, 2)
                month_change = round(((df['Close'][-1] - df['Close'][-22]) / df['Close'][-22]) * 100, 2)
                six = round(((df['Close'][-1] - df['Close'][-124]) / df['Close'][-124]) * 100, 2)

                low = df['Low'].rolling(22).mean()
                high = df['High'].rolling(22).mean()

                sma = round(df['Close'].rolling(20).mean(), 2)
                std = df['Close'].rolling(20).std()
                df['ub'] = round(sma + std * 2, 2)
                df['lb'] = round(sma - std * 2, 2)

                ma_20 = df['SMA_20'][-1]
                ma_50 = df['SMA_50'][-1]

                if df['Close'][-1] > df['SMA_9'][-1]:
                    trend = 'In Trend'
                else:
                    trend = 'Check for 6months'

                condition_1 = df['SMA_200'][-1] < df['SMA_50'][-1] < df['SMA_20'][-1]  # Golden Crossover
                condition_2 = cmp >= df['SMA_20'][-1]  # 20 days Moving Average
                condition_3 = df['ub'][-1] > cmp > df['lb'][-1]  # Bollinger Band
                condition_4 = (df['Close'][-22] < df['Close'][-11] < df['Close'][-1]) and (
                        df['Open'][-22] < df['Open'][-11] < df['Open'][
                    -1]) and month_change > 10  # Higher High Lower Low Strategy
                condition_5 = ((low[-1] + high[-1]) / 2) < cmp  # Support Resistance Strategy
                condition_6 = df['SMA_50'][-1] > df['SMA_50'][-2] > df['SMA_50'][-3]

                if condition_1 and condition_2 and condition_3 and condition_4 and condition_5 and condition_6:
                    final_df_new = pd.DataFrame({'Ticker': [symbol],
                                                 'CMP': [cmp],
                                                 '1W_return': [week_Change],
                                                 '1M_return': [month_change],
                                                 '6M_return': [six],
                                                 'Trend': [trend],
                                                 '20_EMA': [ma_20],
                                                 '50_EMA': [ma_50]})
                    final_df = pd.concat([final_df, final_df_new])

            except Exception as e:
                print(f'{e} for {symbol}')
            final_df.reset_index(drop=True, inplace=True)
            print(final_df)
            final_df.to_csv(f'../Codes/Data/Trending_Shares.csv')
            endtime = time.time()
            print(f'Time taken in total = {round((endtime - starttime) / 60, 2)} mins')

    def week_data():
        starttime = time.time()
        st = dt.datetime.now() - dt.timedelta(days=365)
        et = dt.datetime.now()

        tickers = pd.read_csv('../Codes/Data/Nifty_500.csv')
        symbols = tickers['Ticker'].tolist()
        final_df = pd.DataFrame(
            columns=['Ticker', 'CMP', '1D_return', '1W_return', '2W_return', '3W_return', '4W_return', '5W_return',
                     '6W_return'])
        for symbol in symbols:
            try:
                ticker = symbol + '.NS'
                print(symbol)
                moving_averages = [5, 9, 20, 50, 200]
                df = si.download(ticker, st, et)
                for ma in moving_averages:
                    df['SMA_' + str(ma)] = round(df['Close'].ewm(span=ma).mean(), 2)
                cmp = round(df['Close'][-1], 2)
                day_Change = round(((df['Close'][-1] - df['Close'][-2]) / df['Close'][-2]) * 100, 2)
                week_1 = round(((df['Close'][-1] - df['Close'][-5]) / df['Close'][-5]) * 100, 2)
                week_2 = round(((df['Close'][-5] - df['Close'][-10]) / df['Close'][-10]) * 100, 2)
                week_3 = round(((df['Close'][-10] - df['Close'][-15]) / df['Close'][-15]) * 100, 2)
                week_4 = round(((df['Close'][-15] - df['Close'][-20]) / df['Close'][-20]) * 100, 2)
                week_5 = round(((df['Close'][-20] - df['Close'][-25]) / df['Close'][-25]) * 100, 2)
                week_6 = round(((df['Close'][-25] - df['Close'][-30]) / df['Close'][-30]) * 100, 2)
                month_change = round(((df['Close'][-1] - df['Close'][-22]) / df['Close'][-22]) * 100, 2)

                low = df['Low'].rolling(22).mean()
                high = df['High'].rolling(22).mean()

                sma = round(df['Close'].rolling(20).mean(), 2)
                std = df['Close'].rolling(20).std()
                df['ub'] = round(sma + std * 2, 2)
                df['lb'] = round(sma - std * 2, 2)

                condition_1 = df['SMA_200'][-1] < df['SMA_50'][-1] < df['SMA_20'][-1]  # Golden Crossover
                condition_2 = cmp >= df['SMA_20'][-1]  # 20 days Moving Average
                condition_3 = df['ub'][-1] > cmp > df['lb'][-1]  # Bollinger Band
                condition_4 = (df['Close'][-22] < df['Close'][-11] < df['Close'][-1]) and (
                        df['Open'][-22] < df['Open'][-11] < df['Open'][
                    -1]) and month_change > 10  # Higher High Lower Low Strategy
                condition_5 = ((low[-1] + high[-1]) / 2) < cmp  # Support Resistance Strategy
                condition_6 = df['SMA_50'][-1] > df['SMA_50'][-2] > df['SMA_50'][-3]

                if condition_1 and condition_2 and condition_3 and condition_4 and condition_5 and condition_6:
                    final_df_new = pd.DataFrame({'Ticker': [symbol],
                                                 'CMP': [cmp],
                                                 '1D_return': [day_Change],
                                                 '1W_return': [week_1],
                                                 '2W_return': [week_2],
                                                 '3W_return': [week_3],
                                                 '4W_return': [week_4],
                                                 '5W_return': [week_5],
                                                 '6W_return': [week_6]})
                    final_df = pd.concat([final_df, final_df_new])

            except Exception as e:
                print(f'{e} for {symbol}')
            final_df.reset_index(drop=True, inplace=True)
            print(final_df)
            final_df.to_csv(f'../Codes/Data/{date}_Week_wise_Data.csv')
            endtime = time.time()
            print(f'Time taken in total = {round((endtime - starttime) / 60, 2)} mins')

    def EMA_55():
        tickers = pd.read_csv('../Codes/Data/Nifty_500.csv')
        tickers = tickers['Ticker'].tolist()
        final_df = pd.DataFrame(
            columns=['Ticker', 'CMP', '55 EMA', 'Low'])

        sd = dt.datetime.now() - dt.timedelta(365)
        ed = dt.datetime.now()

        for ticker in tickers:
            print(ticker)
            try:
                tick = ticker + '.NS'
                data = si.download(tick, sd, ed)

                moving_average = [55]
                for ma in moving_average:
                    data['EMA_' + str(ma)] = data['Close'].ewm(span=ma, adjust=False).mean()

                cmp = round(data['Close'][-1])
                EMA_55 = round(data['EMA_55'][-1])
                low = round(data['Low'][-1])
                open = round(data['Open'][-1])

                condition_1 = cmp > EMA_55
                condition_2 = (open or low) <= EMA_55
                condition_3 = cmp > open
                condition_4 = data['EMA_55'][-15] < data['EMA_55'][-1]

                if condition_1 and condition_2 and condition_3 and condition_4:
                    final_df_new = pd.DataFrame({'Ticker': [ticker],
                                                 'CMP': [cmp],
                                                 '55 EMA': [EMA_55],
                                                 'Low': [low]})

                    final_df = pd.concat([final_df, final_df_new])
            except Exception as e:
                print(f'{e} for {ticker}')

            final_df.reset_index(drop=True, inplace=True)
            print(final_df)
            final_df.to_csv(f'../Codes/Data/{date}_EMA_55.csv')
    print('Select options from below')
    Command = input('swing_trades, week_data, EMA_55: ')
    if 'swing_trades' in Command:
        swing_trades()
    if 'week_data' in Command:
        week_data()
    if 'EMA_55' in Command:
        EMA_55()


Share_Market()
