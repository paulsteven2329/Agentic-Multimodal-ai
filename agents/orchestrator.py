from agents.text_agent import handle as text_agent
from agents.image_agent import handle as image_agent
from agents.voice_agent import handle as voice_agent


async def route(prompt):

    prompt_lower = prompt.lower()

    if "draw" in prompt_lower or "image" in prompt_lower:
        return await image_agent(prompt)

    if "voice" in prompt_lower or "speak" in prompt_lower:
        return await voice_agent(prompt)

    return await text_agent(prompt)