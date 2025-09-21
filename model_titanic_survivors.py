import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

titanic_train_data = pd.read_csv('data/train.csv')
titanic_test_data = pd.read_csv('data/test.csv')
# Display the first few rows of the dataset

titanic_train_data.info()
titanic_test_data.info()


sns.countplot(data=titanic_train_data, x="Sex", hue="Survived")
plt.title("Titanic Survivors by Gender")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.legend(title="Survived", labels=["No", "Yes"])
plt.show()