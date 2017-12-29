# -*- coding: utf-8 -*-
import unittest,time
from WebPage import ManagerManagePage
from common import Configuration as cc
from common.LoginAction import LoginAction
from common.ScreenShots import ScreenShots as ss
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By


class ManagerManage(unittest.TestCase):
    u"""管理员管理测试"""
    
      
    @classmethod
    def setUpClass(cls):
        cls.am=ManagerManagePage.AddManagerPage()
        #cls.driver=cls.am.get_driver()
        cls.loginmanager=LoginAction()
        cls.loginmanager.login_manager(cls.driver)                            
        cls.url=cc.baseUrl()+cls.am.url1
        
        
          
    @classmethod
    def tearDownClass(cls):
        cls.am.close_driver()    


    def test_01(self):
          
        u"""打开管理员页面"""       
        self.am.openMMPage(self.url)
        time.sleep(2)
        assert (u"管理员管理" in self.am.page_title())
        
    
    def test_02(self):
         
        u"""新增管理员"""     
        self.am.click_add()        
        for backAccount in range(1111,9999):
            self.am.set_fron_account()
            self.am.set_back_account(backAccount)
            self.am.click_submit()
            time.sleep(0.5)                    
            if self.am.account_dup().decode('utf-8')== u'账号已存在':
                backAccount=backAccount+1
            else:break
        self.am.set_password()
        self.am.set_alert_lots()
        self.am.set_manager_name('test-01')
        self.am.select_langue()
        self.am.set_email()
        self.am.select_role()
        self.am.click_submit()
        #WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_element_located(locator))
        assert self.am.confirm().decode('utf-8')==u'添加成功'
        
        print (u'账号:666002'+str(backAccount),'\n',u'密码:abc123') 
                  
        time.sleep(2)
        
        
#     def test_03(self):
#          
#         u"""查询新增的管理员"""       
#         self.loginmanager.loginpage.openPage(self.url)
#         time.sleep(2)
#         
#     def test_04(self):
#          
#         u"""修改管理员"""       
#         self.loginmanager.loginpage.openPage(self.url)
#         time.sleep(2)        
           
                  

        
        
if __name__ == '__main__':
    unittest.main()