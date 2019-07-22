def minion_game(string):
    count1 =0
    count2 =0
    vowel=['A','E','I','O','U']
    # your code goes here
    for i in range(len(string)):
        if string[i] in vowel:
            count1 += len(string)- i
        else:
           count2 += len(string)- i
    
    if count1>count2:
        print('Kevin {}'.format(count1))
    elif count2> count1:
        print('Stuart {}'.format(count2))
    else:
        print('Draw')
if __name__ == '__main__':
    s = input()
    minion_game(s)