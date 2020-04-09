import XCGD

p = 7 
q = 13
e = 5
m = (p-1)*(q-1)
d = XCGD.xgcd(e,m)[1]

print ("Inverse Modulus of " + str(e) + " in modulus " + str(m) + " = " + str(d) )

cipher = []
cipher.append(72**5 % 91)
cipher.append(69**5 % 91)
cipher.append(76**5 % 91)
cipher.append(76**5 % 91)
cipher.append(79**5 % 91)

print("Ciphertext: ", cipher)

plain = []
plain.append(cipher[0]**29 % 91)
plain.append(cipher[1]**29 % 91)
plain.append(cipher[2]**29 % 91)
plain.append(cipher[3]**29 % 91)
plain.append(cipher[4]**29 % 91)

print("Plaintext:  ", plain)


