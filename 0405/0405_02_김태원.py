year = int(input("년도를 입력하시오. : "))

if (year % 4 ==0 and year % 100 != 0) or (year % 400 == 0) :
    print(f"{year} 년 은 윤년 입니다")
else :
    print(f"{year} 년 은 윤년이 아닙니다")