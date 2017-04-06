
def factorial_simple(n):
    if n == 0:
       return 1
    if n < 0:
       return None
    else:
        return n * factorial_simple(n - 1)

		
def factorial(n):
    return reduce(lambda x,y:x*y, [1]+range(1,n+1))

if __name__ == '__main__':
    value = int(input('Enter a number?'))
    print(factorial_simple(value))