from num_or_die import float_or_die


DEFAULT_DOWN_PAYMENT = 0.25
DEFAULT_ANUAL_RATE = 0.04

ANUAL_SALARY_MSG = "Enter your annual salary: "
PORTION_SAVED_MSG = "Enter the percent of your salary to save, as a decimal: "
TOTAL_COST_MSG = "Enter the cost of your dream home: "


portion_down_payment = DEFAULT_DOWN_PAYMENT
anual_rate = DEFAULT_ANUAL_RATE
monthly_rate = anual_rate / 12.0
current_savings = 0.0
months_to_down_payment = 0


anual_salary = float_or_die(ANUAL_SALARY_MSG)
monthly_salary = anual_salary / 12.0

portion_saved = float_or_die(PORTION_SAVED_MSG)
monthly_savings = monthly_salary * portion_saved

total_cost = float_or_die(TOTAL_COST_MSG)
down_payment = total_cost * portion_down_payment
print("---")


while current_savings < down_payment:
  dividends = current_savings * monthly_rate
  current_savings += dividends

  current_savings += monthly_savings

  months_to_down_payment += 1

print("Number of months:", months_to_down_payment)
