import hashlib
 
def hash_string(input):
    byte_input = input.encode()
    hash_object = hashlib.sha256(byte_input)
    return hash_object 

hash_object = hash_string('Halo Rezza Fahlevi')
print(hash_object.hexdigest())
