# coding=utf-8
class Exception(BaseException):
    _errorNo = 0
    _errorMsg = None
    _errorLevel = 0
    def __init__(self,errorNo,errorMsg,errorLevel=1):
        self._errorNo = errorNo
        self._errorMsg = errorMsg
        self._errorLevel = errorLevel