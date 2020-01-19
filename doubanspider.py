import requests
import lxml
from bs4 import BeautifulSoup


class Spider(object):

    def __init__(self, url_list):
        self.url_list = url_list
        self.headers = {
			'User-Agent' : 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
		}

    def get_top250(self):
        for url in self.url_list:
            result = requests.get(url=url, headers=self.headers)
            soup = BeautifulSoup(result.content, "lxml")
            result_list = []
            for i in range(1, 25):
                result_list.append(soup.select("#content > div > div.article > ol > li:nth-child({})> div > div.info > div.hd > a > span:nth-child(1)".format(i)))
            
            for x in result_list:
                for name in x:
                    print(name.get_text())
            





def run():
    url_list = []
    for page in [i for i in range(0,251,25)]:
        url = "https://movie.douban.com/top250?start={}&filter=".format(page)
        url_list.append(url)
    
    spider = Spider(url_list)
    spider.get_top250()


if __name__ == '__main__':
    run()


