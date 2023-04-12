##Final Project V2.0
#Class: CSCI/ISAT B104 - Spring
#Authors:
    #Scheer, Daniel
    #Hirshout, Gaetano
    
def main():
    
    #Import of assets
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt
    import scipy.stats as sp
    
    #Import of dataset's to pandas dataframe
    yrbs_dataset = pd.read_csv('Final_filter_YRBSS_dataset.csv', sep = ',')
    mtf_dataset = pd.read_csv('Final_filter_MTF_dataset.csv', sep = ',')

    #sns.set(font_scale = 1.5)
    
    #--------------------------------------------------- Settings -----------------------------------------------------#
    #Menu Settings:
    #printing and indexing of graphical functions will be counted from left to right in menu loops:
    show_functions = ['YRBSS - Heatmap - filtered questions', 'YRBSS - Stacked Histogram - Y:count X:Q80 Hue:Q25', 
                      'MTF - Heatmap - full datatset', 'MTF - Stacked Histogram - Y:count X:V7685 Hue:V7302', 
                      'YRBS - Chi square - result', 'MTF - Chi square - result'] 

    #------------------------------------------------- YRBS Settings --------------------------------------------------#
    
    #name list for questions in dataset: (Long form)
    yrbs_question_names = ['25. Sad or Hopeless','80. Computer Use (Screen Time)']
    
    #Column names for heatmap xy index
    yrbs_col_names = ['Sad/hopeless', 'Screen time','Age', 'Sex' ,'Gender Identity', 'Sexual Partners', 'Race']
    
    #Index for anwser values in quesiton 80 - YRBS dataset
    q80_index = ['0 h/day', '<1 h/day', '1 h/day', '2 h/day', '3 h/day', '4 h/day', '>=5 h/day']
    
    #Index for anwser values in question 25 - YRBS dataset
    q25_index = ['No','Yes']
    
    #------------------------------------------------- MTF Settings ---------------------------------------------------#
    #name list for questions in dataset: (Long form)
    mtf_question_names = ['Taking all things together, \nhow would you say things are these days?', 'About how many hours on an average DAY do you spend on social networking sites? ']
    
    #Column names for heatmap xy index
    mtf_col_names = ['Happiness lately', 'Hours/day social media', 'Sex', 'Race']
    
    #Index for anwser values in quesiton V7685 - MTF dataset
    v7685_index = ['0 h/day', '<1 h/day', '1-2 h/day', '3-4 h/day', '5-6 h/day', '7-8 h/day', '9+ h/day']
    
    #Index for anwser values in quesiton V7302 - MTF dataset
    v7302_index = ['Verry happy', 'Pretty happy', 'Not happy']
    
    #------------------------------------------------------------------------------------------------------------------#
    #YRBSS dataset functions
       
   
    #YRBS stacked histogram         
    def yrbs_stacked_histogram(col_names, q80_index, q25_index):
        
        #Set subplot size and res
        f, ax = plt.subplots(figsize = (12, 9), dpi = 300)    
        
        #Color scheme for hues in histogram
        colors = {1:'#38AFC9', 2:'#081A40'}
        
        #Plot histogram using y = count x = question 80, hue = question 25
        sns.histplot(data = yrbs_dataset, stat = "count", multiple = "stack", element = "bars", legend = True, kde = False , bins = 7, palette = colors, hue = yrbs_dataset.q25, x = yrbs_dataset.q80)
        
        #Set question name x axis + spacing of xtick lables
        ax.set(xlabel = col_names[1], xticks = ([1.4, 2.3, 3.15, 4, 4.8, 5.7, 6.6]), xticklabels = q80_index)
        
        #set hue question name and anwser index
        ax.legend(title=col_names[0],labels = q25_index)
        
        plt.setp(ax.get_legend().get_texts(), fontsize='22') 
        plt.setp(ax.get_legend().get_title(), fontsize='25')
        
        #Plot and show graph
        ax.plot()
        plt.show()
     
    #YRBS heatmap
    def yrbs_heatmap_full(yrbs_col_names):
        #Set figure size and res
        plt.figure(figsize=(12, 9), dpi = 300)
        
        #Filter and make dataset readable for heatmap
        yrbs_filter = yrbs_dataset[['q25', 'q80', 'age', 'sex', 'q65', 'q66', 'race7']].corr()
        
        #Create heatmap + set x&y lables
        sns.heatmap(data = yrbs_filter, fmt = '.1f', linewidths = 1, cmap='Blues', annot = True, xticklabels= yrbs_col_names, yticklabels= yrbs_col_names)
        #Rotate names 30deg
        plt.xticks(rotation=30)
        plt.yticks(rotation=30)
        
        #show plot
        plt.show()
        
        
    #------------------------------------------------------------------------------------------------------------------#
    #MTF dataset functions:
    
    #MTF stacked histogram
    def mtf_stacked_histogram(col_names, v7685_index, v7302_index):
        #Set subplot size and resolution
        f, ax = plt.subplots(figsize = (12, 9), dpi = 300)
        
        #Set colors for hues in histogram
        colors = {1:'#38AFC9', 2:'#C4D0D7' ,3:'#081A40'}
        
        #Create histogram
        sns.histplot(data = mtf_dataset, stat = "count", multiple = "stack", element = "bars", legend = True, kde = False, bins = 7, palette = colors, hue = mtf_dataset.V7302, x = mtf_dataset.V7685)
        
        #Set x lable + xtick distances & lables
        ax.set(xlabel = col_names[1], xticks = ([1.4, 2.3, 3.15, 4, 4.8, 5.7, 6.6]), xticklabels = v7685_index)
        
        #Set hue question name and lables
        ax.legend(title = col_names[0],labels = v7302_index)
        
        plt.setp(ax.get_legend().get_texts(), fontsize='16') 
        plt.setp(ax.get_legend().get_title(), fontsize='18')
        
        #plot histogram to subplot
        ax.plot()
        plt.show()
    
    #MTF heatmap
    def mtf_heatmap_full(mtf_col_names):
        
        plt.figure(figsize = (12, 9), dpi = 300)
        
        sns.heatmap(data = mtf_dataset.corr(), fmt = '.1f', linewidths = 1, cmap = 'Blues', annot = True, xticklabels = mtf_col_names, yticklabels = mtf_col_names)
        
        
        plt.xticks(rotation=30)
        plt.yticks(rotation=30)
        
        
        plt.show()
        
    #------------------------------------------------------------------------------------------------------------------#
    #Misc functions
    
    def yrbs_chi_squared_test(q80_index): # semi working produces output values
        #transform data for scipy.stats function   
        yrx_data = pd.crosstab(yrbs_dataset['q25'], yrbs_dataset['q80']).T
       
        #scipy.stats - chi2 squared function
        c, p, dof, expected = sp.chi2_contingency(yrx_data)
       
        #Print results
        print('P-value: ', p)
        print('Test Statistic: ', c)
        print('Degrees of freedom: ', dof)
       
       

    def mtf_chi_squared_test(): # same as above
    
        #transform data for scipy.stats function
        mtf_data = pd.crosstab(mtf_dataset['V7302'],mtf_dataset['V7685']).T

        #scipy.stats - chi2 squared function
        c, p, dof, expected = sp.chi2_contingency(mtf_data)
        
        #Print results
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
                yrbs_stacked_histogram(yrbs_question_names, q80_index, q25_index)
                
            #elif to call menu option #3
            elif (user_input == 3):
                print('Creating plot')
                mtf_heatmap_full(mtf_col_names)
            
            #elif to call menu option #4
            elif (user_input == 4):
                print('Creating plot')
                mtf_stacked_histogram(mtf_question_names, v7685_index, v7302_index)
                
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
                print('\nThe entered value is invalid. Please enter the number of a plot:')
            
        except:
            print('\nThe entered value is invalid. Please enter the number of a plot:')
            

main()