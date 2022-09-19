# Принцип работы бота: при включении бота он проверяет по очереди все группы из подготовленного списка и пишет комментарии на новые посты в этих группах
# Как это нужно сделать:
# Нужно чтобы это не было похоже на спам, никаких призывов вступить, выбирать только проверенные сообщества, где за это не банят админы.

# Импорт библиотек
import requests
import lxml.html
from random import choice
import time
import sys
exec("from {} import *".format(sys.argv[1]))

# Общие параметры
timesleep = 0 # Тайминг между проверками кода
version = 5.101 # Текущая версия

# Функции
def comment(group, post, message, attachments):
	'''Размещение комментария с 2 рандомными фотограффиями из списка картинок. По очереди: id группы, id поста, сообщение'''

	k1 = {
		'v':version,
		'access_token':group_token,
		'owner_id':group,
		'post_id':post,
		'from_group':mygroup,
		'message':message,
		'attachments':attachments
		}

	return requests.post('https://api.vk.com/method/wall.createComment', data = k1)


def get_last_id(group):
	'''Возвращает id последнего поста в группе.'''

	try:	
		html = requests.get("https://vk.com/public"+str(group)[1:])

		doc = lxml.html.fromstring(html.content)

		idq=doc.xpath('//div[@class="wall_item"]/a/@name')


		id1=str(idq[0])
		id2=str(idq[1])

		id1 = int(id1[id1.find("_")+1:])
		id2 = int(id2[id2.find("_")+1:])

		return id1 if id1>id2 else id2
	except:
		print("Ошибка в получении последнего id в группе")


def main():
	n = 1 # Номер комментария

	# Заполняем словарь с последними id из групп
	last_post={}
	for group in groups:
		last_post[group]=get_last_id(group)

	while True:
		for group in groups:
			last_id=get_last_id(group)
			if last_post[group]!=last_id:
				try:
					a = comment(group,last_id,choice(messages),'{},{}'.format(choice(pictures),choice(pictures)))
				except:
					continue
				last_post[group]=last_id
				print('{}. - {} - {}'.format(n, time.strftime('%X',time.localtime(time.time()+14400)), a.json()))
				print('https://vk.com/public{}?w=wall{}_{}\n'.format(-group,group,last_id))
				n+=1
		time.sleep(timesleep) # Время которое программа не работает между прохода всех групп


main()