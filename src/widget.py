from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(number: str) -> str:
    """Функция получает строку и москирует номер карты или счёта"""
    if len(number.split()[-1]) == 16:
        new_number = get_mask_card_number(number.split()[-1])
        result = f'{number[:-16]}{new_number}'
        return result
    elif len(number.split()[-1]) == 20:
        result = f'{number[:-20]}{get_mask_account(number.split()[-1])}'
        return result


def get_data(data_string: str) -> str:
    """Функция принимает дату и меняет формат"""
    data_slise = data_string[0:10].split('-')
    return '.'.join(data_slise[::-1])
