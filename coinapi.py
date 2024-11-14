import requests

def CoinView():
    url = "https://openapiv1.coinstats.app/coins"

    headers = {
        "accept": "application/json",
        "X-API-KEY": "6xocKx4LrIvkrObN+th605Acuj9a/KwZcEi1/FcO2/A="
    }
    response = requests.get(url, headers=headers)
    data = response.json()

    coinData = []
    for i in range(len(data['result'])):
        coin = []
        coin.append((data['result'][i]['id']))
        coin.append((data['result'][i]['name']))
        coin.append((data['result'][i]['price']))
        coin.append((data['result'][i]['marketCap']))
        coin.append((data['result'][i]['availableSupply']))
        coin.append((data['result'][i]['totalSupply']))
        coinData.append(coin)
    for i in coinData:
        print(i)


def Track_wallet(walletId):
    endpoint = str(walletId)


    url = f"https://openapiv1.coinstats.app/wallet/balances?address={endpoint}&networks=all"

    headers = {
        "accept": "application/json",
        "X-API-KEY": "6xocKx4LrIvkrObN+th605Acuj9a/KwZcEi1/FcO2/A="
    }

    responses = requests.get(url, headers=headers)
    return(responses.json())

wallets = []
while True:

    ans = input("Do you want to view the top coins or track a wallet or view all wallets(V or T or X)=  ")
    if ans == 'V':
        CoinView()
    elif ans == 'T':
        wallet_id = str(input("enter wallet address:  "))
        wallets.append(Track_wallet(wallet_id))
    elif ans == 'X':
        print(wallets)



