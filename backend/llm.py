from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os
load_dotenv()

llm= ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.45,
    
)

def process_file(fi: str, user_input: int, topic: str):
    #user_input = int(input("Enter your choice \n1 for getting summary of the doc. \n2 for getting an explanation of the specified topic/keyword "))
    if user_input == "1":
        #f= open(fi, "r")
        #file= f.read()
        template= PromptTemplate(
            template="""You are an expert summarizer. 
        Analyze the following document carefully and provide a clear, concise summary in exactly 10 lines. 
        Each line should capture a distinct and important point, maintaining the original meaning and context.
        Avoid adding personal opinions or information not present in the text.
        Use simple, professional language so the summary is easy to understand.
        Document content:
        {file}""",
            input_variables=["file"]
        )
        prompt= template.invoke({
            "file": fi
        })
        #messages= [
        #SystemMessage(content="You are a helpful assistant that summarizes text present in the follwoing document."),
        #HumanMessage(content=prompt)
    
        #]
        result= llm.invoke(prompt)
        #messages.append(AIMessage(content=result.content))
        #print(messages)
        print(result)
        
    
    elif user_input == "2":
        #topic= input("enter specific topics you want to know about and get explanation of how they were used in the document: ")
        topic= topic
        #f= open(fi, "r")
        #file= f.read()

        
        template= PromptTemplate(
            template="""You are an expert explainer. 
        Read the provided document and focus only on the topic: {topic}. 
        Provide a clear and concise explanation of this topic in exactly 5 lines. 
        Along with the general meaning, also explain:
        - How and where it is used in the document.
        - In what sense or context it appears.
        - Its role or importance in relation to other content.
        - Any related aspects or implications present in the document.
        Do not include personal opinions or external details not found in the document.

        Document content:
        {file}""",

            input_variables=["topic", "file"]
        )
        prompt= template.invoke({
            "topic": topic,
            "file": fi
        })

        #messages= [
        #SystemMessage(content="You are a helpful assistant that explains the  topic in the context of the document."),
        #HumanMessage(content=prompt)
        #]

        result= llm.invoke(prompt)
        #messages.append(AIMessage(content=result.content))
        #print(messages)
    if user_input == "3":
        #f= open(fi, "r")
        #file= f.read()
        template= PromptTemplate(
            template="""You are an expert note-maker. 
        Read the following document carefully and create clear, well-structured notes that:
        - Cover all important topics, concepts, and key points from the document.
        - Include relevant examples from the document wherever possible.
        - Are crisp and concise, avoiding unnecessary details.
        - Are organized in a way that makes them easy to revise during last-minute study.
        - Use bullet points or numbered lists for better readability.
        - Try to add examples too.

        Document content:
        {file}""",
            input_variables=["file"]
        )
        prompt= template.invoke({
            "file": fi
        })
        #messages= [
        #SystemMessage(content="You are a helpful assistant that summarizes text present in the follwoing document."),
        #HumanMessage(content=prompt)
    
        #]
        result= llm.invoke(prompt)
        #messages.append(AIMessage(content=result.content))
        #print(messages)
        print(result)
    return result.content