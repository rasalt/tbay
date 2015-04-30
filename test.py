from sqlalchemy import Table, Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from tbay import User, Bid, Item
engine = create_engine('postgresql://action:action@localhost:5432/tbay')
Session = sessionmaker(bind=engine)
session = Session()

# Adding users to the tbay database
user1 = User(name="Ruchika",password="Ruchika")
user2 = User(name="Shilpa",password="Shilpa")
user3 = User(name="Akanskha",password="Akanksha")
session.add(user1)
session.add(user2)
session.add(user3)

item1 = Item(name="BallR",description="Red Ball",cost=5.25)
item2 = Item(name="BallY",description="Yellow Ball",cost=6.25)
item3 = Item(name="BallG",description="Green Ball",cost=7.25)

session.add_all([item1, item2, item3])
session.commit()

user1.sell = [item1, item2]
session.commit()

#List the items a user is selling

print "Printing items for sale by user1"
for sale in user1.sell:
  print "sale is {}".format(sale.name)

for users in item1.users:
  print "user is {}".format(users.name)
  
bid1 = Bid(price=8.25, item = item1, user=user2)
#bid1.item = item1

bid2 = Bid(price=9.0, item = item2, user =user3 )
bid3 = Bid(price=9.5, item = item1, user =user2 )

session.commit()

# Print the bids on a given item
print "Item name is {}".format(item1.name)
for bi in item1.bids:
  print "bid information is {}".format(bi.price)
  print "user id is {}".format(bi.user_id)
  
  # Print the bids on a given item
print "Item name is {}".format(item2.name)
for bi in item2.bids:
  print "bid information is {}".format(bi.price)
  print "user id is {}".format(bi.user_id)
  
# Print the bids on a given item
print "Item name is {}".format(item3.name)
for bi in item3.bids:
  print "bid information is {}".format(bi.price)
  print "user id is {}".format(bi.user_id)

# Query fr printing the max price for a given item

#select  max(price) from  (select tbayuser.name, price, bid.item_id from tbayuser, bid, item where tbayuser.id=bid.user_id and bid.item_id=item.id) A  group by A.item_id;  
