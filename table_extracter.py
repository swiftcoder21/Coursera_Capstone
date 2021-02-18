import bs4
import pandas as pd
import numpy as np
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

columns = []
list_inside = []
my_url = "https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M"
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")
big_container = page_soup.findAll("div", {"id":"mw-content-text"}) 
table_container = big_container[0].findAll("table")  
row_table = table_container[0].findAll("tr")
each_row = row_table[0].findAll("th")
dataframe = {}

for x in each_row:
    columns.append(x.text.rstrip("\n"))
for row_container in row_table:
    row_list = row_container.findAll("td")
    for x in row_list:
        list_inside.append(x.text.rstrip("\n"))

def table_maker(headers, columns_list):
    no_cols = len(headers)
    df_list = []
    starting_point = -1 * no_cols
    test_run = len(columns_list) // no_cols - 1
    end_point = len(columns_list) // no_cols
    variable_list = []
    var = {}

    for p in range(no_cols):
        f_var = int(p)
        variable_list.append(f_var)

    for x in variable_list:
        var[x] = []

    if end_point%no_cols == 0:
        while test_run >= 0:
            starting_point += no_cols
            end_point += no_cols
            df_list.append(columns_list[starting_point:end_point])
            test_run -= 1

    else:
        print("not divisible")

    for x1 in range(no_cols):
        for y in df_list:
            var[x1].append(y[x1])

    df = pd.DataFrame(var)
    renamed = {}
    for p in range(no_cols):
        renamed[p] = columns[p]
        dataframe_final = df.rename(columns=renamed)
        

    print(dataframe_final)

table_maker(columns, list_inside)


            

