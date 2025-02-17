# To Supress Scientific Notation of Values
import pandas as pd
pd.set_option('display.float_format', lambda x: '%.2f' % x) # for 2 float points

from simple_colors import * # for color print

class descriptivestats:
    
    ############################ Numeric Continuous ############################
    def ncstudy(self, df, col):
        print(green("#######################################################",['bold']))
        print(green("Taken Numeric Continuous Column:",['bold']), black(col,['bold']))
        print(green("#######################################################",['bold']))
        print()
        print(cyan("Uni-Variate Descriptive Stats:",['bold']))
        print()
        print(blue("******** Measures of Central Tendancy ************", ['bold']))
        print(magenta("Mean:",['bold']), round(df[col].mean(),2))
        print(magenta("Median:",['bold']), df[col].median())
        print(magenta("Mode:",['bold']), df[col].mode()[0]) # Taking first value
        print()
        print(blue("******** Measures of Dispersion ************",['bold']))
        print(magenta("Range:",['bold']), df[col].max()-df[col].min())
        print(magenta("Variance:",['bold']), round(df[col].var(),2))
        print(magenta("Standard Deviation:",['bold']), round(df[col].std(),2))
        print(magenta("Five Number Summary:",['bold']))
        print(round(data[col].describe(),2)[['min','25%','50%','75%','max']])
        print()
        print(blue("******** Measures of Symmetry ************",['bold']))
        print(magenta("Skewness:",['bold']), round(df[col].skew(),2))
        print(magenta("Kurtosis:",['bold']), round(df[col].kurt(),2))

    ############################## Numeric Discrete #################################
    def ndstudy(self, df, col):
        print(green("#######################################################",['bold']))
        print(green("Taken Numeric Discrete Column:",['bold']), black(col,['bold']))
        print(green("#######################################################",['bold']))
        print()
        print(cyan("Uni-Variate Descriptive Stats:",['bold']))
        print()
        print("******** Measures of Central Tendancy ************")
        print(magenta("Mean:",['bold']), round(df[col].mean()))
        print(magenta("Median:",['bold']), round(df[col].median()))
        print(magenta("Mode:",['bold']), df[col].mode()[0]) # Taking first value
        print()
        print("******** Measures of Dispersion ************")
        print(magenta("Range:",['bold']), df[col].max()-df[col].min())
        print(magenta("Variance:",['bold']), round(df[col].var()))
        print(magenta("Standard Deviation:",['bold']), round(df[col].std()))
        print(magenta("Five Number Summary:",['bold']))
        print(round(data[col].describe())[['min','25%','50%','75%','max']])
        print()
        print("******** Measures of Symmetry ************")
        print(magenta("Skewness:",['bold']), round(df[col].skew(),2))
        print(magenta("Kurtosis:",['bold']), round(df[col].kurt(),2))    

    ############################# Categorical #######################################
    def catstudy(self, df, col):
        print(green("#######################################################",['bold']))
        print(green("Taken Categorical Column:",['bold']), black(col,['bold']))
        print(green("#######################################################",['bold']))
        print()
        print(cyan("Uni-Variate Descriptive Stats:",['bold']))
        print()
        print(magenta("Number of Categories/Classes in column:",['bold']), df[col].nunique())
        print(magenta("Category Names:",['bold']))
        print(df[col].unique())
        print()
        print(magenta("Value Counts (FD) of each Category:",['bold']))
        print(df[col].value_counts())
        print()
        print(magenta("Value Counts of Each Class (FD) as Percentage:",['bold']))
        print(round((df[col].value_counts()/len(df))*100,2))
        print()
        print(magenta("Mode:",['bold']), df[col].mode()[0])

    ################################ DateTime ######################################
    def datestudy(self, df, col):
        print(green("#######################################################",['bold']))
        print(green("Taken Date Column:",['bold']), black(col,['bold']))
        print(green("#######################################################",['bold']))
        print()
        print(cyan("Uni-Variate Descriptive Stats:",['bold']))
        print()
        print(magenta("Start Date:",['bold']), df[col].min())
        print(magenta("End Date:",['bold']), df[col].max())
        print(magenta("Total Time Period (in Years):",['bold']), (df[col].max()-df[col].min()).days/365)