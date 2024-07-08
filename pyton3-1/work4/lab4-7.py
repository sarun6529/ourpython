def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def interpret_bmi(bmi):
    if bmi < 18.5:
        return "น้ำหนักน้อยเกินไป (Underweight)"
    elif 18.5 <= bmi < 24.9:
        return "น้ำหนักปกติ (Normal weight)"
    elif 25 <= bmi < 29.9:
        return "น้ำหนักเกิน (Overweight)"
    else:
        return "โรคอ้วน (Obesity)"

# รับค่าน้ำหนักและส่วนสูงจากผู้ใช้
weight = float(input("กรุณาใส่น้ำหนักของคุณ (กิโลกรัม): "))
height = float(input("กรุณาใส่ส่วนสูงของคุณ (เมตร): "))

bmi_value = calculate_bmi(weight, height)
bmi_category = interpret_bmi(bmi_value)

print(f"ค่า BMI ของคุณคือ: {bmi_value}")
print(f"คุณอยู่ในเกณฑ์: {bmi_category}")
