def get_student_scores(n):
    scores = []
    for i in range(n):
        while True:
            try:
                score = float(input(f"กรุณากรอกคะแนนของนักศึกษาคนที่ {i + 1}: "))
                scores.append(score)
                break
            except ValueError:
                print("กรุณากรอกค่าคะแนนที่เป็นตัวเลข")
    return scores

def calculate_average(scores):
    total_score = sum(scores)
    average_score = total_score / len(scores)
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
    
    scores = get_student_scores(n)
    average_score = calculate_average(scores)
    print(f"คะแนนเฉลี่ยของนักศึกษาทั้งหมด {n} คนคือ: {average_score:.2f}")

if __name__ == "__main__":
    main()
