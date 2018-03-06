import requests
from lxml import etree


class Tool:
    @classmethod
    def get_view_state(cls, url, view_state, event_validation):
        """
        传入view_state,event_validation的xpath
        :param url: http://www.jscsfc.com/NewHouse/
        :param view_state: //*[@id="__VIEWSTATE"]/@value
        :param event_validation: //*[@id="__EVENTVALIDATION"]/@value
        :return: {'__VIEWSTATE': html_tree.xpath(view_state),
                '__EVENTVALIDATION': html_tree.xpath(event_validation)}
        """
        res = requests.get(url)
        html_tree = etree.HTML(res.content)

        return {'__VIEWSTATE': html_tree.xpath(view_state)[0],
                '__EVENTVALIDATION': html_tree.xpath(event_validation)[0]}

    @classmethod
    def url_quote(cls, url, encoding):
        """
        todo 把url里面的中文转码
        :return:
        """
        pass


if __name__ == '__main__':
    view_dict = Tool.get_view_state('http://www.jscsfc.com/NewHouse/',
                                    view_state='//*[@id="__VIEWSTATE"]/@value',
                                    event_validation='//*[@id="__EVENTVALIDATION"]/@value')
    print(view_dict)
