import matplotlib.pyplot as plt

def generate_chart(df, ticker):
    plt.figure()
    plt.plot(df["Date"], df["Close"])
    plt.title(f"{ticker} Price Trend")
    plt.xlabel("Date")
    plt.ylabel("Price")

    file_path = f"{ticker}_chart.png"
    plt.savefig(file_path)
    plt.close()

    return file_path
