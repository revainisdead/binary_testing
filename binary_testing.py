import hashlib
import struct
import sys

def main():
    test = 'b"test" == "test".encode("utf-8")'
    print(f"{test}:", eval(test))

    hex_vals = {
        0x10: hex(0x10),
        0x20: hex(0x20),
        0x40: hex(0x40),
        0x80: hex(0x80),
    }
    print(hex_vals)

    # Convert list of ints into string of hex
    nums = [0, 1, 2, 3, 127, 200, 255]
    test = "bytearray(nums).hex()"
    print(f"{test}:", eval(test))
    print(" ".join("{:02X}".format(a) for a in nums))


    bytes.fromhex("1234ab")

    # optimization
    print("String hash comparison: ", hash("big string") == hash("big string"))

    # turn a 10 digit number into 8 digits
    print(hash("abc") % (10 ** 8))


    val = "abc"
    hashed = hashlib.sha1(val.encode("utf-8"))
    print(hashed.hexdigest())

    hashed = hashlib.sha1(u"\xcc\x88".encode("utf-8"))
    print(hashed.hexdigest())

    # bytearray: mutable version of bytes, can mutate string representations
    b = bytearray("abc", "utf8")
    print(b)
    print(b.decode())

    # XOR: if both bits are the SAME (0, 0) (1, 1), result is 0
    # XOR: if both bits are DIFFERENT (0, 1) (1, 0), result is 1
    bin_rep17 = bin(17)[2:].zfill(7)
    bin_rep115 = bin(115)[2:].zfill(7)
    result = 17 ^ 115 # 17 XOR 115
    print(result == int(0b1100010))


    # 0x80 is a short way of writing in binary [1000][0000] or 128
    # 0x01 - least significant bit
    # 0x80 - most significant bit
    # 0x1 - 1s place
    # 0x10 - 16s place
    # 0x100 - 256s place
    # Shifting most significant bit gives masks for the individual bits

    # Bit masking: which bits you want to keep, which bits you want to clear
    #
    # AND -> extract a subset of the bits in the value
    # OR  -> set a subset of the bits in the value
    # XOR -> toggle a subset of the bits in the value
    #
    # English: clear first four bits, keep second four bits
    #
    # mask:   00001111
    # value:  01010101
    #       AND
    # result: 00000101
    #
    mask = 0x0f
    val = 0x55
    result = val & mask
    bin(result) == "{:#02b}".format(result)


    byte = ord("a")
    # 5 most significant bits
    byte >> 3 # cut off 3 on the end

    # 5 least significant bits
    byte & 0b00011111 # clear first 3, keep last 5



    # Goal: convert string to binary representation (1011000)
    # a with accent in unicode
    a = b'\xc3\xa1'
    # convert binary to hex
    h = a.hex()
    print(h)
    # or
    # bin(int("abc123eeefff", 16))[2:]
    # format(int("abc123eeefff", 16), "040b")

    # converts int to binary representation, with leading zeros
    spec = "{fill}{align}{width}{type}".format(fill="0", align=">", width=42, type="b")
    print(format(16, spec))


    spec = "{fill}{width}{type}".format(fill="0", width=8, type="b")
    # not technically correct, but could convert str to ascii then use str format to bytes
    # to convert string to binary
    result = "".join(format(c, spec) for c in bytearray("asdf", encoding="utf-8"))
    print(result)

    # For checking bytes received over socket
    # returns number of bytes in a string
    def bytes_in_str(s):
        return len(s.encode("utf-8"))


    # cpus (sockets) -> cores -> (processes) -> threads
    # Multiprocessing in python splits CPUS or/and CORES
    # threads are limited by GIL
    # processes are not

    # convert to binary and add leading zeros to padd (but just for the representation not actualy bytes)
    print(bin(16)[2:].zfill(16))


    # try a right shift to add leading zeros
    print(bin(0xff >> 3))
    # went from 11111111 to 00011111 (or 31)
    # final bin will be 0b11111

    # *** One byte can only contain a value from 0-255 ***
    # 0xff = 255
    # When trying to convert ints to binary (where bytes(5) doesn't work)
    testing = (bytes([5]), bytes([3, 4, 5]))



    # 5/8/21
    struct.pack("I", 0b1)   # 1
    struct.pack("I", 0b10)  # 2
    struct.pack("I", 0b100) # 4
    struct.pack("I", 0b1000)# 8
    i128 = struct.pack("I", 0b10000000) # 128
    print(i128) # b'\x80\x00\x00\x00'

    # get exactly 128 (from bytes)
    struct.unpack("I", i128)# 128

    # simple way to think of it for now:
    # struct -> convert numbers to bytes
    # encode -> convert string to bytes

    # Learned something:
    # to encode values between 0-128:  OR use struct
    # to encode values greater than 255: use struct

    # direction >: most significant bits start from left and go right
    # direction <: most significant bits start right and go left
    #
    # >: big endian
    # <: little endian
    struct.pack(">I", 255)


    x = 0b01100000
    # value at the least significant bit position
    x & 1
    # written out:
    # x (0110 0000)
    # &
    # 1 (0000 0001)
    # ---- ----
    # = (0000 0000)



    x = 0b1101000 # 104
    # the furthest right 1 by itself
    # python has no sign bit
    exp = "x & -x"
    print(exp, eval(exp))

    # js: x & 1
    # js: x & -x
    # js: Math.log2(8) // gives exponent (3), 2 ** 3 => 8

    assert (2 ** 32) == 0xffffffff + 1
    assert struct.pack("I", 255) == struct.pack("I", 0xff)
    assert struct.pack("I", 255) != bytes(str(255), "utf-8")
    # Note: I is always 4 bytes (32 bits)
    #       H is always 2 bytes (16 bits)

    # Most Significant Bit: (1)000 : used for SIGN
    # Least Significant Bit: 100(1): used for EVEN (0) or ODD (1)

    # hash -> changes every program run (but does not change during that run)
    # hashlib.sha1 -> a permanent hash, same forever


    # Real python
    # all integers implictly have a sign attached to them, whether you specify it or not
    ~156 # flip every bit, not operator
    ~156 & 255 # add a mask (& 255) to make number positive


    # Byte Order......
    print(sys.byteorder) # amd and intel are little-endian by default (natively), @ also stands for native
                         # ! represents network byte order, which is always big-endian 
                         # link directly to text:
                         # https://docs.python.org/3/library/struct.html#:~:text=network%20byte%20order

    # However, bin prints as big endian by default


    #           Most significant bit
    #           |  Least significant bit
    #           |  |
    hex_val = 0x1BDB
    # little endian by default (same as system)
    t1 = struct.pack("I", hex_val)
    t2 = struct.pack("<I", hex_val) # little endian
    t3 = struct.pack(">I", hex_val) # big endian
    assert t1 == t2
    # Best way I've found to actually visualize the endianness: pack these hex values and print
    print(t2)
    print(t3)


    # 10 as newline
    var = 10
    t1 = struct.pack(">I", var)
    t2 = x.to_bytes(2, byteorder="big", signed=False)
    # Note: notice the new line character within the binary representation
    print(t1, "===", t2)

    # Convert 10 to hex value (not string), ironically must start with var as str
    hVal = int(str(var), 16) # equals 16

    # Convert 10 (int) from int to hex string (without 0x prefix, so I can create bytearray)
    hString = format(var, "x")
    try:
        barray = bytearray.fromhex(hString)
        print(f"Notice 10 converting to new line: {barray}")
    except ValueError:
        # 'a' is not valid for fromhex
        # as far as I can tell, this is because it's a length of 1, must have len of 2 or more
        pass

    # See how 'deadbeef' works
    test = 'deadbeef'
    barray = bytearray.fromhex(test)
    print(f"Deadbeef as bytearray: {barray}")
    print(f"Convert deadbeef bytearray back to bytes: {bytes(barray)}")
    # Note: bytes is Immutable, bytearray is Mutable

    # Final roundabout trip: go from binary back to hex
    t1 = "deadbeef".encode("utf-8")
    t2 = struct.pack("I", 128)
    print(f"from {t1} to hex: {t1.hex()}")
    print(f"from {t2} to hex: {t2.hex()}")

    # chr -> ascii rep to letter/number/etc
    # ord -> letter/number/etc to ascii re
    # CHR: Return Character
    # ORD: Return Character's Position In a Series (Ordinal Position)




if __name__ == "__main__":
    main()

