def decimal_to_binary(decimal: int, bits_number = 4) -> str:
    binary = ''
    if(decimal < 0):
        binary += '-'
    else:
        binary += '+'
    
    [_ , binary_unsignal] = bin(decimal).split('b')

    while(len(binary_unsignal) < bits_number):
        binary_unsignal = '0' + binary_unsignal

    binary += binary_unsignal
    return binary

def binary_to_decimal(binary: str) -> int:
    return int(binary, 2)
