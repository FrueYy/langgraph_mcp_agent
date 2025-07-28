from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.prompts.base import Message, TextContent
from mcp.server.fastmcp.prompts import base

mcp = FastMCP(name="PromptServer")

# Basic prompt returning a string (converted to user message automatically)
@mcp.prompt("Explain Topic")
def ask_about_topic(topic: str) -> str:
    """Generates a user message asking for an explanation of a topic."""
    return f"Can you please explain the concept of '{topic}'?"

# Prompt returning a specific message type
@mcp.prompt("Generate Code Request")
def generate_code_request(language: str, task_description: str) -> Message:
    """Generates a user message requesting code generation."""
    content = f"Write a {language} function that performs the following task: {task_description}"
    return Message(role="user", content=TextContent(type="text", text=content))

@mcp.prompt("Code Review")
def review_code(code: str) -> str:
    return f"Please review this code:\n\n{code}"


@mcp.prompt("Debug Assistant")
def debug_error(error: str) -> list[base.Message]:
    return [
        base.UserMessage("I'm seeing this error:"),
        base.UserMessage(error),
        base.AssistantMessage("I'll help debug that. What have you tried so far?"),
    ]

if __name__ == "__main__":

    mcp.run(transport="stdio")