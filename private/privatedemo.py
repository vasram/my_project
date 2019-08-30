class TestClass(object):
    def public_method(self):
        print("I am a public method")

    def _single_underscore_method(self):
        print("I am a single-underscore method")

    def __double_underscore_method(self):
        print( "I am a double-underscore method")


#  if __name__ == '__main__':
# obj = TestClass()
# obj.public_method()
# obj._single_underscore_method()
# obj._TestClass__double_underscore_method()