#define is_palindrome function that takes one word in string as input
# and return true if it is palindrome else return false
# Palindrome - word that reads same backwards As for words
# Example
# is_palindrome Madam ---> True
# is_palindrome naman ---> True
# is_palindrome horse ---> False


# Logic (algorithm)
# Step 1--> reverse the string
# Step 2 -->compare reversed string with original string


# ANS:
def is_palindrome(word):
    reversed_word = word[::-1]
    if word==reversed_word:
        return True
    else:
        return False    

print(is_palindrome("naman"))
print(is_palindrome("horse"))

#or
def is_palindrome(word):
    if word==word[::-1]:
        return True
    else:
        return False    

print(is_palindrome("naman"))
print(is_palindrome("horse"))


#OR
def is_palindrome(word):
    return word==word[::-1]

print(is_palindrome("naman"))
print(is_palindrome("horse"))    