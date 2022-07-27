import pandas_datareader as web
import datetime as dt
import pandas as pd
from yahoo_fin import stock_info as si

query = input('Screener, Trend_Shares, Portolio: ').lower()


def screener():
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
            week_Change = round(((df['Close'][-1] - df['Close'][-5]) / df['Close'][-5]) * 100, 2)
            month_change = round(((df['Close'][-1] - df['Close'][-27]) / df['Close'][-27]) * 100, 2)
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
                week_Change = round(((df['Close'][-1] - df['Close'][-5]) / df['Close'][-5]) * 100, 2)
                month_change = round(((df['Close'][-1] - df['Close'][-27]) / df['Close'][-27]) * 100, 2)
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
        final_df.to_csv('Screener.csv')


def trend_shares():
    st = dt.datetime.now() - dt.timedelta(days=1825)
    et = dt.datetime.now()

    tickers = pd.read_csv('../Data/Nifty_500.csv')
    symbols = tickers['Symbol'].tolist()
    final_df = pd.DataFrame(
        columns=['Ticker', 'CMP', '1D_return', '1W_return', '1M_return', 'YTD_Returns', '6M_return',
                 'Support', 'Resistance'])
    for symbol in symbols:
        try:
            ticker = symbol + '.NS'
            moving_averages = [50, 100, 200]
            df = web.DataReader(ticker, 'yahoo', st, et)
            for ma in moving_averages:
                df['SMA_' + str(ma)] = round(df['Close'].rolling(window=ma).mean(), 2)
            cmp = round(df['Close'][-1], 2)
            day_Change = round(((df['Close'][-1] - df['Close'][-2]) / df['Close'][-2]) * 100, 2)
            week_Change = round(((df['Close'][-1] - df['Close'][-5]) / df['Close'][-5]) * 100, 2)
            month_change = round(((df['Close'][-1] - df['Close'][-27]) / df['Close'][-27]) * 100, 2)
            ytd = round(((df['Close'][-1] - df['Close']['2022-01-04']) / df['Close']['2022-01-04']) * 100, 2)
            six = round(((df['Close'][-1] - df['Close'][-124]) / df['Close'][-124]) * 100, 2)

            data = round(web.DataReader(ticker, 'yahoo', dt.datetime.now() - dt.timedelta(days=27), dt.datetime.now()),
                         2)
            low = data['Low'].min()
            high = data['Close'].max()

            condition_1 = df['SMA_50'][-1] >= df['SMA_200'][-1]
            condition_2 = cmp >= df['SMA_50'][-1]
            # Support & Resistance level
            condition_3 = cmp > low
            condition_4 = (data['Open'][-1] > data['Open'][-2] > data['Open'][-3]) and (data['Close'][-1] > data['Close'][-2] > data['Close'][-3])

            if condition_1 and condition_2 and condition_3 and condition_4:
                final_df_new = pd.DataFrame({'Ticker': [symbol],
                                             'CMP': [cmp],
                                             '1D_return': [day_Change],
                                             '1W_return': [week_Change],
                                             '1M_return': [month_change],
                                             'YTD_Returns': [ytd],
                                             '6M_return': [six],
                                             'Support': [low],
                                             'Resistance': [high]})
                final_df = pd.concat([final_df, final_df_new])

        except Exception as e:
            print(f'{e} for {symbol}')
        final_df.set_index('Ticker')
        print(final_df)
        final_df.reset_index(drop=True, inplace=True)
        final_df.sort_values(by='6M_return', ascending=False)
        final_df.to_csv('../Data/Bull shares.csv')


def portfolio():
    sd = dt.datetime.now() - dt.timedelta(days=1825)
    ed = dt.datetime.now()

    command = input('Bull_Shares, Zerodha, live: ').lower()

    if 'bull_share' in command:
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
    elif 'zerodha' in command:
        symbols = pd.read_csv('../Data/holdings.csv')
        symbols = symbols['Ticker']

        final_df = pd.DataFrame(columns=['Ticker', 'CMP', 'Buy_Sell', 'Support', 'Resistance'])
        for symbol in symbols:
            try:
                ticker = symbol + ".NS"
                df = web.DataReader(ticker, 'yahoo', sd, ed)
                moving_averages = [50, 100, 200]
                for ma in moving_averages:
                    df['SMA_' + str(ma)] = round(df['Close'].rolling(window=ma).mean(), 2)
                cmp = round(df['Close'][-1], 2)
                six = round(((df['Close'][-1] - df['Close'][-124]) / df['Close'][-124]) * 100, 2)
                ytd = round(((df['Close'][-1] - df['Close']['2022-01-03']) / df['Close']['2022-01-03']) * 100, 2)

                data = round(
                    web.DataReader(ticker, 'yahoo', dt.datetime.now() - dt.timedelta(days=27), dt.datetime.now()),
                    2)
                low = data['Low'].min()
                high = data['Close'].max()

                condition_1 = (df['SMA_50'][-1] >= df['SMA_200'][-1]) and (cmp >= df['SMA_50'][-1])
                condition_2 = six > 0
                # Support & Resistance level
                condition_3 = ((low + high) / 2) < cmp

                buy = 'Buy'
                sell = 'Sell'

                if condition_1 and condition_2 and condition_3:
                    final_df_new = pd.DataFrame({'Ticker': [symbol],
                                                 'CMP': [cmp],
                                                 'Buy_Sell': [buy],
                                                 'Support': [low],
                                                 'Resistance': [high]})
                    final_df = pd.concat([final_df, final_df_new])
                else:
                    final_df_new = pd.DataFrame({'Ticker': [symbol],
                                                 'CMP': [cmp],
                                                 'Buy_Sell': [sell],
                                                 'Support': [low],
                                                 'Resistance': [high]})
                    final_df = pd.concat([final_df, final_df_new])
            except Exception as e:
                print(f'{e} for {symbol}')
            indicator = final_df
            final_df.reset_index(drop=True, inplace=True)
            print(indicator)
    elif 'live' in command:

        cl = ['Ticker', 'Qty', 'Buy']

        tickers = pd.read_csv('../Data/holdings.csv', usecols=cl)
        tickers = pd.DataFrame(tickers)

        while True:
            for ticker in tickers['Ticker']:
                try:
                    symbol = ticker + '.NS'
                    data = si.get_live_price(symbol)
                    cmp = round(data, 2)
                    qty = int(tickers.loc[tickers['Ticker'] == ticker, 'Qty'])
                    buy = round(int(tickers.loc[tickers['Ticker'] == ticker, 'Buy']), 2)
                    profit = round((cmp - buy) * qty, 2)
                    profit_ = round(((cmp - buy) / buy) * 100, 2)

                    # print(f'{ticker} | CMP = {cmp}| Quantity = {qty}| Buying Price = {buy}| Profit = {profit}| Profit% = {profit_}')
                    print(f'Ticker = {ticker}')
                    print(f'Curr_Price = {cmp}')
                    print(f'Quantity = {qty}')
                    print(f'Cost Price = {buy}')
                    print(f'Profit = {profit}')
                    print(f'Profit_% = {profit_}')
                    print(
                        '*******************************************************************************************************')
                except Exception as e:
                    print(f'{e} for {ticker}')


def main():
    if 'screener' in query:
        screener()
    elif 'trend_shares' in query:
        trend_shares()
    elif 'portfolio' in query:
        portfolio()
    else:
        'Please select from the options'
        main()


main()
