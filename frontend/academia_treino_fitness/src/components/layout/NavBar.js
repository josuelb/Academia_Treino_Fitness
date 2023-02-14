import './css/NavBar.css'
import { Link } from 'react-router-dom'
import Container from './Container';

function NavBar(){
    return(
        <nav>
            <div class='container_nav'>
                <div class='container_title'>
                    <h1>Academia Treino Fitness</h1>
                </div>
                <menu>
                    <ul>
                        <Link to='/'><li>Home</li></Link>
                    </ul>
                </menu>
            </div>
        </nav>
    )
}

export default NavBar;