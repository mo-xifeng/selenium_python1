#Embedded file name: C:\Users\Administrator\eclipse-workspace\selenium_use_case\test_case\WebPages\BasePage.py
#-*- coding:utf-8 -*- 
from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.common.exceptions import StaleElementReferenceException
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
#from selenium.webdriver.support.ui import Select

class BasePage(object):
    """description of class"""
#     def set_brower(self):
#         
#         self.driver = webdriver.Firefox()
#         self.driver.maximize_window()
#         print 'base=',self.driver
#         return self.driver
    def __init__(self,browser):
        """
        initialize selenium webdriver, use chrome as default webdriver
        """
        if browser == 'firefox' or browser == 'ff':
            driver = webdriver.Firefox()
        elif browser == 'chrome':
            driver = webdriver.Chrome()
        elif browser == 'internet explorer' or browser == 'ie':
            driver = webdriver.Ie()
        elif browser == 'opera':
            driver = webdriver.Opera()
        elif browser == 'phantomjs':
            self.driver = webdriver.PhantomJS()        
        try:
            self.driver = driver
        except Exception:
            raise NameError("Not found %s browser,You can enter 'ie', 'ff' or 'chrome'." % browser)
        return self.driver
        
    def findElement(self,element):
        '''
        Find element
        element is a set with format (identifier type, value), e.g. ('id','username')
        Usage:
        self.findElement(element)
        '''
        try:
            type = element[0]
            value = element[1]
            if type == "id" or type == "ID" or type=="Id":
                elem = self.driver.find_element_by_id(value)

            elif type == "name" or type == "NAME" or type=="Name":
                elem = self.driver.find_element_by_name(value)

            elif type == "class" or type == "CLASS" or type=="Class":
                elem = self.driver.find_element_by_class_name(value)

            elif type == "link_text" or type == "LINK_TEXT" or type=="Link_text":
                elem = self.driver.find_element_by_link_text(value)

            elif type == "xpath" or type == "XPATH" or type=="Xpath":
                elem = self.driver.find_element_by_xpath(value)

            elif type == "css" or type == "CSS" or type=="Css":
                elem = self.driver.find_element_by_css_selector(value)
            else:
                raise NameError("Please correct the type in function parameter")
        except Exception:
            raise ValueError("No such element found"+ str(element))
        return elem
    
    
    def findElements(self, element):
        """
        Find elements
        
        element is a set with format (identifier type, value), e.g. ('id','username')
        
        Usage:
        self.findElements(element)
        """
        try:
            type1 = element[0]
            value = element[1]
            if type1 == 'id' or type1 == 'ID' or type1 == 'Id':
                elem = self.driver.find_elements_by_id(value)
            elif type1 == 'name' or type1 == 'NAME' or type1 == 'Name':
                elem = self.driver.find_elements_by_name(value)
            elif type1 == 'class' or type1 == 'CLASS' or type1 == 'Class':
                elem = self.driver.find_elements_by_class_name(value)
            elif type1 == 'link_text' or type1 == 'LINK_TEXT' or type1 == 'Link_text':
                elem = self.driver.find_elements_by_link_text(value)
            elif type1 == 'xpath' or type1 == 'XPATH' or type1 == 'Xpath':
                elem = self.driver.find_elements_by_xpath(value)
            elif type1 == 'css' or type1 == 'CSS' or type1 == 'Css':
                elem = self.driver.find_elements_by_css_selector(value)
            elif type1=='tag' or  type1 == 'Tag' or type1 == 'TAG':
                elem = self.driver.find_elements_by_tag_name(value)
            else:
                raise NameError('Please correct the type in function parameter')
        except Exception:
            raise ValueError('No such element found' + str(element))

        return elem

    def open(self, url):
        """
        Open web url
        
        Usage:
        self.open(url)
        """
        if url != '':
            self.driver.get(url)
        else:
            raise ValueError('please provide a base url')

    def type(self, element, text):
        """
        Operation input box.
        
        Usage:
        self.type(element,text)
        """
        element.clear()
        element.send_keys(text)

    def enter(self, element):
        """
        Keyboard: hit return
        
        Usage:
        self.enter(element)
        """
        element.send_keys(Keys.RETURN)

    def click(self, element):
        """
        Click page element, like button, image, link, etc.
        """
        element.click()
        
        
    def close(self):
        """
        close driver
        """        
        self.driver.close()
        

    def quit(self):
        """
        Quit webdriver
        """
        self.driver.quit()

    def getAttribute(self, element, attribute):
        """
        Get element attribute
        
        """
        return element.get_attribute(attribute)

    def getText(self, element):
        """
        Get text of a web element
        
        """
        return element.text

    def getTitle(self):
        """
        Get window title
        """
        return self.driver.title

    def getCurrentUrl(self):
        """
        Get current url
        """
        return self.driver.current_url

    def getScreenshot(self, targetpath):
        """
        Get current screenshot and save it to target path
        """
        self.driver.get_screenshot_as_file(targetpath)
    
        
    def get_firstcols(self,value):
        """
        Get the firstcols of the current_page_table,return a list
        """
        table=self.findElement(('id','table'))
        rows=table.findElements(('tag','tr'))
        cols=table.findElements(('tag','th'))
        firstcols=[]
        for m in range(len(rows)):                         
            firstcols.append(rows[m].findElements(('tag','th'))[0].text) 
        for n in range(len(cols)):
            if value== cols[n]:
                elem= rows[n].findElements(('tag','th'))[len(cols)-1]
                break
            else:elem=None        
        return firstcols,elem

    def maximizeWindow(self):
        """
        Maximize current browser window
        """
        self.driver.maximize_window()

    def back(self):
        """
        Goes one step backward in the browser history.
        """
        self.driver.back()

    def forward(self):
        """
        Goes one step forward in the browser history.
        """
        self.driver.forward()

    def getWindowSize(self):
        """
        Gets the width and height of the current window.
        """
        return self.driver.get_window_size()

    def refresh(self):
        """
        Refresh current page
        """
        self.driver.refresh()
        self.driver.switch_to()
        
    def select_value(self,elem,value):
        """
        select  drop-down box by value
        """
        Select(elem).select_by_value(value)
    
        
    def select_index(self,element,value):
        """
        select  drop-down box by index
        """    
        Select(element).select_by_index(value)
     
        
    def isElementExist(self,element):
        """
        confirm element exist or not   
        """ 
        flag=True
        try:
            info=self.findElement(element).text
            return flag,info
        except:
            flag=False
            return flag
    
        
    #在新的标签页中打开地址为url的页面
    def openPage(self,url):
        """
        Open url on new pages   
        """
        js='window.open("{value}")'.format(value=url)
        self.driver.execute_script(js)
        self.driver.switch_to_window(self.driver.window_handles[1])
     
        
    #handle指向最新的windows    
    def switch_to_latestWindow(self):
        """
        Make handle switch to latestWindow 
        """
        m=len(self.driver.window_handles)
        self.driver.switch_to_window(self.driver.window_handles[m])   
        
    
        
if __name__==('__main__'):
    test1=BasePage()
    test1.openNewWindow('https://trade.iwisetrader.com/Manager/Manager/Managers')
        
