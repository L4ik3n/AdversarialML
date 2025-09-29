from utils.db import Base, engine, SessionLocal, Cvs, ScreeningResult, JobListing
from utils.run_model import OLLAMA
from sqlalchemy.orm import Session




model  = OLLAMA('gemma3:4b', temperature=0)
     

def build_prompt(cv, job_description):
    return f"""
Jesteś ekspertem do spraw rekrutacji. Szukasz kandydata na podane stanowisko. Na podstawie poniższej ofery pracy:

{job_description}

Podsumuj profil kandydata i dokonaj krótkiej oceny kandydata. Oto jego profil:


{cv}    

"""


def evaluate(cv_content, filename, job_id):


    with Session(engine) as session:
        print("and here")
        job  = session.query(JobListing).get(job_id)
        job_description = job.description
        cv_filename = session.query(Cvs).filter_by(filename=filename).first()
        if not cv_filename:  # nazwa pliku moze byc zajeta 
            cv_filename = Cvs(filename=filename)
            session.add(cv_filename)
        session.commit()

    with Session(engine) as session:        
        print('m here')
        cv = session.query(Cvs).filter_by(filename=filename).first()
        prompt = build_prompt(cv_content, job_description)
        evaluation = model(prompt)[0] #potential issue
        print(evaluation)
        if evaluation !=  "": 
            screening = ScreeningResult(job_id=job_id, cv_id=cv.id, filename=filename, evaluation=evaluation)
            session.add(screening)


        
        session.commit()
    


