#문자열 포매팅 = string 안에 내가 원하는 값을 넣어주는 방법

#1. %s, %d, %f, %c 등을 이용해주기
a = "I eat %d apples" %3
print(a)
b = "I eat %s apples" %15     #integer라서 따옴표 없이 써주면 됨
print(b)
c = "I eat %s apples" %'15s'  #string으로 쓰려면 여기다가도 따옴표를 써주어야 함
print(c)

d = 'how many'
e = "I eat %s apples" %d      #변수로 입력해주어도 됨 
print(e)


#기본적으로 모든 것은 그냥 %s로 써주면 다 됨 (뒤에 오는 것을 자동적으로 STRING으로 바꾸어줌)
# %f는 소수점, %c는 단일 문자(int/ char) 
e1 = "I eat %c apples" %'15'      #단일 문자(integer 1개/ character 1글자만 가능) 
print(e1)

e2 = "I eat %f apples" %2.1      #float도 int와 마찬가지로 따옴표 불필요, 정수를 넣어도 소수점으로 표현해줌 
print(e2)

#여러개를 넣어주기
e3 = "I eat %s apples and %s pears." % (3,'14')   #넣어줄 위치마다 %s해주고, 맨 뒤에 %( , ) 한번에 넣어주면 됨 
                                                  #서로 다른 자료형 넣어주는 것 가능함 
print(e3)


#2. "STRING".format 이용해주기
f = "I eat {} apples".format(3) #string 안에 {} 넣어주고 .format()으로 사용가능, '3' 이렇게 string으로도 ok
print(f)

g = "I eat {number} apples".format(number=3) #변수 넣어줘도 됨
print(g)
print(number)    #e다만, number라는 변수 생성 X



#3. f"STRING" 이용해주기
h = 'how many'
i = f"I eat {h} apples."  #h자리에 integer, string 모두 넣을 수 있음
print(i)

h1 = 3
i1 = f"I eat {h1 + 1} apples"   #표현식(변수와 + - 등의 수식 사용)을 지원함
print(i1)


#4. 소수점 정렬
# "%0.nf" % FLOAT 를 통해서 소수점 n째자리까지 정렬 가능

j = "%0.5f" %3.14159211     
print(j)


###############################################################################3
# 5. 공백 채우기, 정렬에 대해서는 배우지 않았음
# 필요시 https://wikidocs.net/13 참고
###############################################################################3



###STRING 함수 

#1. Index 찾아주는 함수

#1-1  .find()함수
#해당 조건에 가장 먼저 걸리는 애의 index가 노출됨 (없을 경우 -1로 표현) 
# .index() 보다 쓰기 편하다고 함

k = "I eat 3 apples."
k.find("I")    #맨 처음 글자니까 Index는 0임
k.find('e')    #e는 여러개 있지만, 가장 먼저 나오는 e의 index를 돌려줌
k.find(3)      #TypeError 발생, string안에서 찾아주니 string으로 찾아주어야 함
k.find('3')
k.find('z')    #없으니 -1을 돌려줌

#1-2   .index()함수
k.index("I")
k.index('e')    #e는 여러개 있지만, 가장 먼저 나오는 e의 index를 돌려줌
k.index(3)      #TypeError 발생, string안에서 찾아주니 string으로 찾아주어야 함
k.index('3')
k.index('z')    #없어서 ValueError발생 #substring not found 

#2    .join() 함수
#문자열 삽입 = 지정해준 구분자를 string의 매 글자 사이에 넣은 뒤, string으로 돌려주는 것
#list, tuple에 대해서도 사용 가능, list or tuple --> string으로 변경 시에도 사용 가능 

l = ","
l.join('abcd')    

'/'.join('abcd')  #직접 구분자 지정도 가능


#3    .count() 함수
#STRING 속 문자 개수 세기

m = "hobby"
m.count('h')    #당연히 STRING 만 들어가야 함
m.count('b')


#4    .upper(), .lower() 함수
#대소문자 변경 함수

m.upper()
(m.upper()).lower()   

m1 = "Hobby"
m1.lower()


#5.    .strip()
#공백 지우기
# .lstrip() 왼쪽 공백, .rstrip() 오른쪽 공백,  .strip() 양쪽 공백 지우기

n = "   hi   "
n.lstrip()
n.rstrip()
n.strip()



#6      .replace()
#   .replace("바꾸고 싶은 현재 문자열, 새로운 문자열")

o = "I need python for my life"
o.replace('need','love')
o.replace(' ','+')      #STRING내 해당하는 모든 값들을 다 바꾸어줌


o1 = "Pithon"
o1.replace('i', 'y')    #글자 하나 변경도 가능


#7      .split()
#문자열 나누기
#STRING --> LIST에서 사용

#인자를 안넣어주면 공백을 기준으로 나누어줌
#인자를 넣어주면, 해당 인자를 구분자로 나누어줌

p = "Life is, too short. I need Python!"
p.split()     #공백 기준으로만 쪼개줌
p.split(',')  
p.split('.')  #구분자는 쪼개준 뒤, 결과값에 나오지않고 사라짐