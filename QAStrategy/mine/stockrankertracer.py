import datetime

import pymongo

import QUANTAXIS as QA
from QAStrategy.qastockbase import QAStrategyStockBase


class StockRankerTracer(QAStrategyStockBase):

    def init(self, model = 'backtest'):
        # 设置交易费率
        self.commission = 0.0003
        self.min_commission = 5
        self.init_cash = 100000
        self.open_tax = 0
        self.close_tax = 0.001
        self.refresh_days = 5
        self.running_mode = model

        # 初始账户
        self.init_account()

        # 初始化前一日数据

        # 初始化前一日市场数据

    # 盘前选股
    def before_market_open(self):
        #
        pass

    # 盘中交易
    def on_bar(self, bar):
        pass

    def after_market_close(self):
        pass

if __name__ == '__main__':
    my_tracer = StockRankerTracer(strategy_id='QA_STRATEGY', start='2015-01-01', end=datetime.datetime.now())
    my_tracer.run_sim()
    # MACD.run_backtest()





