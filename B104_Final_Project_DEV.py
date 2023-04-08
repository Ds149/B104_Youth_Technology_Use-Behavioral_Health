##Final Project V1.0
#Class: CSCI/ISAT B104 - Spring
#Authors:
    #Scheer, Daniel
    #Hirshout, Gaetano
    
def main():
    
    #Import of assets
    import pandas as pd
    import numpy as np
    import seaborn as sns
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    import scipy.stats as sp
    
    #Import of dataset's to pandas dataframe
    yrbs_dataset = pd.read_csv('Final_filter_YRBSS_dataset.csv', sep = ',')
    mtf_dataset = pd.read_csv('Final_filter_MTF_dataset.csv', sep = ',')

    
    #--------------------------------------------------- Settings -----------------------------------------------------#
    #Menu Settings:
    #printing and indexing of graphical functions will be counted from left to right in menu loops:
    show_functions = ['YRBSS - Heatmap - filtered questions.', 'YRBSS - Stacked Histogram - Y:count X:Q80 Hue:Q25', 
                           'MTF - Plot-Type - 1', 'MTF - Plot-Type - 2', 'YRBS - Chi square - test', 'MTF - Chi square - test'] 

    #name list for questions in dataset, used for most graphical functions: (Long form)
    yrbs_question_names = ['25. Sad or Hopeless','80. Computer Use (Screen Time)']
    
    yrbs_col_names = ['Sad/hopeless', 'Screen time','Age', 'Sex' ,'Gender Identity', 'Sexual Partners', 'Race']
    
    #Index for anwser values in quesiton 80 - YRBS dataset
    q80_index = ['0 h/day', '<1 h/day', '1 h/day', '2 h/day', '3 h/day', '4 h/day', '>=5 h/day']
    
    #Index for anwser values in question 25 - YRBS dataset
    q25_index = ['No', 'Yes']
    
    #Index for anwser values for age column - YRBS dataset
    yrbs_age_index = ['12 years old or younger', '13 year sold','14 years old','15 years old',
                     '16 years old','17 years old','18 years old or older',]
    
    #------------------------------------------------------------------------------------------------------------------#
    #YRBSS dataset functions
       
   
    #YRBS stacked histogram         
    def yrbs_stacked_histogram(col_names, q80_index, q25_index, yrbs_age_index):
        
        #Set subplot size and res
        f, ax = plt.subplots(figsize = (12, 9), dpi = 300)    
        
        #Color scheme for hues in histogram
        colors = {1:'#38AFC9', 2:'#081A40'}
        
        #Plot histogram using y = count x = question 80, hue = question 25
        sns.histplot(data = yrbs_dataset, stat = "count", multiple = "stack", kde = False , bins = 7, palette = colors, hue = yrbs_dataset.q25, x = yrbs_dataset.q80, element = "bars", legend = True)
        
        #Set question name x axis + spacing of xtick lables
        ax.set(xlabel = col_names[1], xticks = ([1.4, 2.3, 3.15, 4, 4.8, 5.7, 6.6]), xticklabels = q80_index)
        
        #set hue question name
        ax.legend(title=col_names[0],labels = q25_index)
        
        ax.plot()
        plt.show()
        
    def yrbs_heatmap_full(yrbs_col_names):
        
        plt.figure(figsize=(12, 9), dpi = 300)
        
        yrbs_filter = yrbs_dataset[['q25', 'q80', 'age', 'sex', 'q65', 'q66', 'race7']].corr()
        
        sns.heatmap(data = yrbs_filter, fmt = '.1f', linewidths = 1, cmap='Blues', annot = True, xticklabels= yrbs_col_names, yticklabels= yrbs_col_names)
        plt.xticks(rotation=30)
        plt.yticks(rotation=30)
        
        plt.show()
        
        
    #------------------------------------------------------------------------------------------------------------------#
    #MTF dataset functions    
    
    
    
    #------------------------------------------------------------------------------------------------------------------#
    #Misc functions
    
    def yrbs_chi_squared_test(q80_index): # semi working produces output values
       yrx_data = pd.crosstab(yrbs_dataset['q25'], yrbs_dataset['q80']).T
       
       c, p, dof, expected = sp.chi2_contingency(yrx_data)
       
       print('P-value: ', p)
       print('Test Statistic: ', c)
       print('Degrees of freedom: ', dof)
       
       

    def mtf_chi_squared_test(): # same as above
    
        #transform data for scipy.stats function
        mtf_data = pd.crosstab(mtf_dataset['V7302'],mtf_dataset['V7685']).T

        #scipy.stats - chi2 squared function
        c, p, dof, expected = sp.chi2_contingency(mtf_data)
        
        print('P-value: ', p)
        print('Test Statistic: ', c)
        print('Degrees of freedom: ', dof)

    
    #------------------------------------------------------------------------------------------------------------------#
    #menu functions
    
    def print_menu(show_functions):
        print('------------------------------------------------------------------------------')
        print('Welcome! \nThis program creates plots for parts of the YRBSS Youth risk survey \n& the University of Michigan MTF survey')
        print('------------------------------------------------------------------------------')
        
        print('\nEnter the number of plot to create:')
        print('#0: Back / Exit')
        for i in range(1, len(show_functions) + 1, 1):
            print(f'#{i}: {show_functions[i - 1]}')

    #------------------------------------------------------------------------------------------------------------------#
    #menu control logic
    
    #main loop
    while (True):
        
        #user input + variable type validation
        try:
            print_menu(show_functions)
            user_input = input('#: ')
            user_input = int(user_input)
            
            #If to  call menu option #0
            if (user_input == 0):
                break
            
            #elif to call menu option #1
            elif (user_input == 1):
                print('Creating plot')
                yrbs_heatmap_full(yrbs_col_names)
                
                
            #elif to call menu option #2
            elif (user_input == 2):
                print('Creating plot')
                yrbs_stacked_histogram(yrbs_question_names, q80_index, q25_index, yrbs_age_index)
                
            #elif to call menu option #3
            elif (user_input == 3):
                print('Creating plot')
                
            
            #elif to call menu option #4
            elif (user_input == 4):
                print('Creating plot')
                #tbc
                
            #elif to call menu option #5
            elif (user_input == 5):
                print('Creating plot')
                yrbs_chi_squared_test(q80_index)
                
            #elif to call menu option #6
            elif (user_input == 6):
                print('Creating plot')
                mtf_chi_squared_test()
            
            #invalid input integer not in list
            else:
                #print('\nThe entered value is invalid. Please enter the number of a plot:')
                print('test')
            
        except:
            print('\nThe entered value is invalid. Please enter the number of a plot:')
            

main()

##Verify chi squared 

##Usefull links:
    #https://python-course.eu/numerical-programming/creating-subplots-in-matplotlib.php #matplotlib subplots info
    #https://dev.to/thalesbruno/subplotting-with-matplotlib-and-seaborn-5ei8 # more matplotlib subplot info
    #https://datascience.stackexchange.com/questions/31746/how-to-include-labels-in-sns-heatmap #Seaborn change fontsize etc