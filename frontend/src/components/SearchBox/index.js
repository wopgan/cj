import React, { useState } from "react";


import "./search.css"
import Cards from "../Cards";
import axios from "axios";

function SearchBox() {

    const [query, setQuery] = useState("");
    const [resposta, setResposta] = useState("");
    const [showModal, setShowModal] = useState(false);

    const handleSubmit = async (e) => {
        e.preventDefault();

        try {

            const response = await axios.post("http://localhost:8000/busca/", {
                busca_citacao: query
            },{
                auth: {
                    username: 'admin',
                    password: 'admin'
                }
            });

            setResposta(response.data.citacao);
            setShowModal(true);
            setQuery("");


        } catch (error) {
            console.error(error);
        }
    }
   

    return(

        <div className="bg-main">

            <form  onSubmit={handleSubmit} >

                <div className="searchBox">

                    <div className="findUperBox">

                        <input className="findBox" placeholder="Buscar citação" type="text" value={query} onChange={(e) => setQuery(e.target.value)}  />

                        <button type="submit" className="btn-find">

                            <i className="fa-sharp fa-solid fa-magnifying-glass"></i>

                        </button>

                    </div>

                </div>

            </form>

            {showModal && (
                <div className="modal">
                    <div className="modal-content">
                        <span className="close" onClick={() => setShowModal(false)}>
                        &times;
                        </span>
                        <p>{resposta}</p>
                    </div>
                </div>
            )}

            <Cards />

        </div>
    )
}

export default SearchBox;