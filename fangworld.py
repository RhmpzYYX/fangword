import requests
import csv
from lxml import etree
import json


first_row = ['城市', '指数', '环比(%)', '指数', '环比(%)', '指数', '环比(%)', '指数', '环比(%)']

with open('./fangworld.csv', mode='w', encoding='mbcs', newline='') as file_obj:
    file_obj = csv.writer(file_obj)
    for k in range(12, 0, -1):  # 11月-1月降序
        month = str(k).zfill(2)  # 单数月份补0
        url = 'https://fdc.fang.com/index/XinFangIndex.aspx?action=month&month=2020%25u5E74' + month'
        month = [month+'月']
        # 前两行的月份和标签
        file_obj.writerow(month)
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





