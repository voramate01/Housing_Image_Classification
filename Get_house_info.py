# -*- coding: utf-8 -*-

from time import sleep
from bs4 import BeautifulSoup
import csv
from random import choice
from requests_html import HTMLSession
import pandas as pd
from numpy import arange
from lxml import html as myxpath


 ####### GET PIC LINK FROM CSV FILE AND DOWNLOAD THEM ########################3#######################
everything= pd.read_csv("mother_of_all_house.csv")

#Add header so we are less likely to get detected as a bot
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
 

####################################################################################################################################################################################################################################################################################################################
#
# Create a file to write to, add headers row
f = csv.writer(open('pic_links.csv', 'a', newline='' , encoding="utf-8"))
#Write first row (header)
f.writerow(['Adress','Price','Beds_Baths_Sqft','Sold_date','Home_type','Year_built','Heating','Cooling','Parking','Lot_size','Picture_links','Description'])



for j in everything.Url :
    try:
        print(j)
        
        sleep(choice(arange (0.025,2, 0.01)))#Randomly select sleep time
        session2 = HTMLSession(browser_args=["--no-sandbox", '--user-agent='+choice(desktop_agents)])
        r= session2.get(j)   
        r.html.render() 
        tree = myxpath.fromstring(r.content)
        soup = BeautifulSoup(r.text, 'html.parser')
        
        ### Find Address ###
        find_address= soup.find("h1",class_="zsg-h1").get_text(" ")

        try:
            ####  Find picture ### 
            find_pic =soup.find("div",class_="hdp-photo-carousel") 
            find_pic2= tree.xpath('//div[@class="hdp-photo-carousel"]//div//img/@src')
            find_pic3= tree.xpath('//div[@class="hdp-photo-carousel"]//div//img/@href')
            print (find_pic)
            print (find_pic2)
            print (find_pic3)
                
            
        except Exception as error:
            print (" ---Picture information is missing--- ")
            pic_link =[]
            
   
        try : #Additional info

            ### Find Bed bath sqrt ###
            find_info =soup.find("h3", class_="edit-facts-light").get_text(" ")
            find_info =find_info.replace("\xa0 ","")
        except Exception as error:
            print (" ---Bed bath sqrt information is missing--- ")
            find_info =""
                       
        try :    
            ###Find Sold price ###
            find_price= soup.find("div",class_="status").get_text().replace(" Sold: ","")
        except Exception as error:
            print (" ---Sold price information is missing--- ")
            find_price =""
                       
        try :    
            ###Find Sold date ###
            find_sold_date =soup.find("div",class_="zsg-fineprint date-sold").get_text()
        except Exception as error:
            print (" ---Sold date information is missing--- ")
            find_sold_date =""
                       
        try :    
            ###Find Basic home info ###
            find_basic = soup.find("div", class_="home-facts-at-a-glance-section").get_text("^").replace("\xa0^","^").split("^")
            #home type
            find_home_type = find_basic[2]        
            #Year built
            find_year_built =find_basic[5]
            #heating
            find_heating =find_basic[8]
            #cooling
            find_cooling =find_basic[11]
            #parking
            find_parking =find_basic[14]
            #lot size
            find_lot =find_basic[17]
        except Exception as error:
            print (" ---Some basic home information is missing--- ")
            find_home_type=""
            find_year_built=""
            find_heating=""
            find_cooling=""
            find_parking=""
            find_lot=""
            
        try : 
            ###Find Home Description ###
            find_description = soup.find("div",class_="Text-sc-1vuq29o-0 sc-iAyFgw bqyLcL").get_text()
        except Exception as error:
            print (" ---Home description information is missing--- ")
            find_description =""
            
                       
            
        ### Write rows to csv file ###
        f.writerow([find_address,find_price, find_info, find_sold_date, find_home_type,find_year_built
                    ,find_heating, find_cooling , find_parking, find_lot , pic_link, find_description])
    
       # print (find_address, pic_link, find_home_type,find_year_built
        #       ,find_heating, find_cooling , find_parking, find_lot, find_sold_date)
            
    except Exception as error:
        print ("[~] No important address information / HTTP Connection error / Encounter RECAPTCHA")
        print ("[~] This address is not be collected. ")
        print ("[~] Error Occured : %s" % (error))
    

del f