def avg(n):
    total_score = 0  

    for i in range(n):
        while True: 
            try:
                score = float(input(f"กรุณากรอกคะแนนของนักศึกษาคนที่ {i + 1}: "))
                total_score += score
                break  
            except ValueError:
                print("กรุณากรอกค่าคะแนนที่เป็นตัวเลข")

    average_score = total_score / n  
    return average_score

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

    average_score = acg(n)
    print(f"คะแนนเฉลี่ยของนักศึกษาทั้งหมด {n} คนคือ: {average_score:.2f}")

if __name__ == "__main__":
    main()
