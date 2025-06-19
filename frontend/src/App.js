import React, { useState } from "react";

function App() {
  const [prompt, setPrompt] = useState("");
  const [temperature, setTemperature] = useState(0.7);
  const [numPredict, setNumPredict] = useState(100);
  const [result, setResult] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setResult("");

    const response = await fetch("http://127.0.0.1:8000/api/ask", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        prompt,
        temperature,
        num_predict: numPredict,
      }),
    });

    const data = await response.json();
    setResult(data.result);
    setLoading(false);
  };

  return (
    <div style={{ padding: "2rem", maxWidth: "600px", margin: "auto" }}>
      <h1>🔮 Local LLM Agent UI</h1>
      <form onSubmit={handleSubmit}>
        <label>Prompt:</label>
        <textarea
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
          rows="4"
          style={{ width: "100%" }}
          placeholder="Ask me anything..."
        />

        <label>Temperature: {temperature}</label>
        <input
          type="range"
          min="0"
          max="2"
          step="0.1"
          value={temperature}
          onChange={(e) => setTemperature(parseFloat(e.target.value))}
          style={{ width: "100%" }}
        />

        <label>Max Tokens (num_predict): {numPredict}</label>
        <input
          type="range"
          min="10"
          max="300"
          step="10"
          value={numPredict}
          onChange={(e) => setNumPredict(parseInt(e.target.value))}
          style={{ width: "100%" }}
        />

        <button
          type="submit"
          disabled={loading || !prompt}
          style={{ marginTop: "1rem" }}
        >
          {loading ? "Generating..." : "Ask Agent"}
        </button>
      </form>

      {result && (
        <>
          <h3>💡 Response:</h3>
          <pre style={{ background: "#f5f5f5", padding: "1rem" }}>
            {result}
          </pre>
        </>
      )}
    </div>
  );
}

export default App;

