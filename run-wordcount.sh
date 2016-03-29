#!/bin/bash
topic_dir="example_data" #directory containing topics and intruder word text files
ti_path="../topic_interpretability/" #path to topic_interpretability repository
ref_corpus="../topic_interpretability/ref_corpus/wiki/" #large external corpus for collecting word statistics
output_dir="example_results" #directory to put generated files

#create output_dir
if [ ! -d $output_dir ]
then
    mkdir -p $output_dir
fi

#aggregate all the topic words
cat $topic_dir/*.topics-with-intruder.txt > $output_dir/all_topics.txt

#collect word statistics
python $ti_path/ComputeWordCount.py $output_dir/all_topics.txt $ref_corpus > $output_dir/wordcount.txt
