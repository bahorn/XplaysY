import React from 'react';
import Config from './config';
import './App.css';

import {
  Container,
  Jumbotron,
  Button,
  Input,
  Form,
  FormGroup,
  Label
} from 'reactstrap';

function App() {
  return (
    <div className="App">
      <Container>
        <Jumbotron>
          <h1 className="display-3">{Config.name}</h1>
        </Jumbotron>
        <Form>
          <FormGroup>
            <Input type="text" name="teamCode" id="teamCode"
              placeholder="Team Code..."/>
          </FormGroup>
        </Form>
      </Container>
    </div>
  );
}

export default App;
