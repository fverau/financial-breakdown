def main():
  salary = int(input("Sueldo: "))

  # Gastos fijos
  CREDIT_CARD = int(input("Cuánto pagarás de tarjeta de crédito?: "))
  RENT = int(input("Cuánto es el pago de arriendo?: "))
  LIGHT = int(input("Cuánto es el pago de luz?: "))
  GAS = int(input("Cuánto es el pago de gas?: "))
  WATER = int(input("Cuánto es el pago de agua?: "))
  EXTRA_BILLS = int(input("Pagos extras?: "))

  TOTAL_FIXED_COSTS = CREDIT_CARD + RENT + EXTRA_BILLS + LIGHT + GAS + WATER

  salary_after_fixed = salary - TOTAL_FIXED_COSTS

  ## Ahorro / Inversiones

  saving = int(input("Cuánto porcentaje destinas a ahorro?: "))

  to_save = get_percentage_of(salary, saving) # valor destinado a ahorrar
  leftover_after_saving = engine(salary_after_fixed, to_save, "ahorro")

  ## Alimentación

  feeding = int(input("Cuánto porcentaje destinas a alimentación?: "))
  to_eat = get_percentage_of(salary, feeding)
  leftover_after_feeding = engine(leftover_after_saving, to_eat, "alimentación")



def engine(remaining, intended_for, reason):
  leftover = remaining - intended_for
  print(f"Dinero destinado a {reason}: ${intended_for}")
  print(f"Te queda: ${leftover}")
  return leftover



# Obtener el valor a descontar del salario
# según el porcentaje que corresponda.
def get_percentage_of(value, n):
  # n es el porcentaje en valor entero (1 - 100)
  percent = n / 100 # porcentaje a valor entre 0 y 1
  percent_of = round(value * percent)
  return percent_of

main()




