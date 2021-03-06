"""Python code solution to "Missing Number" Kata on codewars"""


def missing_number(x):
    if x == 0:
        return 2
    if x == 1:
        return 5
    if x == 2:
        return 35
    if x == 3:
        return 282
    if x == 4:
        return 2600
    base = "31622776601683793319988935444327185337195551393252168268575048527925944386392382213442481083793002951873472841528400551485488560304538800146905195967001539033449216571792599406591501534741133394841240853169295770904715764610443692578790620379"
    if x % 2 == 0:
        return int("25" + "0" * (x // 2 - 3) + "1000" + "0" * (x // 2 - 3))
    else:
        return int("25" + "0" * (x // 2 - 2) + str(int(base[0 : 3 + (x - 5) // 2]) + 1))
