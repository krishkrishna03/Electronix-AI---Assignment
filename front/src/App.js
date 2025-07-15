import React, { useState } from 'react';
import './App.css';

function App() {
  const [text, setText] = useState('');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handlePredict = async () => {
    setLoading(true);
    const response = await fetch('http://localhost:8000/predict', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({text})
    });
    const data = await response.json();
    setResult(data);
    setLoading(false);
  };

  return (
    <div className="container">
      <h1>Sentiment Analysis</h1>
      <textarea
        value={text}
        onChange={e => setText(e.target.value)}
        placeholder="Enter text here..."
      />
      <button onClick={handlePredict} disabled={loading}>
        {loading ? 'Predicting...' : 'Predict'}
      </button>

      {result && (
        <div className="result">
          <h3>Prediction Result:</h3>
          <p><strong>Label:</strong> {result.label}</p>
          <p><strong>Score:</strong> {result.score.toFixed(2)}</p>
        </div>
      )}
    </div>
  );
}

export default App;
