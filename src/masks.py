def get_mask_card_number(number: str) -> str:
    """Функция принимает строку и возвращает маску карты"""
    mask_number = f'{number[0:4]} {number[4:6]}** **** {number[12:]}'
    return mask_number


def get_mask_account(number: str) -> str:
    """Функция принимает строку и возвращает маску счёта"""
    mask_number = f'**{number[-4:]}'
    return mask_number
