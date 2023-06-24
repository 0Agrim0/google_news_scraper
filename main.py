from scraper_manager import  scraper_manager

def main():
    s_m = scraper_manager()
    try:
        topics=s_m.topics()
        print('Choose the topic number:')
        topic_id=input()

        urls=s_m.get_url(topics[topic_id])
        data=s_m.page_data(urls)
        s_m.scrap_data_from_page(data)
        s_m.dump_data()

    except:
        s_m.dump_data()



if __name__ == '__main__':
    main()


