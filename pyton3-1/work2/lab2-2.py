def get_grade(score):
    if 80 <= score <= 100:
        return "เกรด A"
    elif 70 <= score <= 79:
        return "เกรด B"
    elif 60 <= score <= 69:
        return "เกรด C"
    elif 50 <= score <= 59:
        return "เกรด D"
    elif 0 <= score <= 49:
        return "เกรด F"
    else:
        return "กรุณากรอกข้อมูล 0-100"

try:
    score = float(input("กรุณากรอกคะแนน (0-100): "))
    print(get_grade(score))
except ValueError:
    print("กรุณากรอกข้อมูลที่เป็นตัวเลข 0-100")
