import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [description, setDescription] = useState('');
  const [candidates, setCandidates] = useState([]);

  const handleDescriptionUpload = async (e) => {
    const file = e.target.files[0];
    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await axios.post('http://localhost:8000/api/upload-description/', formData);
      setDescription(response.data.description); // Set the extracted description in the textarea
      console.log('Job description uploaded successfully:', response.data);
    } catch (error) {
      console.error('Error uploading job description:', error);
    }
  };

  const handleScoreCandidates = async (e) => {
    e.preventDefault();

    try {
      const response = await axios.post('http://localhost:8000/api/score-candidates/', {
        description,
      });
      setCandidates(response.data.top_candidates);
    } catch (error) {
      console.error('Error scoring candidates:', error);
    }
  };

  return (
    <div>
      <h1>AI-Powered Candidate Screening System</h1>

      <div>
        <h3>Upload Job Description</h3>
        <input type="file" onChange={handleDescriptionUpload} />
        <p>Upload a job description (PDF), or paste it in the text box below.</p>
      </div>

      <form onSubmit={handleScoreCandidates}>
        <textarea value={description} onChange={(e) => setDescription(e.target.value)} maxLength={2000} placeholder="Enter or edit the job description here" />
        <button type="submit">Score Candidates</button>
      </form>

      <h2>Top Candidates</h2>
      <ul>
        {candidates.map((candidate, index) => (
          <li key={index}>
            {index + 1}. {candidate.name}: {candidate.score}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
