# Задача 2.4.

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"

a = ("Hi! Hello!")
b = ("")
c = ("Oh, no!!!")
def remove_exclamation_marks(s):
    return s.replace("!", " ")
print(remove_exclamation_marks(a), (b), (c))

# Пункт B.
# Удалите восклицательный знак из конца строки. 
a = ("Hi!") #== "Hi"
b = ("Hi!!!") #== "Hi!!"
c = ("!Hi") #== "!Hi"

def remove_last_em(s):
  if len(s) > 0 and s[-1] == "!":
    return s[:-1]
  else:
    return s
print(remove_last_em(a), (b), (c))

# Дополнительно

# Пункт С.
# Удалите слова из предложения, если они содержат ровно один восклицательный знак.
# Слова разделены одним пробелом.
# Например,
a = ("Hi!") #=== ""
b = ("Hi! Hi!") #=== ""
c = ("Hi! Hi! Hi!") #=== ""
d = ("Hi Hi! Hi!") #=== "Hi"
e = ("Hi! !Hi Hi!") #=== ""
f = ("Hi! Hi!! Hi!") #=== "Hi!!"
g = ("Hi! !Hi! Hi!") #=== "!Hi!"

def remove_word_with_one_em(s):
    words = s.split()
    new_words = []
    for word in words:
        if word.count("!") != 1:
            new_words.append(word)
    return " ".join(new_words)
# print(remove_word_with_one_em("Hi!"))     
print(remove_word_with_one_em(a))
print(remove_word_with_one_em(b))
print(remove_word_with_one_em(c))
print(remove_word_with_one_em(d))
print(remove_word_with_one_em(e))
print(remove_word_with_one_em(f))
print(remove_word_with_one_em(g))