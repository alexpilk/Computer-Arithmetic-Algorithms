
class IncorrectBaseError(Exception):
    pass

class Number:

    def __init__(self, number, base):
        self.number = int(number)
        self.digits = [int(d) for d in number]
        self.base = int(base)
        self.sign = False if self.digits[0] == self.base-1 else True

    def get_complement(self):
        num = [self.base-1 - digit for digit in self.digits]
        num[-1] += 1
        num = [str(d) for d in num]
        return ''.join(num)

    def convert_to_base(self, base, number=None):
        convertString = "0123456789ABCDEF"
        number = self.number if number is None else number
        if number < base:
            return convertString[number]
        else:
            return self.convert_to_base(base, number // base) + convertString[number % base]


    # def __add__(self, other, current_digit=None, result=None, carrie=0):
    #     current_digit = len(self.digits)-1 if current_digit is None else current_digit
    #     result = [] if result is None else result
    #
    #     print(self, other, current_digit, result, carrie)
    #     if carrie == 0 and current_digit < 0:
    #         return result
    #     if self.base != other.base:
    #         raise IncorrectBaseError()
    #     direct_sum = self.digits[current_digit] + other.digits[current_digit] + carrie
    #     new_carrie = 0
    #     while direct_sum > self.base:
    #         new_carrie += 1
    #         direct_sum -= self.base
    #     result = [direct_sum] + result
    #     print(self, other, current_digit, result, new_carrie)
    #     return Number.__add__(self, other, current_digit, result, new_carrie)
    def __repr__(self):
        return '{} number {} in base {}'.format(self.sign, self.number, self.base)


# a = Number('0012', 8)
# print(a)
# print(a.get_complement())
# print(a.convert_to_base(10))
# print(int('8',5))
# # print(a, b)