from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# Uncomment the following line to use an example of a custom tool
# from content_agent.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool

@CrewBase
class ContentAgentCrew():
	"""ContentAgent crew"""
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def content_strategist(self) -> Agent:
		return Agent(
			config=self.agents_config['content_strategist'],
			# tools=[MyCustomTool()], # Example of custom tool, loaded on the beginning of file
			verbose=True
		)

	@agent
	def linkedin_expert(self) -> Agent:
		return Agent(
			config=self.agents_config['linkedin_expert'],
			verbose=True
		)

	@agent
	def editor_proofreader(self) -> Agent:
		return Agent(
			config=self.agents_config['editor_proofreader'],
			verbose=True
		)

	@task
	def content_strategist_task(self) -> Task:
		return Task(
			config=self.tasks_config['content_strategist_task'],
			agent=self.content_strategist()
		)

	@task
	def linkedin_post_task(self) -> Task:
		return Task(
			config=self.tasks_config['linkedin_post_task'],
			agent=self.linkedin_expert(),
	
		)

	@task
	def review_task(self) -> Task:
		return Task(
			config=self.tasks_config['review_task'],
			agent=self.editor_proofreader(),
		)
	

	@crew
	def crew(self) -> Crew:
		"""Creates the ContentAgent crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=2,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)