###STRING 기본 연산

#1. 더하기
#string끼리 이어붙이는 연산


#2. 곱하기
#동일한 string을 n회 반복해주는 것


#3. 문자열 길이 구하기
#len("STRING")


#4. 문자열 Indexing/ Slicing
#다른 언어에서는 안되는데, Python에서는 가능

a = "Life is too short, You need Python"
a[0]    #모든 indexing은 0부터 시작
a[1]
a[2:4]  #Slicing의 기본은, 이상~미만임
a[2:]   #index 2부터 끝까지
a[:]    #시작점과 끝점 모두 비우면 전체 다 출력

a[-1]


#5. 문자열의 요소 변경 (불가능)
a = 'pithon'
a[2] ='y'  #이렇게 변경 불가능
a1 = a[0] + 'y' + a[2:]
print(a1)


#6. 문자열의 길이
len(a)  #List, Tuple에서 모두 사용 가능 