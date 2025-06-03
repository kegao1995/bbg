import yfinance as yf
import plotext as plt


def show_quote(ticker: str) -> None:
    t = yf.Ticker(ticker)
    try:
        info = t.fast_info
        last_price = info.get("lastPrice")
        open_price = info.get("open")
        high = info.get("dayHigh")
        low = info.get("dayLow")
        volume = info.get("lastVolume")
    except Exception as e:
        print(f"Error retrieving data for {ticker}: {e}")
        return
    print(f"\n{ticker.upper()} Quote")
    print("Last Price:", last_price)
    print("Open:", open_price)
    print("High:", high)
    print("Low:", low)
    print("Volume:", volume)


def show_chart(ticker: str) -> None:
    t = yf.Ticker(ticker)
    try:
        hist = t.history(period="1mo")
    except Exception as e:
        print(f"Error retrieving data for {ticker}: {e}")
        return
    if hist.empty:
        print("No data available.")
        return
    plt.clt()
    plt.date_form("Y-m-d")
    plt.title(f"{ticker.upper()} 1 Month Close")
    plt.plot(hist.index.strftime("%Y-%m-%d").to_list(), hist["Close"].to_list())
    plt.show()


def main() -> None:
    print("Mini Bloomberg Terminal (Simplified)")
    while True:
        print("\nMenu: 1) Quote  2) Chart  q) Quit")
        choice = input("Select option: ").strip()
        if choice == "1":
            tick = input("Enter ticker: ").strip()
            if tick:
                show_quote(tick)
        elif choice == "2":
            tick = input("Enter ticker: ").strip()
            if tick:
                show_chart(tick)
        elif choice.lower() == "q":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
