
starting_salary = float(input("Enter the starting salary: "))


total_cost = 1000000
down_payment = 0.25 * total_cost
annual_return = 0.04
semi_annual_raise = 0.07
months = 36


low = 0
high = 10000
epsilon = 100
steps = 0
best_rate = None


def calculate_savings(rate):
    current_savings = 0
    annual_salary = starting_salary
    monthly_return = annual_return / 12

    for month in range(1, months + 1):
        monthly_salary = annual_salary / 12
        current_savings += current_savings * monthly_return
        current_savings += monthly_salary * (rate / 10000)

        if month % 6 == 0:
            annual_salary += annual_salary * semi_annual_raise

    return current_savings


if calculate_savings(high) < down_payment:
    print("It is not possible to pay the down payment in three years.")
else:
    while low <= high:
        steps += 1
        mid = (low + high) // 2
        savings = calculate_savings(mid)

        if abs(savings - down_payment) <= epsilon:
            best_rate = mid / 10000
            break
        elif savings < down_payment:
            low = mid + 1
        else:
            high = mid - 1

    print("Best savings rate:", round(best_rate, 4))
    print("Steps in bisection search:", steps)