#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[7]:


df=pd.read_csv('supermarket_sales - Sheet1.csv')
df.head()


# - Invoice id: Computer generated sales slip invoice identification number
# 
# - Branch: Branch of supercenter (3 branches are available identified by A, B and C).
# 
# - City: Location of supercenters
# 
# - Customer type: Type of customers, recorded by Members for customers using member card and Normal for without member card.
# 
# - Gender: Gender type of customer
# 
# - Product line: General item categorization groups - Electronic accessories, Fashion accessories, Food and beverages, Health and beauty, Home and lifestyle, Sports and travel
# 
# - Unit price: Price of each product in $
# 
# - Quantity: Number of products purchased by customer
# 
# - Tax: 5% tax fee for customer buying
# 
# - Total: Total price including tax
# 
# - Date: Date of purchase (Record available from January 2019 to March 2019)
# 
# - Time: Purchase time (10am to 9pm)
# 
# - Payment: Payment used by customer for purchase (3 methods are available – Cash, Credit card and Ewallet)
# 
# - COGS: Cost of goods sold
# 
# - Gross margin percentage: Gross margin percentage
# 
# - Gross income: gross income is all the money you earn before taxes and other deductions are subtracted.
# 
# - Rating: Customer stratification rating on their overall shopping experience (On a scale of 1 to 10)

# In[60]:


total=(df['Unit price']*df['Quantity'])+df['Tax 5%']
total


# In[61]:


522.83*7


# In[62]:


522.8299999999999+(522.8299999999999*(5/100))


# In[63]:


#  Gross Margin % = (Revenue – Cost of Goods Sold) / Revenue x 100
gross_Margin=(df['Total']- df['cogs'])/df['Total']*(100)
gross_Margin


# In[64]:


df.shape


# In[65]:


df.info()


# In[66]:


df.describe()


# In[67]:


df.isna().sum()


# In[ ]:





# In[68]:


df['City']


# In[69]:


for i in df:
    if df[i].dtype=='object':
        print(i,'.......',df[i].dtype)


# In[3]:


# find object variables in dataset

obj= [i for i in df if df[i].dtype=='object']

print('The object variables are :',obj)


# In[4]:


# find numerical variables in dataset

numerical = [col for col in df if df[col].dtype!='object']

print('The numerical variables are :', numerical)


# In[72]:


df1=df


# # Categorical Variables

# In[73]:


# for i in obj:
   
#     if i!='Invoice ID' and i!='Date' and i!='Time':
#         print('columns',i)
#         print('no of unique in',i, 'is', df[i].nunique())
#         print('these are the unique in', i, df[i].unique())


# In[123]:


df.head()


# In[74]:


for i in obj:
    if i!='Invoice ID' and i!='Date' and i!='Time':
        print(i,'...',df[i].nunique(),'......',df[i].unique())
        print(i,'.........',df[i].value_counts())


# In[75]:


print("The count of unique values in City variable is ",df['City'].nunique())
print("The unique values in City variable are ",df['City'].unique())


# In[76]:


print("The count of unique values in Customertype variable is ",df['Customer type'].nunique())
print("The unique values in Customertype variable are ",df['Customer type'].unique())


# In[77]:


print("The count of unique values in Gender variable is ",df['Gender'].nunique())
print("The unique values in Gender variable are ",df['Gender'].unique())


# In[78]:


print("The count of unique values in Payment variable is ",df['Payment'].nunique())
print("The unique values in Payment variable are ",df['Payment'].unique())


# In[79]:


print("The count of unique values in Productline variable is ",df['Product line'].nunique())
print("The unique values in Productline variable are ",df['Product line'].unique())


# In[7]:


df[obj].head()


# In[5]:


z=df.select_dtypes(include='object')
z.head()


# In[81]:


plt.figure(figsize=(22,6))
c=1
for i in z:
    if i!='Invoice ID' and i!='Date' and i!='Time' and i!='Product line':
        
        plt.subplot(1,5,c)
        sns.countplot(x = z[i], data = z)
        plt.xticks(rotation=90,fontsize=15)
        c=c+1 # c+=1
plt.show()

sns.countplot(x = z['Product line'],data = z)
plt.xticks(rotation=90);
        


# In[82]:


plt.figure(figsize=(22,6))
plt.subplot(1,5,1)
sns.countplot(x = 'Branch', data = df1)
plt.subplot(1,5,2)
sns.countplot(x = 'City', data = df1)
plt.subplot(1,5,3)
sns.countplot(x = 'Customer type', data = df1)
plt.subplot(1,5,4)
sns.countplot(x = 'Gender', data = df1)
plt.subplot(1,5,5)
sns.countplot(x = 'Payment', data = df1)

plt.show()


# In[83]:


sns.countplot(x = 'Product line', data = df1)
plt.xticks(rotation=90);


# ## Analyzing the data

# ##### WHICH IS THE BEST PRODUCT LINE FOR EACH BRANCH ?

# In[84]:


df1=df.copy()


# In[85]:


pd.pivot_table(df1, index = 'Product line', columns = 'Branch' ,values = 'gross income' ,aggfunc =['count','mean'])


# In[ ]:





# In[31]:


a=df.groupby(['Product line','Branch'])['gross income'].agg(['count','mean'])
a


# In[30]:


a['gross income'].mean()


# In[29]:


a['Branch'].count()


# In[38]:


k=df.groupby(['Product line','Branch'])['gross income'].agg(['count','mean']).reset_index()
k


# In[39]:


sns.barplot(x='Product line',y='mean',hue='Branch',data=k)
plt.xticks(rotation=90);


# In[90]:


df1.head()


# ### Insigth 1 :WHICH IS THE BEST SELLING BRANCH ?

# In[8]:


l=df.groupby(['Branch'])['gross income'].sum().reset_index()
l


# In[138]:


plt.figure(figsize=(10,4))

plt.subplot(1,2,1)
plt.pie('gross income',labels='Branch',data=l,autopct='%0.2f%%')
plt.subplot(1,2,2)
sns.barplot(x='Branch',y='gross income',data=l);


# In[12]:


df


# ### Insight 2:WHICH BRANCH HAS HIGH RATING?

# In[9]:


u=df.groupby(['Branch'])['Rating'].mean().reset_index()
u


# In[11]:


plt.figure(figsize=(10,4))

plt.subplot(1,2,1)
plt.pie('Rating',labels='Branch',data=u,autopct='%0.5f%%')
plt.subplot(1,2,2)
sns.barplot(x='Branch',y='Rating',ci=None,data=u);


# so the branch c is the most branch have a high gross income and high rating so we select this branch to analysis it and create dataframe

# In[18]:


c=df[df['Branch']=='C']
c


# ### insights 3: classify gross income based on customer type?

# In[100]:


c.groupby(['Customer type'])['gross income'].sum().reset_index()


# In[101]:


c['Customer type'].value_counts()


# In[103]:


sns.countplot(x='Customer type',data=c);


# In[12]:


df.head(2)


# ### Insight 4: Which day has most gross income ?

# In[13]:


df['Date']=pd.to_datetime(df['Date'])


# In[14]:


df['Days']=df['Date'].dt.day_name()


# In[15]:


df['month']=df['Date'].dt.month_name()


# In[16]:


df


# In[111]:


df['Days'].unique()


# In[159]:


df['Weeks']=df['Days'].apply(lambda a :'Weekday' if a=='Monday' or a=='Tuesday' or a=='Wednesday'or a=='Thursday' or a=='Friday' else 'Weekend')


# In[160]:


df.head(2)


# In[161]:


df.groupby(['Weeks'])['gross income'].sum()


# In[10]:


i=df.groupby(['month','Days'])['gross income'].max().reset_index().sort_values(by='gross income',ascending=False)
i


# In[12]:


a=df.groupby('month')['gross income'].sum().reset_index().sort_values(by='gross income',ascending=False)
a


# In[16]:


plt.figure(figsize=(9,4),dpi=200)

plt.subplot(1,2,1)
sns.barplot(x='Days',y='gross income',hue='month',data=i)
plt.xticks(rotation=45)

plt.subplot(1,2,2)
sns.barplot(x='month',y='gross income',data=a)
plt.xticks(rotation=45)
plt.show()


# ### Insight 5 :what mode of payment is high ?

# In[47]:


sns.countplot(x='Payment',data=c);


# In[48]:


c['Payment'].value_counts()


# In[18]:


df.groupby(['Gender','Customer type','Payment'])['gross income'].sum()


# In[52]:


sns.catplot(x='Payment',hue='Gender',kind='count',col='Customer type',data=c);
 


# ### Insights 6:calculate the gross income with respect to product line

# In[42]:


Products=c.groupby(['Product line'])['gross income'].sum().reset_index()
Products


# In[21]:


sns.barplot(x='Product line',y='gross income',data=Products);
plt.xticks(rotation=90);


# ### Insights 7: Availability of product

# In[44]:


c['Product line'].value_counts(normalize=True)*100


# In[21]:


c['Product line'].value_counts().index


# In[45]:


c_index=c['Product line'].value_counts().index
c_index


# In[46]:


c_values=c['Product line'].value_counts().values
c_values


# In[47]:


plt.pie(c_values,labels=c_index,autopct='%.2f%%')
plt.show()


# In[ ]:


s='restartt'
# resta###


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[52]:


df.head(1)


# In[53]:


df['Time']=pd.to_datetime(df['Time'])
df['Hour']=df['Time'].dt.hour


# In[54]:


df.info()


# In[55]:


df.head(1)


# In[65]:


plt.figure(figsize=(12,8))
sns.lineplot(x='Hour',y='Quantity',data=df,ci=None)
plt.title('Product sales per hour', fontsize=20)
plt.xlabel('Time of the day', fontsize=15)
plt.xticks(df['Hour'].unique())
# plt.yticks(df['Quantity'].unique())
plt.ylabel('Quantity', fontsize=15)


# INSIGHTS: We can see that the sales is highest at 2pm. Good volume of sales is recorded around 5pm and 7pm. The sales is recorded to be the lowest around 10pm, 3pm and 4pm.

# In[74]:


plt.figure(figsize=(12,8))
sns.lineplot(x='Hour',y='Quantity',data=df, hue='Product line',ci=None)
plt.title('Product sales per hour', fontsize=20)
plt.xlabel('Time of the day', fontsize=15)
plt.ylabel('Quantity', fontsize=15)


# Health and Beauty products has no specific time of purchase Electronic sales are seen around 7 pm which is the end of daily work, when family can enjoy such shopping. Home and lifestyle is recorded around 5 pm and 7 pm which can be an ideal time for homemakers to make such purchases. Food and beverages are seen to be purchased more at 11 am which is an ideal time to purchase daily or weekly food items. Fashion accessories are seen to be purchased at 4 pm which can be an ideal time not only for adults but also for teenagers.

# In[ ]:




