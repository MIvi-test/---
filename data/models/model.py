from sqlalchemy import create_engine, MetaData, Table, Integer, String, \
    Column, DateTime, ForeignKey, Numeric, SmallInteger, Date, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from sqlalchemy.orm import registry
from sqlalchemy.orm import Session
from aiogram import types
# https://pythonru.com/biblioteki/shemy-v-sqlalchemy-orm
#регистрация классов

mapper_registry = registry()
Base = mapper_registry.generate_base()
engine = create_engine("postgresql+psycopg2://postgres:1122banforChild_@localhost:8000/sqlalchemy_tuts")
session = Session(bind=engine)
#создание классов-моделей для базы данных
class User(Base):
    __tablename__ = 'User'
    Id = Column(Integer(), primary_key=True, nullable=False)
    Username = Column(String(100), nullable=False)
    Balance = Column(Integer() )
    is_baned = Column(Boolean()) 
    
    
    
class ModelConnect():
    
    def __init__(self) -> None:
        mapper_registry = registry()
        self.Base = mapper_registry.generate_base()
        engine = create_engine("postgresql+psycopg2://postgres:1122banforChild_@localhost:8000/sqlalchemy_tuts")
        self.session = Session(bind=engine)
    
    
    async def ADDuser(self, message: types.Message):
        id = message.from_user.id
        usname = message.from_user.username
        user = User(
            Id = id,
            Username = usname,
            Balance = 100,
            is_baned = False
        )
        try:
            if self.session.query(User).get(id) == None:
                self.session.add(user)
        except Exception as ex:
            print("ну ладно")
        finally:
            self.Base.metadata.create_all(self.engine)

            self.session.commit()
    def AllData(self):
        try:
            print(self.session.query(User).all())
        except:
            pass
        finally:
            self.session.commit() 
    def ADDbalance(self, username, money):
        try:            
            
            OLDbalance = self.session.query(User.Balance).filter(User.Username == username).all()
            
            self.session.execute(f"UPDATE kazino_users SET balance = {money + OLDbalance} WHERE id = {id}")
        except:
            pass
        finally:
            self.Base.metadata.create_all(self.engine)

            self.session.commit()
            
    def CHEKbalance(self, message:types.Message):
        try:
            OLDbalance = self.session.query(User.Balance).filter(User.id == message.from_user.id).all()
        except:
            pass
        finally:
            self.session.commit()
    def upload(self):
    #загрузка моделей для базы данных     
        self.Base.metadata.create_all(self.engine)

        self.session.commit()       
    

us = ModelConnect()
us.AllData()

# Base.metadata.create_all(engine)
session.commit()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        