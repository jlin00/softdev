import script1

if __name__ == "__main__":
    print("script1 is called: %s" % script1.__name__)
    print("script2 is the main fxn")
    print("script2 is called: %s" % __name__)
else:
    print("this is not the main")
