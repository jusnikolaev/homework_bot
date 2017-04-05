def calculator_base_message(message):
    operators = ['+', '-', '*', '/']
    message = message[2:-2]
    if len(message) != 0:
        if ' ' not in message:
            if message[-1] == '=':
                for i in range(len(operators)):
                    if operators[i] in message:
                        operator = operators[i]
                        values = message.split(operator)
                        value_1 = values[0]
                        value_2 = values[1].replace('=', '')
                        try:
                            value_1 = int(value_1)
                            value_2 = int(value_2)
                        except ValueError:
                            value_1 = float(value_1)
                            value_2 = float(value_2)
                        return calculator(value_1, value_2, operator)
                else:
                    return 'Ошибка! Отсутствует знак оператора.'
            else:
                return 'Ошибка! Отсутсвует знак равно. '
        else:
            return 'Ошибка! В строке не должно быть пробелов. '
    else:
        return 'Ошибка! Вы ввели пустую строку! '


def calculator(value_1, value_2, operator):
    if operator == '+':
        return value_1 + value_2
    elif operator == '-':
        return value_1 - value_2
    elif operator == '*':
        return value_1 * value_2
    elif operator == '/':
        try:
            return value_1 / value_2
        except ZeroDivisionError:
            return 'Ошибка! Деление на ноль.'


if __name__ == '__main__':
    pass
