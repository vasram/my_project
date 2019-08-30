from private import privatedemo
obj = privatedemo.TestClass()
obj.public_method()
obj._single_underscore_method()
obj._TestClass__double_underscore_method()
class hideVariable:
    __hiddenVariable=20
    notHiddenVariable=10
    def add(self,a):

        sum=a+self.__hiddenVariable+self.notHiddenVariable
        print(sum) #30+20+10

myobj=hideVariable()
myobj.add(30)
print("it is not hide variable",myobj.notHiddenVariable)

try:
    # here we cannat access private (__variavle ) outside directly  like above but we can do by ._classname__varablename or  ._class__method name
    print("it is hide element ", myobj._hideVariable__hiddenVariable)

except:
    print("Eroor  due to access hide variable outside the classs  ")
