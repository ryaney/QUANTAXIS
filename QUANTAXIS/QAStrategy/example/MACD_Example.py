import datetime
import pprint

import QUANTAXIS as QA
from QUANTAXIS.QAStrategy import QAStrategyCTABase
from QUANTAXIS.QAStrategy.qastockbase import QAStrategyStockBase


class MACD(QAStrategyStockBase):

    def on_bar(self, bar):

        res = self.macd()

        print(res.iloc[-1])

        if res.DIF[-1] > res.DEA[-1]:

            print('LONG')

            if self.positions.volume_long == 0:
                self.send_order('BUY', 'OPEN', price=bar['close'], volume=100)
            # if self.positions.volume_short > 0:
            #     self.send_order('BUY', 'CLOSE', price=bar['close'], volume=100)

        else:
            print('SHORT')
            # if self.positions.volume_short == 0:
                # self.send_order('SELL', 'OPEN', price=bar['close'], volume=100)
            if self.positions.volume_long > 0:
                self.send_order('SELL', 'CLOSE', price=bar['close'], volume=100)

    def macd(self,):
        return QA.QA_indicator_MACD(self.market_data)

    def risk_check(self):
        pass
        # pprint.pprint(self.qifiacc.message)


if __name__ == '__main__':
    MACD = MACD(code='600519', frequence='5min', data_host='localhost', mongo_ip='localhost', trade_host='localhost', send_wx=True,
                strategy_id='1dds1s2d-7902-4a85-adb2-fbac4bb977fg', start='2022-01-01', end=datetime.datetime.now())
    MACD.run_sim()
    # MACD.run_backtest()
