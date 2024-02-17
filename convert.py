
def money_converter(summa: float, convert_from: str, convert_to: str):
    exchange = {'UAH': {'USD': 38.2,
                        'EUR': 41.4},
                }

    return f'{summa * exchange[convert_from][convert_to]:.2f}'
