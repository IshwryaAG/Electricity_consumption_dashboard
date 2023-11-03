'''
Name: Ishwrya Achuthan Geetha
andrewID: iachutha
Course Number: 12746-A2
Final project -'Electricity Consumption Dashboard'
'''

#Importing the modules 
import streamlit as st 
import plotly
import plotly.express as px
#import plotly.figure_factory as ff
import pandas as pd 

st.title('Electricity Consumption Dashboard') #Displays the title of the dashboard

#Creation of dataframes, Reading the dataframes and assigning it to dataframes
df1=pd.read_csv("A_total.csv") #Reading the data for house A
df2=pd.read_csv("B_total.csv") #Reading the data for house B
df3=pd.read_csv("C_total.csv") #Reading the data for house C

#Creating a list of the houses 
house_option=['A','B','C']
house=st.selectbox('Select house',house_option) #Creating a dropdown list on the dashboard

#Conditional statements to allot the dataframes
if house=='A':  #The data for house A is df1, therefore the DataFrame for the first house is df1, consisting of compiled data for A
    df= df1

if house=='B':#The data for house B is df2, therefore the DataFrame for the first house is df2, consisting of compiled data for B
    df=df2

if house=='C':#The data for house C is df2, therefore the DataFrame for the first house is df2, consisting of compiled data for C
    df=df3

#A dropdown list to select the year desired to see the electricity consumption
year_option=df['Year'].unique().tolist() #lists the years available for the house selected 
year=st.selectbox('Select year',year_option)
df = df[df['Year']==year] #Selecting the year from the DataFrame 

annual_consumption= df.iloc[:,-1].sum() #Calculates the summation of all total consumption of each row,ie., every 30 minutes

st.write("Total consumption for", year, " is : ", annual_consumption,'kW') #Displaying the overall consumption for the year

#Creating a temparory DataFrame which takes the data of each appliance
dftemp = df.iloc[:,5:-1]
sum_dftemp= dftemp.sum(axis=0, skipna=True) #Summation of the consumption of respective appliance 

dftemp = df.iloc[:,5:-1]
sum_dftemp= dftemp.sum(axis=0, skipna=True)

i = sum_dftemp[sum_dftemp==sum_dftemp.max()].index.values
st.write("The maximum consumption from an appliance ", sum_dftemp.max(),", is from:",i[0] ) #Displays the maximum consumption from each appliance, and displays which one contributes the most 
fig = px.bar(df, x='Month', y='total_consumption') #Displays the graph representing Month vs Total Consumption
st.plotly_chart(fig)

#Creating a dropdown list displaying all the months
month_option=df['Month'].unique().tolist() 
month=st.selectbox('Select month',month_option)
df = df[df['Month']==month]
a= df.iloc[:,-1].sum() #Evaluating the summation of the consumption of each month 
st.write("Total consumption for the selected month: ", a,'kW')

#Creating a dropdown list displaying all the appliances 
appliance_option= df.columns
appliance= st.selectbox('Select appliance', appliance_option, 0)
st.write(appliance)

dftemp= df[appliance]


fig=px.line(df, x= 'Date & Time', y=dftemp) #Plotting the graph between Appliance(X-axis) and Date&Time (Y-axis)
st.plotly_chart(fig) #Displaying it on the dashboard

dftemp = df.iloc[:,5:-1]
sum_dftemp= dftemp.sum(axis=0, skipna=True)

i = sum_dftemp[sum_dftemp==sum_dftemp.max()].index.values
st.write("The maximum consumption from an appliance ", sum_dftemp.max(),", is from:",i[0]) #Displays the overall consumption of the appliance and respective appliance





#Code used for pandas merging 
"""
import pandas as pd 

#Creating DataFrames with the csv files
df1=pd.read_csv("A_result_2014.csv")
df2=pd.read_csv("A_result_2015.csv")
df3=pd.read_csv("A_result_2016.csv")

total= pd.concat([df1, df2]) #Merging 2014 and 2015 data
A_total= pd.concat([total, df3]) #Merging 2014, 15 and 16 year data

print(A_total.shape) #Seeing the dimension of the file
A_total.to_csv('A_total.csv') #Converting the DataFrame created to .csv file"""
