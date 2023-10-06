import os
os.environ['OPENAI_API_KEY'] = "enter-yours-here"

from langchain.llms	 import OpenAI
from langchain.agents import load_tools, initialize_agent

prompt = "What is 2+2? Provide an explanation of how the final answer was obtained."

llm = OpenAI(temperature=0)
tools = load_tools(["wikipedia", "llm-math"], llm=llm)
agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)

agent.run(prompt)
