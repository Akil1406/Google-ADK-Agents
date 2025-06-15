import os
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

root_agent = Agent(
    name="greeting_agent",
    model=LiteLlm(model="ollama/llama3.2"),
    #model=LiteLlm(model="openai/gpt-4o"),
    description="Greeting agent",
    instruction="""
    You are a helpful assistant that greets the user. 
    Ask for the user's name and greet them by name.
    """,
)