# coding=utf-8

from selenium import webdriver


# [{'domain': '218.66.59.97', 'expiry': 1560776732.894321, 'httpOnly': True, 'name': 'igz__user_login', 'path': '/', 'secure': False, 'value': '286Xw8Ncbm9ym4NyXdurlauS05rQmcOWXpSbzpvQVaCT1ZTY2aikqJ3Bv2KTzpmeamWYb5xVoGamlKPVkL9f18zJog..'}, {'domain': '218.66.59.97', 'httpOnly': True, 'name': 'SESSION', 'path': '/', 'secure': False, 'value': 'b5581f7f-ef61-44ae-93fb-30dcdc83ecbf'}]

# [{'domain': '218.66.59.97', 'httpOnly': False, 'name': 'igz__Session', 'path': '/', 'secure': False, 'value': 'rk8i0hccn7j6okrcihk65cug24'}, {'domain': '218.66.59.97', 'httpOnly': True, 'name': 'SESSION', 'path': '/', 'secure': False, 'value': 'a9e07b36-c9ea-445f-a2ee-c537402c71a6'}]
d = webdriver.Chrome()
d.get('http://218.66.59.97:8099/auth/goLogin')
d.implicitly_wait(10)
print(d.get_cookies())
d.add_cookie({'domain': '218.66.59.97', 'expiry': 1560776732.894321, 'httpOnly': True, 'name': 'igz__user_login', 'path': '/', 'secure': False, 'value': '286Xw8Ncbm9ym4NyXdurlauS05rQmcOWXpSbzpvQVaCT1ZTY2aikqJ3Bv2KTzpmeamWYb5xVoGamlKPVkL9f18zJog..'})
d.add_cookie({'domain': '218.66.59.97', 'httpOnly': True, 'name': 'SESSION', 'path': '/', 'secure': False, 'value': 'b5581f7f-ef61-44ae-93fb-30dcdc83ecbf'})
print(d.get_cookies())
d.get('http://218.66.59.97:8099/auth/goHome')
print(d.get_cookies())
d.quit()



# [{'domain': '218.66.59.97', 'expiry': 1560776732.894321, 'httpOnly': True, 'name': 'igz__user_login', 'path': '/', 'secure': False, 'value': '286Xw8Ncbm9ym4NyXdurlauS05rQmcOWXpSbzpvQVaCT1ZTY2aikqJ3Bv2KTzpmeamWYb5xVoGamlKPVkL9f18zJog..'}, {'domain': '218.66.59.97', 'httpOnly': True, 'name': 'SESSION', 'path': '/', 'secure': False, 'value': 'b5581f7f-ef61-44ae-93fb-30dcdc83ecbf'}]

# [{'domain': '218.66.59.97', 'httpOnly': False, 'name': 'igz__Session', 'path': '/', 'secure': False, 'value': 'rk8i0hccn7j6okrcihk65cug24'}, {'domain': '218.66.59.97', 'httpOnly': True, 'name': 'SESSION', 'path': '/', 'secure': False, 'value': 'a9e07b36-c9ea-445f-a2ee-c537402c71a6'}]