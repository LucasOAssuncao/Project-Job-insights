from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    data = read(path)
    max_salary = [
        int(job["max_salary"]) for job in data if job["max_salary"].isdigit()
    ]
    return max(max_salary)


def get_min_salary(path: str) -> int:
    data = read(path)
    min_salary = [
        int(job["min_salary"]) for job in data if job["min_salary"].isdigit()
    ]
    return min(min_salary)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        min_salary = int(job["min_salary"])
        max_salary = int(job["max_salary"])
        salary = int(salary)
    except (ValueError, TypeError, KeyError):
        raise ValueError

    if min_salary > max_salary:
        raise ValueError

    return min_salary <= salary <= max_salary


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    filtered_jobs = []
    for job in jobs:
        try:
            matches_salary = matches_salary_range(job, salary)

            if matches_salary is True:
                filtered_jobs.append(job)
        except ValueError:
            print('Error')
    return filtered_jobs
