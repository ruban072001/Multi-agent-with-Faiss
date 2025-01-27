from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from dotenv import load_dotenv
load_dotenv()

@CrewBase
class AgenticCrew():
	"""AgenticCrew crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'
 
	def __init__(self, document_tool):
	
		self.document_tool = document_tool

	@agent
	def query_parser_agent(self) -> Agent:
		return Agent(
			config=self.agents_config["query_parser_agent"],
			verbose = True
		)

	@agent
	def retriever_agent(self) -> Agent:
		return Agent(
			config=self.agents_config["retriever_agent"],
			tools=[self.document_tool], 
			verbose = True
		)
        
	@agent
	def ranker_agent(self) -> Agent:
		return Agent(
			config=self.agents_config["ranker_agent"],
			verbose = True
		)
        
	@agent
	def response_generator_agent(self) -> Agent:
		return Agent(
			config=self.agents_config["response_generator_agent"],	 
			verbose = True
		)
        
	@task
	def query_parser_agent_task(self) -> Task:
		return Task(
			config=self.tasks_config["query_parser_agent_task"],
		)
        
	@task
	def retriever_agent_task(self) -> Task:
		return Task(
			config=self.tasks_config["retriever_agent_task"],
		)
        
	@task
	def ranker_agent_task(self) -> Task:
		return Task(
			config=self.tasks_config["ranker_agent_task"],
		)
        
	@task
	def response_generator_agent_task(self) -> Task:
		return Task(
			config=self.tasks_config["response_generator_agent_task"],
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the AgenticCrew crew"""

		return Crew(
			agents=self.agents, 
			tasks=self.tasks,
			process=Process.sequential,
			verbose=True,
		)
