def fibonacci_generator():
    #pass #this is a null statement which does nothing when executed, useful as a placeholder.
	next, fib = 0,1
    #fib = 1
    #second = 1

    while True:

        #if second == 1:

        #    yield fib
            yield fib

         #   second += 1
            
            
        #else:
            
            #fib = fib + second
            #fib += second
            fib, second = second, fib + second

            #yield fib

def fibonacci(N):
    counter = 0
    
    for n in fibonacci_generator():
        print n
        counter += 1
        if counter == N:
            break
i = input("Enter the how many Fibonacci numbers to calculate: ")
fibonacci(i)