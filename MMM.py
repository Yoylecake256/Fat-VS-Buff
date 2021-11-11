a = 60 + 61 + 63 + 65 + 90 + 91 + 95 + 96 + 98 + 99
print(a)
mean =a/8
print("The of value mean is:",mean)


z = 26+30
y = z/2
print("The value of median is:",y)

from collections import Counter
import csv
with open('SOCR-HeightWeight.csv', newline='') as f:
    reader = csv.reader(f)
    file_data =list(reader)
    print(file_data)
file_data.pop(0)
     #pop out the value on index.
    
  #sort out the datato get the height of the people

new_data =[]
for i in range(len(file_data)):
    n_num= file_data[i][1]
    new_data.append(float(n_num))
    
print(new_data)
  
    