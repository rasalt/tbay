from tbay import User, Item, Bid, session
from datetime import datetime
#name = Column(String, nullable=False)
#password = Column(String, nullable=False)
#beyonce = User(id=1, name = "Beyonce", password = "Beyonce")
#session.add(beyonce)
#session.commit()


# Query the database

print("Printing the first user ")
firstuser = session.query(User).first()
print("First: {}".format(firstuser))

print("Printing all the rows from the User table ")
userlist = []
userlist = session.query(User).all()
for user in userlist:
  print("user {}".format(user))

print "Return a user with a user id of 2"
id = 1
user = session.query(User).get(id)
print "User with {} and user is {}".format(id,user)

print "Returning all users orderend by name in ascending order"
userlist = []
userlist = session.query(User.name).order_by(User.name).all()
for user in userlist:
  print("user {}".format(user))

print "Description of all the items in the database which have a name baseball"

# Returns the description of all of the basesballs
itemlist = []
itemlist = session.query(Item.description).filter(Item.name == "baseball").all()
for item in itemlist:
  print("item {}".format(item))
  
# Return the item id and description for all baseballs which were created in the past.  Remember to import the datetime object: from datetime import datetime
itemlist = session.query(User.id, User.name).filter(User.name == "baseball", Item.start_time < datetime.utcnow()).all()

item = session.query(Item).first()
item.name = "CricketBall"
session.commit()

itemlist = []
itemlist = session.query(Item.name).order_by(Item.name).all()
for item in itemlist:
  print("item {}".format(item))

print("Deleting the first user")
user = session.query(User).first()
session.delete(user)
session.commit()
print("Printing all the rows from the User table ")
userlist = []
userlist = session.query(User).all()
for user in userlist:
  print("user {}".format(user))
