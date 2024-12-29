import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [description, setDescription] = useState('');
  const [candidates, setCandidates] = useState([]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:8000/api/score-candidates/', { description });
      setCandidates(response.data.top_candidates);
    } catch (error) {
      console.error('Error scoring candidates:', error);
      alert('An error occurred while scoring candidates. Please try again.');
    }
  };

  return (
    <div>
      <h1>Candidate Scoring System</h1>
      <form onSubmit={handleSubmit}>
        <textarea value={description} onChange={(e) => setDescription(e.target.value)} maxLength={200} placeholder="Enter job description" aria-label="Job description" />
        <button type="submit">Score Candidates</button>
      </form>
      <h2>Top Candidates</h2>
      {candidates.length > 0 ? (
        <ul>
          {candidates.map((candidate, index) => (
            <li key={index}>
              {candidate.name}: {candidate.score}
            </li>
          ))}
        </ul>
      ) : (
        <p>No candidates found for the given job description.</p>
      )}
    </div>
  );
}

export default App;
