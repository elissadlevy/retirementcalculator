print("I will ask you a few questions, and then I will tell you how your retirement is looking.")

current_age = int(input("What is your age? "))
retirement_age = int(input("How old do you want to be when you retire? "))
yearly_income = int(input("How much money do you make each year today? "))
income_increase = float(input("By what percent is your income likely to increase on average per year? "))
current_savings = int(input("How much money do you already have saved? "))
yearly_expenses = int(input("How much money do you spend each MONTH? "))*12
kids_question = int(input("Do you plan to have kids? If no, type 0.  If yes, type the number of years from now. "))
interest_rate = float(input("What is the interest you expect to earn? Give as decimal. "))

# print("By the time you retire, you will have: ")
# money_will_have = (yearly_income - yearly_expenses)*(retirement_age - current_age) + current_savings
# print(money_will_have)

amt_in_savings = current_savings

#Calculate the amount in savings each year as you are working
for year in range(retirement_age - current_age):
    if year - current_age == kids_question:
        yearly_expenses = yearly_expenses * 2
    amt_in_savings = amt_in_savings * (1 + interest_rate) + (yearly_income - yearly_expenses)
    yearly_income = yearly_income * (1+income_increase)

print("Your final salary before retirement was $" + str(round(yearly_income,2)) + ".")
print("Your money at retirement will be $" + str(round(amt_in_savings,2)) + ".")

#Possible extensions for this:
# 1. Figure out how much money per month you will be able to spend during your retirement.
# 2. Incorporate debt that you may have and need to pay down.
# 3. Incorporate big expenses like paying for your kids' college or a house.
# 4. Incorporate a best-case and worst-case scenario if you plan to invest in risky assets that might or might not work out.
