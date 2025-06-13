
#no 1
def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

print(raise_to_power(5,6))


#no 2
array = [
    [3,4,5],
    [456,5,6],
    [2],
    [4,56,3,3,5,3],
]
'''primary iterable = row,
   secondary iterable = column, 
   nested for loop is used'''
for a in array:
    for b in a:
        print(b)

#no 3
'''In this language, we will replace all vowels with !!'''
def translate(phrase):
    translation = ''
    for letter in phrase:
        if letter.lower() in "aeiou":
            translation = translation + '!!'
        else:
            translation = translation + letter
    return(translation)

print(translate(input('Enter what you want to translate:')))



