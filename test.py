import scTDA
import json
import matplotlib_venn
import networkx
import numexpr
import numpy
import numpy.linalg
import numpy.random
import pandas
import pickle
import pylab
import requests
import sakmapper
import scipy.cluster.hierarchy as sch
import scipy.interpolate
import scipy.optimize
import scipy.signal
import scipy.spatial.distance
import scipy.stats
import sklearn.cluster
import sklearn.metrics.pairwise
from mpl_toolkits.mplot3d import Axes3D
import warnings
import gzip
# warnings.filterwarnings("ignore")
# pylab.rcParams["patch.force_edgecolor"] = True
# pylab.rcParams['patch.facecolor'] = 'k'
#
#
date_list = []
with open('Macs_timepoints.txt','r') as f:
    for l in f:
        date_list.append(l)
print len(date_list)
idx = 0
with gzip.open('Macs_scaledata.txt.gz','rb') as f:
    for l in f:
        idx += 1
print idx
def formatFile(filename):
    firstline = True
    cid = 1
    rpfl = "GENE\t"
    t = filename.split(".")[0]
    with open(filename, 'r') as f:
        for line in f:
            for gene in line.split('\t')[1:]:
                rpfl += str(cid)
                rpfl += "\t"
                cid += 1
            rpfl = rpfl[:-1] + "\n"
            break
    with open(filename, 'r') as input_file, open(t + "_modified.txt", 'w') as output_file:
        for line in input_file:
            if firstline:
                output_file.write(rpfl)
                firstline = False
            else:
                output_file.write(line)
    return cid - 1, t + "_modified.txt"
count, fn = formatFile("MH1.DGE.txt")
files = []
cells = count
libs = []
days = []
for i in range(3):
    files.append(fn)
    libs.append("A")
    days.append(1)
#
p = scTDA.Preprocess(files, days, libs, cells)
p.show_statistics()
# p.subsample(1491)
# p.fit_sigmoid()
# p.select_genes(avg_counts=2.0, min_z=3.0)
#
# p.save('MH1')



