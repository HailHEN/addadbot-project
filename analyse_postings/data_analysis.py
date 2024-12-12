
import matplotlib.pyplot as plt
import pandas as pd





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
    

    # will analyse key words in job title and the description of the job
    # add description section in model later
    def keywords_skill_analyser(self):
        return
    


    def get_data_frame(self):
        return self.job_df
        


