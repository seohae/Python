# 차집합
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print(s1-s2) # {1, 2, 3}
print(s2-s1) # {8, 9, 7}
print(s1.difference(s2)) # {1, 2, 3}
print(s2.difference(s1)) # {8, 9, 7}