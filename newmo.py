import sys
import gzip

def modify_input_file( output, file_list, date_list,lab_list):
    """
    :param file_list: a list of file name
    :param date_list: a list of corresponding dates for files
    :param lab_list: a list of corresponding labs for files
    :return: Nothing, modified file is saved to output
    """
    # used to keep track of cell id in dict
    unique_cell_id = 0
    flist = list(file_list.split(","))
    days = list(date_list.split(","))
    lab = list(lab_list.split(","))
    cell_dict = {}
    first = True
    matrixs = [{} for i in range(len(flist))]
    maxi = 0
    midx = -1
    matrixkeys = [[] for i in range(len(flist)) ]
    for i in range(len(flist)):
        with gzip.open(flist[i], 'rb') as f:
            temp = 0
            fx = True
            for line in f:
                if fx:
                    fx = False
                    continue
                line = line.split("\t")
                matrixs[i][line[0]] = line[1:]
                temp += 1
            matrixkeys[i] = matrixs[i].keys()
            if temp > maxi:
                maxi = temp
                midx = i
    with open(output + ".all.tsv", "w") as o1, open(output + ".mapper.tsv", "w") as o2:
        for i in range(len(flist)):
            with gzip.open(flist[i], 'rb') as f:
                for cellname in matrixs[midx].keys():
                    for line in f:
                        line = line.split("\t")
                        # Build up first line, name for each col
                        if first:
                            first = False
                            p2 = ""
                            p = 'ID\ttimepoint\tlib\t'

                            for word in line:
                                p += str(word)
                                p2 += str(word)
                                p += "\t"
                                p2 += "\t"
                            o1.write(p[:-1] + "\n")
                            o2.write(p2[:-1] + "\n")
                        break

                    # Build the following row
                    cellname = line[0]
                    p2 = ""
                    if cellname not in cell_dict:
                        cell_dict[cellname] = unique_cell_id
                        unique_cell_id += 1
                    p = 'D' + str(days[i]) + '_' + lab[i] + '_' + str(cell_dict[cellname]) + '\t' + str(days[i]) \
                        + '\t' + lab[i] + '\t'
                    if cellname in matrixkeys[i]:
                        for word in line[1:]:

                            p += str(word)[:9]
                            p2 += str(word)[:9]
                            p += "\t"
                            p2 += "\t"
                    else:
                        for word in line[1:]:
                            p += "0.0"
                            p2 += "0.0"
                            p += "\t"
                            p2 += "\t"
                        if cell_dict[cellname] == 0:
                            p += "0.0"
                            p2 += "0.0"
                            p += "\t"
                            p2 += "\t"
                    if len(p.split("\t")) == 1:
                        continue

                    o1.write(p[:-1]+ "\n")
                    o2.write(p2[:-1] + "\n")
if __name__ == "__main__":
    argvs = sys.argv[1:]
    modify_input_file(argvs[0], argvs[1],argvs[2],argvs[3])
