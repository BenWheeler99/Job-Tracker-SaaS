import logo from './logo.svg';
import './App.css';
import { useState } from 'react';

const Card = ({ title, description }) => {
  const [hasLiked, setHasLiked] = useState(false);
  return (
    <div className="card">
      <h2>{title}</h2>
      <p>{description}</p>
      <button onClick={() => setHasLiked(true)}>
        {hasLiked ? 'Liked' : 'Like'}
      </button>
    </div>
  );
};

function App() {
  return (
    <div className="App">
      <header className="App-header">
      <Card title="Card Title 1" description="This is the description for card 1." />
      <Card title="Card Title 2" description="This is the description for card 2." />
      <Card title="Card Title 3" description="This is the description for card 3." />
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
      
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React or Don't
        </a>
      
      </header>
      
    </div>
  );
}

export default App;
