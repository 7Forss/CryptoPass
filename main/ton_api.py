import requests
from config import TON_API_KEY

def get_wallet_statistics(wallet_address):
    url = f"https://api.ton.org/getWalletInfo/{wallet_address}?apikey={TON_API_KEY}"
    response = requests.get(url)
    data = response.json()
    balance = float(data['balance']) / 10**9  # Конвертация из нанотонов в тонны
    transactions_count = data['transaction_count']
    total_received = float(data['total_received']) / 10**9
    total_sent = float(data['total_sent']) / 10**9
    return balance, transactions_count, total_received, total_sent