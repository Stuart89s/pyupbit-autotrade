import time
import pyupbit
import datetime
import schedule
from fbprophet import Prophet

def predict_price(ticker):
    """prophet으로 당일 종가 가격 예측"""
    global predicted_close_price
    df = pyupbit.get_ohlcv(ticker, interval="minute60")
    df = df.reset_index()
    df['ds'] = df['index']
    df['y'] = df['close']
    data = df[['ds','y']]
    model = prophet()
    model.fit(data)
    future = model.make_future_dataframe(periods=24, freq='h')
    forecast = model.predict(future)
    closedf = forecast[forecast['ds'] == forecast.iloc[-1]['ds'].replace(hour=9)]
    if len(closedf) == 0:
        closedf = forecast[forecast['ds'] == data.iloc[-1]['ds'].replace(hour=9)]
    closevalue = closedf['yhat'].values[0]
    predicted_close_price = closevalue
predict_price("krw-btc")
schedule.every().hour.do(lambda: predict_price("krw-btc"))
