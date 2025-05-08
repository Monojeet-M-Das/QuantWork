# Quant Project: AI-Assisted Moving Average Crossover Strategy on Nifty 50 (OpenAI SDK v1.x)

import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import openai
import warnings
warnings.filterwarnings("ignore")

# Download Nifty 50 data
ticker = "^NSEI"
data = yf.download(ticker, start="2020-01-01", end="2024-12-31")[['Close']].dropna()

# Moving Averages
short_window = 50
long_window = 200
data['SMA50'] = data['Close'].rolling(window=short_window).mean()
data['SMA200'] = data['Close'].rolling(window=long_window).mean()

# Signals
data['Signal'] = 0
data.loc[data['SMA50'] > data['SMA200'], 'Signal'] = 1
data['Position'] = data['Signal'].shift(1)
data['Returns'] = data['Close'].pct_change()
data['Strategy_Returns'] = data['Returns'] * data['Position']

# Calculate rolling volatility (30-day window)
data['Volatility'] = data['Returns'].rolling(window=30).std() * np.sqrt(252)  # annualized

# Plot
plt.figure(figsize=(12, 6))
(1 + data[['Returns', 'Strategy_Returns']]).cumprod().plot()
plt.title("Nifty 50 Strategy vs Buy-and-Hold")
plt.ylabel("Cumulative Returns")
plt.grid(True)
plt.show()

# Plot Volatility
plt.figure(figsize=(12, 5))
plt.plot(data['Volatility'], label='30-day Rolling Volatility', color='purple')
plt.title('Nifty 50 Volatility Over Time')
plt.ylabel('Annualized Volatility')
plt.grid(True)
plt.legend()
plt.show()

# Metrics
total_return = (1 + data['Strategy_Returns']).prod() - 1
market_return = (1 + data['Returns']).prod() - 1
sharpe_ratio = data['Strategy_Returns'].mean() / data['Strategy_Returns'].std() * np.sqrt(252)
print(f"Total Strategy Return: {total_return:.2%}")
print(f"Buy & Hold Return: {market_return:.2%}")
print(f"Sharpe Ratio: {sharpe_ratio:.2f}")

# OpenAI v1.x (ensure you installed `openai>=1.0.0`)
from openai import OpenAI

client = OpenAI(api_key="your_API_key_here")

prompt = f"""
A crossover strategy on Nifty 50 (SMA50 vs SMA200) gave {total_return:.2%} return vs market's {market_return:.2%} with Sharpe {sharpe_ratio:.2f}.
Explain this result like a finance quant and suggest one improvement.
"""

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a finance quant expert."},
        {"role": "user", "content": prompt}
    ]
)

print("\n🧠 GPT Analysis:")
print(response.choices[0].message.content)