# from random import randint, seed
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import relationship, backref
from sqlalchemy import ForeignKey, Column, Integer, String 
from sqlalchemy.orm import sessionmaker
import datetime 
# create_engine('sqlite://tracker.db')
Base = declarative_base()
class Budget(Base):
    __tablename__ = 'budgets'
    id = Column (Integer(), primary_key= True)
    budgetName = Column(String())
    startDate = Column(String())
    endDate = Column(String())
    limit = Column(Integer())
    # category_id = Column(Integer(), ForeignKey('categories.id'))
    # reviews = relationship('Category', backref=backref('expense'))
    # def __repr__(self):
    #     return f'Category(id = {self.id})'+\
    #        f'categoryName = {self.categoryName}'+\
           
class User(Base):
    __tablename__ = 'users'
    id = Column (Integer(), primary_key=True)
    userName = Column(String())
    # def __repr__(self):
    #     return f'Review(id = {self.id})'+\
    #        f'rating = {self.rating}'+\
    #        f'customer_id={self.customer_id}'
class Expense(Base):
    __tablename__ = 'expenses'
    id = Column(Integer(), primary_key= True)
    expenseName = Column(String())
    # reviews = relationship('Review', backref=backref('restaurant'))
    # def __repr__ (self):
    #     return f'Restaurant(id = {self.id})'+\
    #         f'name={self.name}'
if __name__ == '__main__':
    engine = create_engine('sqlite:///tracker.db')
    Base.metadata.create_all(engine)
     # use our engine to configure a 'Session' class
    Session = sessionmaker(bind=engine)
    # use 'Session' class to create 'session' object
    session = Session()
# Budget Instances
    budget1 = Budget(
        budgetName = "Alvin's Budget",
        startDate = "1/1/2010",
        endDate = "2/2/2010",
        limit = 5000
        )
    budget2 = Budget(
        budgetName = "Kai's Budget",
        startDate = "3/3/2010",
        endDate = "4/4/2010",
        limit = 6000
        )
    budget3 = Budget(
        budgetName = "Ethan's Budget",
        startDate = "5/5/2010",
        endDate = "6/6/2010",
        limit = 7000
        )
    budget4 = Budget(
        budgetName = "Noah's Budget",
        startDate = "7/7/2010",
        endDate = "8/8/2010",
        limit = 8000
        )
    budget5 = Budget(
        budgetName = "Sam's Budget",
        startDate = "9/9/2010",
        endDate = "10/10/2010",
        limit = 9000
        )
    budget6 = Budget(
        budgetName = "Emma's Budget",
        startDate = "11/11/2010",
        endDate = "12/12/2010",
        limit = 10000
        )
    budget7 = Budget(
        budgetName = "Ava's Budget",
        startDate = "13/1/2011",
        endDate = "14/2/2011",
        limit = 11000
        )
    budget8 = Budget(
        budgetName = "Mia's Budget",
        startDate = "15/3/2011",
        endDate = "16/4/2011",
        limit = 12000
        )
    budget9 = Budget(
        budgetName = "Evelyn's Budget",
        startDate = "17/5/2011",
        endDate = "18/6/2011",
        limit = 13000
        )
    budget10 = Budget(
        budgetName = "Olivia's Budget",
        startDate = "19/7/2011",
        endDate = "20/8/2011",
        limit = 14000
        )

    # Create Users(Instances)
    user1 = User(
        userName = "Olivia"
        )
    user2 = User(
        userName = "Olivia"
        )
    user3 = User(
        userName = "Mia"
        )
    user4 = User(
        userName = "Noah"
        )
    user5 = User(
        userName = "Ava"
        )
    user6 = User(
        userName = "Sam"
        )
    user7 = User(
        userName = "Kai"
        )
    user8 = User(
        userName = "Evelyn"
        )
    user9 = User(
        userName = "Ethan"
        )
    user10 = User(
        userName = "Emma"
        )
    
    # Create Expenses(Instances)
    expense1 = Expense(
        expenseName = "John"
        )
    expense2 = Expense(
        expenseName = "Entertainment"
        )
    expense3 = Expense(
        expenseName = "Electricity"
        )
    expense4 = Expense(
        expenseName = "Water"
        )
    expense5 = Expense(
        expenseName = "Transport"
        )
    expense6 = Expense(
        expenseName = "Groceries"
        )
    expense7 = Expense(
        expenseName = "Insurance"
        )
    expense8 = Expense(
        expenseName = "Clothings"
        )
    expense9 = Expense(
        expenseName = "Savings"
        )
    expense10 = Expense(
        expenseName = "Vacations"
        )

   
   
    session.add_all([budget1,budget2,budget3,budget4,budget5,budget6,budget7,budget8,budget9,budget10])
    session.add_all([user1,user2,user3,user4,user5,user6,user7,user8,user9,user10])
    session.add_all([expense1,expense2,expense3,expense4,expense5,expense6,expense7,expense8,expense9,expense10])
    session.commit()

# #   returns the customer's given name
#     reviews = session.query(Review).filter(Review.restaurant_id == 1)
#     for review in reviews:
#         print("returns the customer's given name")
#         print (review.customer_id)

# #   returns the customer's family name
#     reviews = session.query(Review).all()
#     for review in reviews:
#         print (review.customer_id)
   
# # #    returns the full name of the customer, with the given name and the family name concatenated, Western style.
#     customers = session.query(Customer).all()
#     for customer in customers:
#        print(customer.firstName +' ' +customer.lastName)

