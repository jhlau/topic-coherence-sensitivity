"""
Author:         Jey Han Lau
Date:           Oct 2015
"""

import argparse
import sys
from collections import defaultdict
import os.path
import cPickle
import codecs

#parser arguments
desc = "Computes the model precision for the word intrusion task; saves results in a pickle file"
parser = argparse.ArgumentParser(description=desc)

#####################
#positional argument#
#####################
#str positional argument
parser.add_argument("topic_file", help="file that contains the topics")
parser.add_argument("test_data", help="test data input for SVM")
parser.add_argument("predictions_output", help="predictions output from SVM")

parser.add_argument("-p", "--pickle_output", help="save precision results in a pickle")

args = parser.parse_args()

#parameters
debug = True
repeat = 10 #number of times we inject an intruder word into a topic

#input
topic_file = codecs.open(args.topic_file, "r", "utf-8")
test_file = codecs.open(args.test_data, "r", "utf-8")
predictions_file = codecs.open(args.predictions_output, "r", "utf-8")

#global variables
prediction_scores = []
qid_line_id = defaultdict(list) #which lines for which qid
line_id_word = defaultdict(str) #map from line id to words in test.dat
qid_tw = defaultdict(list) #topic words for each qid
topic_precision = {} #precision for each topic; value = ( [num_intruder], [precision] )

###########
#functions#
###########


######
#main#
######
#use utf-8 for stdout
sys.stdout = codecs.getwriter('utf-8')(sys.stdout)

#process prediction file
for line in predictions_file:
    prediction_scores.append(float(line.strip()))

#process the test file
for (line_id, line) in enumerate(test_file):
    qid = int(line.strip().split()[1].split(":")[1])
    qid_line_id[qid].append(line_id)
    line_id_word[line_id] = line.strip().split()[-1][1:] #remove hash in front

#process the topic file
for (line_id, line) in enumerate(topic_file):
    qid_tw[line_id + 1] = line.strip().split()

#open pickle if it exists
if args.pickle_output != None and os.path.isfile(args.pickle_output):
    topic_precision = cPickle.load(open(args.pickle_output))

#compute the model precision for each topic (binary in this case, 1 or 0)
topic_id = 0
i = 0
p = 0.0
for (qid, line_ids) in sorted(qid_line_id.items()):
    actual_ww_score = prediction_scores[line_ids[0]]
    hit = 1.0
    ww_id = line_ids[0]
    for line_id in line_ids[1:]:
        if prediction_scores[line_id] > actual_ww_score:
            actual_ww_score = prediction_scores[line_id]
            hit = 0.0
            ww_id = line_id
    
    if debug:
        print ("[%.1f]" % hit), " ".join(qid_tw[qid])
        print "\tSystem Chosen Intruder Word =", line_id_word[ww_id]
        print "\tTrue Intruder Word =", line_id_word[line_ids[0]]
        print
    else:
        print hit

    p += hit
    if i == (repeat-1):
        p = float(p) / float(repeat)
        num_tw = len(qid_tw[qid]) - 1
        if topic_id not in topic_precision:
            topic_precision[topic_id] = ([], [])
        topic_precision[topic_id][0].append(num_tw)
        topic_precision[topic_id][1].append(p)
        i = 0
        p = 0.0
        topic_id += 1
    else:
        i += 1

if args.pickle_output != None:
    cPickle.dump(topic_precision, open(args.pickle_output, "w"))
