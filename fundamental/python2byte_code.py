a = 10
b = 20
c = a+b
print(c)


"""

python -m dis python2byte_code.py

  1           0 LOAD_CONST               0 (10)
              2 STORE_NAME               0 (a)

  2           4 LOAD_CONST               1 (20)
              6 STORE_NAME               1 (b)

  3           8 LOAD_NAME                0 (a)
             10 LOAD_NAME                1 (b)
             12 BINARY_ADD
             14 STORE_NAME               2 (c)

  4          16 LOAD_NAME                3 (print)
             18 LOAD_NAME                2 (c)
             20 CALL_FUNCTION            1
             22 POP_TOP
             24 LOAD_CONST               2 (None)
             26 RETURN_VALUE

"""