import pandas as pd
from serpapi import GoogleSearch
from sqlalchemy import create_engine


from config import API_KEY


def search_jobs(job_title: str) -> None:
    """
    Searches for job postings on Google Jobs and saves the job descriptions to a SQLite database.

    Args:
        job_title (str): The job title to search for.
    """

    for num in range(2):
        start = num * 10

        params = {
            'api_key': API_KEY,
            'engine': 'google_jobs',
            'q': job_title,
            'hl': 'en',
            'chips': 'date_posted:today',
            'start': start,
        }

        search = GoogleSearch(params)
        results = search.get_dict()

        try:
            if results['error'] == "Google hasn't returned any results for this query.":
                break
        except KeyError:
            print(f'Getting SerpAPI data for page: {start}')
        else:
            continue

        jobs = results['jobs_results']
        jobs = pd.DataFrame(jobs)
        jobs['job_title'] = job_title
        jobs = jobs[['job_title', 'description']]

        engine = create_engine('sqlite:///jobs.db')
        jobs.to_sql('jobs', con=engine, if_exists='append', index=False)


def main():
    """
    Main function that searches for job postings for a specific job
    title and saves the job descriptions to a database.
    """

    jobs = [
        'Python Developer',
        'PHP Developer',
        'Java Developer',
        'C# Developer',
        'C++ Developer',
        'Data Analysis',
        'Data Science',
        'Machine Learning Engineer',
        'Front-End Developer',
        'Back-End Developer',
        'Full-Stack Developer',
        'IT Manager',
        'Information Security Analyst',
        'Software Developer',
        'Computer Systems Analyst',
        'Network and Computer Systems Administrator',
        'Cloud Engineer',
        'Database Developer',
        'DevOps Engineer',
        'Digital Marketing',
        'Graphic Designer',
    ]

    for job in jobs:
        search_jobs(job)


if __name__ == '__main__':
    main()
