class Test():
    def public_func(self):
        print("Публичный метод")

    def _protected_func(self):
        print("Защищенный метод")


    def __private_func(self):
     print("Приватный метод")

    def test_private(self):
        self.__private_func()

test = Test()
test.public_func()
test._protected_func()
test.test_private()



