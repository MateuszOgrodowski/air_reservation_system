class A(object):
    def __init__(self, magic):
        self.magic = magic

    def do_smth(self, amount):
        print(f'do_smth from {type(self).__name__}, A, {amount}')


class B(A):
    def do_smth(self):
        print(f'do_smth from {type(self).__name__}, B')
        super().do_smth(666)


class C(B):
    def do_smth(self):
        print(f'do_smth from {type(self).__name__}, C')
        super().do_smth()


class X(B):
    def __init__(self, magic, text):
        self.text = text
        super().__init__(magic)

    # def do_smth(self):
    #     print(f'do_smth from {type(self).__name__}')


x = X(42, 'ala')
# print(X.__mro__)
# x.do_smth()
# print(x.magic)
# print(x.text)
# print(x)
print(dir(X))
print(vars(x))
# print(X.__base__)
# print(X.__mro__)
# print(dir(object))

# print(dir('ala ma kota'))