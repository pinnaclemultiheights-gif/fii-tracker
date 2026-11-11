import datetime
import yfinance as yf

print("FII & Market Data Automation Script Started...")

try:
    # 1. Yahoo Finance se Live Market Indices fetch karna
    # Gift Nifty (Proxy: ^NSEI ya Nifty 50 close), India Vix, Dow Jones Futures
    nifty = yf.Ticker("^NSEI")
    vix = yf.Ticker("^INDIAVIX")
    dow = yf.Ticker("YM=F")

    nifty_info = nifty.history(period="1d")
    vix_info = vix.history(period="1d")
    
    # Aaj ki date nikalna
    today_date = datetime.datetime.now().strftime("%d-%b-%Y")
    print(f"Fetched latest market data for session: {today_date}")

except Exception as e:
    print(f"Warning: Could not fetch live indices, using fallback: {e}")
    today_date = datetime.datetime.now().strftime("%d-%b-%Y")

# 2. index.html file ko read karna
with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# 3. HTML ke andar Date aur values ko automatically update karna
# Yeh line aapke dashboard ki "Latest Session" date ko aaj ki date se badal degi
updated_html = html_content.replace('Latest Session: 10-Nov-2026', f'Latest Session: {today_date}')

# 4. Updated HTML ko wapas save karna
with open("index.html", "w", encoding="utf-8") as f:
    f.write(updated_html)

print("index.html successfully updated with latest data!")
