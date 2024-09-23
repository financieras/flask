import React from "react";
import './Player.css';


const Player = ({player}) => {
    return (
        <div className="playerContainer">
            <h2>{player.name}</h2>
            <div>
                <h3>Score: <span>{player.score}</span></h3>
                <p>Algorithm: <span>{player.algorithm_name}</span></p>
            </div>
        </div>
    )
}

export default Player;
