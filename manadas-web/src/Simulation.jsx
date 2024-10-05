import { useState } from 'react';

import Board from "./components/board/Board.jsx";
import testData from "./data/ExampleData.js";
import Player from './components/player/Player.jsx';
import './Simulation.css';

const Simulation = () => {
	const [userData, updateUserData] = useState(testData);

	let players = [];

	userData.players.forEach((player, index) => {
		players.push(
			<div>
				<Player player={player} index={index} key="index" />
			</div>
		)
	})
	return (
		<div id='simulationContainer'>
			<h1>Simulación manadas</h1>
			<section>
				<Board board={userData.board} />
				<div className="playersContainer">
					{players}
				</div>
			</section>
		</div>
	)
}

export default Simulation;
