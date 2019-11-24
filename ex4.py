

if __name__ == '__main__':
    data = {}
    f = open('codes.txt', 'r')
    for line in f:
        if line[2] not in data:
            data[line[2]] = set([])
        data[line[2]].add(line[1])
        data[line[2]].add(line[0])

        if line[1] not in data:
            data[line[1]] = set([])
        data[line[1]].add(line[0])

        if line[0] not in data:
            data[line[0]] = set([])

    res = [0] * len(data)
    for key, value in data.items():
        res[len(value)] = key

    print(res)