# from random import randint, seed
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy.orm import sessionmaker
import datetime 
# create_engine('sqlite://tracker.db')
Base = declarative_base()
class Budget(Base):
    __tablename__ = 'budgets'
    id = Column (Integer(), primary_key= True)
    budgetName = Column(String())
    startDate = Column(datetime())
    endDate = Column(datetime())
    limit = Column(Integer())
    category_id = Column(Integer(), ForeignKey('categories.id'))
    reviews = relationship('Category', backref=backref('expense'))
    def __repr__(self):
        return f'Category(id = {self.id})'+\
           f'categoryName = {self.categoryName}'+\
           
class Category(Base):
    __tablename__ = 'categories'
    id = Column (Integer(), primary_key=True)
    categoryName = Column(String())
    Customer_review = Column(String())
    def __repr__(self):
        return f'Review(id = {self.id})'+\
           f'rating = {self.rating}'+\
           f'customer_id={self.customer_id}'
class Expense(Base):
    __tablename__ = 'expenses'
    id = Column(Integer(), primary_key= True)
    Expense_Name = Column(String())
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
# Budget Instances
    budget1 = Budget(
        budgetName = "Alvin's Budget",
        startDate = 1/1/2010,
        endDate = 2/2/2010,
        limit = 10000
        )
    budget2 = Budget(
        budgetName = "Kai's Budget",
        startDate = 1/1/2010,
        endDate = 2/2/2010,
        limit = 10000
        )
    budget3 = Budget(
        budgetName = "Ethan's Budget",
        startDate = 1/1/2010,
        endDate = 2/2/2010,
        limit = 10000
        )
    budget4 = Budget(
        budgetName = "Noah's Budget",
        startDate = 1/1/2010,
        endDate = 2/2/2010,
        limit = 10000
        )
    budget5 = Budget(
        budgetName = "Sam's Budget",
        startDate = 1/1/2010,
        endDate = 2/2/2010,
        limit = 10000
        )
    budget6 = Budget(
        budgetName = "Emma's Budget",
        startDate = 1/1/2010,
        endDate = 2/2/2010,
        limit = 10000
        )
    budget7 = Budget(
        budgetName = "Ava's Budget",
        startDate = 1/1/2010,
        endDate = 2/2/2010,
        limit = 10000
        )
    budget8 = Budget(
        budgetName = "Mia's Budget",
        startDate = 1/1/2010,
        endDate = 2/2/2010,
        limit = 10000
        )
    budget9 = Budget(
        budgetName = "Evelyn's Budget",
        startDate = 1/1/2010,
        endDate = 2/2/2010,
        limit = 10000
        )
    budget10 = Budget(
        budgetName = "Alvin's Budget",
        startDate = 1/1/2010,
        endDate = 2/2/2010,
        limit = 10000
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