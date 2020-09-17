#!/usr/bin/env python
# coding: utf-8

# In[1]:


# importing the required module 
import matplotlib.pyplot as plt 


# In[4]:


# x axis values 
x = [5,6,3,8,10] 
# corresponding y axis values 
y = [2,4,5,9,11] 
  
# plotting the points  
plt.plot(x, y) 
  
# naming the x axis 
plt.xlabel('X - axis') 
# naming the y axis 
plt.ylabel('Y - axis') 
  
# giving a title to my graph 
plt.title('My First Line graph!') 
  
# function to show the plot 
plt.show() 


# In[9]:


# line 1 points 
x1 = [3,6,5,10,8] 
y1 = [2,4,5,9,11]
# plotting the line 1 points  
plt.plot(x1, y1, label = "Line 1") 
  
# line 2 points 
x2 = [3,6,5,8,10]
y2 = [4,2,9,5,11]
# plotting the line 2 points  
plt.plot(x2, y2, label = "Line 2") 
  
# naming the x axis 
plt.xlabel('X - axis') 
# naming the y axis 
plt.ylabel('Y - axis') 
# giving a title to my graph 
plt.title('Two lines on same graph!') 
  
# show a legend on the plot 
plt.legend() 
  
# function to show the plot 
plt.show() 


# In[17]:


#import matplotlib.pyplot as plt 
  
# x axis values 
x = [1,2,3,4,5]
# corresponding y axis values 
y = [2,3,1,5,4]
  
# plotting the points  
plt.plot(x, y, color='blue', linestyle='dotted', linewidth = 3, 
         marker='o', markerfacecolor='green', markersize=10) 
  
# setting x and y axis range 
plt.ylim(1,8) 
plt.xlim(1,8) 
  
# naming the x axis 
plt.xlabel('X - axis') 
# naming the y axis 
plt.ylabel('Y - axis') 
  
# giving a title to my graph 
plt.title('Some cool customizations!') 
  
# function to show the plot 
plt.show()


# In[20]:


#import matplotlib.pyplot as plt 
  
# x-coordinates of left sides of bars  
left = [1, 2, 3, 4, 5] 
  
# heights of bars 
height = [20, 14, 26, 50, 10] 
  
# labels for bars 
tick_label = ['One', 'Two', 'Three', 'Four', 'Five'] 
  
# plotting a bar chart 
plt.bar(left, height, tick_label = tick_label, 
        width = 0.8, color = ['Blue', 'Green']) 
  
# naming the x-axis 
plt.xlabel('X - axis') 
# naming the y-axis 
plt.ylabel('Y - axis') 
# plot title 
plt.title('My bar chart!') 
  
# function to show the plot 
plt.show() 


# In[24]:


#import matplotlib.pyplot as plt 
  
# frequencies 
ProductSales = [2,5,70,50,20,45,50,45,33,60,45] 
  
# setting the ranges and no. of intervals 
range = (0, 100) 
bins = 10  
# plotting a histogram 
plt.hist(ages, bins, range, color = 'Gray', 
        histtype = 'bar', rwidth = 0.8) 
  
# x-axis label 
plt.xlabel('ProductSales') 
# frequency label 
plt.ylabel('No. of Customers') 
# plot title 
plt.title('My histogram') 
  
# function to show the plot 
plt.show() 


# In[29]:


#import matplotlib.pyplot as plt 
  
# x-axis values 
x = [1,2,3,4,5]
# y-axis values 
y = [5,4,3,2,1]
  
# plotting points as a scatter plot 
plt.scatter(x, y, label= "arows", color= "green",  
            marker= "<", s=30) 
  
# x-axis label 
plt.xlabel('x - axis') 
# frequency label 
plt.ylabel('y - axis') 
# plot title 
plt.title('My scatter plot!') 
# showing legend 
plt.legend() 
  
# function to show the plot 
plt.show() 


# In[62]:


import matplotlib.pyplot as plt 
  
# defining labels 
activities = ['eat', 'sleep', 'code', 'play'] 
  
# portion covered by each label 
slices = [30, 70, 80, 60] 
  
# color for each label 
colors = ['r', 'y', 'g', 'b'] 
  
# plotting the pie chart 
plt.pie(slices, labels = activities, colors=colors,  
        startangle=90, shadow = True, explode = (0, 0, 0.2, 0), 
        radius = 1.2, autopct = '%1.1f%%') 
  
# plotting legend 
plt.legend() 
  
# showing the plot 
plt.show() 


# In[31]:


# importing the required modules 
import matplotlib.pyplot as plt 
import numpy as np 
  
# setting the x - coordinates 
x = np.arange(0, 2*(np.pi), 0.1) 
# setting the corresponding y - coordinates 
y = np.sin(x) 
  
# potting the points 
plt.plot(x, y) 
  
# function to show the plot 
plt.show() 


# In[37]:


Names = ['Group A', 'Group B', 'Group C']
values = [50, 40, 100]

plt.figure(figsize=(15, 6))

plt.subplot(131)
plt.bar(Names, values)
plt.subplot(132)
plt.scatter(Names, values)
plt.subplot(133)
plt.plot(Names, values)
plt.suptitle('Categorical Plotting')
plt.show()


# In[60]:


import matplotlib.pyplot as plt

Products = ['Apple', 'Oneplus', 'Huawei', 'RealMe']

proportions = [80, 70, 40, 50]

colors = ['b', 'y', 'g', 'r']

plt.pie(proportions, labels=Products, colors=colors,
        startangle=20, shadow=bool, explode=(0, 0, 0.2, 0),
        radius=1.2, autopct='%1.1f%%')


#plt.title('Market share of smart phones')
plt.legend()
plt.show()


# In[78]:


import matplotlib.pyplot as plt
import numpy as np
import math
x = np.arange(0, math.pi*2, 0.05)
fig=plt.figure()
axes1 = fig.add_axes([0.1, 0.2, 0.8, 0.7]) # main axes
axes2 = fig.add_axes([0.55, 0.55, 0.3, 0.3]) # inset axes
axes3 = fig.add_axes([0.2, 0.3, 0.2, 0.1]) # inset axes
axes1.plot(x, np.sin(x), 'b')
axes2.plot(x,np.cos(x),'r')
axes3.plot(x,np.tan(x),'g')
axes1.set_title('sine')
axes2.set_title("cosine")
axes3.set_title("tangent")
plt.show()


# In[ ]:




