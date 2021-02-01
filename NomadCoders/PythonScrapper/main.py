from indeed_Scrapper import get_indeed_jobs
from stackoverflow_Scrapper import get_so_jobs
from save import save_to_file

indeed_jobs = get_indeed_jobs()
so_jobs = get_so_jobs()
jobs = indeed_jobs+so_jobs
print(indeed_jobs)
save_to_file(jobs)
