a = [1,2,3,['a','b','c']]
print(a[0]) #1
print(a[-1]) #['a', 'b', 'c'] : 마지막 원소
print(a[3]) #['a', 'b', 'c'] : 4번째 원소 = 마지막 원소

#리스트에 a에 포함된 ['a','b','c']라는 리스트에서 'a'라는 인덱싱을 이용해 끄집어내보자
print(a[-1][0]) #a[-1] 원소에서 0번째 인덱스 출력