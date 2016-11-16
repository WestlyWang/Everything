#coding=utf-8
from Common.Conf import Conf
from Common.Const import APP_PATH,OS_ERROR,LOG_FATAL_LEVEL,LOG_WARNING_LEVEL,LOG_NOTICE_LEVEL,LOG_TRACE_LEVEL,LOG_DEBUG_LEVEL
from time import gmtime, strftime
from os import makedirs
from os.path import isdir,exists
class Log(object):
    _APP_NAME = None
    _LOG_PATH = None
    _STR_TIME = None
    _FILE_NAME =None
    @staticmethod
    def _init():
        appName = Conf.getAppConf("ap/name")
        logPath = Conf.getAppConf("log/path")
        Log._STR_TIME = strftime("%Y%m%d%H", gmtime())
        Log._APP_NAME = appName
        Log._LOG_PATH = APP_PATH + logPath + "/" + appName
        Log._FILE_NAME = Log._APP_NAME + "_log_" + Log._STR_TIME + ".log"

    @staticmethod
    def log(msg, level = LOG_TRACE_LEVEL):
        if(level == LOG_FATAL_LEVEL):
            Log.fatal(msg)
        elif(level == LOG_WARNING_LEVEL):
            Log.warning(msg)
        elif(level == LOG_NOTICE_LEVEL):
            Log.notice(msg)
        elif(level == LOG_TRACE_LEVEL):
            Log.trace(msg)
        else:
            Log.debug(msg)

    @staticmethod
    def fatal(msg):
        Log._init()
        format = "[Fatal][Time:%s][Application:%s][Msg:%s]"
        content = (Log._STR_TIME,Log._APP_NAME,msg)
        msg = format % content
        Log._writeFile(Log._LOG_PATH,Log._FILE_NAME,msg)

    @staticmethod
    def warning(msg):
        Log._init()
        format = "[Warning][Time:%s][Application:%s][Msg:%s]"
        content = (Log._STR_TIME,Log._APP_NAME,msg)
        msg = format % content
        Log._writeFile(Log._LOG_PATH, Log._FILE_NAME, msg)

    @staticmethod
    def notice(msg):
        Log._init()
        format = "[Notice][Time:%s][Application:%s][Msg:%s]"
        content = (Log._STR_TIME,Log._APP_NAME,msg)
        msg = format % content
        Log._writeFile(Log._LOG_PATH, Log._FILE_NAME, msg)

    @staticmethod
    def trace(msg):
        Log._init()
        format = "[Trace][Time:%s][Application:%s][Msg:%s]"
        content = (Log._STR_TIME,Log._APP_NAME,msg)
        msg = format % content
        Log._writeFile(Log._LOG_PATH, Log._FILE_NAME, msg)

    @staticmethod
    def dubug(msg):
        Log._init()
        format = "[Debug][Time:%s][Application:%s][Msg:%s]"
        content = (Log._STR_TIME,Log._APP_NAME,msg)
        msg = format % content
        Log._writeFile(Log._LOG_PATH, Log._FILE_NAME, msg)

    @staticmethod
    def _writeFile(path,file,msg):
        Log._createFile(path)
        try:
            path = path + "/" + file
            fp = open(path,'a+')
            fp.write(msg)
            fp.write("\n")
            fp.close()
        except Exception,e:
            raise Exception(OS_ERROR,"日志无法写入日志文件",LOG_FATAL_LEVEL)
        pass

    @staticmethod
    def _createFile(path):
        if((not exists(path)) or (not isdir(path))):
            try:
                makedirs(path)
            except Exception,e:
                raise Exception(OS_ERROR,"无法创建日志文件",LOG_FATAL_LEVEL)