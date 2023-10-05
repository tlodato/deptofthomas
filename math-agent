# Plan & execute agent, here used to solve a prompt with a math question 

import os
os.environ['OPENAI_API_KEY'] = "enter-yours-here"

from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.experimental.plan_and_execute import PlanAndExecute, load_agent_executor, load_chat_planner
from langchain import LLMMathChain
from langchain.agents.tools import Tool

llm = OpenAI(temperature=0)
llm_math_chain =  LLMMathChain.from_llm(llm=llm, verbose=True)

tools = [

	Tool(

		name = "Calculator",
		func = llm_math_chain.run,
		description = "useful for when you need to answer questions about math"
	)
]

prompt =  "What is 2+2? Explain how you got an answer."

model = ChatOpenAI(temperature=0)
planner = load_chat_planner(model)
executor = load_agent_executor(model, tools, verbose=True)
agent = PlanAndExecute(planner=planner, executor=executor, verbose=False)

agent.run(prompt)
