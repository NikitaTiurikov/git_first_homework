
def money_converter(summa: float, convert_from: str, convert_to: str):
    exchange = {'UAH': {'USD': 38.2,
                        'EUR': 41.4},
                'USD': {'UAH': 37.6,
                        'EUR': 1.08},
                'EUR': {'UAH': 40.4,
                        'USD': 0.93}
                }

    return f'{summa * exchange[convert_from][convert_to]:.2f}'
