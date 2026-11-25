def split_into_stacks(quantity: int, stack_size: int = 20) -> list[int]:
    """Раскладывает предметы по ячейкам рюкзака: 45 стрел по 20 в ячейке -> [20, 20, 5].

    Raises:
        ValueError: если количество отрицательное или размер ячейки меньше 1.
    """
    if quantity < 0:
        raise ValueError("quantity can't be negative")
    if stack_size < 1:
        raise ValueError("stack_size must be at least 1")
    full_stacks, rest = divmod(quantity, stack_size)
    stacks = [stack_size] * full_stacks
    if rest:
        stacks.append(rest)
    return stacks
