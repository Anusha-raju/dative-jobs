#%%
print("Data Dive jobs")

# %%
import pandas as pd
data = pd.read_csv("/Users/anushaugwu.edu/Downloads/IND_2022_PLFS-Urban-Panel_V01_M_V01_A_GLD_ALL.csv")



#%%
# Group by industry and year
df_grouped = data.groupby(['year', 'industrycat_isic']).agg({
    'wage_no_compen': 'mean',
    'whours': 'mean',
    'njobs': 'sum',
    'firmsize_l_year': 'mean',
    'firmsize_u_year': 'mean',
}).reset_index()

# %%
import seaborn as sns
import matplotlib.pyplot as plt

# Scatter plot: Productivity vs Employment
sns.scatterplot(data=df_grouped, x='wage_no_compen', y='njobs', hue='industrycat_isic')

plt.title('Productivity vs Employment by Industry')
plt.xlabel('Average Wage (Productivity Indicator)')
plt.ylabel('Number of Jobs')
plt.show()



#%%
sns.regplot(data=df_grouped, x='whours', y='wage_no_compen')

plt.title('Relationship Between Last Reported Wage and Hours Worked')
plt.ylabel('Last reported wage')
plt.xlabel('Hours')
plt.show()

#%%
# Employment Status and Productivity (Wage vs. Employment Status)
sns.boxplot(x='empstat', y='wage_no_compen', data=data)
plt.title("Wages by Employment Status")
plt.show()

#%%
# Filter data by year and calculate average wage
wage_by_year = data.groupby('year')['wage_no_compen'].mean()

# Plot the trend of average wage over the years
plt.plot(wage_by_year.index, wage_by_year.values)
plt.xlabel('Year')
plt.ylabel('Average Wage')
plt.title('Average Wage Trend Over the Years')
plt.show()

# %%
employment_by_education = pd.crosstab(data['educat7'], data['empstat'])
print(employment_by_education)