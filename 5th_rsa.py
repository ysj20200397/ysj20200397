from math import gcd

p=31
q=17
n = p * q 
phi_n = (p-1) * (q-1)

#e 찾기
for i in range(2,phi_n):
    if gcd(i,phi_n)==1:
        e = i  
        break   

#d 찾기 
d=0
mod=0
while True:
    d += 1
    mod = (e*d) % phi_n
    if mod == 1:
        break
    
#Encryption
#C = P^e mod n 

plain = "CAU DIST Practice Homework"
plain_list= [ord(x) for x in plain]

cipher = []
for i in plain_list:
    x = (i**e) % n   
    cipher.append(int(x))

#Decryption
#p = C^d mod n

decrypted = []
for i in cipher:
    x = (i**d) % n   
    decrypted.append(int(x))
    
print('plain text', plain_list)
print('cipher text', cipher)
print('decrypted text', decrypted)

decrypted_text = ''.join([chr(x) for x in decrypted])
print('decrypted text:', decrypted_text)
