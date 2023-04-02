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
 
        informative_pairs = [
                                ("AAVE/USDT", "15m"),
                                ("AAVE/USDT", "1h"),
                                ("AAVE/USDT", "1d"),
                                ("ADA/USDT", "15m"),
                                ("ADA/USDT", "1h"),
                                ("ADA/USDT", "1d"),
                                ("ALGO/USDT", "15m"),
                                ("ALGO/USDT", "1h"),
                                ("ALGO/USDT", "1d"),
                                ("ANKR/USDT", "15m"),
                                ("ANKR/USDT", "1h"),
                                ("ANKR/USDT", "1d"),
                                ("ATM/USDT", "15m"),
                                ("ATM/USDT", "1h"),
                                ("ATM/USDT", "1d"),
                                ("ATOM/USDT", "15m"),
                                ("ATOM/USDT", "1h"),
                                ("ATOM/USDT", "1d"),
                                ("AVA/USDT", "15m"),
                                ("AVA/USDT", "1h"),
                                ("AVA/USDT", "1d"),
                                ("AVAX/USDT", "15m"),
                                ("AVAX/USDT", "1h"),
                                ("AVAX/USDT", "1d"),
                                ("BTC/USDT", "15m"),
                                ("BTC/USDT", "1h"),
                                ("BTC/USDT", "1d"),
                                ("DASH/USDT", "15m"),
                                ("DASH/USDT", "1h"),
                                ("DASH/USDT", "1d"),
                                ("DOGE/USDT", "15m"),
                                ("DOGE/USDT", "1h"),
                                ("DOGE/USDT", "1d"),
                                ("DOT/USDT", "15m"),
                                ("DOT/USDT", "1h"),
                                ("DOT/USDT", "1d"),
                                ("EGLD/USDT", "15m"),
                                ("EGLD/USDT", "1h"),
                                ("EGLD/USDT", "1d"),
                                ("ENJ/USDT", "15m"),
                                ("ENJ/USDT", "1h"),
                                ("ENJ/USDT", "1d"),
                                ("EOS/USDT", "15m"),
                                ("EOS/USDT", "1h"),
                                ("EOS/USDT", "1d"),
                                ("ETC/USDT", "15m"),
                                ("ETC/USDT", "1h"),
                                ("ETC/USDT", "1d"),
                                ("ETH/USDT", "15m"),
                                ("ETH/USDT", "1h"),
                                ("ETH/USDT", "1d"),
                                ("FIL/USDT", "15m"),
                                ("FIL/USDT", "1h"),
                                ("FIL/USDT", "1d"),
                                ("FTM/USDT", "15m"),
                                ("FTM/USDT", "1h"),
                                ("FTM/USDT", "1d"),
                                ("IOTA/USDT", "15m"),
                                ("IOTA/USDT", "1h"),
                                ("IOTA/USDT", "1d"),
                                ("IOTX/USDT", "15m"),
                                ("IOTX/USDT", "1h"),
                                ("IOTX/USDT", "1d"),
                                ("KAVA/USDT", "15m"),
                                ("KAVA/USDT", "1h"),
                                ("KAVA/USDT", "1d"),
                                ("KSM/USDT", "15m"),
                                ("KSM/USDT", "1h"),
                                ("KSM/USDT", "1d"),
                                ("LINK/USDT", "15m"),
                                ("LINK/USDT", "1h"),
                                ("LINK/USDT", "1d"),
                                ("LPT/USDT", "15m"),
                                ("LPT/USDT", "1h"),
                                ("LPT/USDT", "1d"),
                                ("LTC/USDT", "15m"),
                                ("LTC/USDT", "1h"),
                                ("LTC/USDT", "1d"),
                                ("MANA/USDT", "15m"),
                                ("MANA/USDT", "1h"),
                                ("MANA/USDT", "1d"),
                                ("MASK/USDT", "15m"),
                                ("MASK/USDT", "1h"),
                                ("MASK/USDT", "1d"),
                                ("MATIC/USDT", "15m"),
                                ("MATIC/USDT", "1h"),
                                ("MATIC/USDT", "1d"),
                                ("NEO/USDT", "15m"),
                                ("NEO/USDT", "1h"),
                                ("NEO/USDT", "1d"),
                                ("QTUM/USDT", "15m"),
                                ("QTUM/USDT", "1h"),
                                ("QTUM/USDT", "1d"),
                                ("SAND/USDT", "15m"),
                                ("SAND/USDT", "1h"),
                                ("SAND/USDT", "1d"),
                                ("SOL/USDT", "15m"),
                                ("SOL/USDT", "1h"),
                                ("SOL/USDT", "1d"),
                                ("STX/USDT", "15m"),
                                ("STX/USDT", "1h"),
                                ("STX/USDT", "1d"),
                                ("SUSHI/USDT", "15m"),
                                ("SUSHI/USDT", "1h"),
                                ("SUSHI/USDT", "1d"),
                                ("TRX/USDT", "15m"),
                                ("TRX/USDT", "1h"),
                                ("TRX/USDT", "1d"),
                                ("UNI/USDT", "15m"),
                                ("UNI/USDT", "1h"),
                                ("UNI/USDT", "1d"),
                                ("VET/USDT", "15m"),
                                ("VET/USDT", "1h"),
                                ("VET/USDT", "1d"),
                                ("XLM/USDT", "15m"),
                                ("XLM/USDT", "1h"),
                                ("XLM/USDT", "1d"),
                                ("XMR/USDT", "15m"),
                                ("XMR/USDT", "1h"),
                                ("XMR/USDT", "1d"),
                                ("XRP/USDT", "15m"),
                                ("XRP/USDT", "1h"),
                                ("XRP/USDT", "1d"),
                                        ]
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
