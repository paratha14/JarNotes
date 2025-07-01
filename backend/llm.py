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

#f= open("demo.txt", "r")
#file= f.read()

def process_file(fi: str, user_input: int, topic: str):
    #user_input = int(input("Enter your choice \n1 for getting summary of the doc. \n2 for getting an explanation of the specified topic/keyword "))
    if user_input == "1":
        #f= open(fi, "r")
        #file= f.read()
        template= PromptTemplate(
            template="""Give me a Summary of the following document in 10 lines only: {file}""",
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
            template="Give me an explanation of the following topic: {topic} in the document in 5 lines only: {file}",
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
            template="""Give me Notes on the following document including all important matter along with 2-3 lines of ecxplanation: {file}""",
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

#process_file("demo.txt")