annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
down_payment=0.25*total_cost
annual_return=0.04    #annual_return means the bank gives 4% interest per year on whatever you saved
current_savings=0.0
months=0
monthly_salary=annual_salary/12
monthly_return=annual_return/12
while current_savings<down_payment:
    current_savings=current_savings+(current_savings*monthly_return)+(monthly_salary*portion_saved)
    #total savings=old savings + interest + new salary savings
    #next total savings goes to old savings and keep loop continues till current savings < down payment
    months+=1
print("no of months: ",months)
