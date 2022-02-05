BITS = ('0', '1')
ASCII_BITS = 7

def display_bits(b):
    """converts list of {0, 1}* to string"""
    return ''.join([BITS[e] for e in b])

def seq_to_bits(seq):
    return [0 if b == '0' else 1 for b in seq]

def pad_bits(bits, pad):
    """pads seq with leading 0s up to length pad"""
    assert len(bits) <= pad
    return [0] * (pad - len(bits)) + bits
        
def convert_to_bits(n):
    """converts an integer `n` to bit array"""
    result = []
    if n == 0:
        return [0]
    while n > 0:
        result = [(n % 2)] + result
        n = int(n / 2)
    return result

def string_to_bits(s):
    def chr_to_bit(c):
        return pad_bits(convert_to_bits(ord(c)), ASCII_BITS)
    return [b for group in 
            map(chr_to_bit, s)
            for b in group]

def bits_to_char(b):
    assert len(b) == ASCII_BITS
    value = 0
    for e in b:
        value = (value * 2) + e
    return chr(value)

def list_to_string(p):
    return ''.join(p)

def bits_to_string(b):
    return ''.join([bits_to_char(b[i:i + ASCII_BITS]) 
                    for i in range(0, len(b), ASCII_BITS)])
    
def otp(m, k):
    assert len(m) == len(k)
    return[( mm+ kk) % 2 for mm, kk in zip(m, k)]
    
#My Own M1,M2 and Key   
plaintext1 = "BITCOIN"
plaintext2 = "DALGONA"
k = "POLYGON"


secretkey_bits = string_to_bits(k)

C1 = otp(string_to_bits(plaintext1), secretkey_bits )
C2 = otp(string_to_bits(plaintext2), secretkey_bits )

OTP1 = otp ( C1 , C2 )

#From C1 n C2, to get Plaintext back
#Decryption
revert_C1 = otp( (C1), secretkey_bits )
revert_C2 = otp( (C2), secretkey_bits )


revert_to_stringM1 = bits_to_string ( revert_C1 )
revert_to_stringM2 = bits_to_string ( revert_C2 )


print ("KEY      : " + k )
print ("M1       : " + plaintext1 )
print ("M2       : " + plaintext2 )

print ("\n")

print ( "ENCODE" )#Encryption

print ("\n")


print ("Key       : " + display_bits(string_to_bits(k)))
print ("M1 is     : " + display_bits(string_to_bits(plaintext1)))
print ("C1 is     : " + display_bits((C1)))

print ("\n")

print ("Key       : " + display_bits(string_to_bits(k)))
print ("M2 is     : " + display_bits(string_to_bits(plaintext2)))
print ("C2 is     : " + display_bits((C2)))


print ("\n")

print ("C1 is     : " + display_bits((C1)))
print ("C2 is     : " + display_bits((C2)))
print ("otp(C1,C2): " + display_bits((OTP1)))



print ("\n")

print ( "DECODE" )#Decryption

print ("\n")

print ("C1 is     : " + display_bits( (C1)) )
print ("Key       : " + display_bits(string_to_bits(k)))
print ("M1 is     : " + display_bits(revert_C1) )

print ("\n")

print ("C2 is     : " + display_bits( (C2)) )
print ("Key       : " + display_bits(string_to_bits(k)))
print ("M2 is     : " + display_bits(revert_C2) )

print ("\n")

print ("M1 is     : " + revert_to_stringM1 )
print ("M2 is     : " + revert_to_stringM2 )

