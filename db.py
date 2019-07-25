__author__ = "Mosia Hryhorii (grishamosya@gmail.com)"

from sqlalchemy import create_engine, desc
from sqlalchemy.orm import sessionmaker

from models import Base, FreeProxyModel


class DB:
    __model = FreeProxyModel

    def __init__(self, schema, user, password, host, db_name, limit,
                 echo=False):
        self.limit = limit
        self.engine = create_engine(
            f'{schema}://{user}:{password}@{host}/{db_name}', echo=echo)

        self.create_all_table()

        DBSession = sessionmaker(bind=self.engine)
        self.session = DBSession()

    def create_all_table(self):
        Base.metadata.create_all(bind=self.engine)

    def save_to_db(self, scrap_rez: list):
        for item in scrap_rez:
            proxy_save = self.__model(
                ip_address=item['ip_address'],
                port=item['port'],
                code=item['code'],
                country=item['country'],
                anonymity=item['anonymity'],
                google=item['google'],
                https=item['https'],
                last_checked=item['last_checked']
            )

            proxy_db = self.session.query(self.__model).filter(
                self.__model.ip_address == item['ip_address']).first()

            if proxy_save != proxy_db:
                try:
                    self.session.add(proxy_save)
                    self.session.commit()
                except Exception as e:
                    print(e)
                    self.session.rollback()

        if self.limit:
            self.del_max()

    def del_max(self):
        last_proxy = self.session.query(self.__model) \
            .order_by(desc(self.__model.time_created and self.__model.id)) \
            .first()

        try:
            delete_q = self.__model.__table__.delete() \
                .where(self.__model.id < last_proxy.id - self.limit + 1)
            self.session.execute(delete_q)
            self.session.commit()
        except Exception as e:
            print(e)
            self.session.rollback()

    def get_proxy(self):
        return self.session.query(self.__model).all()
