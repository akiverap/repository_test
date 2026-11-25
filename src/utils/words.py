def coins_word(amount: int) -> str:
    """Слово «монета» в нужной форме: 1 монета, 2 монеты, 5 монет.

    В этой функции спрятана ошибка — её найдёт задача 4.
    """
    last_digit = amount % 10
    if last_digit == 1:
        return 'монета'
    if last_digit in (2, 3, 4):
        return 'монеты'
    return 'монет'
