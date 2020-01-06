def rotate(text, key):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isalpha() == False):
            result += char

        elif (char.isupper()):
            result += chr((ord(char) + key - 65) % 26 + 65)

        else:
            result += chr((ord(char) + key - 97) % 26 + 97)
    
    return result
rotate("hello",5)    
