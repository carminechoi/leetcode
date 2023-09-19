class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fib(n-1) + self.fib(n-2)



# f(0) = 0
# f(1) = 1
# f(2) = f(1) + f(0)
# f(3) = f(2) + f(1)
#        (f(1) + f(0)) + f(1)