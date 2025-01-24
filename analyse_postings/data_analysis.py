

import pandas as pd
import numpy as np

class JobPostingsAnalysis:

    job_df = pd.DataFrame()

    def __init__(self, list_of_jobs):

        self.job_df = pd.DataFrame(list_of_jobs)
        self.job_df["date_posted"] = self.job_df["date_posted"].astype("datetime64[ns]")
        self.job_df.drop('id', axis=1, inplace=True)

    # used to clean the skills
    # this is used as we are currently using a textbox to input skills currently
    # this will not be needed if we had a multple choice set of skills
    # which are then selected by admin for respective jobs

    def filter_skills(skills):

        temp_list = list()


        for skill in skills.split():
            skill = skill.lower()
            skill = skill.replace(',', '')
            skill = skill.replace("'", '')
            skill = skill.replace("[", '')
            skill = skill.replace("]", '')
            
            
            temp_list.append(str(skill))

        return temp_list



    def analyse_skills_list(skills):
        temp_list = set()
        for skill in skills.split():
            skill = skill.lower()
            temp_list.add(str(skill))
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


        expertise_grouped_domain = df.groupby(['area_of_expertise','robotics_domain'], as_index=False).count()
        

        
        expertse_domain = expertise_grouped_domain['area_of_expertise'].tolist()
        domain = expertise_grouped_domain['robotics_domain'].tolist()
        count_for_domain = expertise_grouped_domain['job_count'].tolist()



        for (exp_d, dom, count_d) in zip(expertse_domain, domain, count_for_domain):
            expertise_list_for_domain.append("Industries in " + exp_d + " are composed of " + str(round((count_d/total_jobs_count*100), 2)) + "% " + " of " + dom + " robotics.")            


        return expertise_list_for_domain
    


    def response_creator(skills):
        
        response_list = list()
        response = ""
        for skill, stat in skills.items():
            response = response + str(round((stat*100), 2)) + "% " + "are " + str(skill) + " postings\n"
            response_list.append(response)


        return response_list
    
    
    def types_of_robot_stat_summary(self):
        df = self.job_df

        # go through all the types of robots
        # for each type (after grouping) of robots count all the skills required
        # for each type of robots list all the the skills and their percentages 

        type_of_robot_dict = dict()
        responses_list = list()
        

        robot_type_list = df['robot_type'].to_numpy().tolist()
        robot_skills_list = df['required_skills'].to_numpy().tolist()

        for key in robot_type_list:
            type_of_robot_dict[key] = []


        for (type,skills) in zip(robot_type_list, robot_skills_list):
            
            type_of_robot_dict[type] = skills

        for key in type_of_robot_dict:
            type_of_robot_dict[key] = JobPostingsAnalysis.filter_skills(str(type_of_robot_dict[key]))
            
        for key in type_of_robot_dict:

            type_of_robot_dict[key] = pd.Series(type_of_robot_dict[key]).value_counts(normalize=True)
            



        for key in type_of_robot_dict:

            type_of_robot_dict[key] = JobPostingsAnalysis.response_creator(type_of_robot_dict[key])

            

       
        return type_of_robot_dict
    


    # potential functions 
    def skills_of_robot_stat_summary(self):
        # where are the skills in terms of industry (for each industry list skills similar to above)
        return
    def stat_summary_country(self):
        # industry for each country samea as type of robots
        return

    
  
    def get_data_frame(self):
        
        return self.job_df
        


