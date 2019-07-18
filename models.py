from sqlalchemy import Column, Integer, String, DateTime, CHAR
from sqlalchemy.dialects import mysql
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.sql import func


@as_declarative()
class Base(object):
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())


class FreeProxyModel(Base):
    ip_address = Column(String(15))
    port = Column(mysql.INTEGER(6))
    code = Column(CHAR(5))
    country = Column(String(50))
    anonymity = Column(String(50))
    google = Column(CHAR(5))
    https = Column(CHAR(3))
    last_checked = Column(String(50))

    def __str__(self):
        return self.ip_address

    def get_dict(self):
        return dict(ip_address=self.ip_address, port=self.port,
                    code=self.code, country=self.country,
                    anonymity=self.anonymity, google=self.google,
                    https=self.https)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.get_dict() == other.get_dict()
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)
