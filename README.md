1. To create graphs and descriptiopn analysis must run command "python3 manage.py process_jobs"
2. When inputting the skills into the model, skills are seperated by white space. No special characters otherwise analysis wont work. 
    To make this better, perhaps change the skills field in the jobs model to a multiple choice with given set of skills to avoid typos!

3. Graphs and graph descriptions are saved in django databse. This is done by converting them into json and decoding them when used. This
    essentially caches the result and the server only needs to serve the decoded json to user. NO computation during runtime.


Required packages:

- plotly (plotly express)
- pandas
- json


