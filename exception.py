while True:
    print('hello')
    break

while True:
    try:
        int(input("enter number: "))
        break
    except ValueError:
        print("wrong input entered")
