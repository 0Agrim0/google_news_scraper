from scraper_manager import  scraper_manager
import gradio as gr
import matplotlib.pyplot as plt
import  matplotlib.image as mping
import dataframe_image as dfi
import seaborn as sns
from io import BytesIO
from pandas.plotting import table
from bokeh.io import export_png, export_svgs
from bokeh.models import ColumnDataSource, DataTable, TableColumn

def gns(name):
    s_m = scraper_manager()
    # try:
    # type=s_m.two_options()
    # if type=="2":
    #     topic = s_m.topics()
    #     urls = s_m.get_url(topic)
    #     data = s_m.page_data(urls)
    #     s_m.scrap_data_from_page(data)
    #     s_m.dump_data()
    #
    # elif type=="1":
    urls=s_m.search_by_name(name)
    data=s_m.page_data(urls)
    s_m.scrap_data_from_name_page(data)
    df=s_m.dump_data()
    print(df.to_string())
    df=df.head(20)

    dfi.export(df,"df.png")
    ing=mping.imread("df.png")

    return ing



    # except:
    #     s_m.dump_data()



if __name__ == '__main__':
    gr_interface = gr.Interface(fn=gns, inputs="text", outputs="image",title="Google News Scraper")
    gr_interface.launch()


