def readFile(filename):
    lines = open(filename).readlines()

    # First line is the column titles
    col_names = lines[0].strip().split('\t')[1:]
    row_names = []
    data = []
    for line in lines[1:]:
        p = line.strip().split('\t')

        # First column in each row is the row name
        row_names.append(p[0])

        # The data for this row is the remainder of the row
        data.append([float(x) for x in p[1:]])
    return row_names, col_names, data