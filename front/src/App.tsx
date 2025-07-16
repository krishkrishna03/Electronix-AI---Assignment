import React, { useState } from 'react';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Container, Form, Button, Spinner, Card } from 'react-bootstrap';

interface Prediction {
  label: string;
  score: number;
}

function Sentiment() {
  const [input, setInput] = useState<string>('');
  const [prediction, setPrediction] = useState<Prediction | null>(null);
  const [loading, setLoading] = useState<boolean>(false);

  const handlePredict = async () => {
    if (input.trim() !== "") {
      setLoading(true);
      try {
        const response = await fetch('https://sriKrishnasaipatnala-sentiment-fastapi.hf.space/predict', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ text: input })
        });
        const data = await response.json();
        setPrediction({ label: data.label, score: data.score });
      } catch (error) {
        console.error("Error:", error);
      } finally {
        setLoading(false);
      }
    }
  };

  return (
    <div className="app-bg">
      <Container className="py-5">
        <Card className="shadow-lg rounded-4 p-4 mx-auto" style={{ maxWidth: '600px' }}>
          <Card.Body>
            <h1 className="text-center mb-4 gradient-text">Sentiment Analysis</h1>
            <Form.Group controlId="textInput">
              <Form.Control
                as="textarea"
                rows={4}
                placeholder="Enter your text here..."
                value={input}
                onChange={(e) => setInput(e.target.value)}
                className="mb-3"
              />
            </Form.Group>

            <div className="d-grid">
              <Button variant="primary" onClick={handlePredict} disabled={loading} className="btn-gradient">
                {loading ? <Spinner as="span" animation="border" size="sm" /> : "Predict Sentiment"}
              </Button>
            </div>

            {prediction && (
              <Card className="mt-4 shadow-sm result-card">
                <Card.Body>
                  <h5 className="mb-2">Prediction Result</h5>
                  <p><strong>Label:</strong> {prediction.label}</p>
                  <p><strong>Score:</strong> {prediction.score.toFixed(2)}</p>
                </Card.Body>
              </Card>
            )}
          </Card.Body>
        </Card>
      </Container>
    </div>
  );
}

export default Sentiment;
