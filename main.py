import sqlite3
from sqlalchemy import create_engine, func
from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import relationship, backref
from sqlalchemy import ForeignKey, Column, Integer, String 
from sqlalchemy.orm import sessionmaker
# import datetime 
# create_engine('sqlite://tracker.db')
Base = declarative_base()
class Budget(Base):
    __tablename__ = 'budgets'
    id = Column (Integer(), primary_key= True)
    budgetName = Column(String())
    startDate = Column(String())
    endDate = Column(String())
    limit = Column(Integer())
    def __repr__(self):
        return f'Budget(id = {self.id})'+\
           f'budgetName= {self.budgetName}'+\
           f'startDate = {self.startDate}'+\
           f'endDate  = {self.endDate }'+\
           f'limit = {self.limit}'+\
           f'user_id = {self.user_id}'+\
           f'budget_id = {self.budget_id}'
           
           
class User(Base):
    __tablename__ = 'users'
    id = Column (Integer(), primary_key=True)
    userName = Column(String())
    def __repr__(self):
        return f'User(id = {self.id})'+\
           f'userName={self.userName}'
    
class Expense(Base):
    __tablename__ = 'expenses'
    id = Column(Integer(), primary_key= True)
    expenseName = Column(String())
    user_id = Column(Integer(), ForeignKey('users.id'))
    budget_id = Column(Integer(), ForeignKey('budgets.id'))
    def __repr__(self):
        return f'Budget(id = {self.id})'+\
           f'expenseName= {self.budgetName}'+\
           f'user_id = {self.user_id}'+\
           f'budget_id = {self.budget_id}'



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
        limit = 8000, 
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
        userName = "Alvin"
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
        expenseName = "WiFi",
        user_id = 3,
        budget_id = 8
        )
    expense2 = Expense(
        expenseName = "Entertainment",
        user_id = 5,
        budget_id = 7
        )
    expense3 = Expense(
        expenseName = "Electricity",
        user_id = 1,
        budget_id = 1
        )
    expense4 = Expense(
        expenseName = "Water",
        user_id = 10,
        budget_id = 6
        )
    expense5 = Expense(
        expenseName = "Transport",
        user_id = 4,
        budget_id = 4
        )
    expense6 = Expense(
        expenseName = "Groceries",
        user_id = 9,
        budget_id = 3
        )
    expense7 = Expense(
        expenseName = "Insurance",
        user_id = 6,
        budget_id = 5
        )
    expense8 = Expense(
        expenseName = "Clothings",
        user_id = 8,
        budget_id = 9
        )
    expense9 = Expense(
        expenseName = "Savings",
        user_id = 2,
        budget_id = 10
        )
    expense10 = Expense(
        expenseName = "Vacations",
        user_id = 7,
        budget_id = 2
        )

    session.add_all([budget1,budget2,budget3,budget4,budget5,budget6,budget7,budget8,budget9,budget10])
    session.add_all([user1,user2,user3,user4,user5,user6,user7,user8,user9,user10])
    session.add_all([expense1,expense2,expense3,expense4,expense5,expense6,expense7,expense8,expense9,expense10])
    session.commit()


def main ():
    # initialize tracker list
    trackerList = []

    choice = 0
    while choice !=10:
        print("**<<KARIBU||WELCOME TO PESA TRACKER PROGRAM>>**")
        print("1) Displays all budgetName in budgets")
        print("2) Display userName in users in Descending order")
        print("3) Lookup Expenses")
        print("4) Display Expenses")
        print("5) Displays average limit")
        print("6) Displays limit below 10000")
        print("7) Display limit 10000 and above")
        print("8) Outputs a list")
        print("10) Quit program")
        choice = int(input())


    #   prints all budgetName
        if choice == 1:
            print("Displaying all budgetName  ...")
            budgets = session.query(Budget).all()
            for budget in budgets:
                print(budget.budgetName)

        if choice == 2:
            print("Displaying userName in Descending order  ...")
            budgets = session.query(Budget).first()
            for budget in budgets:
                print(budget.budgetName)
    #   Lookup Expenses
        if choice == 3:
            print("Looking Up Expenses...")
            user_input = input("Enter expenseName:")
            expenses = session.query(Expense).filter(Expense.expenseName == user_input)
           
            for Hitaji in expenses:
              print (("Id:", Hitaji.id, "Name:", Hitaji.expenseName, "UserId", Hitaji.user_id, "BudgetId", Hitaji.budget_id))

        #  prints average limit
        if choice == 5:
            averageLimit = average_limit = session.query(func.avg(Budget.limit)).scalar()
            print("**<<Printing average limit>>**")
            print("THE AVERAGE LIMIT IS" + " " + str(averageLimit))

        #  prints limit below 10000
        if choice == 6:
            budgets = session.query(Budget).filter(Budget.limit < 10000)
            for budget in budgets:
                print("**<<Printing limit below 10000>>**")
                print(budget.budgetName)
    
        #  prints limit 10000 and above
        if choice == 7:
            budgets = session.query(Budget).filter(Budget.limit >= 10000)
            for budget in budgets:
                print("**<<Printing limit 10000 and above>>**")
                print(budget.budgetName)
        #  Outputs a list
        # if choice == 8:
        #     budgets = session.query(Budget).all()
        #     budgets.append([])
        #     for budget in budgets:
        #         print("**<<Printing a list>>**")
        #         print(budget)


        #  Quiting program
        elif choice == 10:
                print("**<<You are no longer on the main menu.>>**")
                print("**<<Thank you for choosing Pesa Tracker.>>**")
                
    
    
        



if __name__ == "__main__":
    main()

