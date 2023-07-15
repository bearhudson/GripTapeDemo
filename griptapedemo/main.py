from griptape.engines import VectorQueryEngine
from griptape.loaders import WebLoader
from griptape.rules import Ruleset, Rule
from griptape.structures import Agent
from griptape.tools import KnowledgeBaseClient
from griptape.utils import Chat
import tkinter as tk
#
# namespace = "physics-wiki"
#
# engine = VectorQueryEngine()
#
# artifacts = WebLoader().load(
#     "https://en.wikipedia.org/wiki/Physics"
# )
#
# engine.vector_store_driver.upsert_text_artifacts(
#     {namespace: artifacts}
# )
# 
#
# kb_client = KnowledgeBaseClient(
#     description="Contains information about physics. "
#                 "Use it to answer any physics-related questions.",
#     query_engine=engine,
#     namespace=namespace
# )
#
# agent = Agent(
#     rulesets=[
#         Ruleset(
#             name="Physics Tutor",
#             rules=[
#                 Rule(
#                     "Always introduce yourself as a physics tutor"
#                 ),
#                 Rule(
#                     "Be truthful. Only discuss physics."
#                 )
#             ]
#         )
#     ],
#     tools=[kb_client]
# )
#
# Chat(agent).start()



def send_message():
    message = entry.get()  # Get the input from the entry widget
    output.insert(tk.END, f"You: {message}\n")  # Display the message in the output

    # Here, you can process the message or send it to a chatbot or server for further handling

    entry.delete(0, tk.END)  # Clear the input field

# Create the main window
window = tk.Tk()
window.title("Chat Window")

# Create the output text widget
output = tk.Text(window, height=10, width=50)
output.pack()

# Create the input entry widget
entry = tk.Entry(window, width=50)
entry.pack()

# Create the send button
send_button = tk.Button(window, text="Send", command=send_message)
send_button.pack()

# Start the main event loop
window.mainloop()