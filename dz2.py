tickets = int(input("Количество приобретаемых билетов:"))
price = 0
N = 1
while N <= tickets:
    age_guest = int(input(f"Возраст посетителя № {N}: "))
    if age_guest < 18:
        print("Стоимость билета: 0 руб.")
    elif 18 <= age_guest < 25:
        price += 990
        print("Стоимость билета: 990 руб.")
    else:
        price += 1390
        print("Стоимость билета: 1390 руб.")
    N +=1
print("Сумма за билеты: ", price)
if tickets > 3:
    price *= 0.9
    print ("Применена скидка 10%")
print("Итого к оплате - ", price, "руб")