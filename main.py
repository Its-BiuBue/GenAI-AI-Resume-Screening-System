import os
from dotenv import load_dotenv
from chains.resume_chain import get_screening_pipeline

# Load environment variables (LangSmith API keys and Tracing flag)
load_dotenv()

def load_resumes_from_folder(folder_path="data"):
    """Reads all .txt files from the specified folder."""
    resumes = {}
    if not os.path.exists(folder_path):
        return resumes
        
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, "r", encoding="utf-8") as file:
                resumes[filename] = file.read()
                
    return resumes

def main():
    # 1. Define the Job Description
    job_description = """
    Data Scientist Role. Requirements: 
    - 3+ years of experience in Data Science.
    - Strong skills in Python, Machine Learning, and SQL.
    - Experience with tools like TensorFlow, PyTorch, and LangChain.
    """

    # 2. Load the LangChain pipeline
    screening_pipeline = get_screening_pipeline()
    
    # 3. Dynamically load resumes from the data folder
    print("Loading resumes from data folder...")
    resumes = load_resumes_from_folder("data")
    
    # Fallback to dummy data if the data folder is empty or missing
    if not resumes:
        print("No files found in 'data/'. Using fallback dummy resumes...\n")
        resumes = {
            "Strong Candidate.txt": """
            John Doe. 4 years of experience as a Data Scientist at TechCorp.
            Skills: Python, Machine Learning, Deep Learning, SQL, NLP.
            Tools: TensorFlow, PyTorch, LangChain, Jupyter.
            """,
            "Average Candidate.txt": """
            Jane Smith. 2 years of experience as a Data Analyst.
            Skills: Python, Data Analysis, SQL, basic Machine Learning.
            Tools: Pandas, Scikit-Learn, Jupyter.
            """,
            "Weak Candidate.txt": """
            Bob Johnson. 5 years of experience in Marketing.
            Skills: Social Media Management, SEO, Content Creation.
            Tools: HubSpot, Google Analytics.
            """
        }

    print(f"Found {len(resumes)} resumes. Starting Evaluation...\n")
    print("-" * 50)
    
    # 4. Process each resume and apply LangSmith tags
    for filename, resume_text in resumes.items():
        print(f"Evaluating: {filename}...")
        
        # Prepare the input payload
        input_data = {
            "resume_text": resume_text,
            "job_description": job_description
        }
        
        # BONUS: Dynamically create safe LangSmith tags based on the filename
        # Example: "Strong Candidate.txt" becomes "strong_candidate.txt"
        safe_tag_name = filename.replace(" ", "_").lower()
        run_tags = ["resume_screening_system", safe_tag_name]
        
        # BONUS: Use .invoke() and pass the tags in the config dictionary
        result = screening_pipeline.invoke(
            input_data, 
            config={"tags": run_tags}
        )
        
        print(f"Result:\n{result}\n")
        print("-" * 50)

if __name__ == "__main__":
    main()