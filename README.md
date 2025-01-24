1. To create graphs and descriptiopn analysis must run command "python3 manage.py process_jobs"
2. When inputting the skills into the model, skills MUST BE seperated by white space. No special characters otherwise analysis wont work. 
    To make this better, perhaps change the skills field in the jobs model to a multiple choice with a given set of skills to avoid typos! 
    This may be better than the textfiled currently.

3. Graphs and graph descriptions are saved in django databse. This is done by converting them into json and decoding them when used. This
    essentially caches the result and the server only needs to serve the decoded json to user. NO computation during runtime.

4. When modifying charts please go to setup_graphs file. Using plotly function you can modify and change everyhting about the charts includding the padding and
        size of the graphs before they are served as html/css will not change the sizes/padding properly. Setting the sizes margins/padding, before the charts are served,
        you can then fit the chart onto the front end how you like.
5. Always run the above script in step 1 when jobs has changed or modifying the structure etc of graphs


Required packages:

- plotly (plotly express)
- pandas
- json


