import re
def count_words(sentence):
    string = ""
    string =  re.sub("[^\w ']| '|' |'[^\w]|_|'$"," ",sentence).lower().strip().split()
    print (string)

    ans = {}
    for i in string:
        ans[i]=string.count(i)
    return ans

# word = "hello it's a 'complex' problem , : ! it's  complex problem . \n my_spacebar_is_broken"
count_words("one,\ntwo,\n'three'")
