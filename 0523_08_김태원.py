"""
    작성일 : 2024년 5월 23일
    작성자 : 컴퓨터소프트웨어공학부 201995026 김태원
    설명 : readlines() 메소드 사용법 - 반복문으로 출력하기
"""
print("== readlines() 메소드 이용하여 읽기 ==")

# with open을 이용하여 읽기 모드로 파일 객체 생성.
with open("test2.txt", "r") as f :
    # 파일에 있는 모든 줄을 하나의 리스트로 만든다.
    textlist = f.readlines()
    
    for line in textlist :
        print(line) # 리스트의 각항목을 출력한다.
    
# with open 을 사용하면 f.close()를 쓸 필요가 없다.