from .unibit import UniBit as ub


class StockPrice(ub):

    def getRealTimeStockPrice(self, ticker, startDate, endDate, startMinute, endMinute, size=None, selectedFields="all",
                              datatype='json'):
        """ Get real time stock prices
        Keyword Arguments:
            ticker: Company ticker
            datatype: Data type of response. Either 'json' or 'csv'
            size: Integer (n) which will have the response return the latest n prices.
                    If unspecified, all real time results will be returned, going back 1 month.
        """

        # endpoints = ['realtime']
        if isinstance(ticker, list):
            ticker = ",".join(ticker)
        else:
            raise TypeError('ticker input should be a list')

        endpoints = "stock/realtime"

        return self.make_request(endpoints=endpoints,
                                 data={'tickers': ticker, 'startDate': startDate, 'endDate': endDate,
                                       'startMinute': startMinute, 'endMinute': endMinute, 'datatype': datatype,
                                       'size': size})

    def getHistoricalStockPrice(self, ticker, startDate, endDate, interval=1, selectedFields="all", datatype='json'):
        """ Get real time stock prices
        Keyword Arguments:
            ticker: Company ticker
            date_range: Range to grab historical prices,
                            either 1m, 3m, 1y, 3y, 5y, 10y, or 20y
            interval: A positive number (n). If passed, chart data will
                        return every nth element as defined by Interval
            datatype: Data type of response. Either 'json' or 'csv'
        """

        # if range not in ['1m', '3m', '1y', '3y', '5y', '10y', '20y']:
        # 	raise ValueError('Unsupported range value')

        # if (not isinstance(interval, int) or interval <= 0):
        # 	raise ValueError('Interval must be a positive integer')

        # endpoints = ['historical']
        if isinstance(ticker, list):
            ticker = ",".join(ticker)
        else:
            raise TypeError('ticker input should be a list')

        endpoints = "stock/historical"

        return self.make_request(endpoints=endpoints,
                                 data={'tickers': ticker, 'startDate': startDate, 'endDate': endDate,
                                       'datatype': datatype})
