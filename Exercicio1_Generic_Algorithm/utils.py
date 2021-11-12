def _get_signal(decimal: int) ->  int:
    if decimal < 0:
        return 1
    return 0

def convert_decimal_to_binary2(decimal: int) -> str:
    return bin(decimal)

def convert_binary_to_decimal2(binary: str) -> int:
    return int(binary, 2)

def convert_decimal_to_binary(decimal: int) -> list:
    signal_bit = _get_signal(decimal)
    binaries = list()

    while(decimal):
        binaries.append(decimal % 2)
        decimal /= 2
    return binaries

def convert_binary_to_decimal(binary: list) -> int:
    binaries = list()
    return binaries
