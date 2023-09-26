"""
Esse robo analisa a média movel do grafico e abre a ordem caso o preço cruze a média de baixo para cima

By: George Telles
+55 11 93290-7425
"""

import MetaTrader5 as mt5
import pandas as pd
import pandas_ta as ta
import time

mt5.initialize()

symbol = "WINV23"
lot = 1.0
request = {}
resulta = 0
position_id = 0


while True:
    data = pd.DataFrame(mt5.copy_rates_from_pos(symbol, mt5.TIMEFRAME_M1, 0, 90))
    data["time"] = pd.to_datetime(data["time"], unit = "s")
    positions_total = mt5.positions_total()

    data["mm9"] = data.ta.sma(9)

    media = (list(data["mm9"])[-1])
    fechamento = (list(data["close"])[-1])

    print(f"Posições abertas: {positions_total}")
    print(f"Média: {media}")
    print(f"Valor Atual: {fechamento}")
    


    if(fechamento > media and positions_total == 0):
        print("Comprando...")
        point = mt5.symbol_info(symbol).point
        price = mt5.symbol_info_tick(symbol).ask
        deviation = 20
        request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": symbol,
            "volume": lot,
            "type": mt5.ORDER_TYPE_BUY,
            "price": price,
            "sl": price - 100 * point,
            "tp": price + 100 * point,
            "deviation": deviation,
            "magic": 234000,
            "comment": "python script open",
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": mt5.ORDER_FILLING_RETURN,
        }
        result = mt5.order_send(request)
        print("1. order_send(): by {} {} lots at {} with deviation={} points".format(symbol,lot,price,deviation));
        if result.retcode != mt5.TRADE_RETCODE_DONE:
            print("2. order_send failed, retcode={}".format(result.retcode))

    elif(fechamento < media and positions_total > 0):
        print("fechar posição")
        price = mt5.symbol_info_tick(symbol).bid
        deviation = 20
        request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": symbol,
            "volume": lot,
            "type": mt5.ORDER_TYPE_SELL,
            "price": price,
            "deviation": deviation,
            "magic": 234000,
            "comment": "python script close",
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": mt5.ORDER_FILLING_RETURN,
        }
        result = mt5.order_send(request)
        print("3. close position #{}: sell {} {} lots at {} with deviation={} points".format(position_id,symbol,lot,price,deviation));
    elif(fechamento > media and positions_total < 0):
        print("Robô em operação")
    else:
        print("Aguardando Sinal")

    time.sleep(10)
