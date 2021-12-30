#Terminal CG Return
# import the requirements
#Written By Message in Blood Studios
#Coded by Arismoth
import  price_helper
import datetime, time,os
coins_to_price = []
# set some classes for colors because yay
# Python program to print
# colored text and background
class colors:
#Colors class:reset all colors with colors.reset; two
#sub classes fg for foreground
#and bg for background; use as colors.subclass.colorname.
#i.e. colors.fg.red or colors.bg.greenalso, the generic bold, disable,
#underline, reverse, strike through,
#and invisible work with the main class i.e. colors.bold#
    reset='\033[0m'
    bold='\033[01m'
    disable='\033[02m'
    underline='\033[04m'
    reverse='\033[07m'
    strikethrough='\033[09m'
    invisible='\033[08m'
    class fg:
        black='\033[30m'
        red='\033[31m'
        green='\033[32m'
        orange='\033[33m'
        blue='\033[34m'
        purple='\033[35m'
        cyan='\033[36m'
        lightgrey='\033[37m'
        darkgrey='\033[90m'
        lightred='\033[91m'
        lightgreen='\033[92m'
        yellow='\033[93m'
        lightblue='\033[94m'
        pink='\033[95m'
        lightcyan='\033[96m'
    class bg:
        black='\033[40m'
        red='\033[41m'
        green='\033[42m'
        orange='\033[43m'
        blue='\033[44m'
        purple='\033[45m'
        cyan='\033[46m'
        lightgrey='\033[47m'
print('*********************************************************')
print('*********************************************************')
print('*******',colors.fg.green, 'COIN-GECKO TRENDING ',colors.reset,'**************************')
print('*******',colors.fg.red,'MESSAGE IN BLOOD STUDIOS ',colors.reset,'**********************')
print('*******',colors.bold,'CODED BY: ARISMOTH ',colors.reset,'****************************')
print('*********************************************************')
print('*********************************************************\n')
time.sleep(10)
#this returns print_data_dict for printing to terminal at slow pace
print_data_dict = {0:{'l1':[],'l2':[],'l3':[],'l4':[],'l5':[],'l6':[],'l7':[]}}

def prior_print():
    raw_data = price_helper.cg_trending()
    #trending_data_dict = {0: {'coin_id':[],'coin_name':[],'market_cap_rank':[]}}
    for key in raw_data:
        coins_to_price.append(raw_data[key]['coin_id'])
    for_id = '%2c'.join(coins_to_price)
    prices = price_helper.price_checker(for_id)
    now = datetime.datetime.now()
    dt_for_print = now.strftime("%c")
    key=0
    for x in prices:
    #price_data_dict = {0:{'name':[],'price':[],'market_cap':[],'price_change':[]}}
    #print_data_dict = {0:{'l1':[],'l2':[],'l3':[],'l4':[],'l5':[],'l6':[],'l7':[],'l8':[]}}
    #price_data_dict[key] ={'name':x,'price':data[x]['usd'],'market_cap':data[x]['usd_market_cap'],'price_change':data[x]['usd_24h_change']}
        if prices[x]['price_change'] > 0:
            pos = colors.fg.green
        elif prices[x]['price_change'] < 0:
            pos = colors.fg.red
        else:
            pos = colors.reset
        if prices[x]['price'] < 1:
            price_format = "${:,.7f}"
        else:
            price_format = "${:,.2f}"
        y = x+1
        print_data_dict[key] = {'l1':[colors.bold,colors.underline,colors.fg.purple,'Trending Number: ', str(y),colors.reset,colors.fg.blue, '\nAs OF: ', colors.reset,str(dt_for_print)], 'l2':['\n*********************************************************'],'l3':[colors.fg.yellow,'Coin Name: ',colors.reset,colors.bold, prices[x]['name'].upper(),colors.reset],'l4':[colors.fg.yellow,'\nPrice: ',colors.reset,price_format.format((prices[x]['price']))],'l5':[colors.fg.yellow,'\n24_hr_Change: ',pos, "{:,.2f}%".format((prices[x]['price_change']))],'l6':[colors.fg.yellow,'\nMarket Cap: ',colors.reset, "${:,.2f}".format((prices[x]['market_cap']))],'l7':['\n*********************************************************']}
       

        key+=1
    return print_data_dict
#Main Loop
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    to_print = prior_print()
    price_helper.print_slow(to_print)
    time.sleep(300)