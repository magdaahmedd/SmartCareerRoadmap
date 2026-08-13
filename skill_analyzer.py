from career_data import get_career_skills


def analyze_skills(career, user_skills):

    required_skills = get_career_skills(career)   #Get the skills required for the selected career


    known_skills = []    #the skills that the user already knows
    missing_skills = []  #the skills that the user is missing

    for skill in required_skills:    #Comparing each required skill with the user's skills

        if skill in user_skills:
            known_skills.append(skill)
        else:
            missing_skills.append(skill)
    return known_skills, missing_skills

def get_first_missing_skill(missing_skills):  #getting the first missing skill
    if missing_skills:
        return missing_skills[0]
    return None