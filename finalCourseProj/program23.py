import matplotlib.pyplot as plt 
import csv 
import pandas as pd
import sqlite3
  
x = [] 
y = [] 
  
conn = sqlite3.connect('population.sqlite')
c = conn.cursor()

users = pd.read_csv('race.csv')
users.to_sql('population', conn, if_exists='append', index = False)



new_column = "ALTER TABLE population ADD COLUMN Numbers CHAR(14)"
c.execute(new_column)

sql1 = "UPDATE population SET Numbers = '1' WHERE Population = '14109297'"
sql2 = "UPDATE population SET Numbers = '2' WHERE Population = '6444435'"
sql3 = "UPDATE population SET Numbers = '3' WHERE Population = '2128184'"
sql4 = "UPDATE population SET Numbers = '4' WHERE Population = '105074'"
sql5 = "UPDATE population SET Numbers = '5' WHERE Population = '124341'"
sql6 = "UPDATE population SET Numbers = '6' WHERE Population = '236266'"
sql7 = "UPDATE population SET Numbers = '7' WHERE Population = '5802086'"
sql8 = "UPDATE population SET Numbers = '8' WHERE Population = '85310'"
sql9 = "UPDATE population SET Numbers = '9' WHERE Population = '134692'"
sql10 = "UPDATE population SET Numbers = '10' WHERE Population = '13586'"
sql11 = "UPDATE population SET Numbers = '11' WHERE Population = '149096'"
sql12 = "UPDATE population SET Numbers = '12' WHERE Population = '5887769'"
sql13 = "UPDATE population SET Numbers = '13' WHERE Population = '1413870'"
sql14 = "UPDATE population SET Numbers = '14' WHERE Population = '2821347'"


conn.execute(sql1)
conn.execute(sql2)
conn.execute(sql3)
conn.execute(sql4)
conn.execute(sql5)
conn.execute(sql6)
conn.execute(sql7)
conn.execute(sql8)
conn.execute(sql9)
conn.execute(sql10)
conn.execute(sql11)
conn.execute(sql12)
conn.execute(sql13)
conn.execute(sql14)
conn.commit()

query= 'select * from population'
data= pd.read_sql(query,conn)
data.to_csv('export.csv')

df = pd.read_csv('export.csv')
column_list=["ID Race", "Race", "Numbers"]
df[column_list].to_csv('export1.csv',index=False)
df.to_csv('export1.csv', columns = column_list,index=False)


with open('export1.csv','r') as csvfile: 
    plots = csv.reader(csvfile, delimiter = ',') 
    for row in plots: 
        x.append((row[2])) 
        y.append((row[1])) 
  
plt.bar(x, y, color = 'b', width = 0.55, label = "Race") 
plt.xlabel('Person by #') 
plt.xticks(fontsize=5)
plt.yticks(fontsize=6)
plt.ylabel('Race') 
plt.title('Number of people of different races') 
plt.xlim([0, 14.5]) 
plt.legend() 
plt.show()
plt.close()