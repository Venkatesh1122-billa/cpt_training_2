# raise [exception [,args[,traceback]]]
# try:
   # num= 11
   # print(num)
   # raise ValueError
# except:
   # print("Exception Occured")
   # Traceback(Most recent calls)


# try:
   # raise NameError
# except:
   # print("Re-raising the exception")
   # raise

try:
    print("Raising Exception")
    raise ValueError
except:
    print("Exception caught....")
finally:
    print("performing clean-up in finally")