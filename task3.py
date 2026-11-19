# Тестовые данные: (название, категория, цена, количество_на_складе)
products = [
    ("Ноутбук ASUS", "Электроника", 75000, 3),
    ("Мышь Logitech", "Электроника", 2500, 15),
    ("Книга «Python»", "Книги", 1200, 8),
    ("Клавиатура", "Электроника", 4500, 4),
    ("Тетрадь", "Канцтовары", 80, 50),
    ("Монитор", "Электроника", 32000, 2),
    ("Ручка", "Канцтовары", 45, 100),
]

# Общая стоимость всех товаров на складе (цена * количество)
total_value = 0
for name, cat, price, qty in products:
    total_value += price * qty

print(f"Общая стоимость всех товаров на складе: {total_value} руб.\n")

# Самый дорогой и самый дешёвый товар
most_expensive = products[0]
cheapest = products[0]

for item in products:
    if item[2] > most_expensive[2]:
        most_expensive = item
    if item[2] < cheapest[2]:
        cheapest = item

print(f"Самый дорогой товар: {most_expensive[0]} ({most_expensive[2]} руб.)")
print(f"Самый дешёвый товар: {cheapest[0]} ({cheapest[2]} руб.)\n")

# Группировка по категориям
categories = []
for name, cat, price, qty in products:
    if cat not in categories:
        categories.append(cat)

print("Статистика по категориям:")
for current_cat in categories:
    count = 0
    cat_total_cost = 0
    cat_price_sum = 0
    
    for name, cat, price, qty in products:
        if cat == current_cat:
            count += 1
            cat_total_cost += price * qty
            cat_price_sum += price
            
    avg_price = cat_price_sum / count
    print(f"Категория: {current_cat} | Позиций: {count} | "
          f"Суммарная стоимость: {cat_total_cost} руб. | Средняя цена: {avg_price:.2f} руб.")

# Сортировка по цене (убывание), при равенстве — по названию (возрастание)
# Создаём вспомогательный список из пар (цена, название, сам_товар)
temp_list = []
for item in products:
    temp_list.append((-item[2], item[0], item))

temp_list.sort()  # Обычный .sort() сам отсортирует сначала по цене, потом по названию

print("\nКаталог товаров (по убыванию цены):")
print(f"{'Название':<18} | {'Категория':<15} | {'Цена':>8} | {'Остаток':>8}")
print("-" * 58)
for neg_price, name, item in temp_list:
    print(f"{item[0]:<18} | {item[1]:<15} | {item[2]:>8} | {item[3]:>8}")

# Товары, которые заканчиваются (количество на складе < 5)
print("\nТовары заканчиваются (< 5 шт.): ")
for name, cat, price, qty in products:
    if qty < 5:
        print(f"- {name}: осталось {qty} шт.")