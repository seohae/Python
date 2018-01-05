# 3. key, value 쌍 얻기

a = {'name':'pey', 'phone':'01199993333', 'birth':'1118'}
print(a.items()) # 쌍을 튜플로 묶은 값을 객체로 돌려준다

# 4. key, value 쌍 지우기
a.clear()
print(a) # {} -> 딕셔너리 안의 모든 요소를 삭제한다