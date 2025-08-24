from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv


load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.89,
)

def process_file(fi: str, user_input: str, topic: str):
    result = None
    
    if user_input == "1":   # Summary
        template = PromptTemplate(
            template="""You are an expert cricket note-maker.  
Summarize the following document into **well-structured bullet points** that are:  
- Start **directly with the main heading of the content** (do not write things like "Here’s a summary" or "In conclusion").
- Concise yet detailed enough for exam revision.  
- Grouped into sections with clear headings/sub-headings.  
- Each point should be crisp (one idea per bullet).  
- Add 1–2 additional relevant points of explanation or context (like why/when a position is used, or example match scenarios).  
- Ensure formatting is neat with indentation and sub-bullets if needed.  

Document content:  
{file}""",
            input_variables=["file"]
        )
        prompt = template.invoke({"file": fi})
        result = llm.invoke(prompt)
        print(result.content)

    elif user_input == "2":   # Topic Explanation
        template = PromptTemplate(
            template="""You are an expert explainer.  
Read the provided document and focus only on the topic: {topic}.  
Provide a clear and concise explanation of this topic in exactly 7–9 lines.  
Along with the general meaning, also explain:
- Start **directly with the main heading of the content** (do not write things like "Here’s a summary" or "In conclusion").
- How and where it is used in the document.  
- In what sense or context it appears.  
- Its role or importance in relation to other content.  
- Any related aspects or implications present in the document.  

Do not include personal opinions or external details not found in the document.  

Document content:  
{file}""",
            input_variables=["topic", "file"]
        )
        prompt = template.invoke({"topic": topic, "file": fi})
        result = llm.invoke(prompt)
        print(result.content)

    elif user_input == "3":   # Detailed Notes
        template = PromptTemplate(
            template="""You are an expert note-maker and exam-prep guide.  
Read the following document and create **detailed bullet-point notes** that are:  
- Start **directly with the main heading of the content** (do not write things like "Here’s a summary" or "In conclusion").
- Well structured with headings and sub-headings.  
- Each point should capture a key idea, with short explanations/examples.  
- Add extra context (where relevant) to help students understand better.  
- Keep sentences short and revision-friendly.  
- Use indentation for sub-points.  
- Ensure the notes can directly help someone **revise quickly before exams**.  

Document content:  
{file}""",
            input_variables=["file"]
        )
        prompt = template.invoke({"file": fi})
        result = llm.invoke(prompt)
        print(result.content)

    return result.content if result else None
