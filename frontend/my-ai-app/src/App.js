import React, { useState } from "react";
import "./App.css";

function App() {
  const [prompt, setPrompt] = useState("");
  const [response, setResponse] = useState("");
  const [loading, setLoading] = useState(false);

  async function send() {
    if (!prompt.trim()) return;
    setLoading(true);
    setResponse(""); // Clear previous for better UX
    try {
      const res = await fetch("http://localhost:8000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ prompt }),
      });
      const data = await res.json();
      setResponse(data.content);
    } catch (err) {
      setResponse("SYSTEM ERROR: Failed to connect to KnightX Intelligence.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="knightx-app">
      <nav className="status-bar">
        <span className="status-dot"></span> 
        SYSTEM: ONLINE | ENCRYPTION: ACTIVE
      </nav>

      <main className="main-content">
        <header className="brand-section">
          <div className="logo-shield">♞</div>
          <h1>KNIGHT<span>X</span></h1>
          <p className="subtitle">STRATEGIC MULTI-MODAL INTELLIGENCE</p>
        </header>

        <section className="interaction-area">
          <div className="input-wrapper">
            <textarea
              rows="1"
              placeholder="Enter strategic command..."
              value={prompt}
              onChange={(e) => setPrompt(e.target.value)}
              onKeyDown={(e) => {
                if (e.key === "Enter" && !e.shiftKey) {
                  e.preventDefault();
                  send();
                }
              }}
            />
            <button 
              className={loading ? "btn-loading" : ""} 
              onClick={send} 
              disabled={loading || !prompt}
            >
              {loading ? <div className="spinner"></div> : "EXECUTE"}
            </button>
          </div>

          <div className={`response-container ${response ? "visible" : ""}`}>
            {loading && <div className="skeleton-loader">Processing KnightX Logic...</div>}
            {response && (
              <div className="response-box">
                <div className="box-header">INTELLIGENCE_REPORT.LOG</div>
                <div className="box-content">{response}</div>
              </div>
            )}
          </div>
        </section>
      </main>

      <footer className="knightx-footer">
        © 2024 KNIGHTX UNIVERSAL • DARK. INTELLIGENT. PRECISE.
      </footer>
    </div>
  );
}

export default App;
