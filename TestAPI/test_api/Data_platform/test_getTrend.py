import requests
from test_api.Data_platform.test_login_token import  login_token
#智能练习时间范围内数据展示


url='https://shuju.zhihuotech.com/api/system/correct_overview/record/getTrend'
header={
        'Host': 'shuju.zhihuotech.com',
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/plain, */*',
        'Authorization': 'Bearer {}'.format(login_token()),
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://shuju.zhihuotech.com/business/analysis',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'cookie': 'rememberMe=true; username=chendong1; password=QftoLO93wbnGrNuHS24EiZUXB+Jb77bs2VCd58EbrnC1Xwk50cd/ZTeDx5gWGhji3w8ENHLM/o8caUqtME/Z5g==; Admin-Token=eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6IjZmNTAyOThmLWQxOWItNDkzYS04ZTZkLTIyYzE3MDUxNGE2NSJ9.q1PkE_tXwbVDrmIHTIvq_y_-RAOuyIkLVZ-xgIx2yWv23emcF5GjzKcKw3oXG9rYHHMExgFVKabJI6aTIdRlWw'
    }
params_data = {'timeType':'1',
                'startDate':'2020-04-21',
                'endDate':'2020-04-21'}
requests.packages.urllib3.disable_warnings()#去除警示提示
r = requests.get(url=url,headers=header,params=params_data,verify=False)
print(r.url)#传递url参数
print(r.text)#想要内容
print(r.status_code)#状态码