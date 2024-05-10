"""
    작성일 : 2024년 5월 10일
    작성자 : 컴퓨터소프트웨어공학부 201995026 김태원
    설명 : 사용자로부터 과일을 입력 받아 리스트를 생성하시오.
    
        좋아하는 과일 5개를 입력받아 리스트에 저장한다.
        좋아하는 과일 이름을 하나 입력하여 그 과일이 
        리스트에 있는지 없는지 판단한다.
        
        리스트에 추가 => append()메소드
        찾기(포함) => in 연산자
        
    [알고리즘]   
    1. 사용자가 입력한 과일을 저장 할 리스트가 필요하다. => 빈 리스트를 생성.
    2. 5번 반복하면서 
        2-1. 과일을 입력 받아 변수에 저장.
        2-2. 과일 변수에 저장된 과일을 리스트에 추가한다.   append()
    3. 리스트에 저장된 과일 출력
    
    4. 과일 이름을 하나 입력 받는다.
    5. 만약에 그 과일이 리스트에 있으면
        5-1. 00은 당신이 좋아하는 과일 입니다.
    6. 아니면
        6-1. 00은 당신이 좋아하는 과일이 아닙니다.
"""
# 빈 리스트를 생성
fruits = []

# 5번 반복하면서 과일 이름 입력 받아 리스트에 저장.
for i in range(5) :
    fruit_name = input(str(i+1) + ".좋아하는 과일 이름을 입력하세요 : ")
    fruits.append(fruit_name)   # 입력받은 변수의 값을 리스트에 추가.

print("입력한 과일 리스트 : ", fruits)

print()

favo_fruits = input("좋아하는 과일은 ? ")

# 사용자가 입력한 과일이 리스트에 있는지 판단
# 만약에 입력한 과일이 리스트에 있다면..

if favo_fruits in fruits :
    print(f"{favo_fruits}는 당신이 좋아하는 과일 입니다.")
else :
    print(f"{favo_fruits}는 당신이 좋아하는 과일이 아닙니다.")