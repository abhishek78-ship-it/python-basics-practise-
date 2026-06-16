while True:
    try:
        x = int(input())
        if x == 1999:
            print("Correct")
            break
        else:
            print("Wrong")
    except EOFError:
        break