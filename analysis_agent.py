def analyze(data):
    info = data["info"]

    try:
        roe = info.get("returnOnEquity", None)
        gross_margin = info.get("grossMargins", None)
        pe = info.get("trailingPE", None)

        analysis = {
            "ROE": roe,
            "Gross Margin": gross_margin,
            "PE": pe
        }

    except Exception:
        analysis = {}

    return analysis
