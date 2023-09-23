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
  leftover_after_saving = salary_after_fixed - to_save
  print(f"Dinero destinado a ahorro: ${to_save}")
  print(f"Te queda: ${leftover_after_saving}")

  ## Alimentación

  feeding = int(input("Cuánto porcentaje destinas a ahorro?: "))
  




# Obtener el valor a descontar del salario
# según el porcentaje que corresponda.
def get_percentage_of(value, n):
  # n es el porcentaje en valor entero (1 - 100)
  percent = n / 100 # porcentaje a valor entre 0 y 1
  percent_of = round(value * percent)
  return percent_of

main()




