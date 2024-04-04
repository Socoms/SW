"""
    작성일 : 2024년 03월 22일
    작성자 : 컴퓨터소프트웨어공학부 201995026 김태원
    설명 : 입력 input()함수 사용하기
"""
 #이름을 입력받아 변수에 저장하시오. ★설명은 필수
name = input("이름을 입력하시오 : ")

#입력받은 이름을 출력하시오.
#○○님 환영합니다.
print(name, "님 환영합니다.")
print("{}님 환영합니다." .format(name))
print(f"{name}님 환영합니다.")

#국어 점수와 수학 점수를 입력받아 각각 변수에 저장하시오.
kor_score = input("국어 점수 입력 : ")
math_score = input("수학 점수 입력 : ")

#두 과목의 점수를 합하여 변수에 저장하시오.
total_score = kor_score + math_score

#두 과목의 합계를 출력하시오.
#두 과목의 점수의 합계는 ○○점 입니다.
print("두 과목의 점수의 합계는", total_score , "점 입니다")
print("두 과목의 점수의 합계는 {}점 입니다." .format(total_score))
print(f"두 과목의 점수의 합계는 {total_score}점 입니다.")

#영어 점수와 컴퓨터 점수를 입력 받아 정수로 변환하여 변수로 저장. 정수값 = int / 실수값 = float
eng_score = int(input("영어 점수 입력 : "))
com_score = int(input("컴퓨터 점수 입력 : "))

#두 과목의 점수 합계를 계산하시오.
total_score = eng_score + com_score #코드는 어차피 차례대로 진행되므로 여기서 같은 변수를 사용해도 상관없다

#두 과목의 합계를 출력하시오.
#두 과목의 점수의 합계는 ○○점 입니다.
print("두 과목의 점수의 합계는", total_score , "점 입니다")
print("두 과목의 점수의 합계는 {}점 입니다." .format(total_score))
print(f"두 과목의 점수의 합계는 {total_score}점 입니다.")