import yfinance as yf

def fetch_data(ticker):
    stock = yf.Ticker(ticker)

    info = stock.info
    financials = stock.financials
    balance_sheet = stock.balance_sheet
    hist = stock.history(period="1y")

    return {
        "info": info,
        "financials": financials,
        "balance": balance_sheet,
        "history": hist
    }
