import { useState } from 'react';
import './App.css';
import Board from "./components/board/Board.jsx";
import testData from "./data/ExampleData.js";
import Player from './components/player/Player.jsx';


function App() {

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
		<div className="App">
			<h1>Manadas Web</h1>
			<section>
				<Board board={userData.board} />
				<div className="playersContainer">
					{players}
				</div>
			</section>
		</div>
	);
}

export default App;
