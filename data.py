import pandas as lt
import matplotlib.pyplot as data
cd= lt.read_csv('gender_submission.csv')
print(cd)
Total_Pass = cd["Survived"].value_counts()
total = len(cd)
a = Total_Pass[0]
perc = (a / total) * 100
print(f"Percentage of non-survivors is: {perc:.2f}%")
Total_Pass.plot(kind = 'bar',color = ["black","blue"])
data.xlabel("Survived people")
data.ylabel("Non-Survived people")
data.title("Survived passenger in the flight")
data.xticks(rotation = 0)
data.yticks(rotation = 22)
data.show() 