# 집합 자료형의 특징
# 중복을 허용하지 않는다.
# 순서가 없다.

s1 = set([1,2,3])
l1 = list(s1)
print(l1) # [1,2,3]
print(l1[0]) # 1

t1 = tuple(s1)
print(t1) # (1,2,3)
print(t1[0]) # 1