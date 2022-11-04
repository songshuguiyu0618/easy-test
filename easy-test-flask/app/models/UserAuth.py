"""
@Desc    : 用户权限分配表 对用户可操作的测试分组、测试项目授权
"""
from lin.interface import InfoCrud as Base
from sqlalchemy import Column, SmallInteger, Integer

from app.libs.enums import UserAuthEnum


class UserAuth(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False, comment='用户id')
    auth_id = Column(Integer, nullable=False, comment='权限id')
    _type = Column('type', SmallInteger, nullable=False,comment='权限id类型 ;  1 -> group分组 |  2 -> project工程')

    @property
    def type(self):
        return UserAuthEnum(self._type)

    @type.setter
    def type(self,user_auth):
        self._type = user_auth.value

    @classmethod
    def get_user_auth(cls,user_id, auth_id, type):
        auth = UserAuth.query.filter().filter_by(user_id=user_id,auth_id=auth_id,_type=type).first()
        return auth
