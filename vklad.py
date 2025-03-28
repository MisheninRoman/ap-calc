print('Приветсвую в калькуляторе накопительного вклада "На ежедневный остаток"')
p = float(input('Введи годовой процент: '))  # Годовой процент
d = 365  # Дней в году
up = int(input('Введи сумму ежемесячных пополнений: '))  # Ежемесячное пополнение
st = int(input('Введи сумму начального капитала: '))  # Начальный капитал
month = int(input('Введи кол-во месяцев (срок дейсвтия вклада): '))

total_interest = 0  # Общая сумма начисленных процентов
total_deposits = 0  # Общая сумма пополнений

for month in range(1, month+1):  # 12 месяцев
    days_in_month = 30  # Для упрощения считаем каждый месяц 30 дней
    month_interest = 0  # Проценты за текущий месяц

    for day in range(1, days_in_month + 1):  # Каждый день месяца
        daily_interest = st * (p / 100) / d  # Начисление процентов
        month_interest += daily_interest  # Добавляем проценты за день
    
    st += month_interest  # Начисленные проценты добавляются к счету
    st += up  # Пополнение в конце месяца
    total_interest += month_interest  # Учитываем в общей сумме
    total_deposits += up  # Учитываем пополнение

    print(f'Месяц {month}: Остаток - {st:.2f}, Начисленные проценты - {month_interest:.2f}')

print(f'\nИтоговая сумма начисленных процентов: {total_interest:.2f}')
print(f'Итоговая сумма пополнений: {total_deposits}')
print(f'Итоговый баланс: {st:.2f}')