stream_counts = {
    "Science and Computer": 0,
    "Commerce and Computer": 0,
    "Arts and Animation": 0,
    "Try again": 0
}

student_records = []

while True:
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    mks = int(input("Enter your marks (or -1 to exit): "))

    if mks == -1:
        print("\nExiting and displaying results...\n")
        break

    if mks >= 300:
        stream = "Science and Computer"
    elif 200 <= mks < 300:
        stream = "Commerce and Computer"
    elif 75 <= mks < 200:
        stream = "Arts and Animation"
    else:
        stream = "Try again"
    
    student_records.append({
        "name": name,
        "age": age,
        "marks": mks,
        "stream": stream
    })

    stream_counts[stream] += 1
print("Student Stream Allocation:")
for student in student_records:
    print(f"{student['name']}, age {student['age']}, marks: {student['marks']} → Stream: {student['stream']}")

print("Stream choice counts:")
for stream, count in stream_counts.items():
    print(f"{stream}: {count}")
