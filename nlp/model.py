import re

import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

import joblib

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

model = joblib.load('model/model.joblib')
vectorizer = joblib.load('model/vectorizer.joblib')


def cleaning(description):
    stop_words = set(stopwords.words('english'))
    lemma = WordNetLemmatizer()

    description = re.sub(r'[^A-z]', ' ', description).lower()
    description = word_tokenize(description)
    description = [word for word in description if word not in stop_words]
    description = [lemma.lemmatize(word) for word in description]

    return ' '.join(description)


def predict_job_title(description):
    # preprocess input description
    clean_description = cleaning(description)
    vectorized_description = vectorizer.transform([clean_description])

    # make prediction
    predicted_title = model.predict(vectorized_description)

    return predicted_title[0]


def main() -> None:
    raise NotImplementedError('No Code')


if __name__ == '__main__':
    main()
