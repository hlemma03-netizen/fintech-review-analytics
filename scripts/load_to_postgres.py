import pandas as pd
import psycopg2

# Connect to PostgreSQL
conn = psycopg2.connect(
    database="bank_reviews",
    user="postgres",
    password="POSTGRES",
    host="localhost",
    port="5432"
)

cursor = conn.cursor()

# Insert banks
banks_data = [
    ("Commercial Bank of Ethiopia", "CBE Mobile Banking"),
    ("Bank of Abyssinia", "BOA Mobile"),
    ("Dashen Bank", "Dashen Super App")
]

cursor.execute("DELETE FROM reviews;")
cursor.execute("DELETE FROM banks;")

for bank in banks_data:
    cursor.execute(
        """
        INSERT INTO banks (bank_name, app_name)
        VALUES (%s, %s)
        """,
        bank
    )

conn.commit()

# Load CSV
df = pd.read_csv("data/raw/analyzed_fintech_reviews.csv")

# Map bank names to IDs
cursor.execute("SELECT bank_id, bank_name FROM banks")
bank_rows = cursor.fetchall()

bank_map = {
    "CBE": 1,
    "BOA": 2,
    "Dashen": 3
}

# Insert reviews
for _, row in df.iterrows():

    cursor.execute(
        """
        INSERT INTO reviews (
            bank_id,
            review_text,
            rating,
            review_date,
            sentiment_label,
            sentiment_score,
            identified_theme,
            source
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """,
        (
            bank_map.get(row.get("bank")),
            row["review_text"],
            None,
            None,
            row["sentiment_label"],
            row["sentiment_score"],
            row["identified_theme"],
            "Google Play"
        )
    )

conn.commit()

print("Data inserted successfully!")

cursor.close()
conn.close()