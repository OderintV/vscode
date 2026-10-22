class Flipgram:
    def __init__(self, word):
        self.word = word

    def ishetero(self):
        return len(set(self.word)) == len(self.word)

    def flip(self):
        half = len(self.word)
        if len(self.word) % 2 == 0:
            self.word =  self.word[half:] + self.word[:half]
        else:
            self.word =  self.word[half+1:] + self.word[half] + self.word[:half]

    def display(self):
        if self.ishetero():
            print("HETEROGRAM")
        else:
            self.flip()
            print(self.word)

def main():
    inp = input("Enter a word: ")
    fg = Flipgram(inp)
    fg.display()

main()
