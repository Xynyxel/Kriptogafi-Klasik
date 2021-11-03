from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
# encryption
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
import string


class MainWindow(Screen):
    def test(self):
        print("test")


class Algortima1Window(Screen):
    def encodeData(self):
        # Menetapkan panjang data yang akan dienkripsi
        pesan = self.data.text
        ubah = ''
        i = len(pesan) - 1
        while i >= 0:
            ubah = ubah + pesan[i]
            i = i - 1
        self.hasilEncode.text = ubah

    def decodeData(self):
        # decryption
        pesan = self.dataEncode.text
        ubah = ''
        i = len(pesan) - 1
        while i >= 0:
            ubah = ubah + pesan[i]
            i = i - 1
        self.hasilDecode.text = ubah

class Algortima2Window(Screen):
    

    def encodeData(self):
        pesan = self.data.text
        kunci = self.kunci.text
        self.hasilEncode.text = self.ubahPesan(kunci, pesan, 'enkripsi')
    
    def decodeData(self):
        pesan = self.dataEncode.text
        kunci = self.kunciEncode.text
        self.hasilDecode.text = self.ubahPesan(kunci, pesan, 'dekripsi')

    def ubahPesan(self, kunci, pesan, mode):
        HURUF = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        ubah = []
        #menyimpan pesan enkripsi dan dekripsi
        kunciIndex = 0
        kunci = kunci.upper()
        for symbol in pesan:
            #akan dilakukan pada seluruh karakter dalam pesan
            nomor = HURUF.find(symbol.upper())
            if nomor != -1: #-1 berarti symbol.upper() tidak ditemukan didalam HURUF
                if mode == 'enkripsi':
                    nomor += HURUF.find(kunci[kunciIndex]) #tambahkan jika dienkripsi
                elif mode == 'dekripsi':
                    nomor -= HURUF.find(kunci[kunciIndex]) #kurangi jika melakukan dekripsi
                nomor %= len(HURUF)
                #tambahkan pada hasil symbol enkrip/dekrip yang sudah diubahkan
                if symbol.isupper():
                    ubah.append(HURUF[nomor])
                elif symbol.islower():
                    ubah.append(HURUF[nomor].lower())
                kunciIndex += 1
                #ubah kunci yang akan dipakai selanjutnya
                if kunciIndex == len(kunci):
                    kunciIndex = 0
            else:
                #symbol tidak berada pada HURUF, maka tambahkan hal tersebut dan ubahkan
                ubah.append(symbol)
        return ''.join(ubah)


class Algortima3Window(Screen):
    def egcd(self,a, b):
        x,y, u,v = 0,1, 1,0
        while a != 0:
            q, r = b//a, b%a
            m, n = x-u*q, y-v*q
            b,a, x,y, u,v = a,r, u,v, m,n
        gcd = b
        return gcd, x, y
 
    def modinv(self,a, m):
        gcd, x, y = self.egcd(a, m)
        if gcd != 1:
            return None  # modular inverse does not exist
        else:
            return x % m

    def encodeData(self):
        pesan = self.data.text
        kunci = [int(self.kunci.text), int(self.kunci2.text)]
        self.hasilEncode.text = ''.join([ chr((( kunci[0]*(ord(t) - ord('A')) + kunci[1] ) % 26)
                  + ord('A')) for t in pesan.upper().replace(' ', '') ])
    
    def decodeData(self):
        pesan = self.dataEncode.text
        kunci = [int(self.kunciEncode.text), int(self.kunciEncode2.text)]
        self.hasilDecode.text = ''.join([ chr((( self.modinv(kunci[0], 26)*(ord(c) - ord('A') - kunci[1]))
                    % 26) + ord('A')) for c in pesan ])
    

class Algortima4Window(Screen):
    def encodeData(self):
        pesan = self.data.text
        kunci = self.kunci.text
        all_letters= string.ascii_letters
        dict1 = {}
        key = int(kunci)
        
        for i in range(len(all_letters)):
            dict1[all_letters[i]] = all_letters[(i+key)%len(all_letters)]
        
        cipher_txt=[]
        
        # loop to generate ciphertext
        
        for char in pesan:
            if char in all_letters:
                temp = dict1[char]
                cipher_txt.append(temp)
            else:
                temp =char
                cipher_txt.append(temp)
                
        cipher_txt= "".join(cipher_txt)
        self.hasilEncode.text = cipher_txt
    
    def decodeData(self):
        pesan = self.dataEncode.text
        kunci = self.kunciEncode.text
        key = int(kunci)
        all_letters= string.ascii_letters
        dict2 = {}    
        for i in range(len(all_letters)):
            dict2[all_letters[i]] = all_letters[(i-key)%(len(all_letters))]
            
        # loop to recover plain text
        decrypt_txt = []
        
        for char in pesan:
            if char in all_letters:
                temp = dict2[char]
                decrypt_txt.append(temp)
            else:
                temp = char
                decrypt_txt.append(temp)
                
        decrypt_txt = "".join(decrypt_txt)
        self.hasilDecode.text = decrypt_txt

class Algortima5Window(Screen):

    def atbash(self, message):
        lookup_table = {'A' : 'Z', 'B' : 'Y', 'C' : 'X', 'D' : 'W', 'E' : 'V',
        'F' : 'U', 'G' : 'T', 'H' : 'S', 'I' : 'R', 'J' : 'Q',
        'K' : 'P', 'L' : 'O', 'M' : 'N', 'N' : 'M', 'O' : 'L',
        'P' : 'K', 'Q' : 'J', 'R' : 'I', 'S' : 'H', 'T' : 'G',
        'U' : 'F', 'V' : 'E', 'W' : 'D', 'X' : 'C', 'Y' : 'B', 'Z' : 'A'}
        cipher = ''
        for letter in message:
            # checks for space
            if(letter != ' '):
                #adds the corresponding letter from the lookup_table
                cipher += lookup_table[letter]
            else:
                # adds space
                cipher += ' '
    
        return cipher

    def encodeData(self):
        # Menetapkan panjang data yang akan dienkripsi
        pesan = self.data.text
        self.hasilEncode.text = self.atbash(pesan.upper())

    def decodeData(self):
        # decryption
        pesan = self.dataEncode.text
        self.hasilDecode.text = self.atbash(pesan.upper())

class Algortima6Window(Screen):

    def encrypt(self, message):
        lookup = {'A':'aaaaa', 'B':'aaaab', 'C':'aaaba', 'D':'aaabb', 'E':'aabaa',
        'F':'aabab', 'G':'aabba', 'H':'aabbb', 'I':'abaaa', 'J':'abaab',
        'K':'ababa', 'L':'ababb', 'M':'abbaa', 'N':'abbab', 'O':'abbba',
        'P':'abbbb', 'Q':'baaaa', 'R':'baaab', 'S':'baaba', 'T':'baabb',
        'U':'babaa', 'V':'babab', 'W':'babba', 'X':'babbb', 'Y':'bbaaa', 'Z':'bbaab'}
        cipher = ''
        for letter in message:
            # checks for space
            if(letter != ' '):
                # adds the ciphertext corresponding to the 
                # plaintext from the dictionary
                cipher += lookup[letter]
            else:
                # adds space
                cipher += ' '
    
        return cipher

    def decrypt(self, message):
        lookup = {'A':'aaaaa', 'B':'aaaab', 'C':'aaaba', 'D':'aaabb', 'E':'aabaa',
        'F':'aabab', 'G':'aabba', 'H':'aabbb', 'I':'abaaa', 'J':'abaab',
        'K':'ababa', 'L':'ababb', 'M':'abbaa', 'N':'abbab', 'O':'abbba',
        'P':'abbbb', 'Q':'baaaa', 'R':'baaab', 'S':'baaba', 'T':'baabb',
        'U':'babaa', 'V':'babab', 'W':'babba', 'X':'babbb', 'Y':'bbaaa', 'Z':'bbaab'}
        decipher = ''
        i = 0
    
        # emulating a do-while loop
        while True :
            # condition to run decryption till 
            # the last set of ciphertext
            if(i < len(message)-4):
                # extracting a set of ciphertext
                # from the message
                substr = message[i:i + 5]
                # checking for space as the first 
                # character of the substring
                if(substr[0] != ' '):
                    '''
                    This statement gets us the key(plaintext) using the values(ciphertext)
                    Just the reverse of what we were doing in encrypt function
                    '''
                    decipher += list(lookup.keys())[list(lookup.values()).index(substr)]
                    i += 5 # to get the next set of ciphertext
    
                else:
                    # adds space
                    decipher += ' '
                    i += 1 # index next to the space
            else:
                break # emulating a do-while loop
    
        return decipher

    def encodeData(self):
        # Menetapkan panjang data yang akan dienkripsi
        pesan = self.data.text
        self.hasilEncode.text = self.encrypt(pesan.upper())

    def decodeData(self):
        # decryption
        pesan = self.dataEncode.text
        self.hasilDecode.text = self.decrypt(pesan.lower())


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("kriptografi.kv")


class MyMainApp(App):
    def build(self):
        return kv

    

    


if __name__ == "__main__":
    MyMainApp().run()