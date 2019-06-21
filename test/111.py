# coding=utf-8

from selenium import webdriver
import time

d = webdriver.Chrome()
d.get("http://125.35.91.158:8099/auth/goLogin")
d.implicitly_wait(10)
    # d.add_cookie({'domain': '218.66.59.97', 'expiry': 1560776732.894321, 'httpOnly': True, 'name': 'igz__user_login', 'path': '/', 'secure': False, 'value': '286Xw8Ncbm9ym4NyXdurlauS05rQmcOWXpSbzpvQVaCT1ZTY2aikqJ3Bv2KTzpmeamWYb5xVoGamlKPVkL9f18zJog..'})
# d.add_cookie({'domain': '218.66.59.97', 'httpOnly': True, 'name': 'SESSION', 'path': '/', 'secure': False, 'value': 'b5581f7f-ef61-44ae-93fb-30dcdc83ecbf'})
d.find_element_by_id('username').send_keys('admin')
d.find_element_by_id('password').send_keys('chn12369')
time.sleep(10)
d.find_element_by_id('loginbutton').click()
time.sleep(10)
# d.add_cookie( {'domain': '125.35.91.158', 'httpOnly': True, 'name': 'SESSION', 'path': '/', 'secure': False, 'value': '2d169729-bede-430e-baa4-db8dd0ba08e1'})
print(d.get_cookies())
d.get('http://125.35.91.158:8099/auth/goHome')


# d.quit()
# #
# import requests
# data1 = {
#     "applyName":"高程",
#     "phone":"17600972628"
# }
#
# r1 = requests.post(url='http://test.mianbaojr.cn',data=data1)
# print(r1.text)
# data2 = {
#     "source":"10265",
#     "data":r1.text
# }
# r2 = requests.post(url='http://test.mianbaojr.cn/api/loanmall/apply',data=data2)
# print(r2.text)
# print(r2.json())

# import re
# d = "FGGNi1cQXb8\/QEZpRVzhO1TUM\/bGAOzq1ZyBROer36YYvPhJmlLM+CZOcd5Jz\/GWE3y4QLHEAYzDFZB4DTS0+6NUC3BH0RpISQLcpKSFYRRYLU55PAN9jfGpIe7i76TVP\/e6QtMvs07K4y9w9cndNA=="
# print(re.findall('"(.)"',d))