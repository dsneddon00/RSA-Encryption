# RSA-Encryption

## 11-1-2021 Notes

P = 43
Q = 59
N = p*q = 2537
R = (p-1)*(q-1) = 2436

e. Pick e such that it is "a little smaller than N, and relatively prime with R."
d is the inverse of e mod r

Public Key:
(n, e)

Private Key:
(n, d)

Convert "st" and "op" from letter to numbers using our algorithm, not the book's.
The book algorithm results in 1819 and 1415

"stop" from alphabet to number
1819 1415
C=M^e % n
2081 == 1819^13 % 2537 --> True
2182 == 1415^13 % 2537 --> True

To Decrypt:
M = C^d % n
1819 = 2081^937 % n
1415 = 2182^937 % n