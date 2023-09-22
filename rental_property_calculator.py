from tabulate import tabulate


class RentalPropertyCalculator():
    """
       The RentalPropertyCalculator have 22 methods: getRentalIncome, getExpenses,
       getPropertyTaxes, getInsuranceCost, getUtiitiesCost, getHOACost, getVacancyCost,
       getrepairsCost, getCapExCost, getManagementCost, getMortageCost, getMiscCost,  
       calculateMonthlyExpenses, getInvestment, getDownPayment, getClosingCost,
       getRehabCost, getAdditionalInvestmentCost, calculateTotalInvesment, calculateCashFlow, 
       calculateROI and displayROI

       Attributes for the class:
       -income: expected to be a float
       -total_investment: expected to be a float
       -total_expenses: expected to be a float
       -expenses: expented to be a list
       -investment: expected to be a list
    """

    def __init__(self):
        self.income = 0.00
        self.total_investment = 0.00
        self.total_expenses = 0.00
        self.expenses = []
        self.investment = []


    #Method ask the user for retal income.
    def getRentalIncome(self):
        while True:
            income = input("Please enter the montly income of your rental property: ")
        
            if income.lower() == 'quit':
                break
            try:
                self.income = float(income)
                return self.income
            except:
                print("Invalid answer. Please enter a valid answer.")

    #Method ask the user for all expenses and add it to expenses list.
    def getExpenses(self):
        while True:
            expense = input("Please enter ammount: ")

            if expense.lower() == 'quit':
                break
            try:
                expense = float(expense)
                self.expenses.append(expense)
                return self.expenses
            except:
                print("Invalid answer. Please enter a valid answer.")

    #Method ask the user for monthly property taxes fee.    
    def getPropertyTaxes(self):
        print("\nExpenses include but not limited to:")
        print("Property Taxes & Management, Insurance, Utilities, Mortage, Repairs etc. ")
        print("Please enter your monthly Property Taxes Fee")
        return self.getExpenses()
    
    #Method ask the user for monthly insurance cost.
    def getInsuranceCost(self):
        print("Please enter your monthly insurance cost")
        return self.getExpenses()
    
    #Method ask the user for monthly utilities cost.
    def getUtiitiesCost(self):
        print("Please enter your monthly utilities cost")
        return self.getExpenses()
    
    #Method ask the user for monthly HOA cost.
    def getHOACost(self):
        print("Please enter your monthly HOA (Home Owner Association) cost")
        return self.getExpenses()
    
    #Method ask the user for monthly vacancy cost.
    def getVacancyCost(self):
        print("Please enter your monthly vacancy cost")
        return self.getExpenses()
    
    #Method ask the user for monthly repairs cost.
    def getRepairsCost(self):
        print("Please enter your monthly repairs cost")
        return self.getExpenses()
    
    #Method ask the user for monthly CapEx cost.
    def getCapExCost(self):
        print("Please enter your monthly CapEx cost")
        return self.getExpenses()
    
    #Method ask the user for monthly Property Management cost.
    def getManagementCost(self):
        print("Please enter your monthly Property Management cost")
        return self.getExpenses()
    
    #Method ask the user for monthly Mortage cost.
    def getMortageCost(self):
        print("Please enter your monthly Mortage cost")
        return self.getExpenses()
    
    #Method ask the user for any aditional expenses.
    def getMiscCost(self):
        print("Please enter any additional monthly expenses")
        return self.getExpenses()
    
    #Method to add all the expenses.
    def calculateMonthlyExpenses(self):
        self.total_expenses = sum(self.expenses)
        return self.total_expenses

    #Method ask the user for total investment of the property.
    def getInvestment(self):
        while True:
            ammount = input("Please enter ammount: ")

            if ammount.lower() == 'quit':
                break
            try:
                ammount = float(ammount)
                self.investment.append(ammount)
                return self.investment
            except:
                print("Invalid answer. Please enter a valid answer.")
    
    #Method ask the user for down payment for the property.
    def getDownPayment(self):
        print("\nInvestment costs include but not limited to:")
        print("Down payment, Closing costs, Rehab Budget, etc.")
        print("Please enter down payment of the property")
        return self.getInvestment()
    
    #Method to ask the user for total of closing costs.
    def getClosingCost(self):
        print("Please enter total of closing costs of the property")
        return self.getInvestment()
    
    #Method to ask the user for budget rehab cost.
    def getRehabCost(self):
        print("Please enter total of rehab cost of the property")
        return self.getInvestment()
    
    #Method ask the user for any aditional investment cost.
    def getAdditionalInvestmentCost(self):
        print("Please enter any additional investment cost of the property")
        return self.getInvestment()

    def calculateTotalInvesment(self):
        self.total_investment = sum(self.investment)
        return self.total_investment

    #Method to calculate monthly cash flow
    def calculateCashFlow(self):
        self.calculateMonthlyExpenses()
        monthly_cash_flow = self.income - self.total_expenses
        return monthly_cash_flow
    
    #Method to calculate Return of investment (ROI)
    def calculateROI(self):
        self.calculateTotalInvesment() 
        anual_cash_flow = self.calculateCashFlow() * 12
        if self.total_investment == 0:
            print("\nROI cannot be calculated because the total investment is zero.")
        else:
            roi = round((anual_cash_flow / self.total_investment) * 100, 2)
            return roi

    
    #Call to the method calculateROI and display a message with result
    def displayRIO(self):
        roi = self.calculateROI()
        if self.total_investment !=0:    
            print(f"\nThe Cash on Cash ROI of your property is: {roi}%")

        data = [[self.total_investment, self.income * 12, self.total_expenses * 12, roi]]
        headers = ["Investment", "Annual Income", "Annual Expenses", "ROI %"]
        table = tabulate(data, headers, tablefmt='grid')
        print(table)

#Function to run the RentalPropertyCalculator methods on instance
def run():
    while True:
        print("\nEnter 'quit' to exit the program at any time.")
        calculator = RentalPropertyCalculator()

        income = calculator.getRentalIncome()
        if income is None:
            return   

        taxes = calculator.getPropertyTaxes()
        if taxes is None:
            return
        
        insurance = calculator.getInsuranceCost()
        if insurance is None:
            return
        
        utilities = calculator.getUtiitiesCost()
        if utilities is None:
            return
        
        hoa = calculator.getHOACost()
        if hoa is None:
            return
        
        vacancy = calculator.getVacancyCost()
        if vacancy is None:
            return
        
        repairs = calculator.getRepairsCost()
        if repairs is None:
            return
        
        capex = calculator.getCapExCost()
        if capex is None:
            return
        
        management = calculator.getManagementCost()
        if management is None:
            return
        
        mortage = calculator.getMortageCost()
        if mortage is None:
            return
        
        misc = calculator.getMiscCost()
        if misc is None:
            return
        
        down_payment = calculator.getDownPayment()
        if down_payment is None:
            return 
        
        closing_cost = calculator.getClosingCost()
        if closing_cost is None:
            return 
        
        rehab_cost = calculator.getRehabCost()
        if rehab_cost is None:
            return 
        
        misc_investment = calculator.getAdditionalInvestmentCost()
        if misc_investment is None:
            return 
    
        calculator.displayRIO()

run()

    

    


        

