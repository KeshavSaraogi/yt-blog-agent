from crewai import Agent
from tools import youtubeTool

## Blog Researcher Agent
researcher = Agent(
    role = 'Blog Researcher from Youtube Videos',
    goal = 'Get relevant video content for the topic {topic} from the Youtube Channel',
    verbose = True,
    memory = True,
    backstory = (
        "Expert in understanding videos in the field of AI, ML, Data Science and GenAI."
    ),
    tools = [youtubeTool],
    allow_delegation = True
)

## Blog Writer Agent with YT tools
writer = Agent(
    role = 'Blog Writer',
    goal = 'Narrate compelling stories about the video {topic} from Youtube channel',
    verbose = True,
    memory = True,
    backstory = (
    """With a flair for simplifying complex topics,
    you craft engaging narratives that captivate and educate,
    bringing new discoveries to light in an accessible way.
    """
    ),
    tools = [youtubeTool],
    allow_delegation = False
)