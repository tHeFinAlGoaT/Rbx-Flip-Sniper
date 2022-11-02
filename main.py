import time
import requests


while True:
    # Get the info from the API
    r = requests.get('https://api.rbxflip.com/roblox/shop')
    # Convert the info to a dictionary
    data = r.json()
    # authorization
    token = ''

    # Get the rates from the dictionary
    for value in data:
        rates = value['rate']

        # Get the values needed to buy
        if 0.1 <= value['rate'] <= 1.8:
            user_asset_id = value['userAsset']['userAssetId']
            user_id = value['userAsset']['userId']
            relative_price = value['price']
            # Send request to get balance
            burp0_url = "https://api.rbxflip.com:443/wallet/balance"
            burp0_headers = {"X-Socket-Id": "RjaheDcBtKEmDRtQAB3l", "Authorization": token, "Sec-Ch-Ua-Mobile": "?0", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36", "Sec-Ch-Ua": "\"Chromium\";v=\"103\", \".Not/A)Brand\";v=\"99\"", "Sec-Ch-Ua-Platform": "\"Windows\"", "Accept": "*/*", "Origin": "https://www.rbxflip.com", "Sec-Fetch-Site": "same-site", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://www.rbxflip.com/", "Accept-Encoding": "gzip, deflate", "Accept-Language": "it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7"}
            s = requests.get(burp0_url, headers=burp0_headers)
            # Convert balance to json
            balancedata = s.json()
            # Actually get the balance
            balance = balancedata['balance']
            print(balance)
            # Check if the balance is enough to buy
            if balance >= relative_price:
                # get the actual full price of the asset 
                price = round(relative_price, 0)
                # Send request to buy the asset
                x_burp0_url = "https://api.rbxflip.com:443/roblox/shop/buy"
                x_burp0_headers = {"X-Socket-Id": "lSzxyOry5rYlgJaTAB78", "Authorization": token, "Sec-Ch-Ua-Mobile": "?0", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36", "Sec-Ch-Ua": "\"Chromium\";v=\"103\", \".Not/A)Brand\";v=\"99\"", "Sec-Ch-Ua-Platform": "\"Windows\"", "Content-Type": "application/json", "Accept": "*/*", "Origin": "https://www.rbxflip.com", "Sec-Fetch-Site": "same-site", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://www.rbxflip.com/", "Accept-Encoding": "gzip, deflate", "Accept-Language": "it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7"}
                x_burp0_json=[{"expectedPrice": price, "userAssetId": user_asset_id, "userId": user_id}]
                g = requests.post(x_burp0_url, headers=x_burp0_headers, json=x_burp0_json)
            else:
                print("daaam bro you broke")
    time.sleep(10)
