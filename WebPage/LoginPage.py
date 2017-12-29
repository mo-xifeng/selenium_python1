#Embedded file name: C:\Users\Administrator\eclipse-workspace\selenium_use_case\test_case\WebPages\LoginPage.py
#-*- coding:utf-8 -*-  
from BasePage import BasePage
from common.OperationFile import OperationXml
class LoginPage(BasePage):
    
    readXml=OperationXml()
    
    #管理员登录页面elements
    username1=readXml.ReadXml('login', 'useraccount')
    password1=readXml.ReadXml('login', 'password')
    login_btn1=readXml.ReadXml('login', 'login_btn')
    error_info1=readXml.ReadXml('login', 'err_info')
    #管理员登录url
    url1=username1[0]
    
    #客户登录url    
    url2=url1.replace('Manager','Client')
    
    #经纪人登录url
    url3=url1.replace('Manager','Sales')
    #bs=BasePage.BasePage()
    
    

    def __init__(self,):
        self.driver=BasePage.__init__(self, 'ff') 
          
        
    #输入账号操作
    def set_username(self,username=username1[3]):
        
               
        userinputbox=self.findElement((self.username1[1],self.username1[2]))
        self.type(userinputbox, username)
    
    #输入密码操作
    def set_password(self, password=password1[3]):
        pwinputbox=self.findElement((self.password1[1],self.password1[2]))
        self.type(pwinputbox, password)        
    
    #点击登录按钮操作
    def click_login_button(self):
        lg_butn = self.findElement((self.login_btn1[1],self.login_btn1[2]))
        self.click(lg_butn)
       
    def get_error_info(self):
        err_info=self.findElement((self.error_info1[1],self.error_info1[2])).text          
        return err_info
        
    
    
    def openPage(self,url):
        js='window.open("{value}")'.format(value=url)
        self.driver.execute_script(js)
        self.driver.switch_to_window(self.driver.window_handles[1])       
    
    def closedriver(self):
        """
        Close driver!
        """
        self.driver.close()
    
if __name__==('__main__'):
    test1=LoginPage()
    test1.openPage('https://trade.iwisetrader.com/Manager/Manager/Managers')      
        