Python Project: Survey Feedback Analyzer to build a text based feedback analysis tool

In this project I have created a feedback analysis tool to analyse the feedback given by customers, so that I can analyse the performance effectively

steps followed:
1.loaded the data to the python file

2.Prompted user to provide further feedback:collected name,feedback and rating from customer, and added the data to the existing dictionary by automatically incrementing the serial number.
USED: append, items

3.Data Cleaning: Removed punctuation and spaces(used replace()," "join(),split()) and converted the text to lowercase

4.Word count:
created a function to count the words in the feedback and printed output containing the numbers of words containing "Good", "poor", "excellent"

5.Summary

printed all cleaned dictionary

printed the average rating(total/number):Used sum() and len() to calculate the total and number of ratings,divided them to find the average rating,and printed the result.

printed the longest comment:Used a for loop and len() to find and store the longest feedback comment, then printed it.

prined unique words in feedback list:Used nested for loops and an if condition to identify and store unique words without duplicates, then printed the list.



