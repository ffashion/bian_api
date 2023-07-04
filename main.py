#!/usr/bin/env python

# curl 'https://fapi.binance.com/fapi/v1/klines?symbol=btcusdt&interval=1d'

import json
import logging
from binance.cm_futures import CMFutures as cm_future
from binance.um_futures import UMFutures as um_future
from binance.lib.utils import config_logging
import functools
import time


def bian_config_log(log_open=True):
    if log_open == True:
        config_logging(logging, logging.DEBUG)
    

def bian_parse_klines(klines:json):
#     [
#   [
#     1607444700000,      // 开盘时间
#     "18879.99",         // 开盘价
#     "18900.00",         // 最高价
#     "18878.98",         // 最低价
#     "18896.13",         // 收盘价(当前K线未结束的即为最新价)
#     "492.363",          // 成交量
#     1607444759999,      // 收盘时间
#     "9302145.66080",    // 成交额
#     1874,               // 成交笔数
#     "385.983",          // 主动买入成交量
#     "7292402.33267",    // 主动买入成交额
#     "0"                 // 请忽略该参数
#   ]
# ]
    if len(klines) == 0:
        return

    # print(klines)
    def cmp(a, b):
        return int(float(a[1]) - float(b[1]))

    def get_local_time(timestamp):
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp/1000))

    max_price = []
    min_price = []

    for kline in klines:
        max_price.append([kline[0], kline[2]])
        min_price.append([kline[0], kline[3]])

    min_price.sort(key=functools.cmp_to_key(cmp))
    max_price.sort(key=functools.cmp_to_key(cmp), reverse=True)

    print("time: %s min_price: %s" %  (get_local_time(min_price[0][0]), min_price[0][1]))
    print("time: %s max_price: %s" %  (get_local_time(max_price[0][0]), max_price[0][1]))
    
    # print(data)
    pass

if __name__ == "__main__":
    bian_config_log(False)

    # cfc = cm_future()
    # cfc.klines("btcusdt", interval="1d")

    ufc = um_future()

    bian_parse_klines(ufc.klines("btcusdt", interval="1d", **{"limit": "100"}))
    # print()











