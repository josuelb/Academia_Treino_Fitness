import './css/Login.css'
import img from '../../musculacao-holdfit.webp'
import { FetchAuthentication } from '../../bd/Fetch'
import { useContext, useEffect } from 'react'
import { Context } from '../../Context'
import { Navigate } from 'react-router-dom'


function Login(){
    const { login } = useContext(Context)

    const Enviar = ()=>{
        let dado = {
            username: document.getElementById('user').value,
            password: document.getElementById('password').value
        }

        FetchAuthentication(dado)

        if (FetchAuthentication(dado) === 'Usuário ou senha incorreta'){
            let alert = document.getElementById('alert')
            alert.innerHTML += `<p>${FetchAuthentication(dado)}</p>`
        }
    }

    return(
        <div class='box_login'>
            <div class='container_login_form'>
                <div class='image_academia'>
                    <img src={img} alt='academia' width='203px' height='100%'></img>
                </div>
                <div class='form'>
                    <h3>Login</h3>
                    <p>
                        <label for='user'>Usuário:</label>
                    </p>
                    <input type='text' id='user' name='user' class='input' required></input>
                    <p>
                        <label for='password'>Password:</label>
                    </p>
                    <input type='password' id='password' name='password' class="input" required></input><br></br>
                    <div class='alert'>

                    </div>
                    <button onClick={Enviar}>Enviar</button>
                </div>
            </div>
        </div>
    )
}

export default Login;