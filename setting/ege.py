def test(N):
    n = bin(N)[2:]
    if n.count("1") % 2 != 0:
        r = n + "11"
    else:
        r = n + "00"
    return int(r, 2)

# space = []
# for i in range(1000):
#     if test(i) > 115:
#        space.append(i)
#     #    space.append(test(i))
# space.sort()
# print(space[0])
    
# def test2(N):
#     n = bin(N)[2:]
#     n = ("0" * abs(len(n) - 8)) + n
#     print(n, end = " ")
#     n = n.replace("1","2")
#     n = n.replace("0",'1')
#     n = n.replace('2','0')    
#     print(n + " " +  str(int(n, 2)))
#     return int(n,2) - N
# i = 1
# while True:
#     if test2(i) == 111:
#         print(i)
#         break
#     else:
#         i += 1


# def test3(N):
#     n = bin(N)[2:]
#     p = n.split("1", 1)
#     return N - int(p[1],2)
    
    
# space = []   
# for i in range(10,1001):
#     if not(test3(i) in space):
#         space.append(test3(i))
# print(len(space))
# print(space)

# def test4(N):
#     n = bin(N)[2:]
#     r = []
#     for i in n:
#         r.append(i)
#     r.reverse()
#     R = ""
#     for i in r:
#         R += i
#     return int(R, 2)

# for i in range(100, 0, -1):
#     if test4(i) == 13:
#         print(i)


# def test5(N):
#     n = bin(N)[2:]
#     zero = n.count("0")
#     one = n.count("1")
#     if one > zero:
#         n += "1"
#     else:
#         n += "0"
#     return int(n, 2)

# for i in range(1, 1000):
#     if test5(i) > 100:
#         print(test5(i))
#         break

# def test6(N):
#     n = bin(N)[2:]
#     if n[-1] == "0":
#         n = "1" + n + "0"
#     else:
#         n = "11" + n + "11"
#     return int(n,2)

# for i in range(1,1000):
#     if test6(i) > 52:
#         print(i)
#         break

def test7(N):
    n = []
    while N > 0:
        n.append( N % 3 )
        N //= 3
    n.reverse()
    
    