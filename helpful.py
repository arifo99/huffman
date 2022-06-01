PATH = 'example.txt'

def getBitwise(path = PATH):
    print("Starting loading file")
    fh = open(path, 'rb')
    fileBytes = []
    print("Done loading file")
    b = True
    print("Started parsing byte-wise")
    while b:
        try:
            b = fh.read(1)
            fileBytes.append(b)
        except:
            pass
    print("Done parsing byte-wise")
    print("Started parsing bit-wise")
    bits = []
    
    for byte in fileBytes:
        byteValue = int.from_bytes(byte, 'little', signed = True)
        for i in range(8):
            bits.append((byteValue >> i) & 1)
    print("Done parsing bit-wise")
    return bits
