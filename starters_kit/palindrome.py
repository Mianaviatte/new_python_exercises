def Pal(str, i): 
        
        if i==len(str)//2: return True;
        if str[i] != str[len(str)-1-i]: return False;
        return Pal(str, i+1);

print(Pal('radar', 0))
print(Pal('truthly', 0))
print(Pal('letter', 0))