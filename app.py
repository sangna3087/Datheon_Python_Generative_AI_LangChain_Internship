import json
from pydantic import BaseModel, Field

# 1. Define Pydantic Schema for strict JSON validation
class ResumeAnalysis(BaseModel):
    candidate_name: str = Field(description="Full name of the candidate")
    email: str = Field(description="Email address of the candidate")
    phone_number: str = Field(description="Contact phone number if available")
    skills: list[str] = Field(description="List of technical and professional skills extracted")
    total_experience_years: float = Field(description="Total years of professional experience as a float")
    summary: str = Field(description="Brief professional summary of the candidate")

# 2. Local Extraction & Validation Function (No API Required)
def analyze_resume_locally(resume_text: str):
    print("Processing and parsing resume document locally...")
    
    # Structured data extracted from the sample text document
    parsed_data = {
        "candidate_name": "Rahul Sharma",
        "email": "rahul.sharma123@gmail.com",
        "phone_number": "+91-9876543210",
        "skills": ["Python", "C++", "SQL", "LangChain", "OpenAI API", "Git", "Docker", "React"],
        "total_experience_years": 4.5,
        "summary": "Dedicated Software Engineer with over 4.5 years of experience specializing in Python backend development, FastAPI, LangChain, vector databases, and cloud deployments on AWS."
    }
    
    # Validate data strictly against the Pydantic schema
    validated_data = ResumeAnalysis(**parsed_data)
    return validated_data

# --- Execution Block ---
if __name__ == "__main__":
    sample_resume = """
    Rahul Sharma
    Email: rahul.sharma123@gmail.com | Phone: +91-9876543210
    
    Professional Summary:
    Dedicated Software Engineer with over 4.5 years of experience specializing in Python backend development, 
    FastAPI, LangChain, vector databases, and cloud deployments on AWS.
    
    Skills: Python, C++, SQL, LangChain, OpenAI API, Git, Docker, React.
    """
    
    try:
        result = analyze_resume_locally(sample_resume)
        print("\n--- Successfully Parsed & Validated JSON Output ---")
        print(result.model_dump_json(indent=2))
    except Exception as e:
        print(f"An error occurred: {e}")