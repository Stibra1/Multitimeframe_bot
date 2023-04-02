from pandas import DataFrame
from freqtrade.strategy import (IStrategy, IntParameter, informative)
import talib.abstract as ta

class Multitimeframe(IStrategy):
    timeframe = '5m'
    informative_timeframes = ['15m', '1h', '1d']

    minimal_roi = {"0": 1}

    stoploss = -0.35
    use_sell_signal = True
    sell_profit_only = False
    process_only_new_candles = True
    startup_candle_count = 100

    INTERFACE_VERSION = 3


    buy_rsi = IntParameter(15, 50, default=45, space='buy')
    buy_fastk = IntParameter(50, 99, default=81, space='buy')
    sell_rsi = IntParameter(50, 90, default=78, space='sell')
    sell_fastk = IntParameter(50, 100, default=62, space='sell')
    buy_rsi_15m = IntParameter(15, 50, default=49, space='buy')
    buy_fastk_15m = IntParameter(50, 99, default=69, space='buy')
    sell_rsi_15m = IntParameter(50, 90, default=56, space='sell')
    sell_fastk_15m = IntParameter(50, 100, default=69, space='sell')
    buy_rsi_1h = IntParameter(15, 50, default=46, space='buy')
    buy_fastk_1h = IntParameter(50, 99, default=72, space='buy')
    sell_rsi_1h = IntParameter(50, 90, default=69, space='sell')
    sell_fastk_1h = IntParameter(50, 100, default=95, space='sell')

    def informative_pairs(self):
 
        pairs = self.dp.current_whitelist()
        informative_pairs = [(pair, self.informative_timeframe) for pair in pairs]
        return informative_pairs

    @informative('15m')    
    @informative('1h')
    @informative('1d')

    def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        stoch_fast = ta.STOCHF(dataframe, 5, 3, 0, 3, 0)
        dataframe['fastd'] = stoch_fast['fastd']
        dataframe['fastk'] = stoch_fast['fastk']
        macd = ta.MACD(dataframe)
        dataframe['macd'] = macd['macd']
        dataframe['macdsignal'] = macd['macdsignal']
        dataframe['macdhist'] = macd['macdhist']
        dataframe['rsi'] = ta.RSI(dataframe, timeperiod=14)
        return dataframe


    def populate_entry_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:

        
        dataframe.loc[
            (
                    (dataframe['rsi'] < self.buy_rsi.value) &
                    (dataframe['macd'] > dataframe['macdsignal'] ) &
                    (dataframe['fastk'] > dataframe['fastd'] ) &
                    (dataframe['fastk']  < self.buy_fastk.value) 

            ),
            ['enter_long', 'enter_tag']] = (1, 'Buy_5m')

        dataframe.loc[
            (
                    (dataframe['rsi_15m'] < self.buy_rsi_15m.value) &
                    (dataframe['macd_15m'] > dataframe['macdsignal_15m'] ) &
                    (dataframe['fastk_15m'] > dataframe['fastd_15m'] ) &
                    (dataframe['fastk_15m']  < self.buy_fastk_15m.value) 

            ),
            ['enter_long', 'enter_tag']] = (1, 'Buy_15m')

        dataframe.loc[
            (
                    (dataframe['rsi_1h'] < self.buy_rsi_1h.value) &
                    (dataframe['macd_1h'] > dataframe['macdsignal_1h'] ) &
                    (dataframe['fastk_1h'] > dataframe['fastd_1h'] ) &
                    (dataframe['fastk_1h']  < self.buy_fastk_1h.value) 

            ),
            ['enter_long', 'enter_tag']] = (1, 'Buy_1h')
        
       
        return dataframe
    
    def populate_exit_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:

        
        dataframe.loc[
            (
                (dataframe['rsi'] > self.sell_rsi.value) &
                (dataframe['macd'] < dataframe['macdsignal']) &
                (dataframe['fastk'] < dataframe['fastd']) &
                (dataframe['fastk'] > self.sell_fastk.value) &
                (dataframe['volume'] > 0)
            ),
            ['exit_long', 'exit_tag']] = (1, 'Sell_5m')

        dataframe.loc[
            (
                (dataframe['rsi_15m'] > self.sell_rsi_15m.value) &
                (dataframe['macd_15m'] < dataframe['macdsignal_15m']) &
                (dataframe['fastk_15m'] < dataframe['fastd_15m']) &
                (dataframe['fastk_15m'] > self.sell_fastk_15m.value) &
                (dataframe['volume_15m'] > 0)
            ),
            ['exit_long', 'exit_tag']] = (1, 'Sell_15m')

        dataframe.loc[
            (
                (dataframe['rsi_1h'] > self.sell_rsi_1h.value) &
                (dataframe['macd_1h'] < dataframe['macdsignal_1h']) &
                (dataframe['fastk_1h'] < dataframe['fastd_1h']) &
                (dataframe['fastk_1h'] > self.sell_fastk_1h.value) &
                (dataframe['volume_1h'] > 0)
            ),
            ['exit_long', 'exit_tag']] = (1, 'Sell_1h')
          
        
        return dataframe