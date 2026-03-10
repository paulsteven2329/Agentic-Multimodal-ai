from groq import Groq
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

tool_schema = {
"name": "generate_text",
"description": "Generate text response",
"parameters": {
"type": "object",
"properties": {
"prompt": {"type":"string"}
}
}
}

async def run(prompt):

    response = client.chat.completions.create(
        model="mixtral-8x7b-32768",
        messages=[{"role":"user","content":prompt}]
    )

    return response.choices[0].message.content