import random


def Lotto(n):
    def LottoRandom(n):
        i = 0
        while i < n:
            a = random.randint(1, 35)
            b = random.randint(1, 35)
            c = random.randint(1, 35)
            d = random.randint(1, 35)
            e = random.randint(1, 35)
            f = random.randint(1, 12)
            g = random.randint(1, 12)
            res = [a,b,c,d,e,f,g]
            i += 1
            if i == n and len(set(res)) == 7:
                return res
            else:
                continue
    s = LottoRandom(n)
    if s == None:
        return "再试一次"
    else:
        return s
print(Lotto(202188))
