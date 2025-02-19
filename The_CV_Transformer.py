import streamlit as st
import openai
import os
import pdfkit

# Set OpenAI API Key
openai.api_key = "sk-proj"  # Replace with your actual API key

st.markdown("<h1 style='text-align: center;'>The CV Transformer</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'> Automate resume revision by prompting GPT-4 through the OpenAI Python API.</p>", unsafe_allow_html=True)

# User Inputs: JD and CV
# Upload CV File
uploaded_file = st.file_uploader("Step 1. Upload your CV (Markdown format - .txt)", type=["txt"])
st.markdown("(Note: This can be accomplished with the assistance of ChatGPT.)")

# Read file content if uploaded
md_resume = ""
if uploaded_file is not None:
    md_resume = uploaded_file.getvalue().decode("utf-8")

#JD
job_description = st.text_area("Step 2: Paste the Job Description (JD) here:", height=200)

if st.button("Optimize CV"):
    if job_description and md_resume:
        with st.spinner("🔄 Optimizing your CV... Please wait!"):
            prompt = f"""
            I have a resume formatted in Markdown and a job description. \
            Please adapt my resume to better align with the job requirements while \
            maintaining a professional tone. Tailor my skills, experiences, and \
            achievements to highlight the most relevant points for the position. \
            Ensure that my resume still reflects my unique qualifications and strengths \
            but emphasizes the skills and experiences that match the job description.

            ### Here is my resume in Markdown:
            {md_resume}

            ### Here is the job description:
            {job_description}

            Please modify the resume to:
            - Use keywords and phrases from the job description.
            - Adjust the bullet points under each role to emphasize relevant skills and achievements.
            - Make sure my experiences are presented in a way that matches the required qualifications.
            - Maintain clarity, conciseness, and professionalism throughout.

            Return the updated resume in Markdown format.
            """

            try:
                response = openai.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[{"role": "system", "content": "You are a helpful assistant."},
                              {"role": "user", "content": prompt}],
                    temperature=0.25
                )

                optimized_resume = response.choices[0].message.content

                # Display optimized CV
                st.subheader("✅ Optimized CV:")
                st.text_area("Modified CV (Markdown Format):", optimized_resume, height=300)

                # Generate PDF
                html_content = f"""
                <html>
                <head><meta charset='utf-8'></head>
                <body>
                <pre>{optimized_resume}</pre>
                </body>
                </html>
                """

                pdf_path = "Optimized_CV.pdf"
                pdfkit.from_string(html_content, pdf_path)

                # Provide download button
                with open(pdf_path, "rb") as pdf_file:
                    st.download_button(
                        label="📥 Download Optimized CV (PDF)",
                        data=pdf_file,
                        file_name="Optimized_CV.pdf",
                        mime="application/pdf"
                    )

            except Exception as e:
                st.error(f"❌ Error: {e}")
    else:
        st.warning("⚠️ Please enter both the Job Description and your CV!")
