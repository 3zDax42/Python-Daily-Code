import requests
import datetime
import matplotlib.pyplot as plt


API_Key = "e76jJThypGmJUdsjrtZXXJ69fkGyVDwe"
Ticker = "GOOG"
Start_Date = "2020-01-01"
End_Date = "2024-01-01"

def Fetch_Stock_Data(Ticker, Start_Date, End_Date):
    URL = f"https://api.polygon.io/v2/aggs/ticker/{Ticker}/range/1/day/{Start_Date}/{End_Date}"

    params = {
        "adjusted" : "true",
        "sort" : "asc",
        "limit" : 50000,
        "apiKey" : API_Key
    }

    Response = requests.get(URL, params = params)

    Data = Response.json()

    if "results" not in Data:
        print("Error:", Data.get("error", "Unknown issue"))
        return []
    
    return Data["results"]



# ___________ Main ___________ #

Stock_Data = Fetch_Stock_Data(Ticker, Start_Date, End_Date)

for day in Stock_Data[:5]:
    Date = datetime.datetime.fromtimestamp(day["t"] / 1000).strftime("%Y-%m-%d")
    print(f"{Date} | Open: {day['o']} | High: {day['h']} | Low: {day['l']} | Close: {day['c']}")

if not Stock_Data:
    print("No data returned. Check the API key, ticker, or date range.")
else:
    Dates = [datetime.datetime.fromtimestamp(day["t"] / 1000) for day in Stock_Data]

    Close_Prices = [day["c"] for day in Stock_Data]

    plt.figure(figsize=(12, 6))
    plt.plot(Dates, Close_Prices, label=f'{Ticker} Closing Price', color = "green")
    plt.title(f'{Ticker} Stock Price ( Since IPO)')
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
