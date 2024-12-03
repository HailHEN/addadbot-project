from django.shortcuts import render


from django.http import HttpResponse

from analyse_postings.data_analysis import JobPostingsAnalysis

def viewStats(request):
    return render(request, "jobs/stats.html")


# Create your views here.
