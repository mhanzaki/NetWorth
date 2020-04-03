import json
import matplotlib.pyplot as plt
import os

BTC_CAD_RATE = 9591.89
ETH_CAD_RATE = 200.8


class ShowNetWorth:

    def __init__(self):
        self.transactions = None
        self.net_worth = []
        self.btc_balance = 0.0
        self.eth_balance = 0.0
        self.cad_balance = 0.0
        self.btc_cad_rate = BTC_CAD_RATE
        self.eth_cad_rate = ETH_CAD_RATE
        self.created_at = []

    def load_transactions(self):
        print(os.path.join(os.getcwd(), 'transactions.json'))
        with open('transactions.json', 'r') as f:
            self.transactions = json.load(f)

    def get_balance(self, transaction):
        if str(transaction['direction']).lower() == 'credit':
            debit_credit = 1
        elif str(transaction['direction']).lower() == 'debit':
            debit_credit = -1
        else:
            return
        if str(transaction['currency']).upper() == 'BTC':
            self.btc_balance += debit_credit * float(transaction['amount'])
        elif str(transaction['currency']).upper() == "ETH":
            self.eth_balance += debit_credit * float(transaction['amount'])
        elif str(transaction['currency']).upper() == 'CAD':
            self.cad_balance += debit_credit * float(transaction['amount'])
        self.created_at.append(transaction['createdAt'])

    def get_net_worth(self):
        return self.cad_balance + (self.btc_balance * self.btc_cad_rate) + (self.eth_balance * self.eth_cad_rate)

    def calculate_net_worth(self):
        self.load_transactions()
        for transaction in self.transactions:
            self.get_balance(transaction)
            self.net_worth.append(self.get_net_worth())
        return self.net_worth

    def plot_net_worth(self):
        plt.plot(self.net_worth)
        plt.show()

    def show_net_worth(self):
        self.plot_net_worth()


if __name__ == '__main__':
    show_networth = ShowNetWorth()
    show_networth.calculate_net_worth()
    show_networth.show_net_worth()

