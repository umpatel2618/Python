import re
def response(hey_bob):
    hey_bob = hey_bob.strip()
    if not hey_bob:
        return "Fine. Be that way!"
    if hey_bob.endswith("?"):
        if hey_bob.isupper():
            return "Calm down, I know what I'm doing!"
        else:
            return "Sure."
    if hey_bob.isupper():
        return "Whoa, chill out!"
    return "Whatever."
response("")