def even_odd(number):
    if number != 0:
        if number % 2 == 0:
            print("even")
        else:
            print("odd")
    else:
        print("zero is not even or odd")

if __name__=="__main__":
    even_odd(6)