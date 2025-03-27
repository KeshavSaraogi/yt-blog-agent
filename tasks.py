from crewai import Task
from tools import youtubeTool
from agents import researcher, writer

## research task
researchTask = Task(
    description = (
        "Identify the video: {topic}"
        "Get detailed information about the video from the channel."
    ), 
    expected_output = 'A comprehensive report of 3 paragraphs based on the {topic} of video content',
    tools = [youtubeTool],
    agent = researcher
)

writeTask = Task(
    description = ("Get information from the youtube channel on the topic {topic}"),
    expected_outcome = "Summarize the information from the youtube channel video on the topic {topic} and write a blog in 3 paragraphs.",
    tools = [youtubeTool],
    agent = writer,
    async_execution = False,
    output_file = 'new-blog-post.md'
)