# -*- coding: utf-8 -*-
import unittest
import time
from WebPage import LoginPage
#from WebPage import BasePage
#import HTMLTestRunnerCN
u"""
修改人：cx
修改时间：2017.12.20
修改内容：
"""

class managerLogin(unittest.TestCase):
    u"""管理员登录测试"""
    
      
    def setUp(self):
                                         
        self.loginpage=LoginPage.LoginPage()
        self.url=self.loginpage.url1
        self.driver=self.loginpage.driver


    def test_01(self):
         
        u"""登录成功 """
 
        self.loginpage.open(self.url)
        time.sleep(2)        
        self.loginpage.set_username()
        self.loginpage.set_password()
        self.loginpage.click_login_button()
            
     
    def test_02(self):
         
        u"""账号不正确"""
         
        
        self.loginpage.open(self.url)
        self.driver.implicitly_wait(30)               
        self.loginpage.set_username(self.loginpage.username1[4])
        self.loginpage.set_password()
        self.loginpage.click_login_button()
        self.driver.implicitly_wait(30)
                 
        self.driver.switch_to_window(self.driver.window_handles[0])
        assert (self.loginpage.error_info1[3].decode('utf-8') ==self.loginpage.get_error_info()) 

        
    @unittest.skipUnless(False, u'为False时跳过')         
    def test_03(self):
        
        u"""密码不正确"""
        
        self.loginpage.open(self.driver,self.url)
        self.driver.implicitly_wait(30)               
        self.loginpage.set_username(self.loginpage.username1[5])
        self.loginpage.set_password()
        self.loginpage.click_login_button()
        self.driver.implicitly_wait(30)
                
        self.driver.switch_to_window(self.driver.window_handles[0])
        assert (self.loginpage.error_info1[4].decode('utf-8') ==self.loginpage.get_error_info())
        print self.loginpage.get_error_info()       
    
    def tearDown(self):
        self.loginpage.closedriver()
        
        
class customerLogin(unittest.TestCase):
    u"""客户登录测试"""
     
       
    def setUp(self):
                                          
        self.loginpage=LoginPage.LoginPage()
        self.url=self.loginpage.url2
        self.driver=self.loginpage.set_brower()
 
 
    def test_01(self):
          
        u"""登录成功 """
  
        self.loginpage.open(self.url)
        time.sleep(2)        
        self.loginpage.set_username('6661111111')
        self.loginpage.set_password()
        self.loginpage.click_login_button()    
      
    def test_02(self):
          
        u"""账号不正确"""
                  
        self.loginpage.open(self.url)
        self.driver.implicitly_wait(30)               
        self.loginpage.set_username()
        self.loginpage.set_password()
        self.loginpage.click_login_button()
        self.driver.implicitly_wait(30)
                  
        self.driver.switch_to_window(self.driver.window_handles[0])
        assert (self.loginpage.error_info1[3].decode('utf-8') ==self.loginpage.get_error_info()) 
 
         
    @unittest.skipUnless(False, u'为False时跳过')         
    def test_03(self):
         
        u"""密码不正确"""
         
        self.loginpage.open(self.url)
        self.driver.implicitly_wait(30)               
        self.loginpage.set_username('6661111111')
        self.loginpage.set_password('abc111')
        self.loginpage.click_login_button()
        self.driver.implicitly_wait(30)
                 
        self.driver.switch_to_window(self.driver.window_handles[0])
        assert (self.loginpage.error_info1[4].decode('utf-8') ==self.loginpage.get_error_info())
        print self.loginpage.get_error_info()       
     
    def tearDown(self):
        self.loginpage.closedriver()
 
class salesLogin(unittest.TestCase):
    u"""经纪人登录测试"""
     
       
    def setUp(self):
                                          
        self.loginpage=LoginPage.LoginPage()
        self.url=self.loginpage.url3
        self.driver=self.loginpage.set_brower()    
 
 
    def test_01(self):
          
        u"""登录成功 """
  
        self.loginpage.open(self.url)
        time.sleep(2)        
        self.loginpage.set_username('6661021111')
        self.loginpage.set_password()
        self.loginpage.click_login_button()    
      
    def test_02(self):
          
        u"""账号不正确"""
          
 
        self.loginpage.open(self.url)
        self.driver.implicitly_wait(30)               
        self.loginpage.set_username()
        self.loginpage.set_password()
        self.loginpage.click_login_button()
        self.driver.implicitly_wait(30)
                  
        self.driver.switch_to_window(self.driver.window_handles[0])
        assert (self.loginpage.error_info1[3].decode('utf-8') ==self.loginpage.get_error_info()) 
 
         
    @unittest.skipUnless(False, u'为False时跳过')       
    def test_03(self):
         
        u"""密码不正确"""
         
        self.loginpage.open(self.url)
        self.driver.implicitly_wait(30)               
        self.loginpage.set_username('6661021111')
        self.loginpage.set_password('abc111')
        self.loginpage.click_login_button()
        self.driver.implicitly_wait(30)
                 
        self.driver.switch_to_window(self.driver.window_handles[0])
        assert (self.loginpage.error_info1[4].decode('utf-8') ==self.loginpage.get_error_info())
        print self.loginpage.get_error_info()       
     
    def tearDown(self):
        self.loginpage.closedriver()

if __name__ == '__main__':
    unittest.main()
