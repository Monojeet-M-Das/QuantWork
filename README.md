
# 📊 Nifty 50 Moving Average Crossover Strategy with OpenAI GPT Analysis

This project implements a simple quantitative trading strategy — the **Moving Average Crossover** — on the Nifty 50 index using Python. It uses OpenAI's GPT model to analyze the performance and suggest improvements to the strategy.

## 🔍 Strategy Summary

- **Instrument**: Nifty 50 Index (`^NSEI`)
- **Method**: 50-day and 200-day Simple Moving Average (SMA) crossover
- **Backtest Period**: 2020–2024
- **Output**: Buy/Sell signals, performance metrics, and GPT-4o-powered AI commentary

## 💻 Tech Stack

- `Python`
- `pandas`, `numpy`, `matplotlib`
- `yfinance`
- `openai`

## 🚀 Getting Started

### 1. Install Requirements

```bash
pip install -r requirements.txt
```

### 2. Run the Script

```bash
python nifty_crossover.py
```

## 🤖 GPT Commentary (Optional)

Get AI-powered insights by adding your [OpenAI API key](https://platform.openai.com/api-keys):

```python
client = OpenAI(api_key="your-api-key-here")
```

## 📄 License

MIT License

