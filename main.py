import os
from dotenv import load_dotenv
from chains.resume_chain import get_screening_pipeline

# Load environment variables (API Keys and Tracing setup)
load_dotenv()

def main():
    # 1. Define the Job Description [cite: 50]
    job_description = """
    Data Scientist Role. Requirements: 
    - 3+ years of experience in Data Science.
    - Strong skills in Python, Machine Learning, and SQL.
    - Experience with tools like TensorFlow, PyTorch, and LangChain.
    """

    # 2. Define the 3 Resumes [cite: 46]
    resumes = {
        "Strong Candidate": """
        John Doe. 4 years of experience as a Data Scientist at TechCorp.
        Skills: Python, Machine Learning, Deep Learning, SQL, NLP.
        Tools: TensorFlow, PyTorch, LangChain, Jupyter.
        """,
        "Average Candidate": """
        Jane Smith. 2 years of experience as a Data Analyst.
        Skills: Python, Data Analysis, SQL, basic Machine Learning.
        Tools: Pandas, Scikit-Learn, Jupyter.
        """,
        "Weak Candidate": """
        Bob Johnson. 5 years of experience in Marketing.
        Skills: Social Media Management, SEO, Content Creation.
        Tools: HubSpot, Google Analytics.
        """
    }

    # 3. Load the pipeline
    screening_pipeline = get_screening_pipeline()

    # 4. Process each resume
    print("--- Starting AI Resume Screening System ---\n")
    for candidate_type, resume_text in resumes.items():
        print(f"Evaluating: {candidate_type}...")
        
        # Prepare the input payload
        input_data = {
            "resume_text": resume_text,
            "job_description": job_description
        }
        
        # Use .invoke() to run the pipeline 
        result = screening_pipeline.invoke(input_data)
        
        print(f"Result:\n{result}\n")
        print("-" * 50)

if __name__ == "__main__":
    main()