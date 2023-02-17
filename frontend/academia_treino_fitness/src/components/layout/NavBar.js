import './css/NavBar.css'
import { Link } from 'react-router-dom'
import Container from './Container';
import { useContext } from 'react';
import { Context } from '../../Context';

function NavBar(){

    const {login, user} = useContext(Context)

    const menu = ()=>{
        const menu = document.getElementsByClassName('menu')[0]
        if (menu.style.display === 'none'){
            menu.style.display = 'block'
        } else{
            menu.style.display = 'none'
        }
        
    }

    return(
        <nav>
            <div class='container_nav'>
                <div class='container_title'>
                    <h1>Academia Treino Fitness</h1>
                </div>
                <div class='container_span'>
                    <span onClick={menu} class="material-symbols-outlined">
                        menu
                    </span>
                </div>
                <menu class='menu'>
                    <ul>
                        {
                            login[0] ? <div><Link to='/'><li>Home</li></Link>
                            <Link to={`/${user[0]}`}><li>{user[0]}</li></Link>
                            <Link to='/alunos'><li>Alunos</li></Link></div> : <Link to='/'><li>Home</li></Link>
                        }
                    </ul>
                </menu>
            </div>
        </nav>
    )
}

export default NavBar;