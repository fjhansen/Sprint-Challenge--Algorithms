'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    th = 'th'
    
    # if th is not present in word
    if th not in word:
       #print(word)
        return 0

    # th at start of word +1 to count of th
    if (word[0:2] == th): 
        word = word.replace(th, 'oo', 1)
        #print(word)
        return count_th(word) + 1
        #print(word)
    
    return count_th(word[1:])

print(count_th("th"))
