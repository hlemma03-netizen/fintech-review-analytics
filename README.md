# Fintech Review Analytics

## Project Overview

This project analyzes customer reviews from Ethiopian banking apps on the Google Play Store.

The analysis focuses on:
- Commercial Bank of Ethiopia (CBE)
- Bank of Abyssinia (BOA)
- Dashen Bank

## Objective

The objective is to collect, preprocess, and prepare customer reviews for sentiment and thematic analysis.

## Data Collection

Reviews were scraped using the google-play-scraper Python library.

Collected fields:
- Review text
- Rating
- Date
- Bank name
- Source

A minimum of 400 reviews per bank were targeted.

## Preprocessing

The preprocessing steps included:
- Removing duplicate reviews
- Removing rows with missing review text or ratings
- Formatting dates to YYYY-MM-DD

## Technologies Used

- Python
- Pandas
- Google Play Scraper
- Git & GitHub
- GitHub Actions

## Limitations

Review availability depends on Google Play Store access and API limitations.

## Sentiment and Thematic Analysis

Sentiment analysis was performed using the TextBlob Python library.

Reviews were classified into:
- Positive
- Negative
- Neutral

TextBlob was selected because it provieds lightweight sentiment anaysis suitable for limited computational resources.

TF-IDF Keyword extraction was used to identify recurring terms and themes from customer reviews.

The major themes identified incude: 
- Account Access Issues
- Transaction Performance
- OTP & Verification
- UI & Design
- Feature Requests