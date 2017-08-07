import sys
import requests
import json

from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import re
import csv


_domain = "http://dudoanvietlott.net/bang-tong-hop-ket-qua-mega-6-45.html"

def get_info_result_vietlott():
    response = requests.get(_domain)

    soup = BeautifulSoup(''.join(str(response.content)))
    result_all_div = soup.findAll('div', { "class" : "statistics-results" } )
    total_result_list = []
    for div in result_all_div:
        result_list = []
        contain_p = div.div.p
        for number in div.findAll('li'):
            result_list.append(number.string)
        total_result_list.append(result_list)
    return total_result_list



if __name__ == '__main__':
    result = get_info_result_vietlott()
    with open("output.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerows(result)
    print("DONE!")


