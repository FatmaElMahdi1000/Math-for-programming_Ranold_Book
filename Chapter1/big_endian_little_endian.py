num = 0x12345678

big_Endian = num.to_bytes(4, byteorder="big") #to_bytes is built in method in python 
little_Endian = num.to_bytes(4, byteorder="little") 

print(big_Endian) #how it's stored in memory.
print(little_Endian) #how it's stored in memory.

#convert back to hex repr. 
print(big_Endian.hex())
print(little_Endian.hex())

print("****************************************************")
"""
big_endian_little_endian.py

Demonstrates how Python represents the same integer value using different
byte orders (big-endian vs little-endian) using an integer created from
a binary literal and the int.to_bytes / int.from_bytes methods.

Purpose
-------
This script shows that:
 - Writing a number as a binary literal (e.g. 0b0100110110011) produces
   a normal Python integer (decimal) immediately.
 - Converting that integer to bytes with .to_bytes(length, byteorder=...)
   produces different byte sequences depending on the chosen byte order.
 - Interpreting those bytes with int.from_bytes(..., byteorder=...) returns
   the original integer only when the interpretation uses the same byte order
   that was used to create the bytes.

Example (from this script)
--------------------------
num = 0b0100110110011   # binary literal
# numeric equivalents:
#   decimal: 2483
#   hex:     0x09B3

# Using 4 bytes for demonstration (pads with zeros)
num.to_bytes(4, "big").hex()    -> '000009b3'   # big-endian byte sequence
num.to_bytes(4, "little").hex() -> 'b3090000'   # little-endian byte sequence

# Printed bytes (exact output from Python)
# b'\x00\x00\t\xb3'   # note: 0x09 prints as '\t' (tab) in bytes repr
# b'\xb3\t\x00\x00'

# Converting back:
int.from_bytes(num.to_bytes(4, "big"), "big")      -> 2483
int.from_bytes(num.to_bytes(4, "big"), "little")   -> 3003711488  # wrong if byteorder mismatched

Key points
----------
 - A Python integer has no internal "endianness" when you manipulate it as an int.
   Endianness only matters when you convert it to a sequence of bytes (serialization,
   file I/O, network protocols, or interfacing with hardware).
 - .to_bytes(length, byteorder) pads or truncates to exactly `length` bytes:
   - If `length` is larger than required, the result is zero-padded (on the
     most-significant side for little-endian, least-significant side for big-endian).
   - If `length` is too small to hold the integer, OverflowError is raised.
 - To avoid confusing escape sequences in printed bytes (e.g. '\t' for 0x09),
   use .hex() for a clear hex string representation of bytes.

Helpful utilities
-----------------
 - Minimal number of bytes required:
     nbytes = max(1, (num.bit_length() + 7) // 8)

 - Example using minimal length:
     nbytes = max(1, (num.bit_length() + 7) // 8)
     num.to_bytes(nbytes, "big").hex()   # -> '09b3'
     num.to_bytes(nbytes, "little").hex()# -> 'b309'

 - Use int.from_bytes(bytes_obj, byteorder) to turn bytes back into an int.
 - For structured packing/unpacking (signed values, floats, specific widths),
   consider the struct module (struct.pack / struct.unpack).
 - To detect host endianness: use `import sys; sys.byteorder`

Pitfall (common)
----------------
Interpreting bytes with the wrong byteorder gives a completely different integer.
Always agree on and document the byte order when exchanging binary data (network
protocols typically use "big-endian" / network byte order).

"""