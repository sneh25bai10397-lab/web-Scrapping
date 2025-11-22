import pandas as pd
import requests
from bs4 import BeautifulSoup
product_name= []
Prices= []
description=[]
reviews=[]

for i in range(2,12):

    url="https://www.flipkart.com/search?q=phone+under+20000&as=on&as-show=on&otracker=AS_Query_OrganicAutoSuggest_4_5_na_na_ps&otracker1=AS_Query_OrganicAutoSuggest_4_5_na_na_ps&as-pos=4&as-type=RECENT&suggestionId=phone+under+20000&requestId=dabfa7cb-7ba3-45c5-8a55-f1305ffaa5e9&as-searchtext=phone&page=2"+str(i)


    r   = requests.get(url)

    #print(r)

    soup=BeautifulSoup(r.text,"lxml")
    box=soup.find("div",class_="DOjaWF gdgoEp")

    names= box.find_all("div",class_="KzDlHZ")

    for i in names:
        name= i.text 
        product_name.append(name)

#print(product_name)

    prices= box.find_all("div",class_="Nx9bqj _4b5DiR")

    for i in prices:
        name=i.text
        Prices.append(name)

#print(Prices)    

    desc= box.find_all("ul",class_="G4BRas")

    for i in desc:
         name=i.text
         description.append(name)

#print(description)

    reviewzs=box.find_all("div",class_="XQDdHH")

    for i in reviewzs:
        name=i.text
        reviews.append(name)
print(len(product_name),len(prices),len(description),len(reviews))
#

df=pd.DataFrame({"Product Name" :product_name, "prices": Prices,"description" :description,"REVIEWS": reviews })
#print(df)

df.to_csv("C:/Users/USER/Desktop/pythonflipkart_mobiles_under_20000.csv")    