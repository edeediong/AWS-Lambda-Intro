import json
import decimal


def lambda_handler(event, context):
    
    print(event)
    if 'body' in event:
        event = json.loads(event["body"])
        
    amount = float(event["amount"])
    res = []
    coins = [1,5,10,25]
    coin_lookup = {25: "quarters", 10: "dimes", 5: "nickles", 1: "pound"}
    coin = coins.pop()
    num, rem = divmod(int(amount*100), coin)
    res.append({num:coin_lookup[coin]})
    while rem > 0:
        coin = coins.pop()
        num, rem = divmod(rem, coin)
        if num:
            if coin in coin_lookup:
                res.append({num:coin_lookup[coin]})
                
    response = {
        "statusCode": "200",
        "headers": { "Content-type": "application/json" },
        "body": json.dumps({"res": res})
    }
    
    return response