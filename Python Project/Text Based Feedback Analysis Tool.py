#preloaded feedback
feedback_data = { 
'S_No': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 
'Name': ['Ravi', 'Meera', 'Sam', 'Anu', 'Raj', 'Divya', 'Arjun', 'Kiran', 'Leela', 'Nisha'], 
'Feedback': [ 
'  Very GOOD Service!!!', 
'poor support,   not happy   ', 
'GREAT experience! will come again.', 
'okay   okay...', 
'  not   BAD', 
'Excellent care, excellent staff!', 
'good food and good ambience!', 
'Poor response and poor handling of issue', 
'Satisfied. But could be better.', 
'Good support... quick service.' 
], 
'Rating': [5, 2, 5, 3, 2, 5, 4, 1, 3, 4] 
}


#print(feedback_data)
print(feedback_data.items())
#to automatically add new s_no
feedback_data['S_No'].append(feedback_data['S_No'][9]+1)
#add more feedbacks
feedback_data['Name'].append(input("Enter your name"))
feedback_data['Feedback'].append(input("Enter your feedback"))
feedback_data['Rating'].append(int(input("What is your rating(1 to 5)?")))
print(feedback_data.items())



#text cleaning
#remove punctuation

for i in feedback_data['Feedback']:
    feedback=i.replace(".","")
    feedback=feedback.replace(",","")
    feedback=feedback.replace("!","")
    feedback=feedback.replace("?","")
    new_feedback=feedback.split()
    new_feedback1=" ".join(new_feedback)
    print(new_feedback1.lower())
    

#count word good
def count_word_in_feedbacks(word):
    count_good=0
    for i in feedback_data['Feedback']:
        count_good = count_good + i.count(word)
    return(count_good)
good=count_word_in_feedbacks('good')    
print("Total no of 'good' are:",good)
#poor
def count_word_in_feedbacks(word):
    count_poor=0
    for i in feedback_data['Feedback']:
        count_poor = count_poor + i.count(word)
    return(count_poor)
poor=count_word_in_feedbacks('poor')    
print("Total no of 'poor' are:",poor)
#excellent
def count_word_in_feedbacks(word):
    count_ex=0
    for i in feedback_data['Feedback']:
        count_ex = count_ex + i.count(word)
    return(count_ex)
ex=count_word_in_feedbacks('ex')    
print("Total no of 'Excellent' are:",ex)
 

# Final summary
cleaned_feedback = []
for i in feedback_data['Feedback']:
    feedback = i.replace(".", "").replace(",", "").replace("!", "").replace("?", "")
    cleaned_feedback.append(" ".join(feedback.split()).lower())
cleaned_feedback_data = feedback_data.copy()
cleaned_feedback_data['Feedback'] = cleaned_feedback
# Display dictionary
print("Final Cleaned Feedback Dictionary:")
print(cleaned_feedback_data)


# Average rating
tot_rating = sum(cleaned_feedback_data['Rating'])
number_of_feedback = len(cleaned_feedback_data['Rating'])

average_rating = tot_rating / number_of_feedback

print("Average Rating:", average_rating)
#longest comment
longest=""
for i in feedback_data['Feedback']:
    if len(i)>len(longest):
        longest = i
print("longest word=",longest)
#unique
unique = []
for i in feedback_data['Feedback']:
    word = i.lower().split()
    for j in word:
        if j not in unique:
            unique.append(j)
print(unique)
#but this contains punctuation, so i called the function above which containes cleaned data
# Unique words
unique = []
for i in cleaned_feedback:
    word = i.split()
    for j in word:
        if j not in unique:
            unique.append(j)
print("Unique words=", unique)
