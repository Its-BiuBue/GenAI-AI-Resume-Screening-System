from langchain_core.prompts import PromptTemplate

# Steps 2, 3, & 4: Match, Score, and Explain (Now with Few-Shot Example!)
evaluation_template = """
You are an AI Resume Evaluator. You need to compare a candidate's extracted details with a Job Description.

Job Description:
{job_description}

Candidate Extracted Details:
{extracted_details}

Tasks:
1. Compare the candidate's skills and experience with the job requirements.
2. Assign a fit score from 0 to 100.
3. Provide a detailed explanation of why this score was assigned.

Format your output strictly as a JSON object:
{{
    "score": <number>,
    "explanation": "<detailed reasoning>"
}}

---
FEW-SHOT EXAMPLE:
If the Job Description asks for "5 years of Python and AWS" and the candidate has "6 years of Python, GCP, and Azure":
{{
    "score": 75,
    "explanation": "The candidate exceeds the 5-year experience requirement and has strong Python skills. However, they lack specific AWS experience, offering GCP and Azure instead. Therefore, a score of 75 reflects strong foundational skills but a gap in the specific cloud platform requested."
}}
---
"""

evaluation_prompt = PromptTemplate.from_template(evaluation_template)