import tkinter as tk
import requests
import time

# Function to fetch and update prices
def get_crypto_price():
    try:
        url = "https://api.coingecko.com/api/v3/simple/price"
        params = {
            'ids': 'bitcoin,ethereum',
            'vs_currencies': 'usd,inr'
        }
        response = requests.get(url, params=params)
        data = response.json()

        btc_price = data['bitcoin']
        eth_price = data['ethereum']

        btc_label.config(text=f"Bitcoin:\n${btc_price['usd']} / ₹{btc_price['inr']}")
        eth_label.config(text=f"Ethereum:\n${eth_price['usd']} / ₹{eth_price['inr']}")
        updated_label.config(text=f"Last updated: {time.strftime('%H:%M:%S')}")

    except Exception as e:
        btc_label.config(text="Error fetching price")
        eth_label.config(text="")
        updated_label.config(text="")

# Setup GUI
root = tk.Tk()
root.title("Live Crypto Tracker")
root.geometry("350x300")
root.resizable(False, False)
root.configure(bg="#1e1e1e")

title = tk.Label(root, text="Crypto Price Tracker", font=("Arial", 18, "bold"), fg="white", bg="#1e1e1e")
title.pack(pady=10)

btc_label = tk.Label(root, text="", font=("Arial", 14), fg="#f2a900", bg="#1e1e1e")
btc_label.pack(pady=10)

eth_label = tk.Label(root, text="", font=("Arial", 14), fg="#3c3c3d", bg="#1e1e1e")
eth_label.pack(pady=10)

updated_label = tk.Label(root, text="", font=("Arial", 10), fg="gray", bg="#1e1e1e")
updated_label.pack(pady=5)

refresh_button = tk.Button(root, text="Refresh", command=get_crypto_price, font=("Arial", 12), bg="#0f0", fg="black")
refresh_button.pack(pady=10)

# Load prices on start
get_crypto_price()

root.mainloop()
