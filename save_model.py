import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle
import csv

# Load your data
raw_mail_data = pd.read_csv('combined_set.csv')
mail_data = raw_mail_data.where((pd.notnull(raw_mail_data)),'')

# Label encoding
mail_data.loc[mail_data['label'] == 'spam', 'label'] = 0
mail_data.loc[mail_data['label'] == 'ham', 'label'] = 1

# Separate features and labels
X = mail_data['Message']
Y = mail_data['label']

# Split the data
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=3)

# Load Swahili stopwords
with open('swahili_stopwords.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    swahili_stop_words = [row[0] for row in reader]

# Create and train the model
feature_extraction = TfidfVectorizer(min_df=1, stop_words=swahili_stop_words, lowercase=True)
x_train_features = feature_extraction.fit_transform(X_train)
Y_train = Y_train.astype('int')

model = LogisticRegression()
model.fit(x_train_features, Y_train)

# Save the model and vectorizer
with open('spam_model.pkl', 'wb') as f:
    pickle.dump(model, f)
    
with open('vectorizer.pkl', 'wb') as f:
    pickle.dump(feature_extraction, f)

print("Model and vectorizer saved successfully!")