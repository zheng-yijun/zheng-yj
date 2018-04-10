#-*-coding:utf-8-*-
__author__ = 'zhengyj'

from sqlalchemy import Column,Integer,String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql+pymysql://admin:makecook@192.168.95.11/zyj',echo=False)
Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer,primary_key=True)
    name = Column(String(32))

    def __repr__(self):
        return "id:%r,name:%r" % (self.id,self.name)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

session = Session()

# user_obj = User(id=1,name='zhengyj')
# session.add(user_obj)
# session.commit()
Query_data = session.query(User).filter_by(name='zhengyj').all()
print(Query_data)