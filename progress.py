import json
import os

PROGRESS_FILE = "data/progress.json"

def calculate_progress(known_skills, missing_skills):
    total_skills = len(known_skills) + len(missing_skills)
    if total_skills == 0:
        return 0
    completed_skills = len(known_skills)
    progress = (completed_skills / total_skills) * 100
    return round(progress, 2)


def save_progress(career, known_skills):
    data = {
        "career": career,
        "known_skills": known_skills
    }

    with open(PROGRESS_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def load_progress():
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    return None

def has_saved_progress():
    return os.path.exists(PROGRESS_FILE)