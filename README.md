The CV Transformer

Overview

The CV Transformer is a Streamlit-based web application that automates resume revision using OpenAI's GPT-4 API. This tool helps job seekers tailor their resumes to match job descriptions more effectively, ensuring their qualifications align with the job requirements.

Features

Upload a CV in Markdown (.txt format).

Paste a Job Description (JD) to tailor the resume accordingly.

Uses OpenAI's GPT-4 to optimize the resume based on the JD.

Highlights relevant skills, experiences, and achievements.

Provides a downloadable optimized resume in Markdown format.

Technologies Used

Streamlit for the web interface.

OpenAI API for AI-powered resume optimization.

Python for backend processing.

Installation & Setup

Prerequisites

Ensure you have Python installed on your system. You can download it from python.org.

Steps to Run the Project

Clone this repository:

git clone https://github.com/your-username/cv-transformer.git
cd cv-transformer

Install the required dependencies:

pip install -r requirements.txt

Set up your OpenAI API key:

Replace openai.api_key = "sk-proj" with your actual OpenAI API key in the script.

Alternatively, set the API key as an environment variable:

export OPENAI_API_KEY="your-api-key"

Run the Streamlit application:

streamlit run app.py

Usage

Upload your CV in Markdown format (.txt file).

Paste the job description (JD) in the provided text area.

Click the Optimize CV button.

The AI will generate an improved version of your CV tailored to the JD.

Download the optimized CV and use it for job applications.

Example Screenshot

![Screenshot 2025-02-19 133934](https://github.com/user-attachments/assets/767bf221-cb72-41ad-bc8b-5e6bc7c8ef76)

Contribution

Feel free to contribute by submitting pull requests or reporting issues.

License

This project is licensed under the MIT License.

Contact

For any questions, reach out to balamurukan.su@gmail.com.
