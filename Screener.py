import pandas_datareader as web
import datetime as dt
import pandas as pd
import nsepy


def Data():
    command = input('5y 1y ytd 6m: ').lower()

    st = dt.datetime.now() - dt.timedelta(days=1825)
    et = dt.datetime.now()

    tickers = pd.read_csv('../Data/Nifty_500.csv')
    tickers = tickers['Symbol'].tolist()
    final_df = pd.DataFrame(
        columns=['Ticker', 'CMP', '1D_return', '1W_return', '1M_return', 'YTD_Returns', '6M_return',
                 '1Y_Return', '3Y_return', '5Y_return'])
    for ticker in tickers:
        try:
            ticker = ticker + '.NS'
            df = web.DataReader(ticker, 'yahoo', st, et)
            cmp = round(df['Close'][-1], 2)
            day_Change = round(((df['Close'][-1] - df['Close'][-2]) / df['Close'][-2]) * 100, 2)
            week_Change = round(((df['Close'][-1] - df['Close'][-6]) / df['Close'][-6]) * 100, 2)
            month_change = round(((df['Close'][-1] - df['Close'][-22]) / df['Close'][-22]) * 100, 2)
            ytd = round(((df['Close'][-1] - df['Close']['2022-01-03']) / df['Close']['2022-01-03']) * 100, 2)
            six = round(((df['Close'][-1] - df['Close'][-124]) / df['Close'][-124]) * 100, 2)
            one_yr = round(((df['Close'][-1] - df['Close'][-248]) / df['Close'][-248]) * 100, 2)
            three_yr = round(((df['Close'][-1] - df['Close'][-742]) / df['Close'][-742]) * 100, 2)
            five_yr = round(((df['Close'][-1] - df['Close'][-1234]) / df['Close'][-1234]) * 100, 2)

            if '5y' in command:
                condition = five_yr > 300
                if condition:
                    final_df_new = pd.DataFrame({'Ticker': [ticker],
                                                 'CMP': [cmp],
                                                 '1D_return': [day_Change],
                                                 '1W_return': [week_Change],
                                                 '1M_return': [month_change],
                                                 'YTD_Returns': [ytd],
                                                 '6M_return': [six],
                                                 '1Y_Return': [one_yr],
                                                 '3Y_return': [three_yr],
                                                 '5Y_return': [five_yr]})
                    final_df = pd.concat([final_df, final_df_new])
            elif '3y' in command:
                condition = three_yr > 200
                if condition:
                    final_df_new = pd.DataFrame({'Ticker': [ticker],
                                                 'CMP': [cmp],
                                                 '1D_return': [day_Change],
                                                 '1W_return': [week_Change],
                                                 '1M_return': [month_change],
                                                 'YTD_Returns': [ytd],
                                                 '6M_return': [six],
                                                 '1Y_Return': [one_yr],
                                                 '3Y_return': [three_yr],
                                                 '5Y_return': [five_yr]})
                    final_df = pd.concat([final_df, final_df_new])
            elif '1y' in command:
                condition = one_yr > 60
                if condition:
                    final_df_new = pd.DataFrame({'Ticker': [ticker],
                                                 'CMP': [cmp],
                                                 '1D_return': [day_Change],
                                                 '1W_return': [week_Change],
                                                 '1M_return': [month_change],
                                                 'YTD_Returns': [ytd],
                                                 '6M_return': [six],
                                                 '1Y_Return': [one_yr],
                                                 '3Y_return': [three_yr],
                                                 '5Y_return': [five_yr]})
                    final_df = pd.concat([final_df, final_df_new])
            elif '6m' in command:
                condition = six > 20
                if condition:
                    final_df_new = pd.DataFrame({'Ticker': [ticker],
                                                 'CMP': [cmp],
                                                 '1D_return': [day_Change],
                                                 '1W_return': [week_Change],
                                                 '1M_return': [month_change],
                                                 'YTD_Returns': [ytd],
                                                 '6M_return': [six],
                                                 '1Y_Return': [one_yr],
                                                 '3Y_return': [three_yr],
                                                 '5Y_return': [five_yr]})
                    final_df = pd.concat([final_df, final_df_new])
            else:
                pass
        except Exception as e:
            print(f'{e} for {ticker}')
            try:
                df = web.DataReader(ticker, 'yahoo', st, et)
                cmp = round(df['Close'][-1], 2)
                day_Change = round(((df['Close'][-1] - df['Close'][-2]) / df['Close'][-2]) * 100, 2)
                week_Change = round(((df['Close'][-1] - df['Close'][-6]) / df['Close'][-6]) * 100, 2)
                month_change = round(((df['Close'][-1] - df['Close'][-22]) / df['Close'][-22]) * 100, 2)
                ytd = round(((df['Close'][-1] - df['Close']['2022-01-03']) / df['Close']['2022-01-03']) * 100, 2)
                six = round(((df['Close'][-1] - df['Close'][-124]) / df['Close'][-124]) * 100, 2)
                one_yr = round(((df['Close'][-1] - df['Close'][-248]) / df['Close'][-248]) * 100, 2)
                three_yr = round(((df['Close'][-1] - df['Close'][0]) / df['Close'][0]) * 100, 2)
                five_yr = round(((df['Close'][-1] - df['Close'][0]) / df['Close'][0]) * 100, 2)
                if '5y' in command:
                    condition = five_yr > 300
                    if condition:
                        final_df_new = pd.DataFrame({'Ticker': [ticker],
                                                     'CMP': [cmp],
                                                     '1D_return': [day_Change],
                                                     '1W_return': [week_Change],
                                                     '1M_return': [month_change],
                                                     'YTD_Returns': [ytd],
                                                     '6M_return': [six],
                                                     '1Y_Return': [one_yr],
                                                     '3Y_return': [three_yr],
                                                     '5Y_return': [five_yr]})
                        final_df = pd.concat([final_df, final_df_new])
                elif '3y' in command:
                    condition = three_yr > 200
                    if condition:
                        final_df_new = pd.DataFrame({'Ticker': [ticker],
                                                     'CMP': [cmp],
                                                     '1D_return': [day_Change],
                                                     '1W_return': [week_Change],
                                                     '1M_return': [month_change],
                                                     'YTD_Returns': [ytd],
                                                     '6M_return': [six],
                                                     '1Y_Return': [one_yr],
                                                     '3Y_return': [three_yr],
                                                     '5Y_return': [five_yr]})
                        final_df = pd.concat([final_df, final_df_new])
                elif '1y' in command:
                    condition = one_yr > 60
                    if condition:
                        final_df_new = pd.DataFrame({'Ticker': [ticker],
                                                     'CMP': [cmp],
                                                     '1D_return': [day_Change],
                                                     '1W_return': [week_Change],
                                                     '1M_return': [month_change],
                                                     'YTD_Returns': [ytd],
                                                     '6M_return': [six],
                                                     '1Y_Return': [one_yr],
                                                     '3Y_return': [three_yr],
                                                     '5Y_return': [five_yr]})
                        final_df = pd.concat([final_df, final_df_new])
                elif '6m' in command:
                    condition = six > 20
                    if condition:
                        final_df_new = pd.DataFrame({'Ticker': [ticker],
                                                     'CMP': [cmp],
                                                     '1D_return': [day_Change],
                                                     '1W_return': [week_Change],
                                                     '1M_return': [month_change],
                                                     'YTD_Returns': [ytd],
                                                     '6M_return': [six],
                                                     '1Y_Return': [one_yr],
                                                     '3Y_return': [three_yr],
                                                     '5Y_return': [five_yr]})
                        final_df = pd.concat([final_df, final_df_new])
                else:
                    pass
            except Exception as e:
                print(f'{e} for {ticker}')
        pd.set_option('display.max_columns', 10)
        final_df.reset_index(drop=True, inplace=True)
        print(final_df)
        final_df.to_csv('Data.csv')


def Shares():
    st = dt.datetime.now() - dt.timedelta(days=1825)
    et = dt.datetime.now()

    tickers = pd.read_csv('../Data/Nifty_500.csv')
    symbols = tickers['Symbol'].tolist()
    final_df = pd.DataFrame(
        columns=['Ticker', 'CMP', '1D_return', '1W_return', '1M_return', 'YTD_Returns', '6M_return'])
    for symbol in symbols:
        try:
            ticker = symbol + '.NS'
            moving_averages = [20, 50, 200]
            df = web.DataReader(ticker, 'yahoo', st, et)
            for ma in moving_averages:
                df['SMA_' + str(ma)] = round(df['Close'].rolling(window=ma).mean(), 2)
            cmp = round(df['Close'][-1], 2)
            day_Change = round(((df['Close'][-1] - df['Close'][-2]) / df['Close'][-2]) * 100, 2)
            week_Change = round(((df['Close'][-1] - df['Close'][-6]) / df['Close'][-6]) * 100, 2)
            month_change = round(((df['Close'][-1] - df['Close'][-22]) / df['Close'][-22]) * 100, 2)
            ytd = round(((df['Close'][-1] - df['Close']['2022-01-03']) / df['Close']['2022-01-03']) * 100, 2)
            six = round(((df['Close'][-1] - df['Close'][-124]) / df['Close'][-124]) * 100, 2)
            data = round(
                web.DataReader(ticker, 'yahoo', dt.datetime.now() - dt.timedelta(days=22), dt.datetime.now()),
                2)
            low = data['Low'].mean()
            high = data['High'].mean()
            vol = data['Volume'].mean()

            sma = round(df['Close'].rolling(20).mean(), 2)
            std = df['Close'].rolling(20).std()
            df['ub'] = round(sma + std * 2, 2)
            df['lb'] = round(sma - std * 2, 2)

            condition_1 = df['SMA_50'][-1] > df['SMA_200'][-1]  # Golden Crossover
            condition_2 = cmp >= df['SMA_20'][-1]  # 20 days Moving Average
            condition_3 = df['ub'][-1] > cmp > df['lb'][-1]  # Bollinger Band
            condition_4 = (df['Close'][-22] < df['Close'][-11] < df['Close'][-1]) and (
                    df['Open'][-22] < df['Open'][-11] < df['Open'][-1]) and month_change > 10  # Higher High Lower Low Strategy
            condition_5 = ((low + high) / 2) < cmp  # Support Resistance Strategy
            condition_6 = df['Volume'][-1] > (vol * 1.5)  # Volume Breakout

            if condition_1 and condition_2 and condition_3 and condition_4 and condition_5 and condition_6:
                final_df_new = pd.DataFrame({'Ticker': [symbol],
                                             'CMP': [cmp],
                                             '1D_return': [day_Change],
                                             '1W_return': [week_Change],
                                             '1M_return': [month_change],
                                             'YTD_Returns': [ytd],
                                             '6M_return': [six]})
                final_df = pd.concat([final_df, final_df_new])

        except Exception as e:
            print(f'{e} for {symbol}')
        final_df.set_index('Ticker')
        print(final_df)
        final_df.reset_index(drop=True, inplace=True)
    final_df.sort_values(by='1M_return', ascending=True)
    final_df.to_csv(f'../Data/Swing_Trades.csv')


def Share_Data():
    st = dt.datetime.now() - dt.timedelta(days=1825)
    et = dt.datetime.now()

    while True:
        ticker = input('Enter Ticker: ') + '.NS'
        moving_averages = [20, 50, 200]
        df = web.DataReader(ticker, 'yahoo', st, et)
        for ma in moving_averages:
            df['SMA_' + str(ma)] = round(df['Close'].rolling(window=ma).mean(), 2)
        cmp = round(df['Close'][-1], 2)
        month_change = round(((df['Close'][-1] - df['Close'][-22]) / df['Close'][-22]) * 100, 2)
        data = round(
            web.DataReader(ticker, 'yahoo', dt.datetime.now() - dt.timedelta(days=22), dt.datetime.now()),
            2)
        low = data['Low'].min()
        high = data['High'].max()

        sma = round(df['Close'].rolling(20).mean(), 2)
        std = df['Close'].rolling(20).std()
        df['ub'] = round(sma + std * 2, 2)
        df['lb'] = round(sma - std * 2, 2)

        condition_1 = df['SMA_50'][-1] > df['SMA_200'][-1]  # Golden Crossover
        condition_2 = cmp >= df['SMA_20'][-1]  # 20 days Moving Average
        condition_3 = df['ub'][-1] > cmp > df['lb'][-1]  # Bollinger Band
        condition_4 = (df['Close'][-22] < df['Close'][-10] < df['Close'][-1]) and (
                df['Open'][-22] < df['Open'][-10] < df['Open'][
            -1]) and month_change > 10  # Higher High Lower Low Strategy
        condition_5 = ((low + high) / 2) < cmp  # Support Resistance Strategy

        print(f"Current Price = {round(df['Close'][-1], 2)}")
        print(f"SMA_20= {df['SMA_20'][-1]}")
        print(f"SMA_50= {df['SMA_50'][-1]}")
        print(f"SMA_200= {df['SMA_200'][-1]}")

        if condition_1:
            print('Golden Crossover = Bullish')
        else:
            print('Golden Crossover = Bearish')

        if condition_2:
            print(f'20 DMA = Bullish at {df["SMA_20"][-1]}')
        else:
            print(f'20 DMA = Bearish at {df["SMA_20"][-1]}')

        if condition_3:
            print('Bollinger Band = Bullish')
        else:
            print('Bollinger Band = Bearish')

        if condition_4:
            print('Higher High Lower Low = Bullish')
        else:
            print('Higher High Lower Low = Bearish')

        if condition_5:
            print(f'Support_Resistance = Bullish at {((low + high) / 2)}')
        else:
            print(f'Support_Resistance = Bearish at {((low + high) / 2)}')


def Portfolio():
    sd = dt.datetime.now() - dt.timedelta(days=1825)
    ed = dt.datetime.now()
    symbol = pd.read_csv('../Data/Bull shares.csv')
    symbol = symbol['Ticker'].tolist()
    inv_date = input('Enter Date yyyy-mm-dd: ')
    final_df = pd.DataFrame(
        columns=['Ticker', 'Investment', 'Curr_price', 'Profit', 'Profit_perc'])
    for ticker in symbol:
        try:
            symbols = ticker + '.NS'
            data = web.DataReader(symbols, 'yahoo', sd, ed)
            cmp = round(data['Close'][-1], 2)
            inv = round(data['Close'][inv_date], 2)
            profit = round((cmp - inv), 2)
            profit_ = round((profit / inv) * 100, 2)

            final_df_new = pd.DataFrame({'Ticker': [ticker],
                                         'Investment': [inv],
                                         'Curr_price': [cmp],
                                         'Profit': [profit],
                                         'Profit_perc': profit_})
            final_df = pd.concat([final_df, final_df_new])
            portfolio = final_df
            print(portfolio)
            portfolio.to_csv(f'../Data/Portfolio dated {inv_date}.csv')
        except Exception as e:
            print(f'{e} for {ticker}')


def main():
    query = input('Data, Shares, Share_Data: ')
    if 'Data' in query:
        Data()
    elif 'Shares' in query:
        Shares()
    elif 'Share_Data' in query:
        Share_Data()
    elif 'Portfolio' in query:
        Portfolio()
    else:
        print('Please select from the options')
        main()


main()
