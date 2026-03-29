### AI Resume Analyzer (ATS Score System)

#### Project Overview
This project is an AI-based Resume Analyzer that allows users to upload a resume (PDF file) and generates an ATS score based on skills, resume structure, and important sections such as education, projects, and experience.
The system uses NLP techniques to extract skills and analyze resume content automatically.

#### Features
1. Upload resume in PDF format
2. Automatic text extraction from resume
3. Skill detection using NLP
4. Resume section detection (skills, projects, education, experience)
5. ATS score generation (0–100)
6. Missing skills suggestion
7. Simple and clean web interface

#### Technologies Used
1. Python
2. FastAPI
3. spaCy (NLP)
4. HTML
5. CSS
6. JavaScript
7. Git & GitHub

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
└── README.md

#### How It Works
1. User uploads a resume (PDF file)
2. The system extracts text from the PDF
3. NLP is used to detect skills in the resume
4. Resume sections are identified
5. ATS score is generated based on the analysis
6. Results are displayed to the user

#### How to Run the Project
1. git clone https://github.com/your-username/ai-resume-analyzer.git
2. cd ai-resume-analyzer
3. pip install -r requirements.txt
4. python -m spacy download en_core_web_sm
5. python -m uvicorn app.main:app --reload

Open in browser:
http://127.0.0.1:8000

#### Real-World Use Case
This project can be used by students and job seekers to check how their resume performs in an ATS (Applicant Tracking System). It helps users understand whether their resume contains the required skills and important sections such as projects, education, and experience. This system can also help freshers improve their resumes before applying for jobs or internships.

#### Future Improvements
1. Add resume vs job description matching
2. Improve skill detection using advanced NLP models
3. Add support for multiple resume formats (DOCX, TXT)
4. Provide better resume improvement suggestions
5. Deploy the project on cloud for public access
6.Improve ATS scoring logic to match real industry tools.
