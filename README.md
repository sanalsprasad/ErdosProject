# CoverMyMeds Project for Erdos Bootcamp

## Team members
Alana Huszar  
Sanal Shivaprasad  
Yueqiao Wu  
Yili Zhang  


## Description from CoverMyMeds
CoverMyMeds designs solutions that help patients get the medication they need
to live healthy lives. When a doctor prescribes a therapy to a patient, they send the
prescription to a pharmacy. The pharmacy, when going to fill the prescription, runs a
claim against the patient’s insurance (in this context known as a Pharmacy Benefit
Manager or PBM), to see if their insurance will cover the therapy as prescribed (correct
drug, dosage, etc.). Thankfully, more times than not insurance companies, or payers,
approve these claims and the pharmacy dispenses the medication as prescribed. The
patient then picks it up and when relevant, pays the remaining cost and completes the
transaction.

However, payers may not cover particular medications or dosages, and may reject the
claim. Claims can be rejected for a variety of reasons. For example, the dosage or
quantity dispensed may not be covered, or the drug might not be on formulary. A
formulary is a list of the preferred drugs a payer has. Typically, formularies are tiered,
with some drugs being the cheapest, some being more costly but covered, and some
requiring a prior authorization for example.

When a claim is rejected, a “reject code” is provided which contextualizes the reason
the claim was rejected. For our purposes, there are 3 rejection codes that we focus on:
70, 75, and 76. A code 70 implies that a drug is not covered by the plan and is not on formulary,
and typically implies that another course of therapy should be pursued. A
code 75 implies that a drug is on the formulary but does not have preferred status and
requires a prior authorization (PA). A PA is a form that care providers submit on behalf
of their patient making the case that the therapy as described is a critical course of
treatment. A code 76 simply means that the drug is covered, but that the plan
limitations have been exceeded, which means that the limitations on the number of fills
for that medication has been met. We might expect there to be variation in the type of
reject codes we see for certain drugs by the payer.

If a claim is rejected, regardless of the reject code provided, a prior authorization can be
started to prevent prescription abandonment and ensure a patient gets the therapy their
provider thinks would work best for them. At CoverMyMeds, one of our products is an
electronic PA (ePA) solution that replaces a largely manual process of looking for the
relevant form, printing it, filling it out, and faxing it to a simple portal-based experience.
When a provider is filling out an ePA, they may frequently be asked to provide
information about a patient’s diagnosis, lab values, contraindications (health-related
reasons not to take certain medications), and if they have tried and failed other
therapies. When reviewing prior authorizations, payers evaluate the information
provided against their formulary and make a decision. That is to say, information
contained on the PA and information contained in the original pharmacy claim can help
us understand whether an ePA is likely to be approved or denied.

## Our Project
Our project focuses on predicting whether a prior authorization form will be approved or not for claims that were rejected. Our top level notebooks are:
+ **Create main csv** - A notebook creating one table with all information for each claim (merging the database of several csvs).
+ **Data_cleaning** - A notebook to check for missing values in the data, and to check if there are claims identical other than date submitted and PA approval with different outcomes (PA approval).
+ **PA approval and date** - A notebook looking at if there are different PA approval outcomes based on the date the claim was submitted.
+ **Data_exploration** - A notebook for preliminary data exploration on the training data. Includes histograms for each feature, colored by PA approval.
+ **create_csv_clf** - A notebook that creates a CSV for PA approval prediciton purposes (drops date information, one hot encodes Drug and BIN).
+ **PA approval rate visualization** - A notebook that explores the relationship between the combination of different variables and PA approval.

In the models folder, we have a notebook for each model we tuned, and a final notebook comparing them:
+ **AdaBoost**
+ **BernoulliNB**
+ **Decision Tree**, creates image file **pa_form_dec_tree.png**, first few levels of decision tree.
+ **Extra Trees**
+ **Logistic Regression**
+ **Random Forest**
+ **Voting Classifier**
+ **xgboost**

Finally, also in the model folder, we do a final comparison in **Comparison of Final Models**, which also generates the table **SummaryTable.pdf** and run our final model (decision tree) on our test set. This exported with the **Exporting Final Model** notebook.

Our webapp uses the repository: https://github.com/huszara2/CMMApp, and can be found at https://cmm-narwhal.herokuapp.com/.
