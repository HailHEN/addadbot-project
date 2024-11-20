from ..models import JobPost
from .data_analysis import JobPostingsAnalysis



def main():
    # sends a list of dictionary of models
    d_analysis = JobPostingsAnalysis(JobPost.objects.all().values())
    
    


if __name__ == "__main__":
    main()