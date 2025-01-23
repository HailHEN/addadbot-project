from django.shortcuts import render
from plotly import express as px
from plotly import io
from django.http import HttpResponse
from jobs.models import JobPost, Graph, GraphDescription

from analyse_postings.data_analysis import JobPostingsAnalysis
from analyse_postings.setup_graphs import ChartSetups

import pandas as pd
import json

# 


def viewStats(request):

    description_json = GraphDescription.objects.all().first().description_dictionary
    description_dict = json.loads(description_json)
    graph_dict = dict()

    # now we will get an iterable collection of all the graphs
    # we iterate and create a dictionary with graph name as key 
    # and the converted (json to Plotly figure) as value
    for graph in Graph.objects.all():
        graph_dict[graph.graph_name] = io.from_json(graph.graph_file).to_html()
    
    graph_dict.update(description_dict)

    return render(request, "jobs/stats.html", graph_dict )

    
