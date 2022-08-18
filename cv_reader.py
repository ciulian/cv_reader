import pprint
from flask import Flask
from flask.cli import with_appcontext

in_memory_datastore = {
    "personal": {
        "name": "Cojocaru Iulian",
        "phone_number": "07123123123123",
        "linkedin": "linkedin.com/in/iulian-cojocaru-b44968194"
    },
    "summary": "Full Stack Web Developer - Artificial Intelligence and Machine Learning Master Student",
    "experience": {
        "job1": {
            "position": "Full-Stack Developer",
            "company": "Cassa",
            "time": "1 year 10 months +"
        },
        "job2": {
            "position": "Trainer",
            "company": "Logiscool",
            "time": "4 months"
        }
    },
    "education": {
        "Master": {
            "name": "TAID - UPB",
            "time": "2021 - 2023",
            "description": "Creating digital image processing and analysis systems, both in terms of hardware and "
                           "software "
        },
        "Bachelor": {
            "name": "TAID - UPB",
            "time": "2017 - 2021",
            "description": "Thesis: Artificial Intelligence System for automatic detection of COVID-19 based on "
                           "medical imagingusing Keras + Tensorflow (Python).",
        },
    },
    "licenses_and_certifications": {
        "certification1": {
            "issuer": "UPB",
            "name": "ECCPR"
        }
    },
    "skills": {
        "Object-Oriented Programming (OOP)",
        "Web Development"
    }
}

app = Flask(__name__)


@app.get('/personal')
def get_personal_candidate_info():
    return {"personal_candidate_info": in_memory_datastore['personal']}


@app.get('/summary')
def get_summary_candidate_info():
    return {"summary_candidate_info": in_memory_datastore['summary']}


@app.get('/experience')
def get_experience_candidate_info():
    return {"experience_candidate_info": in_memory_datastore['experience']}


@app.get('/licenses_and_certifications')
def get_licenses_and_certifications_candidate_info():
    return {"licenses_and_certifications": in_memory_datastore['licenses_and_certifications']}


@app.get('/skills')
def get_skills_candidate_info():
    return {"skills": in_memory_datastore['skills']}


@app.cli.command(name="show-candidate-info")
@with_appcontext
def show_candidate_info():
    for key, value in in_memory_datastore.items():
        print(key + str(':'))
        pprint.pprint(value)


app.cli.add_command(show_candidate_info)

if __name__ == '__main__':
    app.run()
