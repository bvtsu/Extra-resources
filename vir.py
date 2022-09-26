"""3mer to dict

output dict, key is a 3mer, and value is the number of time the 3mer occurs
"""

from itertools import product

test_dna = "CTAGCTAGCTAGCTAGCTAG"

threemer_key = []

threemers = list(product(test_dna, repeat=3))
for threemer in threemers:
    threemer_key.append("".join(threemer))

print(threemer_key)

threemer_dict = {}

for threemer in threemer_key:
    threemer_dict[threemer] = test_dna.count(threemer)

print(threemer_dict)