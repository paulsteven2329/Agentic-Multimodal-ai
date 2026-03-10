from tools.image_tool import run

async def handle(prompt):

    path = await run(prompt)

    return {
        "type": "image",
        "content": path
    }