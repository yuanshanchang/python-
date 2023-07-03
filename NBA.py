import requests
#引入requests模块以获得网站的信息
#安装此模块使用pip方式，命令为""pip install requests"
from lxml import etree
#pip安装lxml
url='https://nba.hupu.com/stats/players'
#用来取得资料的网址
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67'}
#改变访问代理
resp=requests.get(url)#使用get函数来获取信息
e=etree.HTML(resp.text)#html解析？我也不知道什么东西
#找到xpath表达式并解析赋值
nums=e.xpath('//table[@class="players_table"]//tr/td[1]/text()')
names=e.xpath('//table[@class="players_table"]//tr/td[2]/a/text()')
teams=e.xpath('//table[@class="players_table"]//tr/td[3]/a/text()')
scores=e.xpath('//table[@class="players_table"]//tr/td[4]/text()')

#print(nums)
#print(names)
#print(teams)
#print(scores)
with open('nba.txt','w',encoding='utf-8') as f:
#打开文件，权限为：写，使用utf-8的编码模式
    for num,name,team,score in zip(nums,names,teams,scores):
    #python的for循环语法     
        f.write(f'排名:{num}  姓名:{name}  队伍:{team}  分数:{score}\n')
        #写文件