#!/bin/bash

#script that computes the observed coherence (pointwise mutual information, normalised pmi or log 
#conditional probability)
#steps:
#1. sample the word counts of the topic words based on the reference corpus
#2. compute the observed coherence using the chosen metric

#parameters
#input
topic_dir="example_data/"
wordcount_file="example_results/wordcount.txt"
#pickle output
output_pickle="example_results/npmi.pickle"

#clear any previously pickled results
rm -rf $output_pickle 2>/dev/null

#compute npmi for top-5/10/15/20
for x in `seq 5 5 20`
do
    #compute the topic observed coherence (npmi)
    echo "Computing NPMI for top-N = $x..."
    python ComputeObservedCoherence.py $topic_dir/${x}.topics.txt \
        npmi $wordcount_file -t $x -p $output_pickle > /dev/null
done

#print aggregate results
python PrintResults.py $output_pickle $topic_dir/20.topics.txt
