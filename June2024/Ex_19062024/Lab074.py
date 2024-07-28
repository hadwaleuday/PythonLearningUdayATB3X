numbers = [1, 2, 3]


# Collecion of Items

def do_something(uday_list):
    uday_list.append(100)
    uday_list[0] = 123
    return uday_list


def shanti():
    print("dasda")


shanti()
l = do_something(uday_list=numbers)
print(l)
