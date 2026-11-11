import datetime
import yfinance as yf

print("Starting FII & Market Data Automation...")

# 1. Yahoo Finance se Live Indices & Vix fetch karna
try:
    gift_nifty = yf.Ticker("^NSEI") # Ya suitable proxy ticker
    india_vix = yf.Ticker("^INDIAVIX")
    dow_fut = yf.Ticker("YM=F")

    # Latest values nikalna (Sample logic)
    today_date = datetime.datetime.now().strftime("%d-%b-%Y")
    print(f"Data fetched successfully for session: {today_date}")

except Exception as e:
    print(f"Error fetching live data: {e}")

# 2. index.html file ko read karna aur update karna
with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Yahan aapki HTML ke date tag ko automatically update karne ka code
# (Jaise latest session date ko aaj ki date se badalna)
updated_html = html_content.replace('Latest Session: 10-Nov-2026', f'Latest Session: {today_date}')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(updated_html)

print("index.html updated and saved successfully!")
