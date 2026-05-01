def clean_data(raw_data):
    hist = raw_data["history"].reset_index()
    hist = hist[["Date", "Close"]]
    hist.dropna(inplace=True)
    return hist
