import os
from pathlib import Path 
from flask import Flask, request, render_template, redirect, url_for
from utils.db import Base, engine, SessionLocal, Cvs, JobListing, ScreeningResult
from utils.parse_pdf import load_pdf
from rag import evaluate
from sqlalchemy.orm import Session
from werkzeug.utils import secure_filename
from utils.addjl import add_sample_job_listings
#Base.metadata.create_all(bind=engine)
UPLOAD_DIR = Path("data/uploads") # os.path.join
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)



app = Flask(__name__)


add_sample_job_listings()

@app.route("/")
def home():
    with Session(engine) as session:
        listings = session.query(JobListing).order_by(JobListing.posted_at.desc()).all()
        return render_template("index.html", jobs=listings)

@app.route("/job/<int:job_id>")  # description job 
def description(job_id):
    with Session(engine) as session:
        job = session.query(JobListing).get(job_id)
        if not job:
            return "Brak wybranej oferty"
        return render_template("job_details.html", job=job)




@app.route("/upload/", methods=[ "POST"])
def upload():
    job_id = request.form.get("job_id")
    file = request.files.get("file")

    if not job_id or not file:
        return "Coś poszło nie tak"

    if not file.filename.lower().endswith(".pdf"):
        return "Proszę przesłać plik pdf"
    
    filename = secure_filename(file.filename)
    directory  = os.path.join('data', 'uploads')
    file_path = os.path.join(directory, filename)
    file.save(file_path) 
    cv_content = load_pdf(file_path)
    evaluate(cv_content, file.filename, job_id)
        

    return redirect(url_for("home"))

@app.route('/apply/<int:job_id>')
def apply_page(job_id):
    return render_template('apply.html', job_id=job_id)

@app.get("/cv_list/")
def cv_list():
    with Session(engine) as session:
        screening = session.query(ScreeningResult).all()
    return render_template("cv_list.html", screening=screening)

if __name__ == "__main__":
    app.run(debug=True)
