from functools import lru_cache
from typing import List, Dict

import csv


@lru_cache
def read(path: str) -> List[Dict]:

    with open(path, mode="r") as file:
        reader = csv.DictReader(file)
        return list(reader)

    raise NotImplementedError


def get_unique_job_types(path: str) -> List[str]:
    data = read(path)
    job_types = [job["job_type"] for job in data]
    return list(set(job_types))
    raise NotImplementedError


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError
