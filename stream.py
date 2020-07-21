import config
import websocket
import json


def on_open(ws):
    print("Opened")
    auth_data = {
        "action": "authenticate",
        "data": {"key_id": config.API_KEY,
                 "secret_key": config.SECRET_KEY}
    }
    ws.send(json.dumps(auth_data))
    listen_message = {"action": "listen", "data": {"streams": ["AM.TSLA"]}}
    ws.send(json.dumps(listen_message))


def on_message(ws, message):
    print('<< Incoming Message...')
    print(message)


def on_close(ws):
    print("Closed")


def on_error(ws):
    print("Error")


socket = "wss://data.alpaca.markets/stream"

ws = websocket.WebSocketApp(socket, on_open=on_open, on_message=on_message,
                            on_close=on_close, on_error=on_error)
ws.run_forever()

#{"action": "authenticate", "data": {"key_id": "PKLDFKW8BHZE0LGACG6N", "secret_key": "cejbieGOXWoEc/kCPkni4O12KmU32TaROYOWJVcn"}}


# {"action": "listen", "data": {"streams": ["T.SPY"]}}
