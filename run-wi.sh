#!/bin/bash

#script that runs the word intrusion task
#steps:
# generate the svm features (input for svm)
# run svm
# compute the model precision using the system's prediction of intruder words

#parameters
ti_path="../topic_interpretability" #topic_interpretability path
topic_dir="example_data"
svm_dir="example_results/svm" #path to store svm files
wordcount_file="example_results/wordcount.txt"
output_pickle="example_results/wi.pickle"

rm -rf $output_pickle 2>/dev/null

for x in `seq 5 5 20`
do
    echo "Processing top-N = $x..."

    #generate the svm input files
    echo -e "\tGenerating SVM input..."
    rm -rf $svm_dir 2>/dev/null
    mkdir -p $svm_dir
    python $ti_path/GenSVMInput.py $topic_dir/$x.topics-with-intruder.txt \
        $topic_dir/$x.intruder.txt npmi $wordcount_file > $svm_dir/orig.dat

    #split the data into ten partitions (for ten-fold cross validations)
    echo -e "\tSplitting the SVM input ten partitions..."
    python $ti_path/SplitSVM.py $svm_dir < $svm_dir/orig.dat

    #start svm
    echo -e "\tStarting SVM..."
    for i in `seq 0 9`
    do
        $ti_path/svm_rank/svm_rank_learn -c 0.01 $svm_dir/train.dat.$i \
            $svm_dir/model.dat.$i 1>/dev/null
        $ti_path/svm_rank/svm_rank_classify $svm_dir/test.dat.$i $svm_dir/model.dat.$i \
            $svm_dir/predictions.$i 1>/dev/null
    done

    for i in `seq 0 9`
    do
        cat $svm_dir/test.dat.$i >> $svm_dir/test.dat
        cat $svm_dir/predictions.$i >> $svm_dir/predictions
    done

    #compute the model precision
    echo -e "\tComputing the model precision...\n"
    python ComputePrecision.py $topic_dir/$x.topics-with-intruder.txt $svm_dir/test.dat \
        $svm_dir/predictions -p $output_pickle  > /dev/null
done

#print coherence scores
python PrintResults.py $output_pickle $topic_dir/20.topics.txt
