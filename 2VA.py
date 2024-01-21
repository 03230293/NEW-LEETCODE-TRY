s = "anagram"
t = "nagaram"
Output=True

def validAna(s, t):
    for i in s:
        for j in t:
            if i==j:
                print(Output)
            
            else:
                Output==False
                print(Output)
        break
validAna(s, t)