import './App.css';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

import NavBar from './components/layout/NavBar';
import Container from './components/layout/Container';
import Home from './components/layout/Home'

function App() {
  return (
    <Router>
      <NavBar />
      <Container>
        <Routes>
          <Route path='/' element={<Home />}/>
        </Routes>
      </Container>
    </Router>
  );
}

export default App;
