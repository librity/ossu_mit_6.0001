from num_or_die import float_or_die


DEFAULT_DOWN_PAYMENT_PORTION = 0.25
DEFAULT_ANUAL_RATE = 0.04
DEFAULT_COST = 1000000
DEFAULT_SEMI_ANUAL_RAISE = 0.07
TARGET_YEARS = 3
TARGET_MONTHS = TARGET_YEARS * 12
BISECTION_MIN = 0
BISECTION_MAX = 10000


ANUAL_SALARY_MSG = "Enter the starting salary: "


down_payment_portion = DEFAULT_DOWN_PAYMENT_PORTION
anual_rate = DEFAULT_ANUAL_RATE
monthly_rate = anual_rate / 12.0
total_cost = DEFAULT_COST
down_payment = total_cost * down_payment_portion
semi_anual_raise = DEFAULT_SEMI_ANUAL_RAISE


anual_salary = float_or_die(ANUAL_SALARY_MSG)
monthly_salary = anual_salary / 12.0
print("---")


bisection = BISECTION_MIN
while bisection <= BISECTION_MAX:
  target_months = TARGET_MONTHS
  savings = 0.0
  portion_saved = float(bisection) / BISECTION_MAX
  monthly_savings = monthly_salary * portion_saved

  while target_months >= 0:
    dividends = savings * monthly_rate
    savings += dividends

    savings += monthly_savings

    if target_months != TARGET_MONTHS and target_months % 6 == 0:
      raise_ = monthly_salary * semi_anual_raise
      monthly_salary += raise_
      monthly_savings = monthly_salary * portion_saved

    target_months -= 1

  if (down_payment - savings) <= 100:
    print("Best savings rate:", portion_saved)
    print("Steps in bisection search:", bisection)
    quit()

  bisection += 1

print("It is not possible to pay the down payment in three years.")
