import logo from './img/logo.png';
import './header.css';

function Header() {
    return(

        <header>

            <nav className='nav-menu'>
                <div className='logo-menu'>
                    <img className='menu-logo' src={logo} alt="" />
                </div>
{/*                 <div className='btn-menu'>
                    <button className='btn-register'>Registro</button>
                    <button className='btn-login'> login </button>
                </div> */}
            </nav>

        </header>



    );
}

export default Header