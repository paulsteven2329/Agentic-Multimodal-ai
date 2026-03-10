from tools.text_tool import run as text_tool

async def handle(prompt):

    response = await text_tool(prompt)

    return {
        "type": "text",
        "content": response
    }