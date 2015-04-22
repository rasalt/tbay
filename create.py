from tbay import User, Item, Bid, session
from datetime import datetime
#name = Column(String, nullable=False)
#password = Column(String, nullable=False)
Eminem = User(id=2, name = "Eminem", password = "Eminem")
Coldplay = User(id=3, name = "Coldplay", password = "Coldplay")

baseballr = Item(id=1, name = "baseball", description = "Red", start_time=datetime.utcnow())

basebally = Item(id=2, name = "baseball", description = "Yellow", start_time=datetime.utcnow())
baseballv = Item(id=3, name = "baseball", description = "Violet", start_time=datetime.utcnow())

session.add(Eminem)
session.add(Coldplay)

session.add(baseballr)
session.add(basebally)
session.add(baseballv)

session.commit()


#id = Column(Integer, primary_key=True)
#  name = Column(String, nullable=False)
#  description = Column(String)
#  start_time = Column(DateTime, default=datetime.utcnow)