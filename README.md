This repository contains code and dataset described in the publication "The Sensitivity of Topic Coherence Evaluation
to Topic Cardinality"

Running the System
==================
* The code depends on jhlau/topic_interpretability, so check out the repository: https://github.com/jhlau/topic_interpretability
* Use topic_interpretability/ComputeWordCount.py in to collect word co-occurrence statistics between topic words
* For word intrusion:
 * Generate SVM features based on word count features
 * Train an SVM rank model to predict intruder words
* For NPMI:
 * Compute topic coherence using word count features
* Aggregate results over different cardinalities

Scripts
=======
* run_wordcount: runs ComputeWordCount.py to collect word statistics
* run_wi.sh: computes topic coherence using word intrusion
* run_npmi.sh: computes topic coherence using NPMI

Mechanical Turk Annotations
===========================
The coherence ratings of topics collected via mturk are in 
mturk_annotation/annotations.csv (tab-delimited).

Description of columns:
* domain: domain of topic (wiki or news)
* topic: top-20 words of the topic
* top-N: top-N average rating (e.g. top-5 means only the top 5 of the 20 words are presented when collecting the rating)

Publication
-----------
* Jey Han Lau and Timothy Baldwin. The Sensitivity of Topic Coherence Evaluation to Topic Cardinality. In Proceedings of the 2016 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL HLT 2016), San Diego, California, to Appear.
