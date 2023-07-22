# N ** 2
def str_counter(s):
    for sym in s:
        counter = 0
        for sub_sym in s:
            if sym == sub_sym:
                counter += 1

        print(sym, counter)

#str_counter("Привет меня зовут Ярослав.")

# M * N


def str_counter_2(s):
    for sym in set(s):
        counter = 0
        for sub_sym in s:
            if sym == sub_sym:
                counter += 1

        print(sym, counter)


# str_counter_2("aaaaaaaaaavvvvvvvvvvnbbbbbnggggggggg")

# N
def str_counter_3(s):
    syms_counter = {}
    for sym in s:
        syms_counter[sym] = syms_counter.get(sym, 0) + 1

    for sym, count in syms_counter.items():
        print(sym, count)

str_counter_3("l;kmf;sklfmg;slgmfsaf';skm'g;ksam;")