from Common.Conf import Conf
from Common.Exception import Exception
if __name__ == "__main__":
    try:
        result = Conf.getConf("global/log")
        print result
    except Exception,e:
        print "[errorNo]:%d  [errorMsg]:%s" % (e._errorNo, e._errorMsg)