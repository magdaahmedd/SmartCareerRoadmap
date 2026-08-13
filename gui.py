import tkinter as tk
from tkinter import ttk
from career_data import get_careers, get_career_skills
from skill_analyzer import analyze_skills, get_first_missing_skill
from resources import get_resources, get_project_idea
from progress import calculate_progress,save_progress,load_progress,has_saved_progress

def clear_screen(window):
    for widget in window.winfo_children():
        widget.destroy()

# welcome_screen
def show_welcome_screen(window):
    window.configure(bg="#F4F7FC")

    title_label = tk.Label(
        window,
        text="Smart Career Roadmap",
        font=("Arial", 25, "bold"),
        bg="#F4F7FC",
        fg="#163D8F"
    )
    title_label.pack(pady=(90, 20))

    continue_button = tk.Button(
        window,
        text="Continue Previous Progress",
        font=("Arial", 12, "bold"),
        width=27,
        height=2,
        bg="#2563EB",
        fg="white",
        activebackground="#1D4ED8",
        activeforeground="white",
        relief="flat",
        cursor="hand2",
        command=lambda: continue_progress(window)
    )
    continue_button.pack(pady=10)

    new_button = tk.Button(
        window,
        text="Start New Path",
        font=("Arial", 12, "bold"),
        width=27,
        height=2,
        bg="#E8EEF9",
        fg="#163D8F",
        activebackground="#D9E4F7",
        relief="flat",
        cursor="hand2",
        command=lambda: show_career_screen(window)
    )
    new_button.pack(pady=8)


def continue_progress(window):
    if has_saved_progress():
        saved_data = load_progress()
        career = saved_data["career"]
        known_skills = saved_data["known_skills"]
        show_roadmap_screen(window,career,known_skills)
    else:
        show_career_screen(window)

# career_screen
def show_career_screen(window):
    clear_screen(window)

    title_label = tk.Label(
        window,
        text="Choose Your Career",
        font=("Arial", 24, "bold"),
        bg="#F4F7FC",
        fg="#163D8F"
    )
    title_label.pack(pady=(55, 12))

    description_label = tk.Label(
        window,
        text="Select the track you want to learn.",
        font=("Arial", 11),
        bg="#F4F7FC",
        fg="#64748B"
    )
    description_label.pack(pady=8)

    for career in get_careers():
        career_button = tk.Button(
            window,
            text=career,
            width=27,
            height=2,
            font=("Arial", 11, "bold"),
            bg="white",
            fg="#163D8F",
            activebackground="#E8EEF9",
            relief="flat",
            cursor="hand2",
            command=lambda selected=career:show_skills_screen(window, selected)
        )
        career_button.pack(pady=6)


# show_skills_screen
def show_skills_screen(window, selected_career):
    clear_screen(window)

    title_label = tk.Label(
        window,
        text="Choose Your Skills",
        font=("Arial", 24, "bold"),
        bg="#F4F7FC",
        fg="#163D8F"
    )
    title_label.pack(pady=(35, 8))

    description_label = tk.Label(
        window,
        text="Select the skills you already know.",
        font=("Arial", 11),
        bg="#F4F7FC",
        fg="#64748B"
    )
    description_label.pack(pady=8)


    skills = get_career_skills(selected_career)
    skill_vars = {}

    for skill in skills:
        skill_vars[skill] = tk.BooleanVar()
        check_button = tk.Checkbutton(
            window,
            text=skill,
            variable=skill_vars[skill],
            font=("Arial", 11),
            bg="#F4F7FC",
            fg="#334155",
            activebackground="#F4F7FC",
            selectcolor="#E8EEF9",
            cursor="hand2"
        )
        check_button.pack(anchor="w", padx=170, pady=4)

    next_button = tk.Button(
        window,
        text="Next  →",
        font=("Arial", 12, "bold"),
        bg="#2563EB",
        fg="white",
        activebackground="#1D4ED8",
        activeforeground="white",
        relief="flat",
        width=18,
        height=2,
        cursor="hand2",
        command=lambda: start_roadmap(window,selected_career,skill_vars)
    )
    next_button.pack(pady=18)


def start_roadmap(window, selected_career, skill_vars):
    known_skills = []
    for skill, var in skill_vars.items():
        if var.get():
            known_skills.append(skill)
    show_roadmap_screen(window,selected_career,known_skills)


# roadmap
def show_roadmap_screen(window, selected_career, known_skills):
    clear_screen(window)
    known_skills, missing_skills = analyze_skills(selected_career,known_skills)
    progress = calculate_progress(known_skills, missing_skills)
    save_progress(selected_career,known_skills)

    title_label = tk.Label(
        window,
        text=selected_career + " Roadmap",
        font=("Arial", 24, "bold"),
        bg="#F4F7FC",
        fg="#163D8F"
    )
    title_label.pack(pady=(25, 8))
    progress_label = tk.Label(
        window,
        text=f"Progress: {progress}%",
        font=("Arial", 13, "bold"),
        bg="#F4F7FC",
        fg="#2563EB"
    )
    progress_label.pack(pady=(8, 5))

    progress_bar = ttk.Progressbar(
        window,
        orient="horizontal",
        length=450,
        mode="determinate"
    )
    progress_bar["value"] = progress
    progress_bar.pack(pady=(0, 15))


    if not missing_skills:
        complete_label = tk.Label(
            window,
            text="🎉 Congratulations!",
            font=("Arial", 22, "bold"),
            bg="#F4F7FC",
            fg="#16A34A"
        )
        complete_label.pack(pady=35)

        message_label = tk.Label(
            window,
            text="You have completed all the skills in this career!",
            font=("Arial", 12),
            bg="#F4F7FC",
            fg="#334155"
        )
        message_label.pack(pady=10)

        return

    current_skill = get_first_missing_skill(missing_skills)

    skill_title = tk.Label(
        window,
        text="YOUR NEXT SKILL",
        font=("Arial", 11, "bold"),
        bg="#F4F7FC",
        fg="#64748B"
    )
    skill_title.pack(pady=(15, 4))

    skill_label = tk.Label(
        window,
        text=current_skill,
        font=("Arial", 23, "bold"),
        bg="#E8EEF9",
        fg="#2563EB",
        padx=30,
        pady=8
    )
    skill_label.pack(pady=5)

    resources_title = tk.Label(
        window,
        text="Learning Resources",
        font=("Arial", 14, "bold"),
        bg="#F4F7FC",
        fg="#163D8F"
    )
    resources_title.pack(pady=(15, 5))
    resources = get_resources(current_skill)

    for resource in resources:
        resource_label = tk.Label(
            window,
            text="• " + resource,
            font=("Arial", 10),
            bg="#F4F7FC",
            fg="#334155"
        )
        resource_label.pack(pady=2)

    project_title = tk.Label(
        window,
        text="Mini Project",
        font=("Arial", 14, "bold"),
        bg="#F4F7FC",
        fg="#163D8F"
    )
    project_title.pack(pady=(15, 4))

    project_label = tk.Label(
        window,
        text=get_project_idea(current_skill),
        font=("Arial", 11),
        bg="#E8EEF9",
        fg="#334155",
        padx=20,
        pady=7
    )
    project_label.pack(pady=4)

    next_button = tk.Button(
        window,
        text="Next Skill  →",
        font=("Arial", 12, "bold"),
        bg="#2563EB",
        fg="white",
        activebackground="#1D4ED8",
        activeforeground="white",
        relief="flat",
        width=18,
        height=2,
        cursor="hand2",
        command=lambda: complete_current_skill(window,selected_career,known_skills,current_skill)
    )
    next_button.pack(pady=18)

def complete_current_skill(window,selected_career,known_skills,current_skill):
    if current_skill not in known_skills:
        known_skills.append(current_skill)
    show_roadmap_screen(window,selected_career,known_skills)