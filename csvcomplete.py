# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 10:29:18 2016

@author: Brett Barbaro
"""

# -*- coding: utf-8 -*-

import csv  # for dealing with .csv files
import urllib  # for getting stuff off the web

# GOAL: input a csv file containing accession numbers
# output: csv file with accession #s and sequences

print "hello"

# import random  # only for color assignments
# import math
# import numpy
# import json

# import data from csv file - Brett
f = "/Users/mac/Documents/OLSON/Programs/csvcomplete/syn1.0_cut.csv"
all_data = []
# cell_radius = 0.15  # um
# cell_density = 1.07  # g/cc
# protein_content_fraction = 0.163  # 155.0/950.0#0.163#by weight
# cell_volume = 4.0 * math.pi * (math.pow(cell_radius, 3.0) / 3.0)  # cu um
# cell_mass = cell_volume * cell_density * math.pow(10, -12)  # g
# protein_mass = cell_mass * protein_content_fraction  # g
# total_I = [0, 0, 0, 0]
# col_id = [0, 1]
# total = [total_I, total_IBAQ, total_LFQ]
# oneMol = [total_I, total_IBAQ, total_LFQ]

with open(f, 'rU') as csvfile:  # need to open the file in Universal mode so it can read Mac Excel output .csv
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        all_data.append(row)


# fill in missing data
#   Ingredients from proteomics:
#     Needs name (the name in the data you have)
#     Needs unique ID e.g. uniprot or ncbi (synthetic cell or http://wholecelldb.stanford.edu)
#     Needs the copy number of concentration (e.g. from mass spec, or http://wholecelldb.stanford.edu/ or
#     david estimation from his painting...)
#     Fetch the sequence
#     Fetch or calculate  the molecular weight
#     From sequence retrieve a template from the PDB. Keep e-value and score…
#     Retrieve the multimer states for the structure using the PDB (biological assembly).
#     From sequence retrieve the localisation if unknow (e.g. cytoplasm, membrane etc,...)
#       http://www.ncbi.nlm.nih.gov/CBBresearch/Lu/subcellular/
#       http://www.imtech.res.in/raghava/pslpred/
#
#     From sequence and template from the PDB build an homology model (e.g. MODELLER or server license for MODELLER is
#     MODELAJE in upper case)
#     If localisation is inner/outer membrane predict/retrieve the orientation of the structure using
#     http://opm.phar.umich.edu
#     Once a structure is known,
#       Load and center the atoms to the origin
#       apply k-means clustering based on number of atoms.
#       Generate a coarse molecular surface and save it as collada 1.4
#     Generate a recipe file in json.
#
#     Note:
#     http://wholecellkb.stanford.edu/list/Mgenitalium/ProteinComplex contains the mutlimeric states of all
#     proteins from mycoplasma genitalium. All entry are defined according the gene name (MG_001->MG_526).
#     However for each gene there is a link to the uniprort.
#     Example code are in the github repo of autopack in the script folder
#     For ncbi access the fasta sequence can be done with
#     http://www.ncbi.nlm.nih.gov/protein/ADH22250.1?report=fasta&log$=seqview&format=text#

urllibrary = 'http://www.ncbi.nlm.nih.gov/protein/ADH21625.1?report=fasta&log$=seqview&format=Excel#'
for row in range(1):
    response = urllib.urlopen(urllibrary)
    print response.read()
# print response.read()
#    response.close()
#    print "Response:", response
#
#    # Get the URL. This gets the real URL. 
#    print "The URL is: ", response.geturl()
#    
#    # Getting the code
#    print "This gets the code: ", response.code
#    
#    # Get the Headers. 
#    # This returns a dictionary-like object that describes the page fetched, 
#    # particularly the headers sent by the server
#    print "The Headers are: ", response.info()
#    
#    # Get the date part of the header
#    print "The Date is: ", response.info()['date']
#    
#    # Get the server part of the header
#    print "The Server is: ", response.info()['server']
#    
#    # Get all data
#    html = response.read()
#    print "Get all data: ", html
#    
#    # Get only the length
#    print "Get the length :", len(html)
#    
#    # Showing that the file object is iterable
#    for line in response:
#     print line.rstrip()
#    
#    # Note that the rstrip strips the trailing newlines and carriage returns before
#    # printing the output.

print "data length " + str(len(all_data))
print "rows? " + str(len(all_data))
print "columns? " + str(len(all_data[0]))

with open('output.csv', 'wb') as csvfile:  # writes output.csv file with all_data
    spamwriter = csv.writer(csvfile)
    for row in range(len(all_data)):
        spamwriter.writerow(all_data[row])

print"done"
