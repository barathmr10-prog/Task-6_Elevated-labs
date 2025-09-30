from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html',
    name="Barath M R",
    tagline="Python Fullstack developer",
    about="I am a fresher who got passed out in 2024 with 8.7 cgpa and I am doing a intership in Elevated Labs for Python",
    skills=["Python", "Flask", "REST API", "SQL"],
    projects=[
            {"title": "Task1", "description": "Build a Calculator CLI App.", "link": "https://github.com/barathmr10-prog/ElevatedLabs---Task1---22-09-25.git"},
            {"title": "Task2", "description": "Create a To-Do List Application (Console-based)", "link": "https://github.com/barathmr10-prog/barathmr10-prog-ElevatedLabs---Task2---23-09-25.git"},
            {"title": "Task3", "description": "Web Scraper for News Headlines", "link": "https://github.com/barathmr10-prog/Task-3_Elevated_labs.git"},
            {"title": "Task4", "description": "Build a REST API with Flask", "link": "https://github.com/barathmr10-prog/Task-4---Flask-Rest-API.git"},
            {"title": "Task5", "description": "Data Analysis on CSV Files", "link": "https://github.com/barathmr10-prog/Task_5-Elevated_labs.git"},
        ])

if __name__ == "__main__":
    app.run(debug=True)