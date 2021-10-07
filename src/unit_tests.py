from softdes import lambda_handler


def test_correct():
    args = {'ndes': '1', 'code': '"""\nFunção de resolução do desafio\n"""\ndef desafio1(n):\n    """Devolve 0"""\n   '
                                 ' return 0\n', 'args': [[1], [2], [3]], 'resp': [0, 0, 0], 'diag': ['a', 'b', 'c']}

    if lambda_handler(args) == '':
        assert True
    else:
        assert False

def test_function():
    args = {'ndes': '1', 'code': '"""\nFunção de resolução do desafio\n"""\ndef des(n):\n    """Devolve 0"""\n   '
                                 ' return 0\n', 'args': [[1], [2], [3]], 'resp': [0, 0, 0], 'diag': ['a', 'b', 'c']}

    assert lambda_handler(args) == "Nome da função inválido. Usar 'def desafio1(...)'"

def test_result():

    args = {'ndes': '1', 'code': 'oi', 'args': [[1], [2], [3]], 'resp': [0, 0, 0], 'diag': ['a', 'b', 'c']}

    assert lambda_handler(args) == "Função inválida."

