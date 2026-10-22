WordArray = []
NumberWords = 0
def ReadWords(fname):
    global WordArray
    global NumberWords
    with open(fname, 'r') as file:
        for line in file:
            WordArray.append(line.strip())
    NumberWords = len(WordArray) - 1
    Play()
    
def main():
    choice = str(input("Enter choice between easy, medium, hard: ").strip().lower())
    ReadWords(choice + ".txt")

def Play():
    global WordArray
    global NumberWords
    correct_ans = 0
    print(f"Main word is {WordArray[0]}, and the number of answers are {NumberWords}")
    answer = input("Enter answer: ")
    while answer != 'no':
        if answer in WordArray:
            print(f"{answer} is a correct answer")
            index = WordArray.index(answer)
            WordArray[index] = None
            correct_ans += 1
        else:
            print(f"{answer} is a wrong answer")
    print(f"Percentage of correct answers = {correct_ans/NumberWords}")
    for ans in WordArray:
        if ans != None:
            print(ans)

main()
