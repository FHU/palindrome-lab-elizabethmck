word = input()

def palindrome(word):
    word = word.lower().replace("","")
    if word == word [::-1]:
        return True
    else:
        return False

print(palindrome(word))
