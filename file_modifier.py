import sys
import gzip
import scTDA
import os
import pandas
def modify_input_file( output, fname,date_f):
    """
    :param output: the name of output file
    :param fname: the matrix file name, which should be .gz type
    each line is separated by \n and each word is separated by \t
    :param date_f: the date list file name, which should be .txt type
    each line is a date corresponding to each row in matrix file, and
    each line should be a date(integer) followed by \n
    :return:
    """

    # used to keep track of cell id in dict
    unique_cell_id = 0
    date_list = []
    with open(date_f,'r') as f:
        for l in f:
            date_list.append(l[:-1])
    cell_dict = {}
    first = True
    with open(output + ".all.tsv", "w") as o1, open(output + ".mapper.tsv", "w") as o2:
        with gzip.open(fname, "rb") as f:
            idx = 0
            for line in f:
                line = line.split("\t")
                # Build up first line, name for each col
                first_word = True
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
                else:
                # Build the following row
                    for word in line:
                        if first_word:
                            p2 = ""
                            first_word = False
                            if word not in cell_dict:
                                cell_dict[word] = unique_cell_id
                                unique_cell_id += 1

                            p = 'D' + str(date_list[idx]) + '_' + word + '_' + str(cell_dict[word]) + '\t' + str(date_list[idx]) \
                                + '\t' + 'A' + '\t'
                        else:
                            p += word
                            p += "\t"
                            p2 += word
                            p2 += "\t"
                    o1.write(p[:-1]+ "\n")
                    o2.write(p2[:-1] + "\n")
                    idx += 1

def generate_rooted_graph(output, fname,date_list):
    """
       :param output: the name of output file
       :param fname: the matrix file name, which should be .gz type
       each line is separated by \n and each word is separated by \t
       :param date_f: the date list file name, which should be .txt type
       each line is a date corresponding to each row in matrix file, and
       each line should be a date(integer) followed by \n
       :return: a rooted graph defined in scTDA
       """
    # hide intermediate files and processes from user
    modify_input_file(output,fname,date_list)
    t = scTDA.TopologicalRepresentation(output, lens='pca', metric='euclidean')
    t.save(output, 25, 0.4)
    c = scTDA.RootedGraph(output, output + '.all.tsv', groups=False)
    os.remove(output + '.all.tsv')
    os.remove(output + '.mapper.tsv')
    os.remove(output + '.json')
    os.remove(output + '.gexf')
    os.remove(output + '.posg')
    os.remove(output + '.posgl')
    return c

def draw_graphs(c, genes):
    """
    :param c: a root graph object defined in scTDA
    :param genes: genes is a list of gene names(string)
    :return: nothing, just draw the graph
    """
    # a wrapper to draw several graphs
    for gene in genes:
        c.draw(gene)
def sortqval(filename):
    """
    :param filename: a full file name in format xxx.genes.tsv
    :return:
    """
    pd = pandas.read_table(filename)
    pd = pd.sort_values('q-value (BH)')
    pd.to_csv('sorted_' + filename, sep = '\t',index=False)



