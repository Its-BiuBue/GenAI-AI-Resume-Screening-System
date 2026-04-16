from langchain_core.prompts import PromptTemplate

# Step 1: Skill Extraction [cite: 53]
extraction_template = """
You are an expert technical recruiter. Extract the following details from the candidate's resume:
1. Skills [cite: 54]
2. Experience [cite: 55]
3. Tools [cite: 56]

CRITICAL RULE: Do NOT assume skills not present in the resume. [cite: 84]

Resume Text:
{resume_text}

Output the extracted information in a clean, structured JSON format.
"""

extraction_prompt = PromptTemplate.from_template(extraction_template)