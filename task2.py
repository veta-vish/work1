text = input("Введите текст:\n")

# 1. Разбиение текста на предложения
# Защищаем точки внутри дробных чисел (например, 15.5), чтобы не разорвать предложение
protected_text = ""
for i in range(len(text)):
    if text[i] == "." and i > 0 and i < len(text) - 1:
        if text[i - 1] in "0123456789" and text[i + 1] in "0123456789":
            protected_text += "#"
        else:
            protected_text += "."
    else:
        protected_text += text[i]

temp_text = protected_text.replace("!", ".").replace("?", ".")
sentences = []
for s in temp_text.split("."):
    s = s.replace("#", ".")
    # Убираем пробелы по краям с помощью срезов (Лаб. 6)
    while len(s) > 0 and s[0] == " ":
        s = s[1:]
    while len(s) > 0 and s[-1] == " ":
        s = s[:-1]
    if len(s) > 0:
        sentences.append(s)

print("\n--- Предложения ---")
for idx, sentence in enumerate(sentences, 1):
    print(f"Предложение {idx}: {sentence}.")

# 2. Подсчёт частоты гласных букв (только таблица)
vowels = "аеёиоуыэюяaeiou"
text_lower = text.lower()

print("\n--- Таблица гласных ---")
print(f"{'Буква':<8} | {'Количество':<10}")
print("-" * 21)
for v in vowels:
    count = text_lower.count(v)
    if count > 0:
        print(f"{v:<8} | {count:<10}")

# 3. Слова длиной больше 6 символов (в алфавитном порядке без дубликатов)
alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяabcdefghijklmnopqrstuvwxyz"
clean_letters = ""
for char in text_lower:
    if char in alphabet:
        clean_letters += char
    else:
        clean_letters += " "

words = clean_letters.split()
long_words = sorted(set(w for w in words if len(w) > 6))

print("\nСлова > 6 букв:", end=" ")
if len(long_words) == 0:
    print("нет")
else:
    for i in range(len(long_words)):
        if i > 0:
            print(", ", end="")
        print(long_words[i], end="")
    print()

# 4. Поиск всех чисел (целых и вещественных) и их сумма
num_chars = ""
for char in text:
    if char in "0123456789+-.":
        num_chars += char
    else:
        num_chars += " "

numbers = []
for token in num_chars.split():
    while len(token) > 0 and token[0] == ".":
        token = token[1:]
    while len(token) > 0 and token[-1] == ".":
        token = token[:-1]
    try:
        numbers.append(float(token))
    except ValueError:
        pass

if numbers:
    print(f"Найденные числа: {numbers}")
    print(f"Сумма чисел в тексте: {sum(numbers)}")
else:
    print("Числа в тексте не найдены.")

# 5. Замена пробелов и изменение регистра по выбору пользователя
choice = input("\nВыберите преобразование (1 - в нижний регистр, 2 - в верхний): ")
transformed = text.replace(" ", "_")
if choice == "1":
    transformed = transformed.lower()
elif choice == "2":
    transformed = transformed.upper()
print(f"Результат: {transformed}")

# 6. Проверка, является ли строка корректным IPv4-адресом
ip = input("\nВведите строку для проверки IPv4: ")
parts = ip.split(".")
is_valid_ip = True

if len(parts) != 4:
    is_valid_ip = False
else:
    for part in parts:
        try:
            num = int(part)
            if num < 0 or num > 255 or str(num) != part:
                is_valid_ip = False
                break
        except ValueError:
            is_valid_ip = False
            break

print(f"Строка '{ip}' {'является' if is_valid_ip else 'НЕ является'} корректным IPv4.")