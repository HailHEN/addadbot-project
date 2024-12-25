
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

# skills_key_words = {"c++", "c#",
#                     "python", "java", "embedded systems",
#                     "microcontroller",
#                     "math", "control",
#                     "ai","machine learning","computer vision","cad"
#                     ,"circuits", "autonomy", "automonous", "ml", "ai"
#                     ,"programming", "coding"}

class JobPostingsAnalysis:

    job_df = pd.DataFrame()

    def __init__(self, list_of_jobs):

        self.job_df = pd.DataFrame(list_of_jobs)
        self.job_df["date_posted"] = self.job_df["date_posted"].astype("datetime64[ns]")
        self.job_df.drop('id', axis=1, inplace=True)


    # def startswitchchecker(word):

    #     for keyw in skills_key_words:
    #         if word.startswith(keyw):
    #             return True
        
    #     return False

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
    # add trends depending on past month, 6 month or 12 month for each (either going up or down for specified time period)

    # automated summary should include (text only):
            # percentage of jobs that are describing the x axis (top 10)
            # x axis interaction with other dpendednt values. These will be:
                # Jobs posted and its correlation with type of employment and job position every month this year including current month
                # Robot type and its correlation with domain, skills required and country
                # area of expertise required and its correlation with domain of robotics and skills required
                # domain of jobs and its correlation with country and skills
                # skills of jobs and its correlation with ... (tba)
                # country of jobs and its correlation with ... (tba)

        #count how many jobs posted seperated by positions
    

    def stats_summary_for_jobs_posted(self):
        
        df = self.job_df

        job_count_dictionary = dict()
        job_position_list = list()

        total_jobs_count = len(df.index)
        type_grouped = df.groupby('employment_type', as_index=False).count()
        
        types = type_grouped['employment_type'].tolist()
        count_for_each_employment = type_grouped['job_count'].tolist()

        position_grouped = df.groupby(['job_position','employment_type'], as_index=False).count()

        positions = position_grouped['job_position'].tolist()
        type_for_position = position_grouped['employment_type'].tolist()
        count_for_position = position_grouped['job_count'].tolist()

        for (position, type_p, count_p) in zip(positions, type_for_position, count_for_position):
            job_position_list.append("Where " + str(round((count_p/total_jobs_count*100), 2)) + "% " + "are " + position + " and " + type_p)
        
        for (type, count) in zip(types, count_for_each_employment):
            job_count_dictionary[str(type)] = str(round((count/total_jobs_count*100), 2))

        return job_count_dictionary, job_position_list
    
    def area_of_expertise_stat_summary(self):
        df = self.job_df

        total_jobs_count = len(df.index)

        expertise_list_for_domain = list()
        expertise_list_for_skills = list()

        expertise_grouped_domain = df.groupby(['area_of_expertise','robotics_domain'], as_index=False).count()
        expertise_grouped_skills = df.groupby(['area_of_expertise','required_skills'], as_index=False).count()


        expertse_domain = expertise_grouped_domain['area_of_expertise'].tolist()
        domain = expertise_grouped_domain['robotics_domain'].tolist()
        count_for_domain = expertise_grouped_domain['job_count'].tolist()

        expertse_skills = expertise_grouped_skills['area_of_expertise'].tolist()
        skills =  expertise_grouped_skills['required_skills'].tolist()
        count_for_skills= expertise_grouped_skills['job_count'].tolist()

        for (exp_d, dom, count_d) in zip(expertse_domain, domain, count_for_domain):
            expertise_list_for_domain.append("Industries in " + exp_d)            

        

        # area of expertise required and its correlation with domain of robotics and skills required
        # top 10

        return expertise_list_for_domain, expertise_list_for_skills
    
  
    def get_data_frame(self):
        
        return self.job_df
        


