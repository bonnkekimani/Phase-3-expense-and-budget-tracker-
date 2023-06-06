# from random import randint, seed
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy.orm import sessionmaker
# create_engine('sqlite://restaurants.db')
Base = declarative_base()
class Customer(Base):
    __tablename__ = 'customers'
    id = Column (Integer(), primary_key= True)
    firstName = Column(String())
    lastName = Column(String())
    reviews = relationship('Review', backref=backref('customer'))
    def __repr__(self):
        return f'Review(id = {self.id})'+\
           f'firstName = {self.firstName}'+\
           f'lastName={self.lastName}'
class Review(Base):
    __tablename__ = 'reviews'
    id = Column (Integer(), primary_key=True)
    rating = Column(Integer())
    Customer_review = Column(String())
    customer_id = Column(Integer(), ForeignKey('customers.id'))
    restaurant_id = Column(Integer(), ForeignKey('restaurants.id'))
    def __repr__(self):
        return f'Review(id = {self.id})'+\
           f'rating = {self.rating}'+\
           f'customer_id={self.customer_id}'
class Restaurant(Base):
    __tablename__ = 'restaurants'
    id = Column(Integer(), primary_key= True)
    Restaurant_Name = Column(String())
    reviews = relationship('Review', backref=backref('restaurant'))
    def __repr__ (self):
        return f'Restaurant(id = {self.id})'+\
            f'name={self.name}'
if __name__ == '__main__':
    engine = create_engine('sqlite:///restaurants.db')
    Base.metadata.create_all(engine)
     # use our engine to configure a 'Session' class
    Session = sessionmaker(bind=engine)
    # use 'Session' class to create 'session' object
    session = Session()
# Review Instances
    review1 = Review(
        rating = 4.5,
        Customer_review ="The pizza here is amazing! Highly recommend. ",
        customer_id = "John Smith", 
        restaurant_id = 4
        )
    review2 = Review(
        rating = 3.2,
        Customer_review ="The burgers were okay, nothing special.",
        customer_id = "Alex Brown", 
        restaurant_id = 5
        )
    review3 = Review(
        rating = 5.0,
        Customer_review =" Best sushi in town! Fresh and delicious. ",
        customer_id = "Mark Johnson", 
        restaurant_id = 2
        )
    review4 = Review(
        rating = 4.8,
        Customer_review =" The pasta dishes were outstanding.  ",
        customer_id = "David Lee", 
        restaurant_id = 7
        )
    review5 = Review(
        rating = 2.5,
        Customer_review ="Disappointing tacos. Lacked flavor.",
        customer_id = "Emily Davis", 
        restaurant_id = 6
        )
    review6 = Review(
        rating = 4.0,
        Customer_review =" The steak was perfectly cooked. Loved it.",
        customer_id = "Sarah Meg", 
        restaurant_id = 2
        )
    review7 = Review(
        rating = 5,
        Customer_review ="Great service and friendly staff. Will visit again! ",
        customer_id = "John Smith", 
        restaurant_id = 4
        )
    # Create Restaurants(Instances)
    restaurant1 = Restaurant(
        Restaurant_Name = "Bistro Bites"
        )
    restaurant2 = Restaurant(
        Restaurant_Name = "Steak House"
        )
    restaurant3 = Restaurant(
        Restaurant_Name = "Sushi Sushi"
        )
    restaurant4 = Restaurant(
        Restaurant_Name = "Pizza Palace"
        )
    restaurant5 = Restaurant(
        Restaurant_Name = "Burger Bistro"
        )
    restaurant6 = Restaurant(
        Restaurant_Name = "Tacos Tacos"
        )
    restaurant7 = Restaurant(
        Restaurant_Name = "Pasta Paradise"
        )
    # Create Customers(Instances)
    customer1 = Customer(
        firstName = "John",
        lastName= "Smith"
        )
    customer2 = Customer(
        firstName = "Alex",
        lastName= "Brown"
        )
    customer3 = Customer(
        firstName = "Mark",
        lastName= "Johnson"
        )
    customer4 = Customer(
        firstName = "David",
        lastName= "Lee"
        )
    customer5 = Customer(
        firstName = "Emily",
        lastName= "Davis"
        )
    customer6 = Customer(
        firstName = "Sarah",
        lastName= "Meg"
        )
    customer7 = Customer(
        firstName = "Mike",
        lastName= "Sam"
        )
   
   
    session.add_all([review1, review2,review3,review4,review5,review6,review7])
    session.add_all([restaurant1, restaurant2,restaurant3,restaurant4,restaurant5,restaurant6,restaurant7])
    session.add_all([customer1, customer2,customer3,customer4,customer5,customer6,customer7])
    session.commit()

#   returns the customer's given name
    reviews = session.query(Review).filter(Review.restaurant_id == 1)
    for review in reviews:
        print("returns the customer's given name")
        print (review.customer_id)

#   returns the customer's family name
    reviews = session.query(Review).all()
    for review in reviews:
        print (review.customer_id)
   
# #    returns the full name of the customer, with the given name and the family name concatenated, Western style.
    customers = session.query(Customer).all()
    for customer in customers:
       print(customer.firstName +' ' +customer.lastName)