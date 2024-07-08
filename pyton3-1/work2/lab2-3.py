def calculate_bmi(weight, height_cm):
    
    height_m = height_cm / 100
    
    bmi = weight / (height_m ** 2)
    return bmi

def bmi_category(bmi):
   
    if bmi < 18.5:
        return "น้ำหนักน้อยกว่ามาตรฐาน"
    elif 18.5 <= bmi < 22.9:
        return "น้ำหนักมาตรฐาน"
    elif 23 <= bmi < 24.9:
        return "อ้วนระดับ 1"
    elif 25 <= bmi < 29.9:
        return "อ้วนระดับ 2"
    else:
        return "อ้วนระดับ 3"

try:
    weight = float(input("กรุณากรอกน้ำหนัก (กิโลกรัม): "))
    height_cm = float(input("กรุณากรอกส่วนสูง (เซนติเมตร): "))
    
    bmi = calculate_bmi(weight, height_cm)
    category = bmi_category(bmi)
    
    print(f"ค่า BMI ของคุณคือ: {bmi:.2f}")
    print(f"คุณอยู่ในเกณฑ์: {category}")
    
except ValueError:
    print("กรุณากรอกข้อมูลที่เป็นตัวเลขที่ถูกต้อง")
