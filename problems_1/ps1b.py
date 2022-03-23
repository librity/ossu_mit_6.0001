from num_or_die import float_or_die


DEFAULT_DOWN_PAYMENT = 0.25
DEFAULT_ANUAL_RATE = 0.04

ANUAL_SALARY_MSG = "Enter your annual salary: "
PORTION_SAVED_MSG = "Enter the percent of your salary to save, as a decimal: "
TOTAL_COST_MSG = "Enter the cost of your dream home: "
SEMI_ANUAL_RAISE_MSG = "Enter the semi-annual raise, as a decimal: "


portion_down_payment = DEFAULT_DOWN_PAYMENT
anual_rate = DEFAULT_ANUAL_RATE
monthly_rate = anual_rate / 12.0
current_savings = 0.0
months = 0


anual_salary = float_or_die(ANUAL_SALARY_MSG)
monthly_salary = anual_salary / 12.0

portion_saved = float_or_die(PORTION_SAVED_MSG)
monthly_savings = monthly_salary * portion_saved

total_cost = float_or_die(TOTAL_COST_MSG)
down_payment = total_cost * portion_down_payment

semi_anual_raise = float_or_die(SEMI_ANUAL_RAISE_MSG)
print("---")


while current_savings < down_payment:
  dividends = current_savings * monthly_rate
  current_savings += dividends

  current_savings += monthly_savings

  if months != 0 and months % 6 == 0:
    raise_ = monthly_salary * semi_anual_raise
    monthly_salary += raise_
    monthly_savings = monthly_salary * portion_saved

  months += 1

print("Number of months:", months)
