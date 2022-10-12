# chuyển hệ cơ số từ thập phân sang hệ cơ số 2 đến 16
def convert_number(n, b):
    if (n < 0 or n > 1000000):
        if (b < 2 or b > 16):
            return "Invalid number and base"
        return "Invalid number"
    if (b < 2 or b > 16):
        return "Invalid base"
    if (n == 0):
        return "0"

    sb = "";
    m = 0;
    remainder = n;
  
    while (remainder > 0):
        if (b > 10):
            m = remainder % b;
            if (m >= 10):
                sb = sb + str(chr(55 + m));
            else:
                sb = sb + str(m);
        else:
            sb = sb + str(remainder % b);
        remainder = int(remainder / b);
    return "".join(reversed(sb));
  
if __name__ == "__main__":
    print(convert_number(-1, 16))
    print(convert_number(0, 16))
    print(convert_number(1, 16))
    print(convert_number(500000, 16))
    print(convert_number(999999, 16))
    print(convert_number(1000000, 16))
    print(convert_number(1000001, 16))