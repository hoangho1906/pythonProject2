def int_to_text(num):
    d = {0: 'khong', 1: 'mot', 2: 'hai', 3: 'ba', 4: 'bon', 5: 'nam',
         6: 'sau', 7: 'bay', 8: 'tam', 9: 'chin', 10: 'muoi',
         11: 'muoi mot', 12: 'muoi hai', 13: 'muoi ba', 14: 'muoi bon',
         15: 'muoi lam', 16: 'muoi sau', 17: 'muoi bay', 18: 'muoi tam',
         19: 'muoi chin', 20: 'hai muoi',
         30: 'ba muoi', 40: 'bon muoi', 50: 'nam muoi', 60: 'sau muoi',
         70: 'bay muoi', 80: 'tam muoi', 90: 'chin muoi'}
    k = 1000
    m = k * 1000
    b = m * 1000
    t = b * 1000

    assert (0 <= num)

    if num < 20:
        return d[num]

    if num < 100:
        if num % 10 == 0:
            return d[num]
        else:
            return d[num // 10 * 10] + ' ' + d[num % 10]

    if num < k:
        if num % 100 == 0:
            return d[num // 100] + ' ' + ' tram'
        else:
            return d[num // 100] + ' ' + ' tram ' + int_to_text(num % 100)

    if num < m:
        if num % k == 0:
            return int_to_text(num // k) + ' ' + 'nghin'
        else:
            return int_to_text(num // k) + ' ' + 'nghin ' + int_to_text(num % k)

    if num < b:
        if (num % m) == 0:
            return int_to_text(num // m) + ' ' + 'trieu'
        else:
            return int_to_text(num // m) + ' ' + 'trieu, ' + int_to_text(num % m)

    if num < t:
        if (num % b) == 0:
            return int_to_text(num // b) + ' ' + 'ty'
        else:
            return int_to_text(num // b) + ' ' + 'ty, ' + int_to_text(num % b)

    if num % t == 0:
        return int_to_text(num // t) + ' ' + 'nghin ty'
    else:
        return int_to_text(num // t) + ' ' + 'nghin ty, ' + int_to_text(num % t)


def main():
    print('nhap 1 so: ')
    x = int(input())
    print(int_to_text(x))


if __name__ == '__main__':
    main()
