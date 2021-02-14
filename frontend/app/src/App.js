import React from 'react';
import Config from './config';
import './App.css';

import { Container, Jumbotron, Button } from 'reactstrap';

function App() {
  return (
    <div className="App">
      <Container>
        <Jumbotron>
          <h1 className="display-3">{Config.name}</h1>
        </Jumbotron>
      </Container>
    </div>
  );
}

export default App;
