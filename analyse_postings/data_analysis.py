
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np




# convert all objects into pandas dataframe

# make sure statistics are user interaction

# end user, so select paramters and display information
# what skills aare in demand right now, so user selcts

# whichcountries are looking

# and what area of robotics



# for each function add bar graph for

# 



##################################################################

# 1. Selection for user to  investigate which data to see
# 2. Selection for user to investigate date (time period) along side information to display
# 3. Use line graph instead of histogram



# after this week add extra analysis like trend analysis and stuff



##################################################################

skills_key_words = {"c++", "c#",
                    "python", "java", "embedded systems",
                    "microcontroller",
                    "math", "control",
                    "ai","machine learning","computer vision","cad"
                    ,"circuits", "autonomy", "automonous", "ml", "ai"
                    ,"programming", "coding"}

class JobPostingsAnalysis:

    job_df = pd.DataFrame()

    def __init__(self, list_of_jobs):

        self.job_df = pd.DataFrame(list_of_jobs)
        self.job_df["date_posted"] = self.job_df["date_posted"].astype("datetime64[ns]")
        self.job_df.drop('id', axis=1, inplace=True)



    # return dataframe
    def data_frame(self):
        
        return self.job_df
        
    def analyse_type_of_robotics(self):
        self.job_df['robot_type'].value_counts().plot(kind='bar')
        
        return

    def analyse_expertise_of_robotics_field(self):
        return
    #programming skills
    def software_skills_required(self):
        return

    def analyse_skills_required(self):

        return



    def analyse_postings_date_created(self):

        self.job_df["date_posted"].dt.month.value_counts().plot(kind='bar')
        plt.show()

        return


    #bin by month
    #obviously later on paramters can be changed by slider or something by user
    def analyse_job_position_posted(self):
        
        return
    

    

    def startswitchchecker(word):

        for keyw in skills_key_words:
            if word.startswith(keyw):
                return True
        
        return False
    



    
    def analyse_skills_list(skills):
        temp_list = set()


        for skill in skills.split():
            skill = skill.lower()
            temp_list.add(str(skill))
            

        
        # for word in description.split():
        #     word = word.lower()
        #     word = word.replace(',', '')
        #     word = word.replace(':', '')

        #     if (word in skills_key_words or JobPostingsAnalysis.startswitchchecker(word)) and (word not in temp_list):
                
        #         temp_list.add(str(word))

        return list(temp_list)
    
    

   
    
        

    def keywords_skill_description_analyser(self):
        df = self.job_df
        

        required_skills = df['required_skills'].to_list()
        
        list_of_keywords_for_dataframe = []
        for skills in required_skills:
            
            
            list_of_keywords_in_required_skills = JobPostingsAnalysis.analyse_skills_list(skills)
            
            list_of_keywords_for_dataframe.append(list_of_keywords_in_required_skills)
            
            


        self.job_df['Skills'] = pd.Series(list_of_keywords_for_dataframe)
        
        
        return self.job_df['Skills'].explode().value_counts().index.tolist(), self.job_df['Skills'].explode().value_counts().values
    


    def get_data_frame(self):
        return self.job_df
        


