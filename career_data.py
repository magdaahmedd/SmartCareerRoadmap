import json


def load_careers():
    with open("data/career_data.json", "r") as file:
        return json.load(file)


careers = load_careers()


def get_careers():
    return list(careers.keys())


def get_career_skills(career):
    if career in careers:
        return careers[career]["skills"]
    return []


def get_career_description(career):
    if career in careers:
        return print(f"Description: {careers[career]['description']}")
    return "Career not found."

'''
def get_career_details(career):
    if career in careers:
        print("Career:", career)
        print("Description:", careers[career]["description"])
        print("Skills:")

        for skill in careers[career]["skills"]:
            print("-", skill)
    
    else:
        print("Career not found.")
'''