import requests, json, time
#based on input id from coingecko
#returns current_price, market_cap, volume, price_change_24
#set dicts
trending_data_dict = {0: {'coin_id':[],'coin_name':[],'market_cap_rank':[]}}
price_data_dict = {0:{'name':[],'price':[],'market_cap':[],'price_change':[]}}
def price_checker(id):
    price_data_dict = {0:{'name':[],'price':[],'market_cap':[],'price_change':[]}}
    url = requests.get("https://api.coingecko.com/api/v3/simple/price?ids="+id+"&vs_currencies=usd&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true")
    text = url.text
    data = json.loads(text)
    price_data_dict.clear()
    key = 0
    for x in data:
    #price_data_dict = {0:{'name':[],'price':[],'market_cap':[],'price_change':[]}}
        price_data_dict[key] ={'name':x,'price':data[x]['usd'],'market_cap':data[x]['usd_market_cap'],'price_change':data[x]['usd_24h_change']}
        key+=1   
    return (price_data_dict)
# returns the top 7 trending coins on cg
#returns data
def cg_trending():
    trending_data_dict.clear()
    url = requests.get("https://api.coingecko.com/api/v3/search/trending")
    text = url.text
    data = json.loads(text)
    data2 = data['coins']
    key = 0
    for x in data2:
    #trending_data_dict = {0: {'coin_id':[],'coin_name':[],'market_cap_rank':[]}}
        trending_data_dict[key] ={'coin_id':x['item']['id'],'coin_name':x['item']['name'],'market_cap_rank':x['item']['market_cap_rank']}
        key+=1
    return trending_data_dict

    
#print slowing
def print_slow(lsit):
    for x in lsit:
        for f in lsit[x]:
            for i in lsit[x][f]:
                if i == '\n*********************************************************':
                    print(i,'\n')
                else:
                    for char in i:
                        print(char, end='')
                        time.sleep(.1)
        #print('\n')
    end_string ="END OF CURRENT REPORT PERIOD!!"
    for char in end_string:
        print(char,end='')
        time.sleep(.1)