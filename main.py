def palindrome(word):
    word = word.lower()
    word = word.replace(" ","")
    if word == word[::-1]:
        return True
    else:
        return False

if __name__ == '__main__':
    word = input()
    print(palindrome(word))