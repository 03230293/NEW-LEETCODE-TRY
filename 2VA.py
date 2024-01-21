s = "anagram"
t = "nagaram"
Output=True

def validAna(s, t):
    for i in s:
        for j in t:
            countS, countT= {},{}

            if countS[s[i]]==countT[t[j]]:
                print(Output)
            
            else:
                Output==False
                print(Output)
        break
validAna(s, t)