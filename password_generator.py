import string
import random

if __name__ == "__main__":
    s1 = string.ascii_lowercase

    s2 = string.ascii_uppercase

    s3 = string.digits
    s4 = string.punctuation

    length = int(input("Enter Password Length \n"))
    s = []
    s.extend(s1)
    s.extend(s2)
    s.extend(s3)
    s.extend(s4)
    random.shuffle(s)
    print("".join(s[0:length]))
