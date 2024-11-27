from tensorflow.keras.models import load_model

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # '0': all logs, '1': warnings, '2': errors, '3': none

model = load_model('./LSTM_stock_predict.keras')
print(model.summary())


import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler


# Define parameters
start_time = '2005-01-01'
end_time = '2024-10-05'
split_ratio = 0.8
stock_symbol = 'NVDA'  # Replace with the desired stock symbol

# Download data
data = yf.download(stock_symbol, start=start_time, end=end_time)

# Flatten MultiIndex columns if necessary
if isinstance(data.columns, pd.MultiIndex):
    data.columns = data.columns.get_level_values(0)

# Calculate Future_Price and Target
data['Future_Price'] = data['Close'].shift(-60)
data['Target'] = ((data['Future_Price'] - data['Close']) / data['Close']) * 100
data.dropna(inplace=True)



features = data[['Open', 'High', 'Low', 'Close', 'Volume']]
target = data['Target']

scaler = MinMaxScaler(feature_range=(0, 1))
scaled_features = scaler.fit_transform(features)

recent_data = scaled_features[-60:]
recent_data = np.expand_dims(recent_data, axis=0)

# Predict future percentage increase
future_prediction = model.predict(recent_data)
print(f'Predicted Percentage Increase over the Next Three Months: {future_prediction[0][0]:.2f}%')