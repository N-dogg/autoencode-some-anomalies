Anomaly Detection Using Accounting Journals
===================


#### Coding and testing the commercial applications of academic papers and cutting edge analytical techniques.
------------------------------------------------------------------------

**Paper 1:** *Detection of Anomalies in Large-Scale Accounting Data using Deep Autoencoder Networks*

**Abstract:** Learning to detect fraud in large-scale accounting data is one of the long-standing challenges in financial statement audits or fraud investigations. Nowadays, the majority of applied techniques refer to handcrafted rules derived from known fraud scenarios. While fairly successful, these rules exhibit the drawback that they often fail to generalize beyond known fraud scenarios and fraudsters gradually find ways to circumvent them. To overcome this disadvantage and inspired by the recent success of deep learning we propose the application of deep autoencoder neural networks to detect anomalous journal entries. We demonstrate that the trained network's reconstruction error obtainable for a journal entry and regularized by the entry's individual attribute probabilities can be interpreted as a highly adaptive anomaly assessment. Experiments on two real-world datasets of journal entries, show the effectiveness of the approach resulting in high f1-scores of 32.93 (dataset A) and 16.95 (dataset B) and less false positive alerts compared to state of the art baseline methods. Initial feedback received by chartered accountants and fraud examiners underpinned the quality of the approach in capturing highly relevant accounting anomalies.

**Paper 2:** *Detection of Accounting Anomalies in the Latent Space using Adversarial Autoencoder Neural Networks*

**Abstract:** The detection of fraud in accounting data is a long-standing challenge in financial statement audits. Nowadays, the majority of applied techniques refer to handcrafted rules derived from known fraud scenarios. While fairly successful, these rules exhibit the drawback that they often fail to generalize beyond known fraud scenarios and fraudsters gradually find ways to circumvent them. In contrast, more advanced approaches inspired by the recent success of deep learning often lack seamless interpretability of the detected results. To overcome this challenge, we propose the application of adversarial autoencoder networks. We demonstrate that such artificial neural networks are capable of learning a semantic meaningful representation of real-world journal entries. The learned representation provides a holistic view on a given set of journal entries and significantly improves the interpretability of detected accounting anomalies. We show that such a representation combined with the networks reconstruction error can be utilized as an unsupervised and highly adaptive anomaly assessment. Experiments on two datasets and initial feedback received by forensic accountants underpinned the effectiveness of the approach.

----------


Documents
-------------

[Detection of Anomalies in Large-Scale Accounting Data using Deep Autoencoder Networks](https://arxiv.org/pdf/1709.05254.pdf)

[Detection of Accounting Anomalies in the Latent Space using Adversarial Autoencoder Neural Networks](https://arxiv.org/pdf/1908.00734.pdf)


----------


Hypotheses
-------------------
Overall goal is to develop a solution that can identify anomalies in financial accounting journals. The following are the projects hypotheses:

 - Accounting journals hold all transaction data for an entity
 - Deep autoencoder network will be effective at identifying both global and local accounting anomalies
 - Solution can perform better than current auditing procedures in terms of 1) Identifying all anomalies 2) Minimising the testing of      normal transactions.

----------

Process
-------------
We note that for this test we have not used all of the raw journal outputs that are generated from most common ERP systems. Instead we have only used a small sample including GL account number, account class, entry date, period, preparer and source. Each feature was one-hot-encoded, and the total population was split into a training, testing and validation set prior to training.

Drawing from paper 1, a group of global accounting anomalies, those exhibiting ususual or rare individual attributes, and global accounting anomalies, those exhibiting a combination of rare attributes, were created. These were appended to the testing data-set as we want the allow the model to only learn the 'normal' opperations of the business.

Four models of ranging depth were trained, see example architecture below:

(https://user-images.githubusercontent.com/43980002/65396497-1a02fd00-ddea-11e9-8697-14ccfb710f41.JPG)

Trained models were then used to predict the outcome of the test set. A reconstruction error was obtained for each sample and plotted to visually assess the results of the model.


----------


Example Results Screens
--------------------



----------

Next Steps
--------------------

Considerations for further iterations include:
- Journals are usually posted in batches so should potentially be analysed accordingly instead of line-by-line in the current solution
- The value and magnitude of the journal posted should be included in the analysis, but further consideration needs to be given around how its inclusion will affect a model solely focused on categorical variables.
- Quantitative evaluation threshold for further investigation of journals.
----------

Requirements
--------------------
----------
