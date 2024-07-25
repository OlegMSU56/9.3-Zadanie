def all_variants(text):
    length = len(text)
    # Генерируем одиночные символы
    for i in range(length):
        yield text[i]  # Возвращаем одиночный символ
    # Генерируем подпоследовательности длиной больше 1
    for sub_length in range(2, length + 1):  # Длина подстроки от 2 до length
        for start in range(length - sub_length + 1):  # Начальная позиция от 0 до length - sub_length
            end = start + sub_length  # Конечная позиция
            yield text[start:end]  # Возвращаем подстроку от start до end

a = all_variants("abc")
for i in a:
    print(i)
