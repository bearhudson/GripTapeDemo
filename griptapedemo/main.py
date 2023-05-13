from griptape.memory import Memory
from griptape.ramps import TextStorageRamp, BlobStorageRamp
from griptape.structures import Pipeline
from griptape.tasks import ToolkitTask, PromptTask
from griptape.tools import WebScraper, TextProcessor, FileManager

# Ramps enable LLMs to store and manipulate data without ever looking at it directly.
text_storage = TextStorageRamp()
blob_storage = BlobStorageRamp()

# Connect a web scraper to load web pages.
web_scraper = WebScraper(
    ramps={
        "get_content": [text_storage]
    }
)

# TextProcessor enables LLMs to summarize and query text.
text_processor = TextProcessor(
    ramps={
        "summarize": [text_storage],
        "query": [text_storage]
    }
)

# File manager can load and store files locally.
file_manager = FileManager(
    ramps={
        "load": [blob_storage],
        "save": [text_storage, blob_storage]
    }
)

# Pipelines represent sequences of tasks.
pipeline = Pipeline(
    memory=Memory()
)

pipeline.add_tasks(
    # Load up the first argument from `pipeline.run`.
    ToolkitTask(
        "{{ args[0] }}",
        tools=[web_scraper, text_processor, file_manager]
    ),
    # Augment `input` from the previous task.
    PromptTask(
        "Say the following in spanish: {{ input }}"
    )
)

result = pipeline.run("Load https://griptape.readthedocs.io, summarize it, and store it in griptape.txt")

print(result.output.to_text())