import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime




class scraper_manager:

    def __init__(self):
        file_name="_".join(str(datetime.datetime.now().date()).split("-"))+".csv"
        print("The data is going to store in this file: {}   ".format(file_name))
        self.topic="home"
        self.url="https://news.google.com"
        self.data=[]
        self.file_name=file_name


    def two_options(self):
        options={
            "1":"Search by name",
            "2":"Search by topic"
        }
        print(options)
        n=input()
        return n


    def topics(self):
        topic_dict = {"1": "India",
                      "2": "World",
                      "3": "Business",
                      "4": "Technology",
                      "5": "Entertainment",
                      "6": "Sports",
                      "7": "Science",
                      "8": "Health",
                      "9": "ALL"}
        print(topic_dict)
        print('Choose the topic number:')
        topic_id = input()

        return topic_dict[topic_id]

    def get_url(self,topic_name):
        final_url=[]
        url_dict={
            "India":"/topics/CAAqJQgKIh9DQkFTRVFvSUwyMHZNRE55YXpBU0JXVnVMVWRDS0FBUAE",
            "World":"/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRGx1YlY4U0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen",
            "Business":"/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRGx6TVdZU0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen",
            "Technology":"/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRGRqTVhZU0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen",
            "Entertainment":"/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNREpxYW5RU0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen",
            "Sports":"/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRFp1ZEdvU0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen",
            "Science":"/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRFp0Y1RjU0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen",
            "Health":"/topics/CAAqJQgKIh9DQkFTRVFvSUwyMHZNR3QwTlRFU0JXVnVMVWRDS0FBUAE?hl=en-IN&gl=IN&ceid=IN%3Aen"
        }
        if topic_name == 'ALL':
            for topic in url_dict.keys():
                final_url.append([self.url+url_dict[topic],topic])
        else:
            final_url.append([self.url + url_dict[topic_name],topic_name])
        return final_url


    def page_data(self,urls):
        final_data=[]
        for url in urls:
            try:
                print(url[0],url[1])
                data=requests.get(url[0])
                final_data.append([data.text,url[1]])
            except:
                raise TypeError("Url not found")
        return final_data



    def scrap_data_from_page(self,data):

        for text_data in data:
            d=datetime.datetime.now()
            soup = BeautifulSoup(text_data[0], 'html.parser')
            h4_tags = soup.find_all('h4')
            for tag in h4_tags:
                self.data.append([d,tag.text,text_data[1]])


    def scrap_data_from_name_page(self,data):
        for text_data in data:
            d = datetime.datetime.now()
            soup = BeautifulSoup(text_data[0], 'html.parser')
            h4_tags = soup.find_all('h3')
            for tag in h4_tags:
                self.data.append([d, tag.text, text_data[1]])

    def dump_data(self):
        df=pd.DataFrame(self.data,columns=['Date','News','Type'])
        df.to_csv(self.file_name,index=False)
        print("----------------------------------------------Data-Store-------------------------------------------------------------")




    def search_by_name(self):
        name=input("Write the name: ")
        api = [["https://news.google.com/search?q={}&hl=en-IN&gl=IN&ceid=IN%3Aen".format(name),name]]
        return api
