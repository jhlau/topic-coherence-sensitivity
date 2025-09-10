This repository contains code and dataset described in the publication "The Sensitivity of Topic Coherence Evaluation
to Topic Cardinality"

Running the System
==================
* The code depends on jhlau/topic_interpretability, so check out the repository: https://github.com/jhlau/topic_interpretability
* Use **run-wordcount.sh** to collect word co-occurrence statistics between topic words
* If doing word intrusion, use **run-wi.sh**; the script will:
 * generate SVM features based on word count features
 * train an SVM rank model to predict intruder words
* If doing NPMI, use **run-npmi.sh**; the script will:
 * compute topic coherence using word count features
* Both scripts will aggregate coherence scores over different cardinalities and print them at the end
* Note: an example toy dataset is given in example_data. To test, execute **run-wordcount.sh** followed by **run-[npmi/wi].sh**

Scripts
=======
* run_wordcount.sh: runs topic_interpretability/ComputeWordCount.py to collect word statistics
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

Processed Corpus (News and Wiki)
================================
* [2016-naacl-topic-cardinality/news_wiki.tgz](https://mediaflux.researchsoftware.unimelb.edu.au/mflux/data/mover/index.html?token=kg48rxcqq76v15kvwwsfj2iqkvmijugyydjrqr2jq8gseyh4ojrt1nw0rg3dq2k70l23lv5klxose7z8nrm7eccvx47plvyr9ffpidohfl040ushg9dqzmparr5vwiubtfvh8dpwipqlopyrs46otxe4ru60gg4gy772tcprpr33n3eco5ghy9j91dluboyxr3kijm8z7wvhrgr7u8tegejdqgq56n5diqdptsad) (note: you'll be prompted to download a program called "Mediaflux Data Mover" - after installing it, click the link again and open Mediaflux Data Mover and you'll be able to download the data via the program).

Publication
-----------
* Jey Han Lau and Timothy Baldwin. The Sensitivity of Topic Coherence Evaluation to Topic Cardinality. In Proceedings of the 2016 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL HLT 2016), San Diego, California, to appear.
