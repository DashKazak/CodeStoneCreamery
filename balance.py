import requests
from key import API_KEY, SECRET

def get_user_balance(customerID):

    url = f'https://alpha-api.usbank.com/innovation/bank-node/customer-accounts/v1/customer/{customerID}/accounts'

    response = requests.get(url, auth=(API_KEY, SECRET)).json()

    balance = response["accounts"][0]["availableCredit"]

    return balance

    