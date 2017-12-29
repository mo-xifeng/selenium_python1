# -*- coding: utf-8 -*-
import logging
import ResultFolder

#创建 logger实例
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


#创建日志文件
def CreateLoggerFile(filename):
    try:
        fulllogname = ResultFolder.GetRunDirectory()+"\\"+filename+".log"
        fh = logging.FileHandler(fulllogname)
        fh.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s [line:%(lineno)d] %(message)s')
        fh.setFormatter(formatter)
        logger.addHandler(fh)
    except Exception as err:
        logger.debug("Error when creating log file, error message: {}".format(str(err)))

#添加调试message
def Log(message):
    logger.debug(message)