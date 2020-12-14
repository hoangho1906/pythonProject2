units = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín", "mười"]
big_units = ["nghìn", "triệu", "tỷ", "nghìn tỷ", "triệu tỷ", "tỷ tỷ"]


def main():
    num = input("Enter an amount ")
    abc = from_1_to_999(num)
    print(abc)


if __name__ == "__main__":
    main()


def from_1_to_999(n):
    # t(trăm) c(chục) d(đơn vị)
    # convert to int since default data type is float
    d = n % 10  # đơn vị
    c = (n % 100 - d) / 10  # chục
    t = ((n % 1000) - 10 * c - d) / 100  # trăm
    hundered = ""
    if t != 0 and c == 0 and d == 0:  # eg: 400
        hundered = units[t] + " trăm "
    elif t != 0 and c == 0 and d != 0:  # eg: 405
        hundered = units[t] + " trăm linh " + units[d]
    elif t != 0 and c > 1 and d == 0:  # eg: 450
        hundered = units[t] + " trăm " + units[c] + " mươi"
    elif t != 0 and c == 1:  # eg: 130
        hundered = units[t] + " trăm mười " + units[d]
    elif t == 0 and c > 1:  # eg: 45
        hundered = units[c] + " mươi " + units[d]
    elif t == 0 and c == 1:  # eg: 19
        hundered = "mười " + units[d]
    elif t != 0 and c != 0 and d != 0:  # eg: 119
        hundered = units[t] + " trăm " + units[c] + " mươi " + units[d]
    else:  # eg: 6
        hundered = units[d]
    return hundered

    # length / 3 => find ceiling and floor


def money_to_words(num):
    f = 1000
    e = 1000000
    d = 1000000000
    c = 1000000000000
    b = 1000000000000000
    a = 1000000000000000000
    if num == 0:
        return ""
    else:

        hundereds = int(num % f)
        thousands = int(((num % e) - hundereds) / f)
        millions = int(((num % d) - f * thousands - hundereds) / e)
        billions = int(((num % c) - e * millions - f * thousands - hundereds) / d)
        trillions = int(((num % b) - d * billions - e * millions - f * thousands - hundereds) / c)
        quadrillions = int(((num % a) - c * trillions - d * billions - e * millions - f * thousands - hundereds) / b)

        list = [quadrillions:"", trillions, billions, millions, thousands: " nghìn ", hundereds: "trăm"]

        # set name for elements
        quad = from_1_to_999(quadrillions)
        tri = from_1_to_999(trillions)
        bi = from_1_to_999(billions)
        mi = from_1_to_999(millions)
        thou = from_1_to_999(thousands)
        hun = from_1_to_999(hundereds)

        # merge
        words = quad + tri + bi + mi + thou + hun
        if hun == 0:
            return words + " đồng chẵn"
        else:
            return words