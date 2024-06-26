"""
    작성일 : 2024년 04월 05일
    작성자 : 컴퓨터소프트웨어공학부 201995026 김태원
    설명 : 월을 입력받아 해당 계절을 출력하시오.
            3,4,5월 => 봄
            6,7,8월 => 여름
            9,10,11월 => 가을
            12,1,2월 => 겨울
    
    [문제분석]
        필요한 변수 : month
        입력받는 월은 정수값이다.
        월은 1~12 사이이다.
        1~12 사이의 값이 아니면 잘못된 월 입니다.
        봄 , 여름 , 가을 , 겨울 은 출력 값이다.
        
        
        
    [알고리즘]
        1. 달을 입력받는다
        2. 만약에 입력받은 달이 1월~12월 이면
            2-1. 만약 입력받은 달이 3월~5월 이면
                2-1-1. 봄 출력
            2-2. 아니고 만약 입력받은 달이 6월~8월 이면
                2-2-1. 여름 출력
            2-3. 아니고 만약 입력받은 달이 9월~11월 이면
                2-3-1. 가을 출력
            2-4. 아니고 만약 입력받은 달이 12월~2월 이면
                2-4-1. 겨울 출력
         3. 아니면
            3-1. 잘못된 월 출력
"""

month = int(input("달을 입력 하시오 : "))

if 1 <= month <= 12 :
    if 3 <= month <= 5 :
        print(f"{month}월은 봄 입니다.")
    elif 6 <= month <= 8 :
        print(f"{month}월은 여름 입니다.")
    elif 9 <= month <= 11 :
        print(f"{month}월은 가을 입니다.")
    elif 12 or 1 or 2 :
        print(f"{month}월은 겨울 입니다.")
    
else :
    print("잘못 입력하셧습니다.")