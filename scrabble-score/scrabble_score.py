def score(word):
    s1=['A','E','I','O','U','L','N','R','S','T']
    s2=['D','G']
    s3=['B','C','M','P']
    s4=['F', 'H', 'V', 'W', 'Y']
    s5=['K']
    s6=['J','X']
    s7=['Q','Z']
    cnt = 0

    for i in word.upper():
        if(i in s1):
            cnt +=1
        if(i in s2):
            cnt +=2
        if(i in s3):
            cnt +=3
        if(i in s4):
            cnt +=4
        if(i in s5):
            cnt +=5
        if(i in s6):
            cnt +=8
        if(i in s7):
            cnt +=10
    return  cnt
        
        
        

print (score("word"))
