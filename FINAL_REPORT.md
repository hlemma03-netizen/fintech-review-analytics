Customer Experience Analytics for Fintech Apps
Introduction

Mobile banking applications have become essential digital financial tools in Ethiopia. Customer reviews on the Google Play Store provide valuable insights into user experiences, technical issues, and customer expectations.

This project analyzed reviews from three Ethiopian banking applications:

Commercial Bank of Ethiopia
Bank of Abyssinia
Dashen Bank

The project aimed to transform raw customer feedback into actionable business insights using web scraping, sentiment analysis, thematic analysis, and PostgreSQL data storage.

Methodology
Data Collection

Reviews were scraped from the Google Play Store using the google-play-scraper Python library.

Collected fields included:

Review text
Rating
Date
Bank name
Source

More than 1,200 reviews were collected across the three banking applications.

Data Preprocessing

The preprocessing pipeline included:

Duplicate removal
Missing value handling
Date normalization
Text cleaning and stop-word removal

The cleaned dataset was exported into CSV format for analysis.

Sentiment Analysis

Sentiment analysis was performed using TextBlob.

Each review was classified into:
- Positive
- Negative
- Neutral

Sentiment scores were generated to quantify customer satisfaction levels.

Thematic Analysis

TF-IDF keyword extraction was used to identify recurring customer concerns and feature requests.

The main themes identified were:

Account Access Issues
Transaction Performance
OTP & Verification
UI & Design
Feature Requests

Key Insights

Commercial Bank of Ethiopia (CBE)
 
Satisfaction Drivers
 -Users frequently praised the application's convenience and ease of use.
 -Positive reviews highlighted fast transactions and accessible mobile banking services.
Pain Points
 -Many users reported login failures and password issues.
 -Slow transfer processing was a recurring complaint.

 Recommendations

 -Improve authentication stability to reduce login-related frustration.
 -Optimize transfer processing performance during peak usage periods.

Bank of Abyssinia (BOA)

Satisfaction Drivers
 -Users appreciated the availability of mobile banking features.
 -Some customers praised the application interface and navigation.
Pain Points
 -OTP verification delays appeared frequently in negative reviews.
 -App crashes and instability affected customer experience.

 Recommendations
 -Improve OTP delivery reliability and verification systems.
 -Prioritize application stability testing and crash reduction.

Dashen Bank

Satisfaction Drivers
 -Customers positively mentioned smooth user interface design.
 -Reviews frequently praised transaction convenience.
Pain Points
 -Network-related transaction interruptions were common.
 -Some users requested additional modern banking features.

Recommendations
 -Improve transaction reliability under unstable network conditions.
 -Introduce additional customer-requested features such as biometric authentication.

 Comparative Analysis
Sentiment Distribution

CBE and Dashen Bank showed stronger positive sentiment distributions compared to BOA.

BOA displayed a higher proportion of negative reviews, primarily related to OTP and application stability issues.

Dominant Themes

The most dominant themes across all banks were:

Transaction performance
Account access issues
OTP verification problems

These recurring issues suggest that technical reliability strongly influences customer satisfaction in Ethiopian fintech applications.

Visualization Summary
Sentiment Distribution by Bank

The sentiment distribution chart demonstrates differences in positive and negative review patterns among the three banks.

Theme Frequency

The theme frequency visualization highlights the most common customer concerns and requested improvements.

Ethical Considerations

Several biases may affect review-based analysis:

Negativity Bias

Customers are generally more likely to leave reviews after negative experiences than positive ones.

Sampling Bias

The collected reviews only represent users who actively chose to post feedback on the Google Play Store.

Date Range Limitations

Some reviews may reflect temporary technical issues that were later resolved by application updates.

These limitations should be considered when interpreting the findings.

Conclusion

This project successfully demonstrated how customer reviews can be transformed into actionable fintech business insights through data analytics and NLP techniques.

The analysis revealed that transaction reliability, authentication stability, and OTP verification systems are major factors influencing customer satisfaction across Ethiopian banking applications.

Future improvements could include advanced transformer-based NLP models, real-time dashboards, and predictive customer satisfaction analytics.