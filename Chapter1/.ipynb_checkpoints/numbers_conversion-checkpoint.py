def To_Decimal(num):
    """
    Method that convert numbers in any bases to its Decimal(Human Readable repr. of a number)
    Params:
        num: could be binary, octal or Hex
    Returns:
        its equaivalent in Decimal(Human Readable repr. of a number)
    """
    return int(num)
    
Binary_num = 0b1001011  #0b refers to binary
Octal_num = 0o1234  #0b refers to binary
hex_num = 0xFDED  #0b refers to binary
print(To_Decimal(Binary_num))
print(To_Decimal(Octal_num))
print(To_Decimal(hex_num))


def From_Binary_To_Others(num):
    """
    Convert a binary string (e.g. "1001011") into
    Decimal, Octal, and Hexadecimal representations.
    """
    decimal_value = int(num, 2)  # Interpret as binary
    
    return (
        f"to Decimal = {decimal_value}, "
        f"to Octal = {oct(decimal_value)}, "
        f"to Hex = {hex(decimal_value)}"
    )

# Example
num = '1001011'  # binary string
print(From_Binary_To_Others(num))