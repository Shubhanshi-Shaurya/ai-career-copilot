#  AI Career Copilot

An AI-powered career assistant that helps students and job seekers analyze their skills, identify skill gaps, discover suitable career paths, improve resumes, analyze job descriptions, and prepare for interviews.

---

##  Features

###  Career Recommendation
- Analyze user's skills, interests, education, and experience.
- Recommend suitable career roles.
- Provide personalized career paths.

###  AI Resume Analyzer
- Upload your resume.
- Extract skills, education, projects, and experience.
- Analyze the resume against a target job role.
- Identify missing or weak skills.
- Provide improvement suggestions.
- Generate a resume score.

###  Skill Gap Analysis
Compare the user's current skills with the skills required for a target role.

The system identifies:

- ✅ Existing skills
- ⚠️ Partially developed skills
- ❌ Missing skills

###  Personalized Learning Roadmap
Generate a personalized learning path based on the user's skill gaps.

The roadmap can include:

- Beginner topics
- Intermediate topics
- Advanced topics
- Recommended projects
- Technologies to learn

###  Job Description Analyzer
- Paste or upload a job description.
- Extract required skills and technologies.
- Identify qualifications and experience requirements.
- Compare the job requirements with the user's profile.
- Generate a job compatibility score.

###  AI Interview Preparation
Generate personalized interview questions based on:

- Target role
- Resume
- Skills
- Job description

The system can provide:

- Technical questions
- HR questions
- Follow-up questions
- Answer evaluation
- Improvement suggestions

###  AI Career Chatbot
Users can interact with the AI Career Copilot for personalized career guidance.

Example questions:

> What skills do I need to become an ML Engineer?

> What should I learn after Python and Machine Learning?

> Analyze my resume for an AI internship.

> What skills am I missing for this job?

---

##  System Architecture

```text
                    ┌──────────────────────┐
                    │      Frontend        │
                    │      HTML/CSS        │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │       Backend        │
                    │       Flask          │
                    └──────────┬───────────┘
                               │
             ┌─────────────────┼─────────────────┐
             │                 │                 │
             ▼                 ▼                 ▼
      ┌─────────────┐   ┌─────────────┐   ┌─────────────┐
      │   Resume    │   │   Career    │   │     Job     │
      │   Analyzer  │   │ Recommender │   │   Analyzer   │
      └─────────────┘   └─────────────┘   └─────────────┘
             │                 │                 │
             └─────────────────┼─────────────────┘
                               ▼
                    ┌──────────────────────┐
                    │      AI / LLM        │
                    │   NLP + Generation   │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │      Database        │
                    │ Users / Skills /     │
                    │ Progress / Results   │
                    └──────────────────────┘

```

---

## Tech Stack
### Frontend
- HTML
- CSS
- JavaScript

### Backend
- Python
- Flask
- REST APIs
### AI / Machine Learning
- Python
- NLP
- Large Language Models (LLMs)

### Database
- TIDB Database
- SQLAlchemy

### Tools
- Git
- GitHub
- VS Code

---

## Future Improvements
- Real-time job recommendations
- Career progress dashboard
- Advanced skill embeddings
- AI resume generation
- AI cover letter generation
- Voice-based mock interviews
- ATS resume optimization
- LinkedIn profile analysis
- Project recommendations
- Course and resource recommendations
- Personalized career alerts
- Multi-language support

---

## Project Goals
The main objectives of AI Career Copilot are:

1. Provide personalized career recommendations.
2. Analyze resumes using AI/NLP.
3. Identify skill gaps.
4. Generate personalized learning roadmaps.
5. Analyze job descriptions.
6. Match candidates with job requirements.
7. Provide personalized interview preparation.
8. Help users track their career development.

---