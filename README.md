# Agentic-Multimodal-ai

# Multi-Modal Agentic AI Platform

**Production-ready multi-modal AI system**  
Text · Images · Voice — powered by intelligent multi-agent orchestration

<p align="center">
  <strong>Modular • Scalable • Free-tier deployable • Extensible</strong><br>
  <em>Automatic intent detection • Agent routing • Tool calling • Multimodal output</em>
</p>

## What this project does

A production-grade, multi-modal AI platform that:

- understands natural language user requests  
- detects required modality (text / image / voice)  
- routes intelligently to specialized agents  
- executes tools following Model Context Protocol (MCP) style  
- returns clean, structured multimodal responses

## Core Capabilities

| Modality       | Agent               | Primary Models                        | Output Format       |
|----------------|---------------------|---------------------------------------|---------------------|
| Text           | Text Agent          | Llama 3 • Mixtral • Mistral • Phi-3   | Markdown / plain text |
| Image          | Image Agent         | Stable Diffusion XL • SD Turbo        | PNG / JPEG          |
| Voice          | Voice Agent         | Coqui TTS • Piper TTS • Bark          | WAV / MP3           |

## System Architecture

```mermaid
flowchart TD
    A[User Input<br>text / voice / chat] --> B[React Frontend]
    B --> C[FastAPI Gateway]
    C --> D[Orchestrator Agent<br>LangGraph + LLM]
    
    D --> E{Intent & Task Detection}
    
    E -->|Conversation / Reasoning / Explanation| F[Text Generation Agent]
    E -->|Create visual / artwork / scene|      G[Image Generation Agent]
    E -->|Speak / Read aloud / TTS|             H[Voice Generation Agent]
    
    F --> I[Text Tool → LLM inference]
    G --> J[Image Tool → Diffusion model]
    H --> K[Voice Tool → TTS engine]
    
    I --> L[Text Response]
    J --> M[Generated Image]
    K --> N[Generated Audio]
    
    L & M & N --> O[Structured API Response<br>streaming supported]
    O --> B


    Fallback ASCII view (if Mermaid not supported):

User Input
   │
   ▼
React Frontend
   │
   ▼
FastAPI Gateway
   │
   ▼
Orchestrator Agent
   │
   ▼
Intent Detection & Routing
   ├──────────────┬───────────────┬──────────────┐
   ▼              ▼               ▼              │
Text Agent    Image Agent     Voice Agent     (future agents)
   │              │               │
   ▼              ▼               ▼
Text Tool     Image Tool      Voice Tool
   │              │               │
   ▼              ▼               ▼
 LLM          Stable Diffusion    TTS
   │              │               │
   ▼              ▼               ▼
Final Text    Generated Image   Generated Audio
   └──────────────┴───────────────┴──────────────┘
                  API Response


Key Features

Multi-agent architecture with LangGraph orchestration
Automatic modality & intent detection
MCP-style tool schemas for autonomous calling
Semantic memory / RAG via ChromaDB or FAISS
Recursive chunking (500–800 tokens + 100 overlap)
Fully asynchronous execution pipeline
Production-ready extras: logging • retries • rate limiting • streaming
Free-tier friendly deployment (Render / Railway / HF Spaces / Vercel)

Technology Stack


















































LayerTechnologiesPurposeOrchestrationLangGraph, LangChainAgent workflows, state, toolsBackendFastAPI (Python)Async REST/WebSocket APIFrontendReactChat UI, image & audio playbackVector DatabaseChromaDB / FAISSLong-context memory & retrievalText ModelsLlama 3, Mixtral, Mistral, Phi-3, …Reasoning & generationImage ModelsSDXL, SD TurboFast & high-quality image synthesisTTS / VoiceCoqui TTS, Piper TTS, BarkNatural-sounding speechDeployment TargetsRender, Railway, Hugging Face Spaces, VercelFree & low-cost hosting
Quick Start
Bash# 1. Install Python dependencies
pip install -r requirements.txt

# 2. Set API key (Groq, Ollama, or local inference)
export GROQ_API_KEY=your_groq_key_here
# or run Ollama: ollama run llama3

# 3. Start backend
uvicorn api.server:app --host 0.0.0.0 --port 8000 --reload

# 4. Start frontend (from frontend/react-app/)
npm install
npm run dev
Main API Endpoints





























MethodEndpointPurposeExample Request BodyPOST/chatText conversation & reasoning{"prompt": "Explain how transformers work"}POST/generate-imageText-to-image generation{"prompt": "cyberpunk city skyline at night"}POST/generate-voiceText-to-speech synthesis{"text": "Welcome to the next generation AI"}
Responses follow a consistent format:
JSON{
  "type": "text|image|audio",
  "content": "...",
  "path": "optional/file/path"
}
Project Structure
textproject/
├── agents/                 # Agent classes & logic
│   ├── orchestrator.py
│   ├── text_agent.py
│   ├── image_agent.py
│   └── voice_agent.py
├── tools/                  # Tool implementations (MCP style)
│   ├── text_tool.py
│   ├── image_tool.py
│   └── voice_tool.py
├── memory/                 # Vector store + chunking logic
│   ├── vector_store.py
│   └── chunking.py
├── orchestration/          # LangGraph workflow definition
│   └── agent_graph.py
├── api/                    # FastAPI application
│   └── server.py
├── frontend/               # React single-page app
│   └── react-app/
├── utils/                  # Helpers (logging, retries, etc.)
│   ├── logging.py
│   └── retry.py
├── requirements.txt
└── README.md
Free-Tier Deployment
Backend

Render.com / Railway.app / Hugging Face Spaces
Start command: uvicorn api.server:app --host 0.0.0.0 --port $PORT

Frontend

Vercel / Netlify
Standard npm run build → deploy

Production Optimizations Included

End-to-end async execution
Structured logging
Automatic retries + backoff
Rate limiting middleware
Streaming LLM responses
Quantized / GGUF model support
GPU acceleration friendly

Future / Planned Extensions

Video generation agent
Advanced document Q&A + RAG
Web search / browser tool integration
Code interpreter & execution sandbox
Vision + multimodal reasoning
Autonomous research & planning agents

Philosophy
Modern AI applications need to be:

modular → swap models / tools easily
multi-modal → handle text + vision + audio
agentic → use tools & multi-step reasoning
production-ready → async, observable, scalable

This project demonstrates one clean, maintainable, and realistically deployable way to achieve that — even on free infrastructure.
>>>>>>> a14d74e (initial commit)
