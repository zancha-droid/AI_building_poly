salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

money_capital = 0

for month in range(months):
    if spend > salary:
        money_capital += (spend - salary)  # Добавляем недостающие средства к подушке

    spend *= (1 + increase)

required_capital = int(money_capital)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", required_capital)
