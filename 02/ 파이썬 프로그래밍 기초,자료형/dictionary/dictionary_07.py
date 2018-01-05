# 딕셔너리 관련 함수

# 1. Key 리스트 만들기
a = {'name':'pey', 'phone':'01199993333', 'birth':'1118'}
print(a.keys()) # dict_keys(['name', 'phone', 'birth'])

for k in a.keys():
    print(k)

print(list(a.keys())) # 객체를 리스트로 변환