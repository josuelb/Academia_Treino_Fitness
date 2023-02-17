import './css/Login.css'
import img from '../../musculacao-holdfit.webp'


function Login(){
    const Enviar = ()=>{

        fetch('http://127.0.0.1:8000/')

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
                    <div class='erro'>

                    </div>
                    <button onClick={Enviar}>Enviar</button>
                </div>
            </div>
        </div>
    )
}

export default Login;