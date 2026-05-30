from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai_tools import ExaSearchTool


@CrewBase
class DevopsAgent():
    """DevopsAgent crew"""

    agents: list[BaseAgent]
    tasks: list[Task]

    @agent
    def pipeline_log_analyzer(self) -> Agent:
        return Agent(
            config=self.agents_config['pipeline_log_analyzer'], 
            verbose=True
        )

    @agent
    def issue_investigator(self) -> Agent:
        return Agent(
            config=self.agents_config['issue_investigator'], 
            verbose=True,
            tools=[ExaSearchTool()]
        )
    
    @agent
    def solution_synthesizer(self) -> Agent:
        return Agent(
            config=self.agents_config['solution_synthesizer'], 
            verbose=True
        )

    @task
    def log_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['log_analysis_task']
        )

    @task
    def issue_investigation_task(self) -> Task:
        return Task(
            config=self.tasks_config['issue_investigation_task']
        )
    
    
    @task
    def solution_synthesis_task(self) -> Task:
        return Task(
            config=self.tasks_config['solution_synthesis_task']
        )

    @crew
    def crew(self) -> Crew:
        """Creates the DevopsAgent crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
