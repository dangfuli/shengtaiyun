# coding=utf-8
import os
def getElement(file):
    '''
    元素以json数据格式存储，此方法读取文件
    :param file: 数据文件，json格式
    :return: dict
    '''
    if os.path.exists(file):
        try:
            f = open(file,"r")
        except:
            print("打开文件{0}错误".format(file))
            return {}
        try:
            elements = eval(f.read())
            # print(type(elements))
            return elements
        except:
            print("解析文件{0}错误".format(file))
            return {}

    else:
        print("can not find .json file")
        return {}


if __name__ == '__main__':
    getElement(r"C:\Users\Administrator\PycharmProjects\CRM\elements\\login.json")
