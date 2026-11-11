import datetime

# Aaj ki date automatically nikalne ke liye
today_str = datetime.datetime.now().strftime("%d-%b-%Y")
print(f"Running automated FII/DII data script for: {today_str}")

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Yahan aap date update hone ka logic ya apna data fetch karke index.html me inject kar sakte hain
print("index.html loaded successfully for automated update.")
