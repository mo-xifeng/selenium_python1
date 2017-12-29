# -*- coding: UTF-8 -*- 
import xlrd
import xml.etree.ElementTree as ET
class OperationExcel(object): 
    
    #打开并得到Excel文件的对象book
    book=xlrd.open_workbook(r'C:\Users\Administrator\eclipse-workspace\selenium_use_case\test_case\Test preparation data.xlsx')

    #通过sheetname和elementsname读取Excel并返回一个list，例如[(u'id',u'form-username'),'6660021111']
    def readExcellEements(self,sheetname,value):        
        sheet1=self.book.sheet_by_name(sheetname)
        
        #num在0-表格总行数之间循环      
        for num in range(0,sheet1.nrows):
            row_data=sheet1.row_values(num)
            if value in row_data:
                x=num+1
                y=row_data.index(value)
                test_case_id= sheet1.cell_value(num,y-2)                
                str1=sheet1.cell_value(x,y)                
                #str1不含'/'时，转为tuple                
                if '/'not in str1:
                    elements_value=tuple(eval(str1))
                else:
                    elements_value=str1                                                                     
                data_value=sheet1.cell_value(x,y+1)                                                               
                str2= sheet1.cell_value(num,y-1)
                #判断字符串是否包含'/',是的话去除掉'/'之前和后3位字符.py，生成新的字符串 test_case_name
                if "/" in  str2:      
                    test_case_name=str2[str2.rindex(r"/")+1:-3]
                else: 
                    test_case_name=str2
                #生成并返回list1
                list1=[elements_value,data_value,test_case_id,test_case_name]
                #print list1
                return list1
                break
   
        
    #读取Sheet1中第2列内容,并且去掉''、'Function'和以#开头的
    def get_testcasename(self,sheetname):
        sheet1=self.book.sheet_by_name(sheetname)
        cols=sheet1.col_values(1)
        condition=lambda item:item !=''and item !='Function' and (not item.startswith('#')) 
        list1=filter(condition, cols)            
        #print list1
        return list1


class OperationXml():
    
    tree = ET.parse('C:\\Users\\selenium_python1\\common\\testdata.xml')     #打开xml文档 
    root=tree.getroot()
    manager_node=root.getchildren()
    
    def walkData(self,root_node, result_list):    
        temp_list =[root_node.tag, root_node]
        
        #temp_list =[self.unique_id, level, root_node.tag]  
        result_list.append(temp_list)          
        #遍历每个子节点，并且以[[root_node1.tag, root_node1],[root_node2.tag, root_node2]...]返回输入所有节点的节点位置和节点名  
        children_node = root_node.getchildren()  
        if len(children_node) == 0:  
            return  
        for child in children_node:  
            self.walkData(child, result_list)  
        return
    
       
    def ReadXml(self,page_name,elem_name):                  
        
        #level=1
        #在子节点中查找节点page_name
        child_node=self.manager_node[0].find(page_name)
        
        #把page_name的属性中获取testcase信息['id','testcasename','attch_url']
        testcase_info=child_node.attrib.values()
        result_list=[]
        self.walkData(child_node,result_list)
        elemdata=[]
        #查找到elem_name的节点位置
        for m in range(len(result_list)):
            list1=result_list[m]
            if elem_name in list1:
                
                #获取节点的属性和数据放在一个list中
                elemdata=list1[1].attrib.values()+[x.text for x in list1[1].getiterator()]
                
                #去掉以'\n\t'开头的str
                for value in elemdata:
                    if isinstance(value, str):
                        if value.startswith('\n\t'):              
                            elemdata.remove(value)  
        list2=testcase_info+elemdata       
        return list2    
    
    
    #获取要执行的testcasename，去掉含‘#’的
#     def get_excutename(self):
#         #获取根节点
#         for x in range(len(self.manager_node)):
#             child_node=self.manager_node[x].getchildren()
#             excute_testcase=[item.attrib['excutename'] for item in  child_node]
#             condition =lambda item: not item.startswith('#') 
#             excute_testcase=filter(condition,excute_testcase)
#         return excute_testcase

  

                
  
        
        
    
if __name__==('__main__'):
    test1=OperationXml()
    test2=OperationExcel()
    a= test1.ReadXml('manager_manage','add_btn')
    print a
    test2.readExcellEements('Sheet1','user_elements')
