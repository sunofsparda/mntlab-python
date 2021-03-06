# Task 1
# https://www.codewars.com/kata/polynomials-i-string-format


import ast


def calc_pol(pol_str, x = None):
    if x == None: return "There is no value for x"
    res = eval(pol_str)
    if res == 0:
        return "Result = {}, so {} is a root of {}".format(res, x, pol_str)
    return "Result = {}".format(res)
print(calc_pol("5*x+x",0))
print(calc_pol("5*x+x",5))
print(calc_pol("5*x+x"))

# Task 2
# https://www.codewars.com/kata/sum-of-numbers-from-0-to-n


def show_sequence(n):
    if n == 0:
        result = "0=0"
    elif n < 0:
        result = str(n) + "<0"
    else:
        summ = 0
        line = ""
        for i in range(n+1):
            summ += i
            line += str(i) + "+"
        result = line[0:-1] + " = " + str(summ)
    return result
print(show_sequence(5))
print(show_sequence(0))
print(show_sequence(-10))

# Task 3
# https://www.codewars.com/kata/reverser


def reverse(n):
    """Returns n with all digits reversed. Assume positive n."""
    i = str(n)
    return int(i[::-1])

# Task 4
# https://www.codewars.com/kata/plotting-points-on-a-grid


class Grid:
    def __init__(self, width, height):
        self.grid = ""
        self.wid = width
        for _ in range(height):
            self.grid += ("0" * width + "\n")
        self.grid = self.grid[:-1]

    def plot_point(self, x, y):
        mylist = list(self.grid)
        x -= 1
        y -= 1
        mylist[y * (int(self.wid) + 1) + x] = "X"
        self.grid = ''.join(mylist)
        print(self.grid)

    def __repr__(self):
        pass
test1 = Grid(10, 10)
test1.plot_point(8, 5)

# Task 5
# https://www.codewars.com/kata/a-disguised-sequence-i


def fcn (n):
    return 2**n
