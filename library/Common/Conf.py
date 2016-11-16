# coding=utf-8
"""
@author wangshuai
@date 2016-11-15
@desc 读取配置文件
"""
from ConfigParser import RawConfigParser
from Common.Const import APP_PATH,LOG_FATAL_LEVEL,PARAM_ERROR
from Common.Exception import Exception
from string import split
class Conf(object):
    """
    获取Conf配置文件中的信息
    path:"section" ----conf/global.conf 下的section
    path:"section/option" -----conf/global.conf下的section中的option
    path:"path/section/option" -----conf/path.conf下的section中的option
    """
    @staticmethod
    def getConf(path):
        path = split(path, "/")
        path_len = len(path)
        if(path_len == 1):
            field = None
            section = path[0]
            path = APP_PATH + "/conf/global.conf"
        elif(path_len == 2):
            field = None
            section = path[1]
            path = APP_PATH + "/conf/" + path[0] + ".conf"
        elif(path_len == 3):
            field = path[2]
            section = path[1]
            path = APP_PATH + "/conf/" + path[0] + ".conf"
        else:
            raise Exception(PARAM_ERROR,"参数设置异常",LOG_FATAL_LEVEL)
        rcp = RawConfigParser()
        rcp.read(path)
        if(field != None):
            items = rcp.get(section,field)
        else:
            items = rcp.items(section)
            items_len = len(items)
            dict = {}
            for index in range(items_len):
                tuple = items[index]
                dict[tuple[0]] = tuple[1]
            items = dict
        return items

    """
    获取global.conf中的内容
    name : "section" -----conf/global.conf下的section
    name : "section/field"  -----conf/global.conf下section中的field的值
    """
    @staticmethod
    def getAppConf(name):
        name = "global/" + name
        return Conf.getConf(name)