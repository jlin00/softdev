__name__ = "__main__"

if __name__ == "__main__":
    print("script1 is the main fxn")


'''
    Conclusions:
        - whatever file you are running in the terminal is the main
            - e.g. python3 script1 --> script1's name is called __main__
        - the module imported is not called the main, it is called by the filename
            - e.g. inside script2.py -->
                import script1
                print("script1's name is: %s" % script1.__name__) --> will print out script1
        - if the file is the main, all the code written in there will be executed
            - e.g. inside script1.py -->
                __name__ = "__main__"
                print("this is the main fxn") --> this will be printed
        - you can designate multiple files to be the main
            - e.g you can set the name manually in a file by declaring at the top
                __name__ = "__main__"
            - if I declare the above in script1 and I run script2 in the terminal, both will be considered the main
            - however, this is probably not good practice

'''
