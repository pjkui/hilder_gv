"""
url = http://www.czhome.com.cn/complexPro.asp?page=1&districtID=0&projectAdr=&projectName=&buildingType=0&houseArea=0&averagePrice=0&selState=-1
city : 滁州
CO_INDEX : 7
author: 吕三利
小区数量 : 936    2018/2/23
"""

from crawler_base import Crawler
from lxml import etree
from comm_info import Comm, Building, House
import requests, re
from retry import retry

CO_INDEX = 7
building_id = 0


class Chuzhou(Crawler):
    def __init__(self):
        self.url = 'http://www.czhome.com.cn/complexPro.asp?page=1&districtID=0&projectAdr=&projectName=&buildingType=0&houseArea=0&averagePrice=0&selState=-1'

    def start_crawler(self):
        self.start()

    @retry(retry(3))
    def get_all_page(self):
        response = requests.get(url=self.url)
        html = response.content.decode('gbk')
        tree = etree.HTML(html)
        page = tree.xpath('//*[@id="Table7"]/tr/td[2]/text()')[1]
        page = re.search('\d+', page).group()
        print(page)
        return page

    def is_none(self, xpath_adv):
        if xpath_adv:
            xpath_adv = xpath_adv[0]
        else:
            xpath_adv = None
        return xpath_adv

    @retry(retry(3))
    def start(self):
        page = self.get_all_page()
        for i in range(1, int(page) + 1):
            url = 'http://www.czhome.com.cn/complexPro.asp?page=' + str(
                i) + '&districtID=0&projectAdr=&projectName=&buildingType=0&houseArea=0&averagePrice=0&selState=-1'
            response = requests.get(url)
            html = response.content.decode('gbk')
            tree = etree.HTML(html)
            comm_url_list = tree.xpath('//*[@id="Table8"]/tr/td[2]/a/@href')
            for i in comm_url_list:
                comm = Comm()
                comm_url = 'http://www.czhome.com.cn/' + i
                self.get_comm_info(comm_url, comm)

    @retry(retry(3))
    def get_comm_info(self, comm_url, comm):
        response = requests.get(comm_url)
        html = response.content.decode('gbk').replace(' ', '').replace('\n', '').replace('\r', '').replace('\t', '')
        tree = etree.HTML(html)
        # 小区id
        co_id = re.search('projectID=(\d+?)&', comm_url).group(1)
        # 小区名称
        co_name = re.search('项目名称：(.*?)<', html).group(1)
        # 小区地址
        co_address = re.search('所在区名：(.*?)<', html).group(1)
        # 开发商
        co_develops = re.search('企业名称：<(.*?)>(.*?)<', html).group(2)
        # 小区总套数
        co_all_house = re.search('总套数<(.*?)><(.*?)<(.*?)>(.*?)<', html).group(4)
        # 占地面的
        co_size = re.search('总面积<(.*?)><(.*?)<(.*?)>(.*?)<', html).group(4).replace('㎡', '')
        # 建筑面积
        co_build_size = re.search('住宅面积<(.*?)<(.*?)<(.*?)<(.*?)>(.*?)<', html).group(5).replace('㎡', '')
        self.get_build_info(co_id, co_name)
        comm.co_index = CO_INDEX
        comm.co_id = co_id
        comm.co_name = co_name
        comm.co_address = co_address
        comm.co_develops = co_develops
        comm.co_all_house = co_all_house
        comm.co_size = co_size
        comm.co_build_size = co_build_size
        comm.insert_db()

    def get_build_info(self, co_id, co_name):
        url = 'http://www.czhome.com.cn/Presell.asp?projectID=' + co_id + '&projectname=' + co_name
        response = requests.get(url)
        html = response.content.decode('gbk')
        tree = etree.HTML(html)
        xpath_list = tree.xpath('//tr[@class="indextabletxt"]')
        for i in xpath_list[1:]:
            build_url = i.xpath('td[2]/a/@href')[0]
            url = 'http://www.czhome.com.cn/' + build_url
            result = requests.get(url)
            html = result.content.decode('gbk')
            tree = etree.HTML(html)
            # 总套数
            bu_xpath = tree.xpath('/html/body/table/tr/td/table/tr/td/table/tr')[1:]
            for i in bu_xpath:
                building = Building()
                global building_id
                building_id += 1
                building.bu_id = building_id
                bu_all_house = i.xpath('td[7]/text()')[0]
                bu_url = i.xpath('td[1]/a/@href')[0]
                url = 'http://www.czhome.com.cn/' + bu_url
                response = requests.get(url)
                html = response.content.decode('gbk')
                tree = etree.HTML(html)
                # 楼层
                bu_floor = tree.xpath('//*[@id="Table4"]/tr[2]/td/table[3]/tr/td[1]/u/text()')[-1]
                house_url_list = tree.xpath('//*[@id="Table4"]/tr[2]/td/table[3]/tr/td/a/@href')
                for i in house_url_list:
                    house = House()
                    house_url = 'http://www.czhome.com.cn/' + i
                    self.get_house_info(house_url, house, co_id, building_id)
                building.bu_all_house = bu_all_house
                building.bu_floor = bu_floor
                building.bu_id = building_id
                building.co_id = co_id
                building.co_index = CO_INDEX
                building.insert_db()

    def get_house_info(self, house_url, house, co_id, building_id):
        response = requests.get(house_url)
        html = response.content.decode('gbk').replace('\t', '').replace('\n', '').replace('\r', '').replace(' ', '')
        if response.status_code is not 200:
            return
        # 房号id
        ho_num = re.search('室号<(.*?)<(.*?)>(.*?)<', html).group(3)
        # 房屋类型
        ho_type = re.search('房屋类型<(.*?)<(.*?)>(.*?)<', html).group(3)
        # 户型
        ho_room_type = re.search('房型<(.*?)<(.*?)>(.*?)<', html).group(3)
        # 楼层
        ho_floor = re.search('名义层/实际层<(.*?)<(.*?)>(.*?)<', html).group(3)
        ho_floor = re.search('/(.*?)$',ho_floor).group(1)
        # 建筑面积
        ho_build_size = re.search('预测建筑面积<(.*?)<(.*?)>(.*?)<', html).group(3)
        # 预测套内面积
        ho_true_size = re.search('预测套内面积<(.*?)<(.*?)>(.*?)<', html).group(3)
        # 分摊面积
        ho_share_size = re.search('预测分摊面积<(.*?)<(.*?)>(.*?)<', html).group(3)
        house.co_index = CO_INDEX
        house.co_id = co_id
        house.bu_id = building_id
        house.ho_num = ho_num
        house.ho_type = ho_type
        house.ho_room_type = ho_room_type
        house.ho_floor = ho_floor
        house.ho_build_size = ho_build_size
        house.ho_true_size = ho_true_size
        house.ho_share_size = ho_share_size
        house.insert_db()
