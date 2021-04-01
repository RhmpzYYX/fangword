import requests
import csv
from lxml import etree
import json


first_row = ['月份', '指数', '环比(%)', '指数', '环比(%)']
city = ['北京','上海','广州','深圳','天津','武汉','重庆','南京','杭州','成都']

with open('./ErShouFang.csv', mode='w', encoding='mbcs', newline='') as file_obj:
	file_obj = csv.writer(file_obj)
	for k in range(len(city)):  
		cityuni = str(city[k].encode('unicode-escape').decode()).upper()
		cityuni = '%25u'+cityuni[2:6]+'%25u'+cityuni[8:]
		url = 'https://fdc.fang.com/index/ErShouFangIndex.aspx?action=city&city=' + cityuni
		file_obj.writerow([city[k]])
		file_obj.writerow(first_row)
		# 请求页面的值
		response = requests.get(url)
		html = json.loads(response.text)['data']
		tree = etree.HTML(html)
		# 找到每个tr
		tr_list = tree.xpath('//tr')
		for i in range(len(tr_list)):
			td = tr_list[i].xpath('.//td')
			# 获取每个td的值
			row = []
			for j in range(len(td)):
				row.append(td[j].xpath('string(.)').strip())
			file_obj.writerow(row)
		file_obj.writerow('')





