from sqlalchemy import Table, Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime

engine = create_engine('postgresql://action:action@localhost:5432/tbay')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

sell_table = Table('tbay_sell_association', Base.metadata,
    Column('item_id', Integer, ForeignKey('item.id')),
    Column('user_id', Integer, ForeignKey('tbayuser.id'))
)

#bid_table = Table('tbay_bid_association', Base.metadata,
#    Column('bid_id', Integer, ForeignKey('bid.id')),              
#    Column('user_id', Integer, ForeignKey('tbayuser.id'))
#)

biditem_table = Table('tbay_biditem_association', Base.metadata,
    Column('item_id', Integer, ForeignKey('item.id')),
    Column('bid_id', Integer, ForeignKey('bid.id')),           
)

class Item(Base):
  __tablename__ = "item"
  
  id = Column(Integer, primary_key=True)
  name = Column(String, nullable=False)
  description = Column(String)
  start_time = Column(DateTime, default=datetime.utcnow)
  cost = Column(Float, default=0.0)
  bids = relationship("Bid", backref="item")
  
  def __str__(self):
    str = "id= " + `self.id` + " name= " + self.name + " description= " + self.description + " cost= " + self.cost
    return str  


class User(Base):
  __tablename__ = "tbayuser"
  
  id = Column(Integer, primary_key=True)
  name = Column(String, nullable=False)
  password = Column(String, nullable=False)
  sell = relationship("Item", secondary="tbay_sell_association",
                            backref="users")
  bid = relationship("Bid", backref="user")
                      
#  bids = relationship("Bid", secondary="tbay_bid_association",
#                            backref="users")
  def __str__(self):
    str = "id= " + `self.id` + " name= " + self.name + " pass= " + self.password
    return str  

  
class Bid(Base):
  __tablename__ = "bid"
  
  id = Column(Integer, primary_key=True)
  price = Column(Float, nullable=False)
  bid_time = Column(DateTime, default=datetime.utcnow)
  item_id = Column(Integer, ForeignKey('item.id'), nullable=False)
  user_id = Column(Integer, ForeignKey('tbayuser.id'), nullable=False)
  
Base.metadata.create_all(engine)



