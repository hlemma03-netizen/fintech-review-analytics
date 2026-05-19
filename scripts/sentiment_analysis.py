import pandas as pd
import re

from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords

df = pd.read_csv("data/raw/fintech_reviews.csv")


df["review_id"] = range(1, len(df) + 1)


stop_words = set(stopwords.words("english"))

def clean_text(text):
    text = str(text).lower()

    text = re.sub(r'[^a-zA-Z\s]', '', text)

    words = text.split()
    words = [word for word in words if word not in stop_words]

    return " ".join(words)

df["clean_review"] = df["review"].apply(clean_text)

from textblob import TextBlob

sentiment_labels = []
sentiment_scores = []

print("Performing sentiment analysis...")

for review in df["clean_review"]:

    polarity = TextBlob(review).sentiment.polarity

    sentiment_scores.append(polarity)

    if polarity > 0:
        sentiment_labels.append("Positive")
    elif polarity < 0:
        sentiment_labels.append("Negative")
    else:
        sentiment_labels.append("Neutral")

df["sentiment_label"] = sentiment_labels
df["sentiment_score"] = sentiment_scores



vectorizer = TfidfVectorizer(
    max_features=20,
    ngram_range=(1, 2)
)

X = vectorizer.fit_transform(df["clean_review"])

keywords = vectorizer.get_feature_names_out()

print("\nTop Keywords:")
print(keywords)


def identify_theme(text):

    text = text.lower()

    if "login" in text or "password" in text:
        return "Account Access Issues"

    elif "transfer" in text or "slow" in text:
        return "Transaction Performance"

    elif "ui" in text or "design" in text:
        return "UI & Design"

    elif "otp" in text or "verification" in text:
        return "OTP & Verification"

    elif "feature" in text or "fingerprint" in text:
        return "Feature Requests"

    else:
        return "General Feedback"

df["identified_theme"] = df["clean_review"].apply(identify_theme)


final_df = df[
    [
        "review_id",
        "review",
        "bank",
        "rating",
        "date",
        "sentiment_label",
        "sentiment_score",
        "identified_theme"
    ]
]

final_df.rename(columns={"review": "review_text"}, inplace=True)

final_df.to_csv(
    "data/raw/analyzed_fintech_reviews.csv",
    index=False
)

print("\nAnalysis completed successfully!")
print(final_df.head())