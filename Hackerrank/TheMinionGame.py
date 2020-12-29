def minion_game(string):
    # your code goes here
    vowels = 'AEIOU'

    kes = 0
    stu = 0

    for i in range(len(s)):
        if s[i] in vowels:
            kes += (len(s)-i)
        else:
            stu += (len(s)-i)
    if kes > stu:
        print("Kevin", kes)

    elif kes < stu:
        print("Stuart", stu)

    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)