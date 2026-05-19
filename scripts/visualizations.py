import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("data/raw/analyzed_fintech_reviews.csv")

# -----------------------------------
# SENTIMENT DISTRIBUTION BY BANK
# -----------------------------------

plt.figure(figsize=(8,6))

sns.countplot(
    data=df,
    x="bank",
    hue="sentiment_label"
)

plt.title("Sentiment Distribution by Bank")
plt.xlabel("Bank")
plt.ylabel("Number of Reviews")

plt.tight_layout()
plt.savefig("sentiment_distribution.png")

# -----------------------------------
# THEME FREQUENCY
# -----------------------------------

plt.figure(figsize=(10,6))

theme_counts = df["identified_theme"].value_counts()

sns.barplot(
    x=theme_counts.values,
    y=theme_counts.index
)

plt.title("Theme Frequency")
plt.xlabel("Count")
plt.ylabel("Theme")

plt.tight_layout()
plt.savefig("theme_frequency.png")

print("Visualizations created successfully!")