#Embedded file name: C:\Users\Administrator\eclipse-workspace\selenium_use_case\test_case\WebPages\LoginPage.py
#-*- coding:utf-8 -*-  
from BasePage import BasePage
from common.OperationFile import OperationXml
from LoginPage import LoginPage


class ManagerManagePage(BasePage):
    
    readXml=OperationXml()
    
    #管理员登录页面elements
    useraccount=readXml.ReadXml('manager_manage', 's_manager_account')
    
    email=readXml.ReadXml('manager_manage', 's_manager_email')
    
    click_search=readXml.ReadXml('manager_manage', 'search_btn')

    
    
    def __init__(self,ff):
        self.driver=BasePage.__init__(self, 'ff')
                 
    #输入账号
    def set_useraccount(self,email):

        self.type(self.findElement((self.email[1],self.email[2])), email)
        
    #输入邮箱    
    def set_email(self,useraccount=useraccount[3]):

        self.type(self.findElement((self.useraccount[1],self.useraccount[2])), useraccount)    
    
    #点击查询        
    def click_search(self):
          
        self.click(self.findElement((self.useraccount[1],self.useraccount[2]))) 
        
    #获取表格第一列内容    
    def get_firstcols(self):
        
        table=self.findElement(('id','table'))
        rows=table.findElements(('tag','tr'))
        cols=[]
        for m in range(len(rows)):                         
            cols.append(rows[m].findElements(('tag','th'))[0])            
        return cols
          
    
    
        



class AddManagerPage(BasePage):
    
    
    readXml=OperationXml()
    clickAdd=readXml.ReadXml('manager_manage', 'add_btn')
    
    setFronAccount=readXml.ReadXml('manager_manage', 'add_manager_account1')
    
    setBackAccount=readXml.ReadXml('manager_manage', 'add_manager_account3')
    
    accDupErr=readXml.ReadXml('manager_manage', 'acc_dup_err')
    
    setPassword=readXml.ReadXml('manager_manage', 'add_manager_password')
    
    setAlertLots=readXml.ReadXml('manager_manage', 'add_alert_lot')
    
    setName=readXml.ReadXml('manager_manage', 'add_manager_name')
    
    setEmail=readXml.ReadXml('manager_manage', 'm_email')
    
    selectRole=readXml.ReadXml('manager_manage', 'select_manager_role')
    
    selectLangue=readXml.ReadXml('manager_manage', 'langue')
    
    submitBtn=readXml.ReadXml('manager_manage', 'confirm_btn')
    
    suc_info=readXml.ReadXml('manager_manage', 'suc_info')
        
    url1=clickAdd[0]
    
    
    
    #初始化
    def __init__(self):
        self.driver=BasePage.__init__(self,'ff')
        
    #返回当前webdriver    
    def get_driver(self):
        self.driver=self.driver
        return self.driver 
    
           
    #在新的标签页中打开地址为url的页面
    def openMMPage(self,url):
        self.openPage(url)
    
          
    #点击【新增】按钮      
    def click_add(self):
        
        self.click(self.findElement((self.clickAdd[1],self.clickAdd[2])))
        self.switch_to_latestWindow()
        
    def click_revise(self,manager_count):
        tup=self.get_firstcols(manager_count)
        if tup[1]==None:
            print 'Cannot find '+manager_count+' in the table!'
        else:
            tup[1].click()
            
        
    
     
    #输入账号前3位，默认为‘666’           
    def set_fron_account(self,fronaccount=setFronAccount[3]):
                
        self.type(self.findElement((self.setFronAccount[1],self.setFronAccount[2])), fronaccount)
    
     
    #输入账号后4位，默认为‘1111’     
    def set_back_account(self,backaccount=setBackAccount[3]):
        
        self.type(self.findElement((self.setBackAccount[1],self.setBackAccount[2])), backaccount)
    
    
    #获取重复账号信息
    def account_dup(self):
        
        tup=self.isElementExist((self.accDupErr[1],self.accDupErr[2]))
        if  isinstance(tup, tuple):
            return tup[1]
        else:return None
            
            
    #输入密码，默认为‘abc123’   
    def set_password(self,password=setPassword[3]):
        
        self.type(self.findElement((self.setPassword[1],self.setPassword[2])), password)
    
     
    #输入告警手数，默认为50    
    def set_alert_lots(self,alertlots=setAlertLots[3]):
        
        self.type(self.findElement((self.setAlertLots[1],self.setAlertLots[2])), alertlots)
    
    
    #输入用户名   
    def set_manager_name(self,managername):
        
        self.type(self.findElement((self.setName[1],self.setName[2])), managername) 
     
    #输入邮箱名   
    def set_email(self,email=setEmail[3]):
        
        self.type(self.findElement((self.setEmail[1],self.setEmail[2])), email) 
        
         
    #选择角色    
    def select_role(self,value=selectRole[3]):
        
        elem=self.findElement((self.selectRole[1],self.selectRole[2]))
        self.select_index(elem, value) 
        
    #选择语言    
    def select_langue(self,value=selectLangue[3]):
        
        elem=self.findElement((self.selectLangue[1],self.selectLangue[2]))
        self.select_index(elem, value)        
    
     
     
    #点击提交   
    def click_submit(self):
          
        self.click(self.findElement((self.submitBtn[1],self.submitBtn[2])))
        self.driver.implicitly_wait(30)
        self.switch_to_latestWindow()
        
    
    #确认添加成功
    def confirm(self):
                
        return self.findElement((self.suc_info[1],self.suc_info[2])).text        
         
    
    
    # 获取标题
    def page_title(self):
        return self.getTitle()
    
    
    #关闭driver
    def close_driver(self):
        self.close()
    
       
    
        
    
                
    
if __name__==('__main__'):
    test1=AddManagerPage()
    test1.openPage('https://trade.iwisetrader.com/Manager/Manager/Managers')      
        