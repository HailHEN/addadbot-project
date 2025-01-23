from jobs.models import JobPost, Graph
import pandas as pd
from plotly import express as px
import plotly
import json
from django.core.files import File
class ChartSetups:

    def charts_setup(df, list_of_skills_unique, frequency_of_skills_counts):

        Graph.objects.all().delete()
        
        
        line_df = df[["date_posted", "job_country"]]
        temp_line_df = line_df
        line_df = pd.DataFrame(line_df['date_posted'].dt.date.value_counts()).reset_index()
        line_df['date_posted'] = pd.to_datetime(line_df['date_posted'])
        line_df = temp_line_df.merge(line_df, how='left', on='date_posted')
        

        fig = px.line(line_df, x='date_posted', y = 'count', title="Total jobs posted", markers=True, color='job_country')

        fig.update_xaxes(
            rangeslider_visible=True,
            rangeselector=dict(
                buttons=list([
                    dict(count=1, label="1m", step="month", stepmode="backward"),
                    dict(count=6, label="6m", step="month", stepmode="backward"),
                    dict(step="all")
                ])
            )
        )

        fig.update_layout(margin=dict(
            l=0,
            r=0,
            b=80,
            t=40,
            pad=4), title_x=0.5,yaxis=dict(tickmode = 'linear',
            tick0 = 0,
            dtick = 1))
        graph = Graph(graph_file = fig.to_json(), graph_name = "chart")
        graph.save()

        

        fig = px.bar(df, x="area_of_expertise",
                    width=600, height=450)
        fig.update_layout(xaxis={'categoryorder':'total descending'}) 
        fig.update_layout(margin=dict(
            l=0,
            r=0,
            b=10,
            t=40,
            pad=4),title_text='Area of expertise', title_x=0.5)
        # save to graphs folder
        graph = Graph(graph_file = fig.to_json(), graph_name = "chart3")
        graph.save()
        
        
        fig = px.bar(df, x="employment_type",
                    width=650, height=450)
        
        fig.update_layout(margin=dict(
            l=0,
            r=0,
            b=10,
            t=40,
            pad=4),title_text='Type of employment posted', title_x=0.5)
        fig.update_layout(xaxis={'categoryorder':'total descending'}) 

        # save to graphs folder
        graph = Graph(graph_file = fig.to_json(), graph_name = "chart4")
        graph.save()

        fig = px.bar(df, x="robot_type",
                    width=650, height=450)
        fig.update_layout(margin=dict(
            l=0,
            r=0,
            b=10,
            t=40,
            pad=4),title_text='Types of robots used by employers', title_x=0.5)
        fig.update_layout(xaxis={'categoryorder':'total descending'}) 
        # save to graphs folder
        graph = Graph(graph_file = fig.to_json(), graph_name = "chart5")
        graph.save()

        fig = px.bar(df, x="robotics_domain",
                    width=600, height=450)
        fig.update_layout(margin=dict(
            l=0,
            r=0,
            b=10,
            t=40,
            pad=4),title_text='Domain of robotics', title_x=0.5)
        fig.update_layout(xaxis={'categoryorder':'total descending'}) 
        # save to graphs folder
        graph = Graph(graph_file = fig.to_json(), graph_name = "chart6")
        graph.save()

        #so later, maybe use line graphs with date as x axis (can be acheived by using color as skills and x axis date)
        fig = px.bar(x=list_of_skills_unique, y=frequency_of_skills_counts, width=650, height=450,
                    )
        fig.update_layout(margin=dict(
            l=0,
            r=0,
            b=10,
            t=40,
            pad=4),title_text='Skills in robotics', title_x=0.5,
                        xaxis_title="Skills", yaxis_title="count")
        
        fig.update_layout(xaxis={'categoryorder':'total descending'}) 
        # save to graphs folder
        graph = Graph(graph_file = fig.to_json(), graph_name = "chart7")
        graph.save()

        fig = px.pie(df,values='job_count', names='job_country', title="Jobs posted per country"
                    ,width=650, height=450, labels={'job_count':'Jobs','job_country':'Country'})
        fig.update_traces(textposition='inside', textinfo='percent+label')
        # save to graphs folder
        graph = Graph(graph_file = fig.to_json(), graph_name = "chart8")
        graph.save()

        fig = px.sunburst(df, path=['employment_type', 'job_position', 'robot_type'], values='job_count', color='employment_type')
        # save to graphs folder
        graph = Graph(graph_file = fig.to_json(), graph_name = "chart9")
        graph.save()


        