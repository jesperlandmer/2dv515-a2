
def readFile(fileName):
    lines = open(fileName).readlines()

    colNames = lines[0].strip().split('\t')[1:]
    rowNames = []
    data = []

    for line in lines:
        p = line.strip().split('\t')
        rowNames.append(p[0])
        data.append(float(x) for x in p)

    return rowNames, colNames, data

print(readFile('blogData.txt'))