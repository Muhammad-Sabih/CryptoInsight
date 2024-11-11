class wallet:
    def __init__(self, user_id, api_key):
        self.user_id = user_id
        self.api_key = api_key
        self.balance = {}
        self.transcation = []

    def fetch_wallet_data(self):
        pass

    def update_balance(self):
        pass

    def fetch_transaction_history(self):
        pass

class Transaction:
    def __init__(self, transaction_id, coin, amount, date, transaction_type):
        self.transaction_id = transaction_id
        self.coin = coin
        self.amount = amount
        self.date = date
        self.transaction_type = transaction_type  #buy or sell

    def display_transaction(self):
        pass

class cryptoAPI:
    def __init__(self):
        self.base_url: 'https://api.coingecko.com/api/v3/'

    def get_coin_data(self, coin_id):
        pass

    def get_market_trends(self):
        pass

    def get_historical_data(self, coin_id, days):
        pass

class RecommendationEngine:
    def __init__(self, wallet_data, marlet_data):
        self.wallet_data = wallet_data
        self.market_data = marlet_data

    def calculate_average_holding(self):
        pass

    def recommend_coin(self):
        pass

    def generate_alert(self,coin):
        pass

class Portfolio:
    def __init__(self, user_id, wallet):
        self.user_id = user_id
        self.wallet = wallet
        self.transactions = []
        self.recommendation = []

    def add_transaction(self, transaction):
        pass

    def display_portfolio(self):
        pass

    def get_recommendation(self):
        pass

class Database:
    def __init__(self, db_url):
        self.db_url

    def store_wallet_data(self, wallet_data):
        pass

    def store_transaction(self, transaction):
        pass

    def fetch_user_data(self, user_id):
        pass

    def fetch_wallet_history(self, user_id):
        pass

    class UserInterface:
        def __init__(self):
            self.portfolio = None

        def display_welcome_message(self):
            pass

        def show_wallet_details(self):
            pass

        def show_recommendations(self):
            pass

        def update_wallet(self):
            pass

        def get_user_input(self):
            pass


