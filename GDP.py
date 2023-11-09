"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#Create the Line plots
def lineplot(gdp_df) :
    years = list(gdp_df.index)
    plt.xlim(years[0], years[-1])
    plt.plot(gdp_df.index, gdp_df, label=gdp_df.columns)
    plt.xlabel('Year')
    plt.ylabel('GDP')
    plt.title('GDP for India, UK, USA(1990 to 2018)')
    plt.legend()
    plt.savefig('gdp.png')
    plt.show()
    
#Create the PiePlot
def piechart(gdp_df) :
    gdp_1990 = gdp_df.loc[1990]
    plt.pie(gdp_1990, autopct='% 1.1f %%', labels=gdp_1990.index)
    plt.title('GDP Distribiution b/w India, UK, USA in 1990')
    plt.savefig('gdp_dist_1990.png')
    plt.show()

    gdp_2018 = gdp_df.loc[2018]
    plt.pie(gdp_2018, autopct='% 1.1f %%', labels=gdp_2018.index)
    plt.title('GDP Distribiution b/w India, UK, USA in 2018')
    plt.savefig('gdp_dist_2018.png')
    plt.show()
 
#Create the Barplot
def barchart(gdp_df) :
    gdp_1990 = gdp_df.loc[1990]
    gdp_2018 = gdp_df.loc[2018]
    width = 0.25
    r = np.arange(3)
    plt.bar(r, gdp_1990, color = 'b', 
            width = width, edgecolor = 'black', 
            label='1990')

    plt.bar(r + width, gdp_2018, color = 'g', 
            width = width, edgecolor = 'black', 
            label='2018')

    plt.xticks(r + width/2,['India', 'UK', 'USA'])
    plt.xlabel('Country')
    plt.ylabel('GDP')
    plt.title('Comparison of GDP for 1990 and 2018 for India, UK, USA')
    plt.legend()
    plt.savefig('gdp_comparison.png')
    plt.show()

#Read the data from csv file
df = pd.read_csv('GDP.csv', index_col='Country ')
df.drop(['Country Code'], axis=1, inplace=True)
gdp_df = df.loc[['India', 'United Kingdom', 'United States']].fillna(0)
print(gdp_df)
gdp_df.columns = list(map(int, gdp_df))
gdp_df = gdp_df.transpose()[:-1]
print(gdp_df)

lineplot(gdp_df)
piechart(gdp_df)
barchart(gdp_df)
