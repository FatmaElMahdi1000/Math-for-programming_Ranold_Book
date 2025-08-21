def Decimal_num_To_ANY(Decimal_num: int, Base: int) -> str:  
    """int, ->str don't affect the code they're only explanatory"""
    def Remainder_Conversion(Remainder):
        if Remainder < 10:
            return chr(48 + Remainder) #48 in Ascii is '0' -> str
        elif Remainder >= 10:
            return chr(55 + Remainder)
    Remainder = Decimal_num % Base    
    Decimal_num = Decimal_num // Base #floor to round down and be  able to get a remainder later if the product is with fractional part.
    
    Final_str_repr = Remainder_Conversion(Remainder)
    
    while Decimal_num != 0: #didn't reach the end of our successive division process to get all corresponding digits in any number system
        Remainder = Decimal_num % Base   #Remainder must come first before division
        Decimal_num = Decimal_num // Base
        Final_str_repr = Final_str_repr + Remainder_Conversion(Remainder)
    return Final_str_repr[::-1]  #[::-1]means → take the string from beginning to end, but with a step of -1, i.e. backwards.
          
Decimal_num = 75
Base = 2   #Binary: Base2, Octal: change to 8: Base8 , Hex: change to 16: Base16
print(Decimal_num_To_ANY(Decimal_num, Base))