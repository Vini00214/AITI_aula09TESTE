def somar (a,b):
    return a+b

def comprimento(lista):
    return len(lista)

def test_somar():
    assert somar(2,3) == 5
    assert somar(5,6) == 11

def comprimento():
    assert comprimento([1,2,3,4,5]) == 5
    assert comprimento([1,2,3,4,5]) == 5