import timeit
for i in range(10000, 1000000, 20000): 
    set_dict = timeit.Timer("x[(random.randrange(%d))]"%i, 
                            "from __main__ import random, x") 
    
    get_dict = timeit.Timer("x.get(random.randrange(%d))"%i, 
                            "from __main__ import random, x") 

    x = {j:None for j in range(i)} 

    set_time = set_dict.timeit(number=1000) 
    get_time = get_dict.timeit(number=1000) 
    print("%d, %10.4f, %10.4f" % (i, get_time, set_time)) 