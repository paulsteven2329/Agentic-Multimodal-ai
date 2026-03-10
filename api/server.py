from fastapi import FastAPI
from orchestration.agent_graph import run_agent

app = FastAPI()

@app.post("/chat")
async def chat(data: dict):

    prompt = data["prompt"]

    result = await run_agent(prompt)

    return result


@app.post("/generate-image")
async def generate_image(data: dict):

    result = await run_agent("image " + data["prompt"])

    return result


@app.post("/generate-voice")
async def generate_voice(data: dict):

    result = await run_agent("voice " + data["text"])

    return result