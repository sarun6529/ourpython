def calculate_total_score(homework, midterm, final):
    total_score = homework + midterm + final
    return total_score

def evaluate_score(total_score):
    if total_score > 80:
        return "ดีมาก"
    elif total_score > 50:
        return "ผ่าน"
    else:
        return "ไม่ผ่าน"

def main():
    while True:
        try:
            n = int(input("กรุณากรอกจำนวนนักศึกษา: "))
            if n > 0:
                break
            else:
                print("กรุณากรอกจำนวนที่มากกว่า 0")
        except ValueError:
            print("กรุณากรอกจำนวนที่เป็นตัวเลข")
    
    for i in range(n):
        print(f"\nนักศึกษาคนที่ {i + 1}")
        
        while True:
            try:
                homework = float(input("กรุณากรอกคะแนนการบ้าน (เต็ม 20): "))
                if 0 <= homework <= 20:
                    break
                else:
                    print("กรุณากรอกคะแนนระหว่าง 0 ถึง 20")
            except ValueError:
                print("กรุณากรอกค่าคะแนนที่เป็นตัวเลข")
        
        while True:
            try:
                midterm = float(input("กรุณากรอกคะแนนสอบกลางภาค (เต็ม 40): "))
                if 0 <= midterm <= 40:
                    break
                else:
                    print("กรุณากรอกคะแนนระหว่าง 0 ถึง 40")
            except ValueError:
                print("กรุณากรอกค่าคะแนนที่เป็นตัวเลข")
        
        while True:
            try:
                final = float(input("กรุณากรอกคะแนนสอบปลายภาค (เต็ม 40): "))
                if 0 <= final <= 40:
                    break
                else:
                    print("กรุณากรอกคะแนนระหว่าง 0 ถึง 40")
            except ValueError:
                print("กรุณากรอกค่าคะแนนที่เป็นตัวเลข")

        total_score = calculate_total_score(homework, midterm, final)
        evaluation = evaluate_score(total_score)
        
        print(f"คะแนนรวมของนักศึกษาคนที่ {i + 1}: {total_score:.2f}")
        print(f"ผลการประเมิน: {evaluation}")

if __name__ == "__main__":
    main()
