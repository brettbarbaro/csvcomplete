# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 10:29:18 2016

@author: Brett Barbaro
"""

# -*- coding: utf-8 -*-

import csv  # for dealing with .csv files
import urllib  # for getting stuff off the web
import os
from HTMLParser import HTMLParser
from Bio import Entrez
Entrez.email = "X@Y.com"

# GOAL: input a csv file containing accession numbers
# output: csv file with accession #s and sequences

print "hello"

# import random  # only for color assignments
# import math
# import numpy
# import json

# import data from csv file - Brett

csvpath = "/Users/mac/Documents/OLSON/Programs/csvcomplete/syn1_0_cut.csv"
head, tail = os.path.split(csvpath)
model_dir = head + '/'
csvname, ext = tail.split('.')
pdbpath = model_dir + 'PDB' + os.sep
all_data = []


class MyHTMLParser(HTMLParser):
    #
    # def __init__(self, html, lookforTag="a", lookforData="[Show]", lookforAttr=None, gatherData=False):
    #     self.lookforTag = lookforTag
    #     self.lookforData = lookforData
    #     self.lookforAttr = lookforAttr
    #     self.gatherData = gatherData
    #     self.tag_stack = False
    #     self.tag_attr = []
    #     self.stored = []
    #     self.stored_attr = []
    #     self.feed(html)

    def print_p_contents(self, html, lookforTag="a", lookforData="[Show]", lookforAttr=None, gatherData=False):
        self.lookforTag = lookforTag
        self.lookforData = lookforData
        self.lookforAttr = lookforAttr
        self.gatherData = gatherData
        self.tag_stack = False
        self.tag_attr = []
        self.stored = []
        self.stored_attr = []
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        if tag == self.lookforTag:
            self.tag_stack = True
            self.tag_attr = []
            # print "Encountered the beginning of a %s tag" % tag
            # print attrs
            if len(attrs):
                if self.lookforAttr is not None:
                    for atr in self.lookforAttr:
                        for attr in attrs:
                            if attr[0] == atr:
                                self.tag_attr.append(attr[1])
                else:
                    self.tag_attr = attrs[0][1]

    def handle_endtag(self, tag):
        self.tag_stack = False
        # self.tag_attr = None
        pass

    #        print "Encountered the end of a %s tag" % tag

    def handle_data(self, data):
        if self.tag_stack:
            if self.lookforData is None:
                if self.gatherData:
                    self.stored.append(data)
                else:
                    if len(self.tag_attr):
                        self.stored.append(self.tag_attr)
            else:
                if data == self.lookforData:
                    # print "Encountered data %s" % data
                    # print self.tag_attr
                    self.stored.append(self.tag_attr)


with open(csvpath, 'rU') as csvfile:  # need to open the file in Universal mode so it can read Mac Excel output .csv
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        all_data.append(row)

headers = {'test': 'headers test works'}
for num in range(len(all_data[0])):
    headers[all_data[0][num]] = num  # This establishes a dictionary with the header names in it.
    # After this, columns can be indicated with e.g. "name = all_data[x][headers['NAME']]".
    # The headers must be correctly labeled.


# acc2seq will take an accession number as input and return the sequence of that molecule

def acc2seq(accession):
    handle = Entrez.efetch(db="protein", id=accession, rettype="fasta")
    response = handle.read()
    header, sequence = response.split(']')
    sequence = sequence.replace('\n', '')
    return header, sequence


# Can also be used instead of Entrez package:
# urllibrary = 'http://www.ncbi.nlm.nih.gov/protein/ADH21625.1?report=fasta&log$=seqview&format=Excel#'
# for row in range(1):
#     response = urllib.urlopen(urllibrary)
#     print response.read()
#


for x in range(1,len(all_data)):
    accession = all_data[x][headers['ACCESSION']]
    header, sequence = acc2seq(accession)
    all_data[x][headers['SEQUENCE']] = sequence


with open(str(model_dir + csvname + '_complete.csv'), 'wb') as csvfile:   # writes output.csv file with all_data
    spamwriter = csv.writer(csvfile)
    for row in range(len(all_data)):
        spamwriter.writerow(all_data[row])


print"done"
