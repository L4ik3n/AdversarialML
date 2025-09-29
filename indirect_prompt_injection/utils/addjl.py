from sqlalchemy.orm import Session
from utils.db import JobListing, engine, SessionLocal

def add_sample_job_listings():
    # Utwórz przykładowe oferty pracy
    sample_jobs = [
        JobListing(
        title="Junior Python Developer",
        description="Tworzenie i rozwój aplikacji webowych. Wymagana znajomość Pythona i Django. Praca zdalna lub hybrydowa."
        ),
        JobListing(
        title="Specjalista ds. IT Helpdesk",
        description="Wsparcie użytkowników w codziennych problemach IT. Znajomość Windows i podstaw sieciowych. Praca stacjonarna w Krakowie."
        ),
        JobListing(
        title="Frontend Developer (React)",
        description="Rozwój interfejsów użytkownika w React.js. Wymagane doświadczenie z HTML, CSS, JavaScript. Praca zdalna 100%."
        ),
        JobListing(
        title="Tester oprogramowania",
        description="Manualne testowanie aplikacji mobilnych i webowych. Doświadczenie w pracy z Jira mile widziane. Umowa o pracę lub B2B."
        ),
        JobListing(
        title="Administrator systemów Linux",
        description="Zarządzanie serwerami Linux, tworzenie skryptów bash. Praca hybrydowa, atrakcyjny system premiowy."
        ), 
        ]

    # Otwarcie sesji
    with Session(engine) as session:
        # Dodaj oferty pracy do sesji
        session.add_all(sample_jobs)
        # Zatwierdź zmiany w bazie danych
        session.commit()

    print("Sample job listings have been added successfully!")

# Wywołaj funkcję, aby dodać przykładowe oferty pracy

