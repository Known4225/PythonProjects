'''
Enter a string to be hashed
Output: SHA256 hash of your string
Non-ASCII characters like ş and ö don't work, because of complications with the ord() python function, 
I could not get it to decode to utf-8 even though it should be able to with an extra parameter, I never figured it out
Sadly doesn't generate primes and finds their cube roots for the initial constants, python float precision was unfortunately not precise enough
'''
def generate_primes(kaç):
    pr = [2, 3, 5, 7]
    i = 4
    if kaç > 4:
        g = 11
        while i < kaç:
            y = 0
            while pr[y] < g ** (1/2) and g % pr[y] != 0:
                y += 1
            if g % pr[y] != 0:
                pr.append(g)
                i += 1
            g += 2
    return pr[0:kaç]
def generate_constants():
    primes = generate_primes(64)
    # for i in range(10):
        # print(round(primes[i] ** (1/3), 16))
        # print(bin(round(primes[i] ** (1/3), 16)))
    co = [0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2]
    inst = [0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a, 0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19]
    con = []
    for i in co:
        test = str(bin(i))[2:]
        while len(test) < 32:
            test = '0' + test
        con.append(test)
    for i in inst:
        test = str(bin(i))[2:]
        while len(test) < 32:
            test = '0' + test
        con.append(test)
    return con
def ascii(mes):
    li = []
    for i in mes:
        li.append(str(ord(i)))
    return li
def shr(bin, shift):
    st1 = '00000000000000000000000000000000'
    return st1[0:shift] + bin[0:len(bin) - shift]
def rotr(bin, shift):
    st2 = ''
    for i in range(len(bin) - shift, len(bin)):
        st2 += bin[i]
    return st2 + bin[0:len(bin) - shift]
def xor(bin1, bin2):
    st3 = ''
    for i in range(len(bin1)):
        if int(bin1[i]) + int(bin2[i]) % 2 == 1:
            st3 += '1'
        else:
            st3 += '0'
    return st3
def add(bin1, bin2):
    aj = int(bin1, 2) + int(bin2, 2)
    test = str(bin(aj % 2 ** 32))[2:]
    while len(test) < 32:
        test = '0' + test
    return test
def choice(bin1, bin2, bin3):
    st4 = ''
    for i in range(len(bin1)):
        if bin1[i] == '1':
            st4 += bin2[i]
        else:
            st4 += bin3[i]
    return st4
def majority(bin1, bin2, bin3):
    st5 = ''
    for i in range(len(bin1)):
        st5 += str((int(bin1[i]) + int(bin2[i]) + int(bin3[i])) // 2)
    return st5
def sigma0(bin):
    return xor(xor(rotr(bin, 7), rotr(bin, 18)), shr(bin, 3))
def sigma1(bin):
    return xor(xor(rotr(bin, 17), rotr(bin, 19)), shr(bin, 10))
def SIGMA0(bin):
    return xor(xor(rotr(bin, 2), rotr(bin, 13)), rotr(bin, 22))
def SIGMA1(bin):
    return xor(xor(rotr(bin, 6), rotr(bin, 11)), rotr(bin, 25))
def displayDigest(dig):
    out = []
    for i in range(0, len(dig), 8):
        dis = ''
        for j in range(8):
            dis += dig[i + j]
        out.append(int(dis, 2))
    print(out)
    print()
def displayDigestList(digList):
    con = ''
    for i in range(len(digList)):
        con += digList[i]
    displayDigest(con)
def sha(message):
    Hash = []
    for i in initstate:
        Hash.append(i)
    mes = ascii(message)
    print(mes)
    print()
    binmes = ''
    for i in mes:
        test = str(bin(int(i)))[2:]
        while len(test) < 8:
            test = '0' + test
        binmes += test
    binlen = str(bin(len(binmes)))[2:]
    while len(binlen) < 64:
        binlen = '0' + binlen
    binmes += '1'
    while len(binmes) % 512 != 448:
        binmes += '0'
    binmes += binlen
    print('Padded:')
    displayDigest(binmes)
    for n in range(len(binmes) // 512):
        tra = 0 + n * 512
        W = []
        for k in range(16):
            st = ''
            for i in range(32):
                st += binmes[tra]
                tra += 1
            W.append(st)
        tra = 16
        # for i in W:
            # print(i)
            # displayDigest(i)
        for i in range(48):
            W.append(add(add(add(sigma1(W[tra - 2]), W[tra - 7]), sigma0(W[tra - 15])), W[tra - 16]))
            tra += 1
        H = []
        for i in Hash:
            H.append(i)
        # print()
        # for i in H:
        #     print(i)
        print('Constructed (+ 48 lines):')
        displayDigestList(W)
        print('Starting Values:')
        displayDigestList(H)
        K = constants
        for i in range(64):
            T1 = add(add(add(add(SIGMA1(H[4]), choice(H[4], H[5], H[6])), H[7]), K[i]), W[i])
            T2 = add(SIGMA0(H[0]), majority(H[0], H[1], H[2]))
            H.insert(0, add(T1, T2))
            H.pop()
            H[4] = add(H[4], T1)
        print('Intermediate')
        displayDigestList(H)
        for i in range(8):
            Hash[i] = add(Hash[i], H[i])
        print('Added to starting values')
        displayDigestList(Hash)
    st = ''
    for i in Hash:
        st += str(hex(int(i, 2)))[2:]
    print('Final Hash:')
    return st
def init_sha():
    global constants, initstate
    pool = generate_constants()
    constants = pool[0:64]
    initstate = pool[64:]
init_sha()
m = input('Hash:')
print(sha(m))
