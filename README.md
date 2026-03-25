# QuickCraft

A Django web app that generates question papers using AI. Fill in the subject details, optionally upload a PDF, and download a ready-to-use `.docx` question paper.

## Features

- AI-generated questions via DeepSeek (OpenRouter)
- Configure subject, total marks, difficulty, number of questions, and duration
- Optional PDF upload — generate questions **only from the PDF** or use it as **additional context**
- Downloads a formatted `.docx` question paper

## Tech Stack

- **Backend**: Django 5.2, Python 3.12
- **AI**: DeepSeek R1 via OpenRouter API
- **PDF parsing**: PyMuPDF (`fitz`)
- **Document generation**: `python-docx`
- **Database**: SQLite

## Setup

1. **Clone the repo**
   ```bash
   git clone <repo-url>
   cd QuickCraft/myproject
   ```

2. **Install dependencies**
   ```bash
   pip install django pymupdf python-docx openai
   ```

3. **Add your API key**

   In `myapp/views.py`, replace the placeholder with your OpenRouter API key:
   ```python
   client = OpenAI(
       base_url="https://openrouter.ai/api/v1",
       api_key="your-api-key-here",
   )
   ```

4. **Run the server**
   ```bash
   python manage.py runserver
   ```

   Visit `http://127.0.0.1:8000`

## Usage

1. Go to the dashboard and fill in:
   - Subject name
   - Total marks
   - Difficulty level
   - Number of questions
   - Duration
2. Optionally upload a PDF and choose:
   - **Only from PDF** — questions are strictly based on the PDF content
   - **Also from PDF** — PDF is used as additional context alongside the subject
3. Click generate and the `.docx` file will download automatically.

## Project Structure

```
myproject/
├── myapp/
│   ├── views.py       # Core logic: PDF parsing, AI request, docx generation
│   └── urls.py        # URL routing
├── myproject/
│   └── settings.py    # Django settings
├── templates/         # HTML templates
├── static/            # CSS and images
└── manage.py
```
