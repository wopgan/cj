import './footer.css'
import Facebook from './img/Facebook.png'
import Instagram from './img/Instagram.png'


function Footer() {
    return(

        <footer>

            <div className="footer-container">

{/*                 <div className="footer-section">

                    <h2> Quem Somos </h2>
                    <p> Lorem ipsum dolor, sit amet  <br /> consectetur adipisicing elit. </p>

                </div>

                <div className="footer-section">

                    <h2> Acesso Rápido </h2>
                    <p> Lorem ipsum dolor, sit amet consectetur  <br /> adipisicing  elit. </p>

                </div> */}


                <div className="footer-section">

                    <h2> Redes Sociais </h2>
                    <div className="redes">

                        <a href="https://instagram.com/citacoesjuridicas.com.br?igshid=ZDdkNTZiNTM="> <img src={Instagram} alt="Instagram" /> </a>
                        <a href="https://www.facebook.com/profile.php?id=100086047664955&mibextid=ZbWKwL"> <img src={Facebook} alt="" /> </a>
                        
                        

                    </div>

                </div>

            </div>


        </footer>


    );
}

export default Footer;