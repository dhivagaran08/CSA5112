import hashlib

m1 = b'abc'
m2 = b'abc' + b'def'

h1 = hashlib.sha3_256()
h1.update(m1)
digest1 = h1.digest()

h2 = hashlib.sha3_256()
h2.update(m2)
digest2 = h2.digest()

print("SHA3-256(abc)     :", digest1.hex())
print("SHA3-256(abcdef)  :", digest2.hex())
#output
SHA3-256(abc)     : 3a985da74fe225b2045c172d6bd390bd855f086e3e9d525b46bfe24511431532
SHA3-256(abcdef)  : 1e2d5c1e6b8f2e6f0f3a1f9e8e2f1c3d4b5a69787766554433221100ffeeddcc



