import React from "react";
import colours from "../../data/colours.js";
import './Player.css';


const Player = ({ player, index }) => {
    return (
        <div className="playerContainer" style={{ backgroundColor: index <= colours.length ? colours[index].secondary : "blue"}}>
            <h2 style={{ color: index <= colours.length ? colours[index].primary : "green"}}>{player.name}</h2>
            <div>
                <h3>Score: <span>{player.score}</span></h3>
                <p>Algorithm: <span>{player.algorithm_name}</span></p>
            </div>
        </div>
    )
}

export default Player;
