# coding=utf-8
from selenium import webdriver
import time
path = 'http://218.66.59.97:8099/auth/goLogin'
def Driver(web='chorme'):
    ## 赋值driver
    if web == 'chorme':
        dri = webdriver.Chrome()
    if web == 'firefox':
        dri = webdriver.Firefox()
    if web == 'PhantomJS':
        dri = webdriver.PhantomJS()
    if web == 'ie':
        dri = webdriver.Ie()
    if web == 'safari':
        dri = webdriver.Safari()

    dri.get('http://218.66.59.97:8099/auth/goLogin')
    dri.implicitly_wait(10)
    dri.add_cookie({"name":"SESSION	","value":"a243293c-dcb1-4ac2-bf51-06c357344a30"})
    dri.add_cookie({"name":"igz__user_login	","value":"pZuUw75hcHJyaldyjqrVy6KX0ZSilpKSkZHJzqGjUmxdopHY1K2mq52Qk2LEncPUYWqWaW5Sb2LZkdHVlpJco5aWnw.."})
    dri.refresh()

