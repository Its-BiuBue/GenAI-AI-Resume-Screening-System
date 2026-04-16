from langchain_core.prompts import PromptTemplate

# Steps 2, 3, & 4: Match, Score, and Explain [cite: 57, 58, 59]
evaluation_template = """
You are an AI Resume Evaluator. You need to compare a candidate's extracted details with a Job Description.

Job Description:
{job_description}

Candidate Extracted Details:
{extracted_details}

Tasks:
1. Compare the candidate's skills and experience with the job requirements.
2. Assign a fit score from 0 to 100. [cite: 58]
3. Provide a detailed explanation of why this score was assigned. [cite: 60]

Format your output strictly as a JSON object:
{{
    "score": <number>,
    "explanation": "<detailed reasoning>"
}}
"""

evaluation_prompt = PromptTemplate.from_template(evaluation_template)