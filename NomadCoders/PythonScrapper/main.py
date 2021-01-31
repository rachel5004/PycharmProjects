import indeed_Scrapper
import stackoverflow_Scrapper

indeed_jobs = indeed_Scrapper.get_jobs()
so_jobs = stackoverflow_Scrapper.get_jobs()

print(indeed_jobs)
print(so_jobs)