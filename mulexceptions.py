try :

  num1 = int(input("enter a number: "))
  num2 = int(input("enter a number: "))
  result = num1/num2
  print("result is :", result)
  print("result is :", result)


except ZeroDivisionError:
      print("division by zero in error")
except ValueError:
    print("enter numeric value")
except NameError as ex:
    print("Exception is ", ex)
except:
    print("some error occured")
finally:
    print("I will execute")