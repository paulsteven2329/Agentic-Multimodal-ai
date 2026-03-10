from tools.voice_tool import run

async def handle(text):

    path = await run(text)

    return {
        "type": "audio",
        "content": path
    }