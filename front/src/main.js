import React, { useState } from 'react';
import './App.css';
import { ApolloClient, InMemoryCache, ApolloProvider, gql, useLazyQuery } from '@apollo/client';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Container, Form, Button, Spinner, Card } from 'react-bootstrap';

// Apollo Client setup
const client = new ApolloClient({
  uri: 'http://localhost:8000/graphql',
  cache: new InMemoryCache(),
});

// GraphQL query
const PREDICT_QUERY = gql`
  query Predict($text: String!) {
    predict(text: $text) {
      label
      score
    }
  }
`;

function Sentiment() {
  const [input, setInput] = useState('');
  const [getPrediction, { loading, data }] = useLazyQuery(PREDICT_QUERY);

  const handlePredict = () => {
    if (input.trim() !== "") {
      getPrediction({ variables: { text: input } });
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

            {data && (
              <Card className="mt-4 shadow-sm result-card">
                <Card.Body>
                  <h5 className="mb-2">Prediction Result</h5>
                  <p><strong>Label:</strong> {data.predict.label}</p>
                  <p><strong>Score:</strong> {data.predict.score.toFixed(2)}</p>
                </Card.Body>
              </Card>
            )}
          </Card.Body>
        </Card>
      </Container>
    </div>
  );
}

function App() {
  return (
    <ApolloProvider client={client}>
      <Sentiment />
    </ApolloProvider>
  );
}

export default App;
