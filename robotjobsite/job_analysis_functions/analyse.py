from .jobs import JobPosts


def initialise_jobs():
    job_list = []
    job_list.append(JobPosts())

def main():
    initialise_jobs()
    


if __name__ == "__name__":
    main()