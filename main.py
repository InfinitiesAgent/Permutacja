def permute(original, func):
    out = []
    for i in range(len(original)):
        out.append(func[original[i] - 1])
    return out


while True:
    func = input("Permutation\n").split()

    try:
        for i in range(len(func)):
            func[i] = int(func[i])
    except:
        print("Not an array of numbers")
        continue

    e = False
    for i in func:
        if i > len(func) or i <= 0:
            print("Not a function")
            e = True
            break
    if e:
        continue

    found = []
    for i in func:
        if not i in found:
            found.append(i)
        else:
            print("Not an injection")
            e = True
            break
    if e:
        continue
    
    while True:
        print("\n\nInput", func)

        current = []
        orig = []
        inv = []
        for i in range(len(func)):
            current.append(i + 1)
            orig.append(i + 1)
            inv.append(i + 1)
        
        r = 0
        b = True
        while b or current != orig:
            b = False
            current = permute(current, func)
            r += 1
        print("Rank", r)
        
        for i in range(r - 1):
            inv = permute(inv, func)
        print("Inverse", inv, "\n")

        try:
            p = int(input("Powers to compute\n"))
        except:
            print("Not a number")
            continue

        if p > 0:
            for i in range(p):
                current = permute(current, func)
                print(i + 1, current)
        if p < 0:
            for i in range(-p):
                current = permute(-(i + 1), current, inv)
    
        a = input("\nContinue? (y/n)\n")
        if a == 'y':
            continue
        if a == 'n':
            break
        print("Unexpected input")
        break
    a = input("\nExit? (y/n)\n")
    if a == 'y':
        break
    if a == 'n':
        print("\n")
        continue
    print("Unexpected input")
    break
