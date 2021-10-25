#List --> 문자열은 join을 사용
i = ['a', 'b', 'c']
print(''.join(i))    # 구분자 없이 list 원소 붙이기 
print(','.join(i))   # 쉼표를 구분자로 이어붙이기
print('?'.join(i))   

print('\t'.join(i))  #탭 또는 줄바꿈 기호를 구분자로도 가능 
print('\n'.join(i))  

print('\t'.join(['1','2','3']))  #List를 인자로 직접 넣는 것도 가능
print('\t'.join([ 1 , 2 , 3 ]))  #List속 원소가 Integer인 것은 안됨!!!!!! 하나라도 Integer면 안됨!!

#String 각 요소들 사이에 구분자를 넣는 데도 사용 가능  
print(','.join('12345'))
print(','.join(12345))  #integer는 string이 아니라서 안됨, iterable하지 않음 


#String --> List는 split을 사용
e
