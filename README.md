Results
-------
These files represent the results of training and running the summarizer over documents.

To view the main library's source code see [summarize](https://github.com/vighneshbirodkar/summarize)

File organization
-----------------

#### train.py
This script will train the SVR over the document in `train/doc.txt` over the summary `train/sum.txt`

#### train/doc.txt
The document used to train the model

#### train/sum.txt
The summary used to train the model

#### machine/
Files that store the trained machine

#### generate.py 
The script that reads a document and generates a summary. Usage  : `python generate.py folderName`.


Generated Summaries
-------------------
In the rest of the folers, `doc.txt` is the document amd `sum.txt` is the generated summary.

The description of the documents is as follows


#### nexus
An article reviewing the Neuxs 5 phone. It consists of technical but non-scientific comments. Summary seems accurate

#### sift
The introduction from Lowe's SIFT paper.The text is techinical, Summary seems accurate.

#### 300
A review of the movie 300. Article is non technical, but is mostly descriptive.Summary is accurate.

#### airline
A news article regarding the lost malaysian airline.The text mostly describes events. Summary is relevant, but not as good as others.

#### sachin
An article about Sachin Tendulkar. The text non descriptve, and tends more towards a story-like organization. Summary seems to list out some important events from the article.