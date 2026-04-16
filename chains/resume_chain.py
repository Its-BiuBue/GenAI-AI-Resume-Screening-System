from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.output_parsers import StrOutputParser
from prompts.extraction_prompt import extraction_prompt
from prompts.evaluation_prompt import evaluation_prompt

def get_screening_pipeline():
    # 1. Initialize Qwen 2.5 (Without forcing the text-generation task)
    base_llm = HuggingFaceEndpoint(
        repo_id="Qwen/Qwen2.5-7B-Instruct",
        temperature=0.1, 
        max_new_tokens=512
    )
    
    # 2. WRAP IT in ChatHuggingFace to satisfy the "conversational" rule for Together AI
    chat_llm = ChatHuggingFace(llm=base_llm)
    
    parser = StrOutputParser()

    # 3. Create the extraction step
    extraction_chain = extraction_prompt | chat_llm | parser

    # 4. Create the full LCEL pipeline
    pipeline = (
        {
            "extracted_details": extraction_chain, 
            "job_description": lambda x: x["job_description"]
        }
        | evaluation_prompt
        | chat_llm
        | parser
    )
    
    return pipeline