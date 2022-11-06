def dive_pt():
    with open("inputpt1.txt", 'r') as f:
        depth = 0
        horizontal = 0
        lines = f.readlines()
        for line in lines:
            if "forward" in line:
                horizontal += int(line.split(" ")[1])
            if "down" in line:
                depth -= int(line.split(" ")[1])
            if "up" in line:
                depth += int(line.split(" ")[1])
        return abs(depth * horizontal)




print(f'Part one: {dive_pt()}')

