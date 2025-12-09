import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random

# Generate a 3x3 matrix with random intergers between 10 and 50
matrix = np.random.randint(10, 51, size=(5,5))
print("Generated Matrix:\n", matrix)

#Find and print the maximum value in the matrix
max_value = np.max(matrix)
print("Maximum Value:", max_value)

# Find and print the minimum value in the matrix
min_value = np.min(matrix)
print("Minimum Value:", min_value)

# Initial data for the pie chart
sizes = [5, 10, 70, 15] #Percentages for each category
labels = ['Tired','Tired uhh come on',' MICHAEL!! ',' Seriously, Seriously MICHAEL']
color = ['lightgray','gray','darkgray', 'black']
explode = (0, 0, 0.1, 0)

# Create a basic pie chart
plt.pie(sizes, labels=labels, colors=color, explode=explode, autopct='%1.2f%%')
plt.title("Reason Ezri is grumpy today")
plt.show()

causes = ['hardware projects','half-eaten snacks','mysterious sticky notes', 'enoch','papers that blew off the desk',]
items_count = [8,5,10,7,12]

plt.bar(causes, items_count, color=[f'#{random.randint(0,255):02x}{random.randint(0,255):02x}{random.randint(0,255):02x}' for i in causes])



plt.xlabel('causes of mess')
plt.ylabel('number of items')
plt.title("why mo's classroom is messy: a scientific study")
plt.suptitle("because cleaning is optional", fontsize=10, color='gray')

plt.xticks(rotation=30, ha='right')

plt.show()

data = {
    'Friend': ['Melissa','Natalie', 'Ezri'],
    'Favorite Candy': ['Chocolate Bar', 'Candy Corn', 'All Chocolate'],
    'Number Eaten this week' : [5,3,298657]
    }

df = pd.DataFrame(data)
df.sort_values(by='Number Eaten this week', ascending=False, inplace=True)
print("Candy Preferences DataFrame:")
print(df)


scores_data = {
    'Student': ['Gus', 'Liam', 'Jayden', 'Michael'],
    'Test 1 Score': [-41645456, -174456, -135864, -5282563],
    'Test 2 Score': [-345483135, -3546841, -348684, -987459874],
    'Test 3 Score': [-168684, -652256, -813614, -174528936],
    }

scores_df = pd.DataFrame(scores_data)
print("Student Test Scores DataFrame")
print(scores_df)

scores_df['Average Score'] = (scores_df['Test 1 Score'] + scores_df['Test 2 Score'] + scores_df['Test 3 Score']) /3
print("\nUpdated DataFrame with Average Scores:")
print(scores_df)

failed_students = scores_df[scores_df['Average Score'] < 60]
print("\nStudents Who Failed (Average Score Below 60):")
print(failed_students)
