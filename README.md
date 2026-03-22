# JarNotes

Transform your thoughts into structured insights with AI-powered note-taking.

![Python](https://img.shields.io/badge/Python-3.12-blue?style=flat)
![HTML](https://img.shields.io/badge/HTML-5-orange?style=flat)
![Dockerfile](https://img.shields.io/badge/Dockerfile-containerized-2496ED?style=flat)
![License](https://img.shields.io/badge/License-MIT-brightgreen?style=flat)

---

## Overview

JarNotes is a modern, full-stack application engineered to revolutionize how you capture and organize your thoughts. By leveraging the power of large language models (LLMs), it intelligently processes your unstructured notes, ideas, and observations, transforming them into clear, concise, and actionable insights. Whether you're brainstorming new concepts, learning complex subjects, or planning your next big project, JarNotes acts as your intelligent companion, ensuring your valuable ideas are never lost or unorganized. It empowers you to make sense of information overload and build a dynamic personal knowledge base.

---

## Features

*   **Intelligent Note Processing**: Submit raw text and receive AI-summarized, categorized, or expanded insights tailored to your needs.
*   **Intuitive Web Interface**: Interact seamlessly with a clean, responsive web application designed for effortless note input and management.
*   **Robust Backend Services**: A Python-powered backend efficiently handles all LLM interactions, data processing, and API requests.
*   **Containerized Deployment**: Utilize Docker for consistent, reproducible environments, simplifying deployment and scaling.
*   **Dynamic Knowledge Hub**: Cultivate a personal repository of processed thoughts, making your insights easily accessible and searchable.

---

## Tech Stack

![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.111.0-009688?style=flat&logo=fastapi&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=flat&logo=git&logoColor=white)
![Visual Studio Code](https://img.shields.io/badge/VS%20Code-007ACC?style=flat&logo=visual-studio-code&logoColor=white)

---

## Architecture / Workflow

JarNotes operates as a client-server application, employing a clear separation of concerns to deliver its intelligent note-processing capabilities.

1.  **User Interaction (Frontend)**: Users interact with the web-based interface (`frontend/index.html`) to input new notes or view existing processed insights.
2.  **API Request (Backend)**: User actions trigger asynchronous API calls to the Python backend service, typically for note submission or retrieval.
3.  **LLM Processing**: The `backend/main.py` service, acting as the API gateway, routes relevant requests to `backend/llm.py`. This module orchestrates interaction with a Large Language Model to perform tasks like summarization, categorization, or expansion of the user's input.
4.  **Data Transformation & Response**: The LLM's output is received by the backend, potentially undergoing further refinement or structuring, before being formatted and sent back to the frontend.
5.  **Display Results (Frontend)**: The frontend receives the processed data and dynamically updates the user interface, presenting the AI-generated insights in an organized manner.

---

## Project Structure

```
.
├── .dockerignore                 # Files and patterns to ignore during Docker image builds.
├── Dockerfile                    # Main Dockerfile to build and run the entire JarNotes application.
├── LICENSE                       # Project's open-source license (MIT).
├── README.md                     # This documentation file.
├── backend/                      # Contains all Python source code for the backend API and LLM logic.
│   ├── .dockerignore             # Specific ignore rules for the backend Docker context.
│   ├── .gitignore                # Git ignore rules for backend-specific files.
│   ├── Dockerfile                # Dockerfile for building the backend service image.
│   ├── main.py                   # Entry point for the FastAPI backend application.
│   ├── llm.py                    # Module dedicated to Large Language Model interactions.
│   └── requirements.txt          # Lists all Python package dependencies for the backend.
└── frontend/                     # Holds all static web assets for the user interface.
    ├── assets/                   # Directory for static multimedia resources like images and fonts.
    │   ├── Bangers-Regular.ttf   # Custom font file.
    │   ├── Landing_Page.png      # Landing page hero image.
    │   ├── Tomorrow-Regular.ttf  # Custom font file.
    │   ├── books.jpeg            # Image asset.
    │   ├── brain.jpeg            # Image asset.
    │   ├── notes.jpeg            # Image asset.
    │   └── typewriter.jpeg       # Image asset.
    ├── icon.ico                  # Favicon for the web application.
    └── index.html                # The main HTML file that defines the web application's structure.
```

---

## Usage

Get JarNotes up and running by following these detailed steps. You have the flexibility to run the application locally for development and rapid iteration, or leverage Docker for a containerized, production-like environment.

### Setup

1.  **Clone the Repository**:
    Begin by cloning the JarNotes repository to your local machine:
    ```bash
    git clone https://github.com/your-username/JarNotes.git
    cd JarNotes
    ```

2.  **Virtual Environment (Recommended for Local Development)**:
    It is highly recommended to create a Python virtual environment to manage dependencies for the backend. This isolates project dependencies from your system-wide Python installation.
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
    ```

3.  **Install Backend Dependencies**:
    Navigate into the `backend` directory and install all required Python packages using `pip`:
    ```bash
    cd backend
    pip install -r requirements.txt
    cd .. # Return to the root directory
    ```

### Execute Pipeline

You have two primary options for running JarNotes:

#### Option 1: Local Execution (Development)

This method allows you to run the backend and serve the frontend separately, ideal for active development.

1.  **Start the Backend Service**:
    From the root `JarNotes` directory, ensure your virtual environment is active (if you created one), then start the FastAPI application:
    ```bash
    cd backend
    python main.py
    ```
    You should observe output indicating that FastAPI is running, typically on `http://127.0.0.1:8000`. Keep this terminal window open as the backend must remain active.

2.  **Serve the Frontend**:
    Open a *new* terminal window. Navigate to the `JarNotes/frontend` directory. While you can open `index.html` directly in your browser, using a simple HTTP server provides a more robust web application experience.
    ```bash
    cd frontend
    # Use Python's built-in HTTP server:
    python -m http.server 8080
    ```
    *Note*: If your backend is running on port `8000`, it's best to use a different port for the frontend server (e.g., `8080`) to avoid conflicts. The frontend JavaScript will typically make requests to the backend's default port (`http://localhost:8000`).

3.  **Access JarNotes**:
    Open your web browser and navigate to `http://localhost:8080` (or the port you chose for the frontend server).

#### Option 2: Docker Execution (Containerized)

For a more robust and production-ready setup, use Docker. This approach builds and runs both the frontend and backend services within a single container.

1.  **Build Docker Image**:
    From the root `JarNotes` directory, build the Docker image. This process might take a few minutes as it sets up the environment and installs dependencies.
    ```bash
    docker build -t jarnotes-app .
    ```

2.  **Run Docker Container**:
    Once the image is built, run the container, mapping the application's internal port to an accessible port on your host machine:
    ```bash
    docker run -p 8000:8000 jarnotes-app
    ```
    This command maps port `8000` on your host to port `8000` inside the container, where the JarNotes application is served.

3.  **Access JarNotes**:
    Open your web browser and navigate to `http://localhost:8000`.

### Customization

*   **LLM Integration**: Dive into `backend/llm.py` to modify or switch between different Large Language Model providers (e.g., OpenAI, Hugging Face models) or fine-tune model parameters such as temperature and max tokens.
*   **Backend Logic**: Extend or modify API endpoints, data processing workflows, and business logic within `backend/main.py` to add new features or adjust existing functionality.
*   **Frontend UI/UX**: Customize the user interface and user experience by editing `frontend/index.html`, `frontend/assets/` (for images and fonts), and adding custom CSS or JavaScript to match your aesthetic preferences.

### Expected Outputs

Upon successful execution, you should expect:

*   A fully functional web application accessible in your browser at the specified address (e.g., `http://localhost:8080` or `http://localhost:8000`).
*   The ability to input text notes into the frontend's user interface.
*   Processed, AI-generated insights or summaries displayed back within the web interface after interaction with the backend.
*   Console output from the backend (if running locally) showing API requests, responses, and potential LLM interactions.

---

## Contributing

We wholeheartedly welcome contributions to JarNotes! To ensure a smooth and collaborative development process, please adhere to these guidelines.

1.  **Fork the Repository**: Begin by forking the `JarNotes` repository to your GitHub account.
2.  **Create a New Branch**: Create a new branch for your feature, enhancement, or bug fix. Use a descriptive name, such as `feat/add-auto-tagging` or `fix/frontend-layout-bug`.
    ```bash
    git checkout -b your-branch-name
    ```
3.  **Implement Your Changes**: Make your modifications, ensuring your code adheres to existing style and quality standards.
4.  **Commit Your Changes**: Write clear, concise, and descriptive commit messages that explain the purpose and scope of your changes.
    ```bash
    git commit -m "feat: implement short summary generation capability"
    ```
5.  **Push to Your Fork**: Push your newly created branch to your forked repository on GitHub.
    ```bash
    git push origin your-branch-name
    ```
6.  **Open a Pull Request**: Create a pull request from your branch to the `main` branch of the original JarNotes repository. Provide a detailed description of your changes, including why they were made and how they impact the project, and reference any relevant issues.

---

## License

JarNotes is distributed under the MIT License. For more details, please refer to the `LICENSE` file in the repository root.
