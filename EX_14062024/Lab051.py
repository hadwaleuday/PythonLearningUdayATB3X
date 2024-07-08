# Break ->  based on condition if will kick you
# out of the loop.
# Pass -> ? pass do nothing  - Skip the code

for rau in range(10): # here range(10) will give 0-9
    if rau == 5 or rau == 8 :
        pass                    # this will skip for 5 and 8 and loop continues
    else:
        print(rau)

