# Before running anythin code, use following commend to activate the environment

source scTDA/bin/activate

1.
make sure the data file is in good format. Rows should be cells and cols should
be Genes.
the date file should have same number of lines as the number of cells provided
in matrix file.
2.
Access the Jupyter through your computer by following the instruction given
at the end of file. 
3.
Create a new notebook, type in the following the beginning to set up:
%matplotlib inline
%pylab inline
import scTDA
import file_modifier
import random
4. Call file_modifier.generate_rooted_graph(<output_file_name>,<data_file_name>,<date_file_name>)
this will give you a rooted graph object defined in scTDA.py
The you can use this object to do analysis. For more information about this part, go see scTDA doc.
5. After you call RootGraph.save(), a file named xxx.genes.tsv is generated. To
get this file sorted by q value, call file_modifier.sortqval(<file_name>), this
will generate a sorted file with name sorted_<file_name>

For remote access through jupyter: 
http://amber-md.github.io/pytraj/latest/tutorials/remote_jupyter_notebook
