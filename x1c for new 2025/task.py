from os import urandom
from hashlib import sha256
from Crypto.Util.number import *

class AES:
    def __init__(self, key, round = 10):
        self.s_box = (
            0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,
            0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0,
            0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15,
            0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75,
            0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84,
            0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf,
            0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8,
            0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2,
            0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73,
            0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb,
            0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
            0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08,
            0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a,
            0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e,
            0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf,
            0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16
        )
        self.inv_s_box = (
            0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3, 0x9e, 0x81, 0xf3, 0xd7, 0xfb,
            0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f, 0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb,
            0x54, 0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b, 0x42, 0xfa, 0xc3, 0x4e,
            0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24, 0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25,
            0x72, 0xf8, 0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c, 0xcc, 0x5d, 0x65, 0xb6, 0x92,
            0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda, 0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84,
            0x90, 0xd8, 0xab, 0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3, 0x45, 0x06,
            0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1, 0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b,
            0x3a, 0x91, 0x11, 0x41, 0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6, 0x73,
            0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9, 0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e,
            0x47, 0xf1, 0x1a, 0x71, 0x1d, 0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b,
            0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0, 0xfe, 0x78, 0xcd, 0x5a, 0xf4,
            0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07, 0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f,
            0x60, 0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d, 0x2d, 0xe5, 0x7a, 0x9f, 0x93, 0xc9, 0x9c, 0xef,
            0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5, 0xb0, 0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61,
            0x17, 0x2b, 0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0c, 0x7d
        )
        self.r_con = (
            0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36
        )
        self.key = key
        self.rnd = round
        self.round_keys = self._key_expansion()

    def _sub_word(self, word):
        return bytes(self.s_box[b] for b in word)

    def _rot_word(self, word):
        return word[1:] + word[:1]

    def _key_expansion(self):
        round_keys = [self.key]
        for i in range(self.rnd):
            prev_key = round_keys[-1]
            temp = self._rot_word(prev_key[-4:])
            temp = self._sub_word(temp)
            temp = bytes([temp[0] ^ self.r_con[i]]) + temp[1:]
            new_key = bytes([prev_key[j] ^ temp[j] for j in range(4)])
            for k in range(4, 16, 4):
                new_key += bytes([prev_key[j+k] ^ new_key[j+k-4] for j in range(4)])
            round_keys.append(new_key)
        return round_keys

    def _sub_bytes(self, state):
        return bytes(self.s_box[b] for b in state)

    def _inv_sub_bytes(self, state):
        return bytes(self.inv_s_box[b] for b in state)

    def _shift_rows(self, state):
        return bytes([
            state[0], state[5], state[10], state[15],
            state[4], state[9], state[14], state[3],
            state[8], state[13], state[2], state[7],
            state[12], state[1], state[6], state[11]
        ])

    def _inv_shift_rows(self, state):
        return bytes([
            state[0], state[13], state[10], state[7],
            state[4], state[1], state[14], state[11],
            state[8], state[5], state[2], state[15],
            state[12], state[9], state[6], state[3]
        ])

    def _mix_columns(self, state):
        new_state = bytearray(16)
        for i in range(0, 16, 4):
            a, b, c, d = state[i:i+4]
            new_state[i] = (self._gmul(a, 2) ^ self._gmul(b, 3) ^ c ^ d)
            new_state[i+1] = (a ^ self._gmul(b, 2) ^ self._gmul(c, 3) ^ d)
            new_state[i+2] = (a ^ b ^ self._gmul(c, 2) ^ self._gmul(d, 3))
            new_state[i+3] = (self._gmul(a, 3) ^ b ^ c ^ self._gmul(d, 2))
        return bytes(new_state)

    def _inv_mix_columns(self, state):
        new_state = bytearray(16)
        for i in range(0, 16, 4):
            a, b, c, d = state[i:i+4]
            new_state[i] = (self._gmul(a, 0x0e) ^ self._gmul(b, 0x0b) ^ 
                          self._gmul(c, 0x0d) ^ self._gmul(d, 0x09))
            new_state[i+1] = (self._gmul(a, 0x09) ^ self._gmul(b, 0x0e) ^ 
                            self._gmul(c, 0x0b) ^ self._gmul(d, 0x0d))
            new_state[i+2] = (self._gmul(a, 0x0d) ^ self._gmul(b, 0x09) ^ 
                            self._gmul(c, 0x0e) ^ self._gmul(d, 0x0b))
            new_state[i+3] = (self._gmul(a, 0x0b) ^ self._gmul(b, 0x0d) ^ 
                            self._gmul(c, 0x09) ^ self._gmul(d, 0x0e))
        return bytes(new_state)

    def _gmul(self, a, b):
        p = 0
        for _ in range(8):
            if b & 1:
                p ^= a
            hi_bit_set = a & 0x80
            a <<= 1
            if hi_bit_set:
                a ^= 0x1b
            b >>= 1
        return p & 0xff

    def encrypt(self, plaintext):
        state = self._add_round_key(plaintext, self.round_keys[0])
        for i in range(1, self.rnd):
            state = self._sub_bytes(state)
            state = self._shift_rows(state)
            state = self._mix_columns(state)
            state = self._add_round_key(state, self.round_keys[i])
        state = self._sub_bytes(state)
        state = self._shift_rows(state)
        state = self._add_round_key(state, self.round_keys[self.rnd])
        return state

    def decrypt(self, ciphertext):
        state = self._add_round_key(ciphertext, self.round_keys[self.rnd])
        state = self._inv_shift_rows(state)
        state = self._inv_sub_bytes(state)
        for i in range(self.rnd - 1, 0, -1):
            state = self._add_round_key(state, self.round_keys[i])
            state = self._inv_mix_columns(state)
            state = self._inv_shift_rows(state)
            state = self._inv_sub_bytes(state)
        state = self._add_round_key(state, self.round_keys[0])
        return state

    def _add_round_key(self, state, round_key):
        return bytes(s ^ k for s, k in zip(state, round_key))

class ECC:
    def __init__(self):
        # SM2 Curve parameters
        self.p = 0xFFFFFFFEFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF00000000FFFFFFFFFFFFFFFF
        self.a = 0xFFFFFFFEFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF00000000FFFFFFFFFFFFFFFC
        self.b = 0x28E9FA9E9D9F5E344D5A9E4BCF6509A7F39789F515AB8F92DDBCBD414D940E93
        self.n = 0xFFFFFFFEFFFFFFFFFFFFFFFFFFFFFFFF7203DF6B21C6052B53BBF40939D54123
        self.Gx = 0x32C4AE2C1F1981195F9904466A39C9948FE30BBFF2660BE1715A4589334C74C7
        self.Gy = 0xBC3736A2F4F6779C59BDCEE36B692153D0A9877CC62A474002DF32E52139F0A0
        self.G = (self.Gx,self.Gy)

        self.d = int.from_bytes(urandom(32)) % self.n
        self.Q = self.mul(self.d,self.G)

    def is_on_curve(self, point):
        if point is None:
            return True
        x, y = point
        return (y**2 - x**3 - self.a * x - self.b) % self.p == 0

    def add(self, p1, p2):
        if p1 is None or p2 is None:
            return p1 if p2 is None else p2

        x1, y1 = p1
        x2, y2 = p2

        if x1 == x2 and y1 != y2:
            return None
        if x1 == x2:
            m = (3 * x1 * x1 + self.a) * pow(2 * y1, -1,  self.p) % self.p
        else:
            m = (y2 - y1) * pow((x2 - x1) % self.p, -1, self.p) % self.p
        
        x3 = (m * m - x1 - x2) % self.p
        y3 = (m * (x1 - x3) - y1) % self.p
        return (x3, y3)

    def mul(self, k:int, P:tuple[int,int]):
        if P is None:
            return None
        
        R = None        
        while k > 0:
            if k & 1:
                R = self.add(R, P)
            P = self.add(P,P)
            k >>= 1
        return R
    

def pad(msg:bytes):
    ll = 16 - len(msg) % 16
    return msg + bytes([ll] * ll) 

topic = '--- X1ct34m Entry Challenge! ---'

menu = '''
[1] Play with the encryption service
[2] Get some hint
[3] Obtain flag
[4] Exit
'''

if __name__=='__main__':
    print(topic)

    cv = ECC()
    key = urandom(16)
    aes = AES(key,round=4)
    hashval = sha256(long_to_bytes(cv.d) + key).digest()

    print(menu)

    # IN Parameters
    encryption_atp = 1000
    hint_atp = 20

    def aes_enc():
        global encryption_atp
        if encryption_atp <= 0:
            print('[!] You\'ve ran out of encryption attempts!')
            return
        
        lucky = urandom(1)
        encryption_atp -= 1
        print(f'[+] You can still check out on my lucky byte for {encryption_atp} times!')
        print(f'[+] Today my lucky byte is:{lucky.hex()}')
        print(f'[+] And the ciphertext is: {aes.encrypt(pad(lucky)).hex()}')

    def ghint():
        global hint_atp

        if hint_atp <= 0:
            print('[!] You\'ve ran out of hint attempts!')
            return
    
        print(f'[+] You still have {hint_atp} chances to conduct key exchange!')
        if hint_atp == 20:
            print(f'[+] Today my pubkey is {cv.Q}')
            print(f'[+] Now send your pubkey for key exchange!')

        hint_atp -= 1
        cx = int(input('[-] Your pubkey\'s x coordinate:'))
        cy = int(input('[-] Your pubkey\'s y coordinate:'))

        print(f'The shared key is: {cv.mul(cv.d,(cx,cy))}')


    def fetch_flag():
        if bytes.fromhex(input('[-] Give me the hash value:')) == hashval:
            print(f'[+] Congratulations! Here\'s your flag: {open("flag.txt").read().strip()}')
            exit()
        else:
            print('[!] Incorrect hash value')

    fun_dc = {'1':aes_enc,'2':ghint,'3':fetch_flag,'4':exit}

    while True:
        opt = input('[-] Your option:')
        if not opt in fun_dc:
            print('[!] Invalid input')
            continue

        fun_dc[opt]()

    


    
    
    