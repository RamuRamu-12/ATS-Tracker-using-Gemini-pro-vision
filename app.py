# from dotenv import load_dotenv

# load_dotenv()
# import base64
# import streamlit as st
# import os
# import io
# from PIL import Image 
# import pdf2image
# import google.generativeai as genai

# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# def get_gemini_response(input,pdf_content,prompt):
#     model=genai.GenerativeModel('gemini-pro-vision')
#     response=model.generate_content([input,pdf_content[0],prompt])
#     return response.text

# def input_pdf_setup(uploaded_file):
#     if uploaded_file is not None:
#         ## Convert the PDF to image
#         images=pdf2image.convert_from_bytes(uploaded_file.read())

#         first_page=images[0]

#         # Convert to bytes
#         img_byte_arr = io.BytesIO()
#         first_page.save(img_byte_arr, format='JPEG')
#         img_byte_arr = img_byte_arr.getvalue()

#         pdf_parts = [
#             {
#                 "mime_type": "image/jpeg",
#                 "data": base64.b64encode(img_byte_arr).decode()  # encode to base64
#             }
#         ]
#         return pdf_parts
#     else:
#         raise FileNotFoundError("No file uploaded")

# ## Streamlit App

# st.set_page_config(page_title="ATS Resume EXpert")
# st.header("ATS Tracking System")
# input_text=st.text_area("Job Description: ",key="input")
# uploaded_file=st.file_uploader("Upload your resume(PDF)...",type=["pdf"])


# if uploaded_file is not None:
#     st.write("PDF Uploaded Successfully")


# submit1 = st.button("Tell Me About the Resume")

# submit2 = st.button("Customization Tips")

# submit3 = st.button("Percentage match")

# submit4 = st.button("Keywords Missed")

# submit5 = st.button("Cover letter for above Job Description")

# input_prompt1 = """
#  You are an experienced Technical Human Resource Manager,your task is to review the provided resume against the job description. 
#   Please share your professional evaluation on whether the candidate's profile aligns with the role. 
#  Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
# """

# input_prompt3 = """
# You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality, 
# your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume matches
# the job description. First the output should come as percentage and then keywords missing and last final thoughts.
# """

# input_prompt2="""
# You are an expert career advisor, and you need to help job seekers understand how to customize their resumes effectively. When responding to the question "How Can I Customize the Resume?", ensure that you cover the following key points:

# Understanding the Job Description:

# Explain the importance of carefully reading the job description.
# Highlight how to identify key skills and requirements mentioned in the job description.

# Tailoring Content:
# Describe how to align your resume content with the job description.
# Include advice on highlighting relevant experiences, skills, and achievements that match the job requirements.

# Using Keywords:
# Discuss the significance of using keywords from the job posting.
# Provide examples of how to incorporate these keywords naturally into the resume.

# Your response should be detailed, practical, and actionable, providing clear steps and examples where applicable.

# """

# input_prompt4="""
# You are an expert career advisor, and you need to help job seekers identify the keywords they may have missed in their resumes. When responding to the question "What keywords did I miss in my resume?", ensure that you cover the following key points:


# Comparing with the Resume:

# Provide a method for comparing the extracted keywords with the content of the current resume.
# Suggest tools or techniques for identifying missing keywords (e.g., keyword comparison tools, manual review).

# Your response should be detailed, practical, and actionable, providing clear steps and examples where applicable.
# """

# input_prompt5="""
# You are an expert career advisor, and you need to help job seekers write an effective cover letter that aligns with a specific job description and their resume. When responding to the question "How can I write a cover letter for the above job description?"
# Your response should be detailed, practical, and actionable, providing clear steps and examples where applicable.
# Give the cover letter in a structured format by analysing the above job description.
# """




# if submit1:
#     if uploaded_file is not None:
#         pdf_content=input_pdf_setup(uploaded_file)
#         response=get_gemini_response(input_prompt1,pdf_content,input_text)
#         st.subheader("The Repsonse is")
#         st.write(response)
#     else:
#         st.write("Please uplaod the resume")

# if submit2:
#     if uploaded_file is not None:
#         pdf_content=input_pdf_setup(uploaded_file)
#         response=get_gemini_response(input_prompt2,pdf_content,input_text)
#         st.subheader("The Repsonse is")
#         st.write(response)
#     else:
#         st.write("Please uplaod the resume")       

# if submit3:
#     if uploaded_file is not None:
#         pdf_content=input_pdf_setup(uploaded_file)
#         response=get_gemini_response(input_prompt3,pdf_content,input_text)
#         st.subheader("The Repsonse is")
#         st.write(response)
#     else:
#         st.write("Please uplaod the resume")


# if submit4:
#     if uploaded_file is not None:
#         pdf_content=input_pdf_setup(uploaded_file)
#         response=get_gemini_response(input_prompt4,pdf_content,input_text)
#         st.subheader("The Repsonse is")
#         st.write(response)
#     else:
#         st.write("Please uplaod the resume")


# if submit5:
#     if uploaded_file is not None:
#         pdf_content=input_pdf_setup(uploaded_file)
#         response=get_gemini_response(input_prompt5,pdf_content,input_text)
#         st.subheader("The Repsonse is")
#         st.write(response)
#     else:
#         st.write("Please uplaod the resume")



import base64
import io
import os
from dotenv import load_dotenv

import pdf2image
import streamlit as st
from PIL import Image
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Google API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get response from Gemini model
def get_gemini_response(input, pdf_content, prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input, pdf_content[0], prompt])
    return response.text

# Function to process the uploaded PDF
def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        # Convert the PDF to image
        images = pdf2image.convert_from_bytes(uploaded_file.read())

        first_page = images[0]

        # Convert to bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()  # encode to base64
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")

# Streamlit App Configuration
st.set_page_config(page_title="ATS Resume Expert", page_icon=":briefcase:", layout="wide")

# CSS for custom styling
st.markdown("""
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
        }
        .main-container {
            background-color: #ffffff;
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        .header {
            color: #2c3e50;
            text-align: center;
        }
        .button-container {
            text-align: center;
            margin-top: 1rem;
        }
        .stButton button {
            background-color: #2c3e50;
            color: white;
            border: none;
            border-radius: 5px;
            padding: 10px 20px;
        }
        .stButton button:hover {
            background-color: #1abc9c;
        }
    </style>
""", unsafe_allow_html=True)

# Main Container
with st.container():
    st.markdown("<h1 class='header'>ATS Tracking System</h1>", unsafe_allow_html=True)

    # Input Area
    input_text = st.text_area("Job Description:", key="input", height=200)
    uploaded_file = st.file_uploader("Upload your resume (PDF)...", type=["pdf"])

    if uploaded_file is not None:
        st.success("PDF Uploaded Successfully")

    # Button Container
    with st.container():
        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            submit1 = st.button("Review Resume")

        with col2:
            submit2 = st.button("Customization Tips")

        with col3:
            submit3 = st.button("Percentage Match")

        with col4:
            submit4 = st.button("Keywords Missed")

        with col5:
            submit5 = st.button("Cover Letter")

    # Input Prompts
    input_prompt1 = """
    You are an experienced Technical Human Resource Manager,your task is to review the provided resume against the job description. 
  Please share your professional evaluation on whether the candidate's profile aligns with the role. 
 Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
    """

    input_prompt2 = """
    You are an expert career advisor, and you need to help job seekers understand how to customize their resumes effectively. When responding to the question "How Can I Customize the Resume?", ensure that you cover the following key points:

Understanding the Job Description:

Explain the importance of carefully reading the job description.
Highlight how to identify key skills and requirements mentioned in the job description.

Tailoring Content:
Describe how to align your resume content with the job description.
Include advice on highlighting relevant experiences, skills, and achievements that match the job requirements.

Using Keywords:
Discuss the significance of using keywords from the job posting.
Provide examples of how to incorporate these keywords naturally into the resume.

Your response should be detailed, practical, and actionable, providing clear steps and examples where applicable.
    """

    input_prompt3 = """
    You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality, 
your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume matches
the job description. First the output should come as percentage and then keywords missing and last final thoughts.
    """

    input_prompt4 = """
    You are an expert career advisor, and you need to help job seekers identify the keywords they may have missed in their resumes. When responding to the question "What keywords did I miss in my resume?", ensure that you cover the following key points:


Comparing with the Resume:

Provide a method for comparing the extracted keywords with the content of the current resume.
Suggest tools or techniques for identifying missing keywords (e.g., keyword comparison tools, manual review).

Your response should be detailed, practical, and actionable, providing clear steps and examples where applicable.
    """

    input_prompt5 = """
    You are an expert career advisor, and you need to help job seekers write an effective cover letter that aligns with a specific job description and their resume. When responding to the question "How can I write a cover letter for the above job description?"
    Your response should be detailed, practical, and actionable, providing clear steps and examples where applicable.
    Give the cover letter in a structured format by analyzing the above job description.
    """

    # Button Actions
    if submit1:
        if uploaded_file is not None:
            pdf_content = input_pdf_setup(uploaded_file)
            response = get_gemini_response(input_prompt1, pdf_content, input_text)
            st.subheader("The Response is")
            st.write(response)
        else:
            st.error("Please upload the resume")

    if submit2:
        if uploaded_file is not None:
            pdf_content = input_pdf_setup(uploaded_file)
            response = get_gemini_response(input_prompt2, pdf_content, input_text)
            st.subheader("The Response is")
            st.write(response)
        else:
            st.error("Please upload the resume")

    if submit3:
        if uploaded_file is not None:
            pdf_content = input_pdf_setup(uploaded_file)
            response = get_gemini_response(input_prompt3, pdf_content, input_text)
            st.subheader("The Response is")
            st.write(response)
        else:
            st.error("Please upload the resume")

    if submit4:
        if uploaded_file is not None:
            pdf_content = input_pdf_setup(uploaded_file)
            response = get_gemini_response(input_prompt4, pdf_content, input_text)
            st.subheader("The Response is")
            st.write(response)
        else:
            st.error("Please upload the resume")

    if submit5:
        if uploaded_file is not None:
            pdf_content = input_pdf_setup(uploaded_file)
            response = get_gemini_response(input_prompt5, pdf_content, input_text)
            st.subheader("The Response is")
            st.write(response)
        else:
            st.error("Please upload the resume")


