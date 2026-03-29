### AI Resume Analyzer (Advanced ATS Scoring)

#### Project Overview
The AI Resume Analyzer is a full-stack project that analyzes a user's resume (PDF format) and generates a realistic ATS score based on skills, resume structure, and important sections such as projects, education, and experience.
This project simulates how real Applicant Tracking Systems (ATS) evaluate resumes.

#### Features
✔ Upload resume in PDF format
✔ Extract text from resume automatically
✔ Detect technical skills using NLP
✔ Identify resume sections (skills, projects, education, experience, summary)
✔ Generate a realistic ATS score (0 – 100)
✔ Show missing skills to improve the resume
✔ User-friendly web interface
✔ FastAPI backend with NLP integration

#### Technologies Used
Python
FastAPI
NLP (spaCy)
HTML, CSS, JavaScript
Jinja2 Templates
PDF text extraction
Git & GitHub

#### Project Structure
ai-resume-analyzer/
│
├── app/
│   ├── main.py
│   ├── model.py
│   ├── skills.py
│   ├── utils.py
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
├── requirements.txt
├── README.md
└── render.yaml

#### How It Works
User uploads a resume (PDF file)
The system extracts text from the PDF
NLP is used to detect skills and important resume sections
ATS score is calculated based on:
Skills match

#### Professional summary
Projects
Experience
Education
Resume structure
The result is displayed with:
ATS Score
Skills Found
Missing Skills

#### Installation and Running the Project
Step 1: Clone the repository
git clone https://github.com/your-username/ai-resume-analyzer.git
cd ai-resume-analyzer
Step 2: Install dependencies
pip install -r requirements.txt
Step 3: Download spaCy model
python -m spacy download en_core_web_sm
Step 4: Run the project
python -m uvicorn app.main:app --reload

Open this in your browser:
http://127.0.0.1:8000
Sample Output

#### The system will show:
ATS Score (out of 100)
Skills detected in the resume
Missing skills to improve the resume
Real-World Use Case

#### This project helps:
Students improve their resumes
Job seekers understand ATS systems
Beginners learn how NLP works in real applications
Recruiters quickly analyze resumes

#### Future Improvements
Resume vs Job Description matching
Better skill ranking (beginner / intermediate / advanced)
Dashboard with graphs
Multiple resume analysis
Resume improvement suggestions
