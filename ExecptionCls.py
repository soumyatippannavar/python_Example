
class excpetion:
    a = int(input("enter 1st number:"))
    b = int(input("enter 2nd number :"))

    try:

       s = a/b
       print(s)

    except Exception as e:
        print("dont enter zero exception is:", e)
    finally:
        print("exit  the block")



