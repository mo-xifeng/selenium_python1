#Embedded file name: C:\Users\Administrator\eclipse-workspace\selenium_use_case\test_case\CommonLibrary\CommonConfiguration.py
from datetime import datetime

def driverPath():
    return 'C:\\Program Files\\Mozilla Firefox\\firefox.exe'


def baseUrl():
    return 'https://trade.iwisetrader.com/'


def getCurrentTime():
    format1 = '%Y_%m_%d_%H_%M_%S'
    return datetime.now().strftime(format1)




