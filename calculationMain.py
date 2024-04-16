
# from calculation.addition import add1, add2
from calculation.subtraction import sub1, sub2

import calculation.addition as addition
# import calculation.subtraction as subtraction

if __name__ == "__main__":
    result1 = addition.add1(10,20)  # import로 했을 때
    result2 = sub1(50,20)   # from으로 했을 때
    print(result1)
    print(result2)