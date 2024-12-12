from django.shortcuts import render


from django.http import HttpResponse
from jobs.models import JobPost
from analyse_postings.data_analysis import JobPostingsAnalysis

def viewStats(request):
    d_analysis = JobPostingsAnalysis(JobPost.objects.all().values())
    print(d_analysis.data_frame().to_string())
          
          
          

          #user selects what to graph

          #demo
    # d_analysis.analyse_type_of_robotics()

    return render(request, "jobs/stats.html")


# Create your views here.
