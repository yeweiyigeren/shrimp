# -*- coding:utf-8 -*-
__author__ = 'yewei'

import MySQLdb
import os
from urllib import request
import re
import time
from random import choice
import threading
import queue


def change_content(cursor,connect,q):
	while True:
		try:
			article = q.get_nowait()
			i = q.qsize()
		except Exception as e:
			print(e)
			break
		print("还剩 %s 个任务！" % i)
		content = article[2]
		pattern = re.compile('<a.*?>', re.S)
		a_nums = pattern.findall(article[2])
		for a in a_nums:
			content = content.replace(a, '')
		content = content.replace('</a>', '')

		pattern = re.compile('<img.*?/>', re.S)
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
				image_name = 'image/{0}/{1}{2}.img'.format(article[8], int(time.time() * 1000), code)
			try:
				request.urlretrieve(image_url, image_name)
				content = content.replace(image, '<img src="{}" />'.format(image_name))
			except ValueError:
				request.urlretrieve('https:{}'.format(image_url), image_name)
				content = content.replace(image, '<img src="{}" />'.format(image_name))
			except:
				content = content.replace(image, '')

		print('...')

		cursor.execute("update qyer_copy set content = '%s' where id = %s" % (content,article[0]))
		# connect.commit()
		#
		# cursor.execute("update qyer set haha = 0 where id = %s" % (article[0]))
		# connect.commit()



if __name__ == '__main__':
	connect = MySQLdb.connect(
		host = '127.0.0.1',
		port = 3306,
		user = 'root',
		password = 'root',
		charset = 'utf8',
		db = 'article_spider',
	)
	cursor = connect.cursor()

	q = queue.Queue()
	cursor.execute("SELECT * FROM qyer where haha = 1 limit 10")
	for article in cursor.fetchall():
		q.put(article)

	nums = 10
	threads = []

	for i in range(nums):
		t = threading.Thread(target=change_content, args=(cursor,connect,q))
		threads.append(t)

	for t in threads:
		t.start()

	for t in threads:
		t.join()

	connect.commit()
	cursor.close()
	connect.close()












