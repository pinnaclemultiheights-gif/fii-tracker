import datetime
import yfinance as yf

print("FII & Market Data Automation Script Started...")

# 1. Live Market Data / Date fetch karna
try:
    # Yahoo Finance se live indices fetch karne ka setup
    nifty = yf.Ticker("^NSEI")
    vix = yf.Ticker("^INDIAVIX")
    dow = yf.Ticker("YM=F")

    nifty_info = nifty.history(period="1d")
    vix_info = vix.history(period="1d")

    today_date = datetime.datetime.now().strftime("%d-%b-%Y")
    print(f"Fetched latest market data for session: {today_date}")

except Exception as e:
    print(f"Warning while fetching live data: {e}")
    today_date = datetime.datetime.now().strftime("%d-%b-%Y")

# 2. index.html file ko read karna
with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# 3. Values ko update karne ka logic
# Dashboard ki session date ko automatically aaj ki date se replace karna
updated_html = html_content.replace('Latest Session: 10-Nov-2026', f'Latest Session: {today_date}')

# Agar aage aapko aur bhi values (jaise PCR ya prices) replace karni hon, toh aap unhe yahan add kar sakte hain:
# updated_html = updated_html.replace('1.24 (Bullish)', '1.28 (Bullish)')

# 4. Updated HTML ko wapas save karna
with open("index.html", "w", encoding="utf-8") as f:
    f.write(updated_html)

print("index.html successfully updated and saved!")
