"""
url = http://fsfc.fsjw.gov.cn/search/index.do
city : 东莞
CO_INDEX : 10
author: 吕三利
小区数量：2757    2018/2/27
"""

from base import AllListUrl
from crawler_base import Crawler
from lxml import etree
from comm_info import Comm, Building, House
import requests, re
from retry import retry

CO_INDEX = 10


class Foshan(Crawler):
    def __init__(self):
        self.url = 'http://fsfc.fsjw.gov.cn/search/index.do'

    def start_crawler(self):
        self.start()

    @retry(retry(3))
    def start(self):
        b = AllListUrl(first_page_url=self.url,
                       request_method='get',
                       encode='utf-8',
                       regex_group=1,
                       regex='pageTotal = (.*?);', )
        page = b.get_page_count()
        for i in range(1, int(page) + 1):
            url = 'http://fsfc.fsjw.gov.cn/search/index.do?p=' + str(i)
            response = requests.get(url)
            html = response.text
            tree = etree.HTML(html)
            comm_url_list = tree.xpath('//*[@id="content"]/div[2]/div[1]/dl/dd/h3/a/@value')
            for i in comm_url_list:
                comm = Comm()
                url = 'http://fsfc.fsjw.gov.cn/hpms_project/roomView.jhtml?id=' + i
                self.get_comm_info(url, comm)

    def get_comm_info(self, url, comm):
        response = requests.get(url)
        html = response.text
        tree = etree.HTML(html)
        # 小区名称
        co_name = tree.xpath('//*[@id="content"]/div[2]/div[1]/div[2]/table/tr[1]/td/strong/span/text()')[0]
        # 小区地址
        co_address = tree.xpath('//*[@id="content"]/div[2]/div[1]/div[2]/table/tr[2]/td/span/text()')[0]
        # 开发商
        co_develops = tree.xpath('//*[@id="content"]/div[2]/div[1]/div[2]/table/tr[3]/td[1]/span/@title')[0]
        # 物业公司
        # co_develops = tree.xpath('//*[@id="content"]/div[2]/div[1]/div[2]/table/tr[4]/td[1]/span/@title')[0]
        # 容积率
        co_volumetric = tree.xpath('//*[@id="content"]/div[2]/div[1]/div[2]/table/tr[5]/td[2]/span/text()')[0]
        # 预售证书
        co_pre_sale = tree.xpath('//*[@id="content"]/div[2]/div[1]/div[2]/table/tr[6]/td[1]/text()')[0]
        # 建筑面积
        co_build_size = tree.xpath('//*[@id="content"]/div[2]/div[1]/div[2]/table/tr[5]/td[1]')[0].text
        # 小区id
        co_id = re.search('id=(.*?)$', url).group(1)
        html_ = html.replace('\t', '').replace('\r', '').replace('\n', '').replace(' ', '')
        # building_url_list = tree.xpath('//p[@class="bot-a"]/a')
        bu_url_info = re.search('<pclass="bot-a">(.*?)</p>', html_).group(1)
        building_url_list = re.findall('<td><aid="(.*?)"(.*?)>(.*?)</a>', bu_url_info)
        for i in building_url_list:
            build = Building()
            value = i[0]
            bu_name = i[2]
            url = 'http://fsfc.fsjw.gov.cn/hpms_project/room.jhtml?id=' + value
            self.get_build_info(url, co_id, value)
            build.co_id = co_id
            build.co_index = CO_INDEX
            build.bu_id = value
            build.bu_name = bu_name
            build.insert_db()
        comm.co_name = co_name
        comm.co_id = co_id
        comm.co_index = CO_INDEX
        comm.co_address = co_address
        comm.co_develops = co_develops
        comm.co_volumetric = co_volumetric
        comm.co_pre_sale = co_pre_sale
        comm.co_build_size = co_build_size
        comm.insert_db()

    def get_build_info(self, url, co_id, bu_id):
        response = requests.get(url)
        json_html = response.json()
        for i in json_html:
            house = House()
            ho_name = i['roomno']  # 房号
            ho_num = i['code']  # 房号id
            ho_room_type = i['ghyt']  # 户型
            ho_true_size = i['tnmj']  # 预测套内面积
            ho_floor = i['floorindex']  # 楼层
            ho_build_size = i['jzmj']  # 建筑面积
            house.co_id = co_id
            house.co_index = CO_INDEX
            house.bu_id = bu_id
            house.ho_name = ho_name
            house.ho_num = ho_num
            house.ho_room_type = ho_room_type
            house.ho_true_size = ho_true_size
            house.ho_floor = ho_floor
            house.ho_build_size = ho_build_size
            house.insert_db()
