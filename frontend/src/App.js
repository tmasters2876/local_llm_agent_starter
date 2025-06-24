import React, { useState } from "react";

function App() {
  const [prompt, setPrompt] = useState("");
  const [temperature, setTemperature] = useState(0.7);
  const [numPredict, setNumPredict] = useState(100);
  const [model, setModel] = useState("mistral"); // Dynamic model selector
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
        model,
      }),
    });

    const data = await response.json();
    setResult(data.result);
    setLoading(false);
  };

  return (
    <div style={{ padding: "2rem", maxWidth: "600px", margin: "auto" }}>
      <h1>🔮 Masters LLM Agent UI</h1>
      <form onSubmit={handleSubmit}>
        <label>Model:</label>
        <select
          value={model}
          onChange={(e) => setModel(e.target.value)}
          style={{ width: "100%", marginBottom: "1rem" }}
        >
          <option value="mistral">Mistral</option>
          <option value="llama3">Llama 3</option>
          <option value="deepseek-coder">DeepSeek Coder</option>
          <option value="llama4">Llama 4</option>
          {/* Add more options as needed */}
        </select>

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
          <div
            style={{
              maxWidth: "100%",
              maxHeight: "800px",
              overflowY: "auto",
              overflowX: "auto",
              marginTop: "1rem",
              background: "#f5f5f5",
              padding: "1rem",
              borderRadius: "8px",
            }}
          >
            <pre
              style={{
                whiteSpace: "pre-wrap",
                wordWrap: "break-word",
                margin: 0,
              }}
            >
              {result}
            </pre>
          </div>
        </>
      )}
    </div>
  );
}

export default App;
