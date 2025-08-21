import React, { useState } from 'react';
import JourneyForm from './components/JourneyForm';
import ResultsTable from './components/ResultsTable';
import { calculateFares } from './services/api';

const App = () => {
  // State for journeys: array of objects with from_zone and to_zone strings
  const [journeys, setJourneys] = useState([
    { from_zone: '', to_zone: '' },
  ]);
  const [results, setResults] = useState(null);
  const [error, setError] = useState('');

  const handleAdd = () => {
    // Limit to 20 journeys per day
    if (journeys.length < 20) {
      setJourneys([...journeys, { from_zone: '', to_zone: '' }]);
    }
  };

  const handleRemove = (index) => {
    const newJourneys = journeys.filter((_, i) => i !== index);
    setJourneys(newJourneys.length ? newJourneys : [{ from_zone: '', to_zone: '' }]);
  };

  const handleChange = (index, field, value) => {
    const newJourneys = journeys.map((journey, i) => {
      if (i === index) {
        return { ...journey, [field]: value };
      }
      return journey;
    });
    setJourneys(newJourneys);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    // Validate and convert to integers
    try {
      const payload = journeys.map((j) => {
        const fromZone = parseInt(j.from_zone, 10);
        const toZone = parseInt(j.to_zone, 10);
        if (Number.isNaN(fromZone) || Number.isNaN(toZone)) {
          throw new Error('Please enter valid numeric zones for all journeys.');
        }
        return { from_zone: fromZone, to_zone: toZone };
      });
      const data = await calculateFares(payload);
      setResults(data);
      setError('');
    } catch (err) {
      // If the error comes from axios, use the response detail
      const message = err.response?.data?.detail || err.message;
      setError(message);
      setResults(null);
    }
  };

  return (
    <div className="container">
      <h1>PearlCard Fare Calculator</h1>
      <JourneyForm
        journeys={journeys}
        onAdd={handleAdd}
        onRemove={handleRemove}
        onChange={handleChange}
        onSubmit={handleSubmit}
      />
      {error && <p className="error" role="alert">{error}</p>}
      <ResultsTable results={results} />
    </div>
  );
};

export default App;