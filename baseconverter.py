# chuyển hệ cơ số từ thập phân sang hệ cơ số 2 đến 16
def convert_number(n, b):
    if ((n < 0 or n > 1000000) or (b < 2 or b > 16)):
        return "Invalid"
    elif (n==0):
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
                sb = sb + str(m)
        else:
            sb = sb + str(remainder % b)
        remainder = int(remainder / b)
    return "".join(reversed(sb))

if __name__ == "__main__":
    print(convert_number(3, 8))
    print(convert_number(22, 12))
    print(convert_number(11, 12))