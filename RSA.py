def main():
    message = [37,39,29]
    print(decrypt_message(7,11,17,message))
    #print(modular_large_number(667, 937, 2537))


def decrypt_message(p,q,e, encrypted_message):
    n = p*q
    z = (p-1)*(q-1)
    public_key = [n,e]
    #print(public_key)
    d = calculate_modular(n,1,z)
    #print(d)
    private_key = [n, d]
    #print(private_key)
    decrypted_message = ""
    for c in encrypted_message:
        m = modular_large_number(c,d,n)
        print(m)
        decrypted_message += chr(m)
        print(m)
    return decrypted_message


def calculate_modular(a,b,n):
    mod = n
    p = []
    x =[]
    p.append(0)
    p.append(1)
    quotient = []
    remainder = []

    #print('p0 = ', p[0])
    #print('p1 = ', p[1])


    while n%a != 0:
        q = n//a
        #print(q)
        r = n%a
        n= a
        a = r
        quotient.append(q)
        remainder.append(r)
    for i in range(len(quotient)):
        p.append(p[i+2-2] - p[i+2-1]*quotient[i])
        while p[i+2] < 0:
            p[i+2] = p[i+2] + mod
        while p[i+2] > mod:
            p[i+2] = p[i+2] - mod
        #print('p', i, ' = ', p[i+2-2], '-', p[i+2-1], '*', quotient[i], ' mod ', mod,  ' = ',p[i+2] )
    t = p[len(p)-1]
    return t
    if b > 1:
        d = remainder[len(remainder)-1]
        x.append((p[len(p)-1]*b)//d)
        while x[0] < 0:
            x[0] = x[0] + mod
        while x[0] > mod:
            x[0] = x[0] - mod
        i = -1
        while (x[0] + i*(mod//d)) < mod and (x[0]+i*(mod//d) > 0):
            x.append(x[0] + i*(mod//d))
            i -= 1
        x.sort()
        #print('x = ', x)
    #print('---------------------------------------------------------')


def modular_large_number(a, b, n):
    b_binary = bin(b)
    binary = b_binary[2:]
    list_binary = []
    list_index = []
    list_mod = []
    #print(binary)
    for i in binary:
        list_binary.append(i)
    list_binary.reverse()
        # print(list_binary)
    for j in range(len(list_binary)):
        if int(list_binary[j]) == 1:
            # print(list_binary[j])
            list_index.append(j)
            # print(list_index)
    mod = cal_mod(a, n)
    #print(mod)
    for i in range(len(list_binary)):
        mod = cal_mod(mod, n)
        list_mod.append(mod)
        # print(mod)
        mod = pow(mod, 2)
        # print(list_mod)
    result = 1
    for i in range(len(list_mod)):
        if i in list_index:
            result = int(result * list_mod[i])
    return cal_mod(result, n)


def cal_mod(a, b):
        return a % b


main()
