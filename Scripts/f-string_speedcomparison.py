from timeit import default_timer as timer

a = 765903.094095
b = 5.98509348

# % method
start = timer()
string_1 = "the answer is %.4e" %a**b
print(string_1)
stop = timer()
print(stop - start)

# format method
start = timer()
string_2 = "the answer is {:.4e}".format(a**b)
print(string_2)
stop = timer()
print(stop - start)

# f string method
start = timer()
string_3 = f"the answer is {a**b:.4e}"
print(string_3)
stop = timer()
print(stop - start)


'''Usually we can see that f string is faster than format that is in turn faster than % but as the f string involves
 additional parsing overhead, so .format() optimizes certain operations better in this specific case'''

