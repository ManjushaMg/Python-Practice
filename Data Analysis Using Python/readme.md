Social Media Engagement Analytics Using Python:

In this project, I aimed to analyse social media engagement to gain deeper insights into user behaviour, identify trends, and improve content performance."
Steps followed:
1.Imported the csv file into Jupyter notebook and python libraries to do analytics(NumPy,Pandas,Matplotlib,Seaborn,Plotly)

2.Data Cleaning 
Checked for missing values and duplicate records using isnull() and duplicated().
Handled missing values using dropna(), fillna(), and statistical imputation techniques such as median and mode.
Checked categorical values for consistency and corrected inconsistencies where necessary.
Extracted hashtag counts using a user-defined function.
Checked sentiment labels and confirmed that they were already in the required format.

3.Data Exploration using Pandas:
Using head(),tail(),columns and info() to view the structure of the dataset and describe() to get the summary statistics.
Then analyzed categorical distributions using value_counts(), unique(), and nunique() and , numeric entries distribution by creating a correlation matrix
Used groupby() function to get better analysis of the dataset.Eg.,average age of users in countries,avg age of users in each gender,total watch time in each gender,total engagement time in each category of post.

4.Data Visualisation using Matplotlib and seaborn
Using matplotlib:Scatter(likes vs impressions), Line(daily engagement trend) ,Bar: posts by category ,Pie: gender distribution ,Histogram: age 
Using seaborn:Count plot: post type,Bar plot: avg likes by category ,Violin: followers vs sentiment ,Pair plot: numeric features ,Heatmap: correlation matrix
Using Plotly: Bar:Average Likes by Category

 Final Insights:
 
 1.Content Performance
 a)The discending order of engagement rate by post type is:video>Text>image>reel
 b)Best-performing content category is food
 c)country that have highest avg engagement rate is Brazil then Australia.India is in the 9th position out of top 10 countries list
 
 2.User Trends 
 a)Age is definitely a factor while analysing user trends,those who are aged between 20-28 and above 50 and near 60 years old are more engaged in social media than other age groups
 b)users from non verified accounts show high average engagement rate than with verified accounts

3.Behavioral Insights 
a)Average rate of impressions in a week is remain almost consistently throughout the week, while weekends and Tuesday showing a slightly higher activity.
b)Mobile phones are the mostly used device for using social media

4.Sentiment Analysis 
 a)The descending order of average engagement rate by sentiment is Negative > Neutral > Positive
b)While looking into the behavior of negative/neutral sentiment posts, the distribution of neutral post is higher than negative posts
