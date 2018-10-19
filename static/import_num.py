# -*- coding:utf-8 -*-
__author__ = 'yewei'


import MySQLdb
import os
import sys
import random
import requests

connect = MySQLdb.connect(
	host = '127.0.0.1',
	port = 3306,
	user = 'root',
	password = 'root',
	charset = 'utf8',
	db = 'article_spider',
)
pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd+"../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myblog.settings")
import django
django.setup()

from django.contrib.auth.hashers import make_password
from blog.models import Blog,BlogType
from users.models import UserProfile
from urllib import request
import re
import time
from random import choice

cursor = connect.cursor()
'''
UK_Ireland
Switzerland_Liechtenstein
Turkey
Norway_Sweden
Italy_Vatican
East_Africa
African_island
North_Africa
Other_African
Australia
New_Zealand
Pacific_Island
Taiwan
Japan
Thailand
Singapore
Sri_Lanka
Hongkong_Macao
Malaysia_Brunei
Cambodia
Maldives
Myanmar
Iran
India_Bangladesh
Canada
USA
Sino_American
South_America
'''
i = 0
names = [
	'Canada',
	'USA',
	'Sino_American',
	'South_America',
]
for name in names:
	cursor.execute("SELECT * FROM qyer where haha = 1 and place = '{}' limit 30".format(name))
	for article in cursor.fetchall():
		print(article[1],'-----------',name)
		blog = Blog()
		user = UserProfile()
		blog.title = article[1]
		content = article[2]
		pattern = re.compile('<a.*?>',re.S)
		a_nums = pattern.findall(article[2])
		for a in a_nums:
			content = content.replace(a,'')
		content = content.replace('</a>','')

		pattern = re.compile('<img.*?/>',re.S)
		images = pattern.findall(content)
		for image in images:
			pattern = re.compile('data-original="(.*?)"')
			image_urls = pattern.findall(image)
			for image_url in image_urls:
				print(image_url)
				seeds = "1234567890"
				random_str = []
				for i in range(6):
					random_str.append(choice(seeds))

				code = "".join(random_str)
				if not os.path.exists('image/{}'.format(article[8])):
					os.mkdir('image/{}'.format(article[8]))
				image_name = 'image/{0}/{1}{2}.img'.format(article[8],int(time.time() * 1000), code)
				try:
					request.urlretrieve(image_url, image_name)
					content = content.replace(image,'<img src="{}" />'.format(image_name))
				except ValueError:
					request.urlretrieve('https:{}'.format(image_url), image_name)
					content = content.replace(image, '<img src="{}" />'.format(image_name))
				else:
					content = content.replace(image,'')
		blog.content = content

		if article[3]:
			seeds = "1234567890"
			random_str = []
			for i in range(4):
				random_str.append(choice(seeds))

			code =  "".join(random_str)
			thumb_img_name = 'thumb_image/lvyou/{0}{1}.img'.format(int(time.time()*1000),code)
			request.urlretrieve(article[3], thumb_img_name)
		else:
			thumb_img_name = ''
		blog.thumb_img = thumb_img_name

		if UserProfile.objects.filter(username=article[5]):
			blog.author = UserProfile.objects.filter(username=article[5])[0]
		else:
			user.username = article[5]
			user.password = make_password('wohenxili520')
			user.save()
			blog.author = UserProfile.objects.filter(username=article[5])[0]
		blog.blog_type = BlogType.objects.filter(type_name=article[9])[0]
		blog.save()

		cursor.execute("update qyer set haha = 0 where id = %s" % (article[0]))
		connect.commit()
# for good in cursor.fetchall():
# 	i += 1
# 	goods = Goods()
# 	goods.id = i
# 	goods.name = good[2].replace('【国美自营】','')
# 	goods.goods_num = random.randint(50,1000)
# 	goods.market_price = good[4]
# 	goods.shop_price = good[4]
# 	goods.goods_desc = good[5]
# 	goods.goods_front_image = good[3]
# 	print(GoodsCategory.objects.filter(id=good[-3]))
# 	goods.category = GoodsCategory.objects.filter(id=good[-3])[0]
# 	goods.save()
#
# 	images = good[-2]
# 	images = images.replace("[",'').replace("]",'').replace("'",'').split(',')
# 	for image in images:
# 		image = image.split("/")
# 		image_name = image[-1]
# 		good_image = GoodsImage()
# 		good_image.image = 'goods/thumbnail/' + image_name
# 		good_image.goods = goods
# 		good_image.save()




cursor.close()
connect.close()



