import pandas as pd 

#Load the crossword training set
train_data = pd.read_csv('test_all.csv')
#take 1000 samples
random_samples = train_data.sample(n=1000)
#random_samples.to_csv('random_samples_test.csv', index=False)
random_samples["annotated"] = " "
random_samples.to_csv('random_samples_test.csv', index =False)
random_samples = pd.read_csv('random_samples_test.csv')
print(random_samples.info())