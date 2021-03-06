"""
url = http://222.139.215.89:81/yscx/spfba.asp
city : 南阳
CO_INDEX : 214
小区数量：
对应关系：
"""

import requests
from comm_info import Comm, Building, House
import re

url = 'http://222.139.215.89:81/yscx/spfba.asp'
co_index = '214'
city = '南阳'
count = 0


class Nanyang(object):
    def __init__(self):
        self.headers = {
            'User-Agent':
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119Safari/537.36',
        }

    def start_crawler(self):
        response = requests.get(url, headers=self.headers)
        html = response.content.decode('gbk')
        page = re.search('1/(\d+)', html, re.S | re.M).group(1)
        for i in range(1, int(page) + 1):
            page_url = 'http://222.139.215.89:81/yscx/spfba.asp?Page=' + str(page)
            res = requests.get(page_url, headers=self.headers)
            res_paper = res.content.decode('gbk')
            comm_url_list = re.findall('onMouseOver=.*?<a href="(.*?)"', res_paper, re.S | re.M)
            self.get_comm_info(comm_url_list)

    def get_comm_info(self, comm_url_list):
        for i in comm_url_list:
            comm = Comm(co_index)
            comm_url = 'http://222.139.215.89:81/yscx/' + i
            response = requests.get(comm_url, headers=self.headers)
            html = response.content.decode('gbk')
            comm.co_name = re.search('项目名称.*?<td>(.*?)<', html, re.S | re.M).group(1)
            comm.co_pre_sale = re.search('售许可证号.*?<td>(.*?)<', html, re.S | re.M).group(1)
            comm.co_develops = re.search('开发建设单位.*?<td>(.*?)<', html, re.S | re.M).group(1)
            comm.co_address = re.search('项目地址.*?<td>(.*?)<', html, re.S | re.M).group(1)
            comm.co_build_size = re.search('建筑面积.*?<td>(.*?)<', html, re.S | re.M).group(1)
            comm.co_all_house = re.search('住宅套数.*?<td>(.*?)<', html, re.S | re.M).group(1)
            comm.co_pre_sale_date = re.search('批准日期.*?<td>(.*?)<', html, re.S | re.M).group(1)
            comm.insert_db()
