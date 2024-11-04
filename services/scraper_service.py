import uuid
import requests
from bs4 import BeautifulSoup
from models.tourist_attraction import TouristAttraction
from extensions import db
from datetime import datetime
def scrape_tourist_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    attractions = []
    items=soup.select('.list_item')
    # 示例：假设爬取某个网站的旅游数据
    for item in items:
        title = item.find('h2', class_='tit').find('a').text
        travel_link=item.find('a',class_='face').get('href')
        if travel_link:
            travel_link='https:'+travel_link
        user_info = item.select_one('.user_info')
        user_name=user_info.find('span',class_='user_name').find('a').text
        days=int(user_info.select_one('.days').text[1:2])
        date=user_info.select_one('.date').text.strip()[:10]
        people_element=user_info.select_one('.people')
        if people_element:
            user_auth = people_element.text
        else:
            user_auth=''
        user_tag_element=user_info.select_one('.trip')
        if user_tag_element:
            user_tag=user_tag_element.text.replace(" ", ",")
        else:
            user_tag=''
        places = item.select('.places')
        if len(places)>1:
           route=places[0].text.split("途经：")[-1]
           trip= places[1].text.split("行程：")[-1]
        else:
           trip=''
           route=''
        attraction = TouristAttraction(id=str(uuid.uuid4()),title=title, user_name=user_name, days=days,date=date,user_auth=user_auth,user_tag=user_tag,route=route,trip=trip,travel_link=travel_link)
        if attraction is None:
            print('none')
        else:
            attractions.append(attraction)
        #单条插入，批量插入会报错
        db.session.add(attraction)
        db.session.commit()
    return attractions
