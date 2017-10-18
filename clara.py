# clara=int(input("What's your number?\n"))
# print(clara)

while True:
    try:
        number = int(input("What's your fav number?\n"))
        print((18 / number))
        break
    except ValueError:
        print("Make Sure and enter a number")
    except:
        break
    finally:
        print("loop complete")
