from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from application.model import Base
from flask import g


class DBManager:
    __engine = None
    __session = None

    @staticmethod
    def init(db_url):

        DBManager.__engine = create_engine(db_url, echo = True) # 인자로 엔진객체 생성
        DBManager.__session = \
            scoped_session(sessionmaker(autocommit=False,
                                        autoflush=False, 
                                        bind=DBManager.__engine)) #세션레지스트리 얻어서

        g.dao = DBManager.__session #dao에 할당, 다른 모듈에서 참조가능
        print('*'*100)
        print('init')
        print(g.dao)
        print('*'*100)
            
    @staticmethod
    def init_db(): #모델을 연결된 데이터베이스에 생성하는 함수
        Base.metadata.create_all(bind=DBManager.__engine) #데이터베이스 테이블 생성
        print('*'*100)
        print('init_db')
        print('*'*100)
