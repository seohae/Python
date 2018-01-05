# key로 value 얻기

a = {'name':'pey', 'phone':'01199993333', 'birth':'1118'}
print(a.get('name'))
print(a.get('phone'))

# 딕셔너리 안에 찾으려는 key 값이 없을 경우 미리 정해둔 디폴트 값을 대신 가져오게한다.
print(a.get('foo', 'bar'))