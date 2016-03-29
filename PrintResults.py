"""
Stdin:          N/A
Stdout:         N/A
Author:         Jey Han Lau
Date:           Mar 15
"""

import argparse
import sys
import cPickle
import codecs

#parser arguments
desc = "Print topic coherence results"
parser = argparse.ArgumentParser(description=desc)

#####################
#positional argument#
#####################
parser.add_argument("coherence_pickle", help="pickle file generated by run-npmi/wi.sh")
parser.add_argument("topic_file", help="text file containing the topic words")

###################
#optional argument#
###################

args = parser.parse_args()

#parameters


###########
#functions#
###########

######
#main#
######

data = cPickle.load(open(args.coherence_pickle))
topics = [ item.strip() for item in codecs.open(args.topic_file).readlines() ]

for t in sorted(data.keys()):
    print "="*30
    print "Topic =", topics[t]
    for ci, c in enumerate(range(5, 21, 5)):
        print "\tTop", c, "coherence score =", data[t][1][ci]
