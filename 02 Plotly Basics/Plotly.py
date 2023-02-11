#!/usr/bin/env python
# coding: utf-8

# # Introduction to Plotly

# ## Scatter Plot
# Scatter plots allow the comparison of two variables for a set of data. \
# Depending on the trend of te scatter points, we could interpret a correlation.

# In[29]:


import pandas as pd
import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go


# In[2]:


np.random.seed(42)
random_x = np.random.randint(1, 101, 100)
random_y = np.random.randint(1, 101, 100)


# In[3]:


data = [go.Scatter(x= random_x, y= random_y, mode= 'markers')]
pyo.plot(data, filename='Scatter_Plot_01.html')


# In[4]:


data = [go.Scatter(
                    x= random_x, 
                    y= random_y, 
                    mode= 'markers',
                    marker= dict(
                                size= 12,
                                color= 'rgb(51, 204, 153)',
                                symbol= 'star',
                                line= {'width': 2}
                    ))]

layout = go.Layout(
                    title= 'Correlation Between Two Variables',
                    xaxis= {'title': 'MY X AXIS'},
                    yaxis= dict(title='MY Y AXIS'),
                    hovermode= 'closest'
                )

fig = go.Figure(data= data, layout= layout)
pyo.plot(fig, filename='Scatter_Plot_02.html')


# ## Line Chart 
# A line chart displays a series of data points (markers) connected by line segments. \
# Similar to scatter plot, but the measurement points are orders (typically by their x-axis value) and joined with straight line segments \
# Often used to visualize a trend in data over intervals of time (time series)

# ### Part I

# In[5]:


np.random.seed(56)
x_values = np.linspace(0, 1, 100)
y_values = np.random.randn(100)


# In[6]:


trace0 = go.Scatter(x= x_values, y= y_values+7, 
                    mode= 'markers', name= 'markers')
trace1 = go.Scatter(x= x_values, y= y_values, 
                    mode= 'lines', name= 'mylines')
trace2 = go.Scatter(x= x_values, y= y_values-7, 
                    mode= 'lines+markers', name= 'line+markers')

data = [trace0, trace1, trace2]

layout = go.Layout(title= 'Line Chart')
fig = go.Figure(data= data, layout= layout)
pyo.plot(fig, filename= 'Line_Chart')


# ### Part II

# In[7]:


df = pd.read_csv('../Data/nst-est2017-alldata.csv')
df.head()


# In[8]:


df2 = df[df['DIVISION'] == '1']
df2.set_index('NAME', inplace= True)

# LIST COMPREHENSION
list_of_pop_col = [col for col in df2.columns if col.startswith('POP')]
df2 = df2[list_of_pop_col]


# In[9]:


df2.head()


# In[10]:


data = [go.Scatter(
                    x= df2.columns,
                    y= df2.loc[name],
                    mode= 'lines',
                    name= name) for name in df2.index]
pyo.plot(data, filename= 'Scatter_Plot_02')


# ### Exercise
# Objective: Using the file 2010YumaAZ.csv, develop a Line Chart that plots seven days worth of temperature data on one graph. \
# You can use a for loop to assign each day to its own trace.

# In[10]:


# Perform imports here:
import pandas as pd
import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go


# Create a pandas DataFrame from 2010YumaAZ.csv
df = pd.read_csv('../Data/2010YumaAZ.csv')
days = ['TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY','MONDAY']
df

# Use a for loop (or list comprehension to create traces for the data list)
data = [{
    'x': df.LST_TIME,
    'y': df[df.DAY == day].T_HR_AVG,
    'mode': 'lines',
    'name': day
} for day in df.DAY.unique()]

for day in days:
    # What should go inside this Scatter call?
    trace = go.Scatter()
    data.append(trace)

# Define the layout
layout = go.Layout(title= 'Daily temperatures', hovermode= 'x unified')


# Create a fig from data and layout, and plot the fig
fig = go.Figure(data= data, layout= layout)
pyo.plot(fig, filename= 'Exercise_Line_Plot')


# In[12]:


df


# ## Bar Charts
# - A Bar chart presents categorial data with rectangular bars with heigths (or lengths) proportional to the values that they represent;
# - Can be **Continuous** or **Categorical**:
#     - The weight, height and age of respondents in a survey would represent continuous variable;
#     - person's gender, occupation, or marital status are categorial or discrete variables.
# - With Bar Charts we can visualize categorical data.
# - Tipycally the x-axis is the categories and the y-axis is the count (occurences) in each category;
#     - However, the y-axis can be any aggregation (count, sum, average, etc).
# 
# 

# In[13]:


df = pd.read_csv('../Data/2018WinterOlympics.csv')
df.head(7)


# Normal Bar Chart with only one element (totals)

# In[14]:


data = [go.Bar(
                x=df.NOC,
                y= df.Total)]
                
layout = go.Layout(title= 'Medals')
fig = go.Figure(data= data, layout= layout)
pyo.plot(fig, filename= 'Bar_Medals_01')


# Nested Bar chart

# In[15]:


trace_gold = go.Bar(x= df.NOC, 
                y= df.Gold, 
                name= 'Gold', 
                marker= {'color': '#FFD700'})

trace_silver = go.Bar(x= df.NOC, 
                y= df.Silver, 
                name= 'Silver', 
                marker= {'color': '#9EA0A1'})

trace_bronze = go.Bar(x= df.NOC, 
                y= df.Bronze, 
                name= 'Bronze', 
                marker= {'color': '#CD7F32'})

data = [trace_gold, trace_silver, trace_bronze]
layout = go.Layout(title= 'Medals')
fig = go.Figure(data= data, layout= layout)
pyo.plot(fig, filename= 'Bar_Medals_02')


# Normal Bar chart (Stacked) with **barmode** setted

# In[16]:


trace_gold = go.Bar(x= df.NOC, 
                y= df.Gold, 
                name= 'Gold', 
                marker= {'color': '#FFD700'})

trace_silver = go.Bar(x= df.NOC, 
                y= df.Silver, 
                name= 'Silver', 
                marker= {'color': '#9EA0A1'})

trace_bronze = go.Bar(x= df.NOC, 
                y= df.Bronze, 
                name= 'Bronze', 
                marker= {'color': '#CD7F32'})

data = [trace_gold, trace_silver, trace_bronze]
layout = go.Layout(title= 'Medals', barmode= 'stack')
fig = go.Figure(data= data, layout= layout)
pyo.plot(fig, filename= 'Bar_Medals_03')


# ### Exercise
# Objective:
# \
# Create a stacked bar chart from the file ../data/mocksurvey.csv. Note that questions appear in the index (and should be used for the x-axis), while responses appear as column labels.  Extra Credit: make a horizontal bar chart!

# In[17]:



#######

######

# create a DataFrame from the .csv file:
df = pd.read_csv('../Data/mocksurvey.csv', index_col= 0)


# create traces using a list comprehension:
traces = [go.Bar({
        'x': df.index,
        'y': df[response],
        'orientation': 'h',
        'name': response
}) for response in df.columns]





# create a layout, remember to set the barmode here
layout = go.Layout(title= 'Survey Results - Bar Chart', barmode= 'stack')
fig = go.Figure(data= traces, layout= layout)
pyo.plot(fig, filename= 'Exercise_Bar_Chart')




# create a fig from data & layout, and plot the fig.


# In[18]:


df.head()


# ## Bubble Charts
# - Very similar to scatter plots, except we have a third variable information through the size of the markers;
# - We can also continue to add variable information by coloring points based on a category;

# In[20]:


df = pd.read_csv('../Data/mpg.csv')
df.head(5)


# In[22]:


data = [go.Scatter(
                    x= df.horsepower,
                    y= df.mpg,
                    text= df.name,
                    mode= 'markers',
                    marker= dict(size= 2*df.cylinders)
                )]

layout = go.Layout(title= 'Bubble chart')
fig = go.Figure(data= data, layout= layout)
pyo.plot(fig, filename= 'Bubble_Chart_01')


# In[25]:


data = [go.Scatter(
                    x= df.horsepower,
                    y= df.mpg,
                    text= df.name,
                    mode= 'markers',
                    marker= dict(size= df.weight/200)
                )]

layout = go.Layout(title= 'Bubble chart')
fig = go.Figure(data= data, layout= layout)
pyo.plot(fig, filename= 'Bubble_Chart_02')


# In[27]:


data = [go.Scatter(
                    x= df.horsepower,
                    y= df.mpg,
                    text= df.name,
                    mode= 'markers',
                    marker= dict(size= df.weight/100, color= df.cylinders, showscale= True)
                )]

layout = go.Layout(title= 'Bubble chart')
fig = go.Figure(data= data, layout= layout)
pyo.plot(fig, filename= 'Bubble_Chart_03')


# ### Bubble Chart Exercises
# 
# Objective:  
# Create a bubble chart that compares three other features
# from the mpg.csv dataset. \
# Fields include: 'mpg', 'cylinders', 'displacement'
# 'horsepower', 'weight', 'acceleration', 'model_year', 'origin', 'name'

# In[35]:


# create a DataFrame from the .csv file:
df = pd.read_csv('../Data/mpg.csv')

# create data by choosing fields for x, y and marker size attributes
data = [go.Scatter(
                    x= df.acceleration,
                    y= df.horsepower,
                    text= df.name,
                    marker= dict(size= df.mpg/2, color= df.model_year, showscale= True),
                    mode= 'markers'

)]

# create a layout with a title and axis labels
layout = go.Layout(title= 'Bubble Chart Exercise', hovermode= 'closest')

# create a fig from data & layout, and plot the fig
figure = go.Figure(data= data, layout= layout)
pyo.plot(figure, filename= 'Exercise_Bubble_Chart')


# In[28]:


df.head(3)


# ## Box Plots
# - Box Plots visualize the variation of a feature by depicting the continuous numerical data through quartiles;
# - We can then separate the data based on a categorical feature to compare the continuous feature based on category;
# - The Box Plot is a way of visually displyaing the data distribution through their quartiles;
# - We can use it to perform a real analysis.

# In[38]:


y = [1,14,14,15,16,18,18,19,19,20,20,23,24,26,27,27,28,29,33,54]

data = [go.Box(y=y, boxpoints= 'all', jitter=0.3, pointpos= 0)]
pyo.plot(data, filename= "Box_Plot_01")


# Displaying **ONLY** the Outliers

# In[40]:


y = [1,14,14,15,16,18,18,19,19,20,20,23,24,26,27,27,28,29,33,54]


data = [go.Box(y=y, boxpoints= 'outliers')]
pyo.plot(data, filename= "Box_Plot_02")


# Three-word frequency analysis between Twain and Snodgrass

# In[4]:


snodgrass = [.209,.205,.196,.210,.202,.207,.224,.223,.220,.201]
twain = [.225,.262,.217,.240,.230,.229,.235,.217]

data = [
        go.Box(y=snodgrass, name= 'Snoodgrass'),
        go.Box(y= twain, name= 'Twain')
        ]
pyo.plot(data, filename= "Box_Plot_03")


# ### Exercise
# - Objective: Make a DataFrame using the Abalone dataset (../data/abalone.csv).
# - Take two independent random samples of different sizes from the 'rings' field.
#     - HINT: np.random.choice(df['rings'],10,replace=False) takes 10 random values
# - Use box plots to show that the samples do derive from the same population.

# In[13]:


# create a DataFrame from the .csv file:
df = pd.read_csv('../Data/abalone.csv')

# take two random samples of different sizes:
sample_1 = np.random.choice(df.rings, 10, replace= False)
sample_2 = np.random.choice(df.rings, 24, replace= False)

# create a data variable with two Box plots:
data = [
        go.Box(y= sample_1, name= 'Sample 1'),
        go.Box(y= sample_2, name= 'Sample 2')
]

# add a layout
layout = go.Layout(title= 'Bubblet Chart exercise')

# create a fig from data & layout, and plot the fig
fig = go.Figure(data= data, layout= layout)
pyo.plot(fig, filename= 'Exercise_Bubble_Chart')


# ## Histogram
# - Display an accurate representation of the overall distribution of a continuous feature;
# - To create a histogram, we divide the entire range of values of the continuous feature into a series of intervals;
#     - This series of intervals are known as "bins";
# - We then conunt the number of occurences per bin;
# - We can change the bin size to get either more or less details.

# In[15]:


df = pd.read_csv('../Data/mpg.csv')

data = [go.Histogram(x= df.mpg)]
layout = go.Layout(title= 'Histogram')
fig = go.Figure(data= data, layout= layout)

pyo.plot(fig, filename= 'Histogram_01')


# Setting the bins

# In[25]:


df = pd.read_csv('../Data/mpg.csv')

data = [
        go.Histogram(x= df.mpg,
        xbins= dict(start= 0, end= 50, size= 10)
    )]
layout = go.Layout(title= 'Histogram Size 10')
fig = go.Figure(data= data, layout= layout)

pyo.plot(fig, filename= 'Histogram_01.html');


# In[26]:


df = pd.read_csv('../Data/mpg.csv')

data = [
        go.Histogram(x= df.mpg,
        xbins= dict(start= 0, end= 50, size= 2)
    )]
layout = go.Layout(title= 'Histogram Size 2')
fig = go.Figure(data= data, layout= layout)

pyo.plot(fig, filename= 'Histogram_02.html');


# ### Exercise
# - Objective: Create a histogram that plots the 'length' field from the Abalone dataset (../data/abalone.csv).
# - Set the range from 0 to 1, with a bin size of 0.02

# In[29]:


# create a DataFrame from the .csv file:
df = pd.read_csv('../Data/abalone.csv')


# create a data variable:
data = [
        go.Histogram(
            x= df.length,
            xbins= dict(
                start=0 , end=1 , size= 0.02
            )

        )]


# add a layout
layout = go.Layout(title= 'Exercise - Histogram of Length Field')
fig = go.Figure(data= data, layout= layout)

# create a fig from data & layout, and plot the fig
pyo.plot(fig, filename= 'Exercise_Histogram')


# ## Distribution Plot
# - Known as Distplots, tipycally layer three plots on top of one another;
# - The first is a histogram, where each data point is placed inside a bin of similar values;
# - The second is a rug plot, where marks are placed along the x-axis for every data point;
#     - Which let you see the distribution of values inside each bin.
# - The third plot, include a **Kernel Density Estimate** (KDE) line that tries to describe the shape of the distribution.

# In[7]:


import scipy
import plotly.offline as pyo
from plotly.tools import FigureFactory as ff ## More complex figures
import numpy as np
import pandas as pd


# In[5]:


x1 = np.random.randn(1000)+2


hist_data = [x1]
group_labels = ['X1']

fig = ff.create_distplot(hist_data, group_labels);
pyo.plot(fig, filename= 'Distplot_01');


# In[4]:


x1 = np.random.randn(1000)+2
x2 = np.random.randn(1000)
x3 = np.random.randn(1000)-2
x4 = np.random.randn(1000)+4


hist_data = [x1, x2, x3, x4]
group_labels = ['X1', 'X2', 'X3', 'X4']

fig = ff.create_distplot(hist_data, group_labels);
pyo.plot(fig, filename= 'Distplot_02');


# ### Exercise
# - Objective: Using the iris dataset, develop a Distplot that compares the petal lengths of each class.
# - File: '../data/iris.csv'
#     - Fields: 'sepal_length','sepal_width','petal_length','petal_width','class'
#     - Classes: 'Iris-setosa','Iris-versicolor','Iris-virginica'

# In[26]:


# create a DataFrame from the .csv file:
df = pd.read_csv('../Data/iris.csv')


# Define the traces

# HINT:
# This grabs the petal_length column for a particular flower
x1 = df[df['class']=='Iris-setosa']['petal_length']
x2 = df[df['class']=='Iris-versicolor']['petal_length']
x3 = df[df['class']=='Iris-virginica']['petal_length']

# Define a data variable
data = [x1, x2, x3]
group_labels= ['Iris Setosa','Iris Versicolor','Iris Virginica']

# Create a fig from data and layout, and plot the fig
fig = ff.create_distplot(data, group_labels)
pyo.plot(fig, filename= 'Exercise_distplot')


# ## Heatmap
# - Heatmaps allow the visualization of three features:
#     -  categorical or continuoufeatures along the x and y axis to make up a grid;
#         - It can be categorical features on both x and y axis.
#     - a 3rd continuous feature displayed through color.

# In[35]:


df = pd.read_csv('../Data/2010SantaBarbaraCA.csv')

data = [go.Heatmap(
                    x=df.DAY, 
                    y= df.LST_TIME, 
                    z= df.T_HR_AVG.values.tolist())]
layout = go.Layout(title= 'SB CA Temps');
fig = go.Figure(data= data, layout= layout);

pyo.plot(fig, filename= 'Heatmap_01');


# Change color scale

# In[44]:


df = pd.read_csv('../Data/2010SantaBarbaraCA.csv')

data = [go.Heatmap(                    
                    x=df.DAY, 
                    y= df.LST_TIME, 
                    z= df.T_HR_AVG.values.tolist(),
                    colorscale= 'Jet')]
layout = go.Layout(title= 'YU MA Temps');
fig = go.Figure(data= data, layout= layout);

pyo.plot(fig, filename= 'Heatmap_02');


# Multiple Heatmaps with Subplots

# In[50]:


from plotly import tools

df1 = pd.read_csv('../Data/2010SitkaAK.csv')
df2 = pd.read_csv('../Data/2010SantaBarbaraCA.csv')
df3 = pd.read_csv('../Data/2010YumaAZ.csv')

trace1 = go.Heatmap(
    x= df1.DAY,
    y= df1.LST_TIME,
    z= df1.T_HR_AVG,
    colorscale= 'Jet',
    zmin= 5,
    zmax= 40
)

trace2 = go.Heatmap(
    x= df2.DAY,
    y= df2.LST_TIME,
    z= df2.T_HR_AVG,
    colorscale= 'Jet',
    zmin= 5,
    zmax= 40
)

trace3 = go.Heatmap(
    x= df3.DAY,
    y= df3.LST_TIME,
    z= df3.T_HR_AVG,
    colorscale= 'Jet',
    zmin= 5,
    zmax= 40
)

fig = tools.make_subplots(
    rows= 1, 
    cols= 3, 
    subplot_titles= ['Sitka AK', 'SB CA', 'YUMA AZ'], 
    shared_yaxes=True)
    
fig.append_trace(trace1, 1, 1)
fig.append_trace(trace2, 1, 2)
fig.append_trace(trace3, 1, 3)
fig.layout.update(title= 'Multiple Heatmaps with Subplots')

pyo.plot(fig, filename= 'Heatmap_03.html');


# ### Exercise
# - Objective: Using the "flights" dataset available
# - from the data folder as flights.csv
# - create a heatmap with the following parameters:
# - x-axis="year"
# - y-axis="month"
# - z-axis(color)="passengers"

# In[59]:


# Create a DataFrame from  "flights" data
df = pd.read_csv('../Data/flights.csv')

# Define a data variable
data = [go.Heatmap(
    x= df.year,
    y= df.month,
    z= df.passengers,
)]

# Define the layout
layout = go.Layout(title= 'Heatmaps Exercise - Flights Dataset')

# Create a fig from data and layout, and plot the fig
fig = go.Figure(data= data, layout= layout)
pyo.plot(fig, filename= 'Exercise_Heatmap.html');

