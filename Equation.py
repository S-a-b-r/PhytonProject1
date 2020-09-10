import math
class Equation:
    # a * x^2 + b * x + c = 0;
    def lineEquation(self, a, b):
        if a == 0:
            return None
        return [-b / a]

    def squareEquarion(self, a, b, c):
        if a == 0:
            self.lineEquation(b, c)
        D = b ** 2 - 4 * a * c
        if D < 0:#ладно, ладно, шарим за комплексные числа. Только нинадо кубическое уравнение, пожалуйстя)
           D = -D
           return [[-b / (2 * a), math.sqrt(D)/(2 * a)], [-b / (2 * a) , - math.sqrt(D)/(2 * a)]]
        elif D == 0:
            return [-b / 2 / a]
        else:
            return [(-b + math.sqrt(D))/ (2 * a), (-b - math.sqrt(D))/ (2 * a)]

    def equation(self, a , b , c ):
        if(c == None):
            return self.lineEquation(a, b)
        return self.squareEquarion(a, b, c)
