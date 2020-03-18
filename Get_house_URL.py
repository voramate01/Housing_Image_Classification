# -*- coding: utf-8 -*-


from lxml import html as myxpath
from requests_html import HTMLSession
import pandas as pd


#############################################################################
##################################### Get all house links #####################

desktop_agents = ['"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"',
                 '"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"',
                 '"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36"',
                 '"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0"',
                 '"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1"',
                 '"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36"',
                 '"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.83 Safari/537.1"',
                 '"Mozilla/5.0 (Windows NT 5.1; rv:33.0) Gecko/20100101 Firefox/33.0"',
                 '"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"',
                 '"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"',
                 '"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0"',
                 '"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299"',
                 '"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0"',
                 '"Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)"',
                 '"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"',
                 '"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"',
                 '"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/603.3.8 (KHTML, like Gecko)"',
                 '"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1 Safari/605.1.15"',
                 '"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/604.3.5 (KHTML, like Gecko) Version/11.0.1 Safari/604.3.5"',
                 '"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"',
                 '"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/604.3.5 (KHTML, like Gecko) Version/11.0.1 Safari/604.3.5"',
                 '"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:57.0) Gecko/20100101 Firefox/57.0"',
                 '"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"',
                 '"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0"',
                 '"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8"',
                 '"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/601.4.4 (KHTML, like Gecko) Version/9.0.3 Safari/601.4.4"',
                 '"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/600.7.12 (KHTML, like Gecko) Version/8.0.7 Safari/600.7.12"',
                 '"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.0.3705; .NET CLR 1.1.4322; Media Center PC 4.0)"',
                 '"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"',
                 '"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"',
                 '"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"',
                 '"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0"',
                 '"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36"']
from random import choice
from time import sleep
import time
from numpy import arange

df= pd.read_csv("GA_zipcode.csv")
df.head()
df.shape
df.City=df.City.apply(lambda x : x.lower().replace(" ","-"))
df['Zip Code'] =df['Zip Code'].apply(lambda x : str(x))
df['wanted'] = df.City +'-ga-'+df['Zip Code']

all_list = []
for i in df.wanted:
    for j in range(1,21):
        mylink='https://www.zillow.com/'+i+'/sold/homes/recently_sold/'+ str(j)+'_p/'
        all_list.append(mylink)
        
#In this website, each zipcode show maximum of 20 page house address
#Some zipcode has less than 20 page.
mother_of_all_list=[]
start = time.time()
house40=['dummy']
marker=0
for i in all_list:  #Collect all houses address url into 1 list.
    try:
        if marker !=0 : #Marker to skip the link if the link is the same of the previous ( will jump to the next zip code) 
            marker-=1
            print("Skip")
            continue
        #Each session, randomly select desktop agent.
        session = HTMLSession(browser_args=["--no-sandbox", '--user-agent='+choice(desktop_agents)])
        page= session.get(i)
        tree = myxpath.fromstring(page.content)
        #Random select sleep time
        sleep(choice(arange (0.25,3, 0.05)))
        #Use xpath to collect house Url
        if tree.xpath('//a[@class="list-card-link list-card-info"]//@href')[0] != house40[0]:
            house40 =tree.xpath('//a[@class="list-card-link list-card-info"]//@href')
            print (house40[0])
            mother_of_all_list.extend(house40)
        else:
            marker=20-int(i.split('/')[-2][0:-2])
    except Exception as err:
        print (err)
end = time.time()
print((end-start)/60 ,"Minute") # Check timelapse

mother_of_all_list=pd.DataFrame(mother_of_all_list, columns=['Url'])
mother_of_all_list.to_csv("mother_of_all_house.csv")
