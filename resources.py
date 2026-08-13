import json


def load_resources():
    with open("data/resources.json", "r", encoding="utf-8") as file:
        return json.load(file)

def get_resources(skill):
    resources_data = load_resources()
    if skill in resources_data:
        return resources_data[skill]["resources"]
    return []


def get_project_idea(skill):
    resources_data = load_resources()
    if skill in resources_data:
        return resources_data[skill]["project_idea"]
    return "No project idea available."

'''
def get_skill_recommendations(missing_skills):
    resources_data = load_resources()
    recommendations = {}
    for skill in missing_skills:
        if skill in resources_data:
            recommendations[skill] = {
                "resources": resources_data[skill]["resources"],
                "project": resources_data[skill]["project_idea"]
            }
    return recommendations
'''