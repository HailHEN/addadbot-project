from django.shortcuts import render


from django.http import HttpResponse



def viewStats(request):
    return render(request, "jobs/stats.html")


# Create your views here.
