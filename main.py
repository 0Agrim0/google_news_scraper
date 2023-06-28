from scraper_manager import  scraper_manager

def main():
    s_m = scraper_manager()
    try:
        n=s_m.two_options()
        if n=="2":
            topic = s_m.topics()
            urls = s_m.get_url(topic)
            data = s_m.page_data(urls)
            s_m.scrap_data_from_page(data)
            s_m.dump_data()

        elif n=="1":
            urls=s_m.search_by_name()
            data=s_m.page_data(urls)
            s_m.scrap_data_from_name_page(data)
            s_m.dump_data()



    except:
        s_m.dump_data()



if __name__ == '__main__':
    main()


