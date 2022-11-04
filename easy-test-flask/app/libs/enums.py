"""
@Desc    : 枚举类
"""
from enum import Enum, unique


@unique
class UserAuthEnum(Enum):
    """用户权限枚举类"""
    GROUP = 1
    PROJECT = 2


@unique
class CaseMethodEnum(Enum):
    """用例请求方法枚举类"""
    GET = 1
    POST = 2
    PUT = 3
    DELETE = 4

    @classmethod
    def data(cls):
        return {
            cls.GET.value: cls.GET.name,
            cls.POST.value: cls.POST.name,
            cls.PUT.value: cls.PUT.name,
            cls.DELETE.value: cls.DELETE.name
        }


@unique
class CaseSubmitEnum(Enum):
    """用例提交方法枚举类 """
    JSON = 1
    FORM = 2

    @classmethod
    def data(cls):
        return {
            cls.JSON.value: cls.JSON.name,
            cls.FORM.value: cls.FORM.name
        }


@unique
class CaseDealEnum(Enum):
    """用例后置处理方法枚举类"""
    NOT = 1
    # 默认处理  存取所有的键值对
    DEFAULT = 2
    # 指定key 存value
    JSON = 3
    # 正则表达式
    REGULAR = 4
    # 自定义处理,支持写一个python方法,参数为接口返回数据\当前运行工程的全局变量字典，返回一个字典，如下：
    """
    def my_customize(data, var_dick):
        age = var_dick['age']
        for i in data:
            if i['age'] == age:
                name = i['name']
                return {'name': name}
    """
    CUSTOMIZE = 5

    @classmethod
    def data(cls):
        return {
            cls.NOT.value: '不做处理',
            cls.DEFAULT.value: '保存全部键值对',
            cls.JSON.value: 'json提取器',
            cls.REGULAR.value: '正则表达式',
            cls.CUSTOMIZE.value: '自定义处理'
        }


@unique
class CaseTypeEnum(Enum):
    """用例类型枚举类"""
    INTERFACE = 1
    UI = 2

    @classmethod
    def data(cls):
        return {
            cls.INTERFACE.value: cls.INTERFACE.name,
            cls.UI.value: cls.UI.name
        }


@unique
class CaseAssertEnum(Enum):
    """用例断言类型枚举类"""
    EQUAL = 1
    NOTEQUAL = 2
    IN = 3
    NOTIN = 4
    SUCCESS = 5

    @classmethod
    def data(cls):
        return {
            cls.EQUAL.value: cls.EQUAL.name,
            cls.NOTEQUAL.value: cls.NOTEQUAL.name,
            cls.IN.value: cls.IN.name,
            cls.NOTIN.value: cls.NOTIN.name,
            cls.SUCCESS.value: cls.SUCCESS.name
        }


@unique
class ProjectTypeEnum(Enum):
    """工程型枚举类"""
    RELATION = 1
    COPY = 2

    @classmethod
    def data(cls):
        return {
            cls.RELATION.value: '关联',
            cls.COPY.value: '副本'
        }


@unique
class CaseExcelEnum(Enum):
    """用例表格枚举类"""
    NAME = 0
    GROUP = 1
    URL = 2
    METHOD = 3
    DATA = 4
    HEADER = 5
    SUBMIT = 6
    DEAL = 7
    CONDITION = 8
    ASSERTION = 9
    EXPECTION = 10
    INFO = 11


@unique
class EmailStrategyEnum(Enum):
    """邮件发送策略枚举类"""
    ALL = 1
    SUCCESS = 2
    FAIL = 3

