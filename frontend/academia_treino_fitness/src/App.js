import './App.css';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import { useContext, useEffect } from 'react';
import { Context } from './Context';

import NavBar from './components/layout/NavBar';
import Container from './components/layout/Container';
import Home from './components/layout/Home';
import Footer from './components/layout/Footer';
import Login from './components/layout/Login';


function App() {
  const {login} = useContext(Context)
  

  return (
    <Router>
      <NavBar />
      <Container>
        <Routes>
          <Route path='/' element={login[0] ? <Home /> : <Login />}/>
          <Route path='/login' element={login[0] ? <Home/> : <Login />}/>
        </Routes>
      </Container>
      <Footer/>
    </Router>
  );
}

export default App;
