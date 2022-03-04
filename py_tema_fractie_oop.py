def hcf(a, b):  # Define the highest common factor (euclid algorithm)
    if a == 0:
        return b
    else:
        return hcf(b % a, a)


class Fraction:

    # constructor
    def __init__(self, numerator, denominator):
        gcd = hcf(numerator, denominator)  # Greatest common denominator
        self.top_num = numerator // gcd  # Divide the numerator and denominator to the greatest common denominator
        self.bottom_den = denominator // gcd  # Use // to obtain integer number instead of the real number

    def __str__(self):
        if self.bottom_den == 1:  # If the denominator is 1, then we will display the numerator, otherwise display the fraction
            return str(self.top_num)
        else:
            return str(self.top_num) + "/" + str(self.bottom_den)

    def __add__(self, other):  # other receives the numerator and denominator from the second fraction
        new_top_num = self.top_num * other.bottom_den + other.top_num * self.bottom_den
        new_bottom_den = self.bottom_den * other.bottom_den
        return Fraction(new_top_num, new_bottom_den)

    def __sub__(self, other):
        new_top_num = self.top_num * other.bottom_den - other.top_num * self.bottom_den
        new_bottom_den = self.bottom_den * other.bottom_den
        return Fraction(new_top_num, new_bottom_den)

    def inverse(self):
        return Fraction(self.bottom_den, self.top_num)

print('\r\n----- Tests 1:')

print(hcf(15, 21))
x = Fraction(15, 21)
print(x)
print(x.__add__(Fraction(5, 7)))
print(Fraction(3, 4).__add__(Fraction(1, 2)))
print(x + Fraction(2, 7))
print(Fraction(3, 4) + Fraction(1, 2))
print(Fraction(1, 2) - Fraction(3, 7))
print(Fraction(1, 4) - Fraction(1, 2))
print(x.inverse())

print('\r\n----- Tests 2:')

fra1 = Fraction(3, 5)
fra2 = Fraction(8, 7)
print(f'Fractii: {fra1}, {fra2}')
print(f'Add: {fra1 + fra2}')
print(f'Sub: {fra1 - fra2}')
print(f'Inverse: {fra1.inverse()}, {fra2.inverse()}')

