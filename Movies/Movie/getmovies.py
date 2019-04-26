import requests
from bs4 import BeautifulSoup
import  pymysql

def get_movies():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT6.1; Win64; x64)AppleWebKit/537.36 (KHTML,like Gecko) Chrome/52.0.2743.82 Safari/537.36',
        'Host': 'movie.douban.com'
    }
    movie_list=[]
    director_list=[]
    picture_list=[]
    intro_list=[]
    for i in range(0,5):
        url = 'https://movie.douban.com/top250?start=' + str(25*i)
        r = requests.get(url, headers=headers,timeout=10)
        soup = BeautifulSoup(r.text, "lxml")
        div_aa=soup.find_all('div',class_='hd')
        div_bb=soup.find_all('div',class_='bd')
        div_cc=soup.find_all('div',class_='pic')
        div_dd = soup.find_all('p', class_='quote')

        for data in div_aa:
            k = data.a.span.text.title()
            movie_list.append(k)
        for i in div_bb:
            j=i.p.text
            director_list.append(j)
        for i in div_cc:
            p=i.a.img['src']
            picture_list.append(p)
        for i in div_dd:
            v=i.span.text
           # print(i.text)
            intro_list.append(v)

    return movie_list,director_list,picture_list,intro_list

get_movies()

# l1,l2,l3,l4=get_movies()
# for i in range(len(l1)):
#     print(l1[i])
#     print(l2[i])
#     print(l3[i])
# for i in range(len(l4)):
#     print(l4[i])












# movies = get_movies()
# db = pymysql.connect("localhost", "root", "s13958920775", "novel", charset="utf8")
# cs = db.cursor()
# for i in movies:
#     sql = "insert into movie(name) values('" + i + "')"
#
#     cs.execute(sql)
#     db.commit()
# db.close()