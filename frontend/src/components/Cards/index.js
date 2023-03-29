import './cards.css';
import Book from './img/Livro.png'
import Clock from './img/Relogio.png'
import Trecho from './img/Trechos.png'


function Cards() {
    return(

        <div className='cards'>

            <div className="cards-container">

                <div className="card-info">

                    <img src={Book} className="livro" alt="" />

                    <p> Tenha acesso a um acervo <br /> de citações que conta com <br /> mais de 180 Livros </p>

                </div>

                <div className="card-info">

                    <img src={Clock} className="tempo" alt="" />

                    <p> Poupe tempo na sua busca </p>

                </div>

                <div className="card-info">

                    <img src={Trecho} className="trecho" alt="" />

                    <p> Cite os trechos mais relevantes <br /> na sua argumentação juridica </p>

                </div>

            </div>

        </div>

    );
}

export default Cards;