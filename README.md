# Flask ToDo App

A simple and clean ToDo web application built with Flask, featuring a SQLite backend and deployed with a full CI/CD pipeline using GitHub, Jenkins, Docker, and AWS EC2.

---

## Tech Stack

- **Frontend**: HTML, CSS, JavaScript (Vanilla)
- **Backend**: Python Flask
- **Database**: SQLite
- **CI/CD**: GitHub Webhooks + Jenkins
- **Containerization**: Docker
- **Deployment**: AWS EC2
- **Image Registry**: Docker Hub

---

## Project Pipeline (CI/CD)

### 1. Local Development
- Built a Flask app with routes to add, update, check, uncheck, and delete ToDos.
- Used SQLite for lightweight, file-based storage.
- Followed UTC timezone for consistency.

### 2. Source Control
- Codebase pushed to GitHub repository for versioning and collaboration.

### 3. Continuous Integration
- Configured **GitHub Webhooks** to trigger **Jenkins** jobs on push.
- Jenkins pulls the latest code and builds the application.

### 4. Containerization
- Jenkins creates a **Docker image** for the Flask app.
- The image is pushed to **Docker Hub** for centralized access.

### 5. Continuous Deployment
- Jenkins then SSHs into the **AWS EC2** instance.
- Pulls the Docker image from Docker Hub and runs the container.

---

## Preview

![Flask To-Do Pipeline Overview](https://dl.dropboxusercontent.com/scl/fi/ktwibcwgztapbtepmom9i/flask-to-do-pipeline-overview.png?rlkey=y1s4h6y5q8ecbkq22k2hqz6l5&st=hv5y4swd&dl=0?raw=1)


![Flask To-Do App CI/CD](https://dl.dropboxusercontent.com/scl/fi/nhagw5s9y2dvq4n5syodq/flask-to-do-app-cicd.png?rlkey=u54xl9dlgo770rro9lqu8y38g&st=n08fv15e&dl=0?raw=1)


![Jenkins CI/CD Pipeline](https://dl.dropboxusercontent.com/scl/fi/5moxjkihp0a8buae74sqe/jenkins-flask-to-do-app.png?rlkey=coecafb4enm9wsjhwuufsgk3x&st=5d2o4c40&dl=0?raw=1)



## License

This project is open-source and available under the [MIT License](LICENSE).

