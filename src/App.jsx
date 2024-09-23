import { useState } from 'react';
import './App.css';
import Board from "./components/Board.jsx";
import testData from "./ExampleData.js";
import Player from './components/player/Player.jsx';


function App() {

	const [userData, updateUserData] = useState(testData);

	let players = [];

	userData.players.forEach((player, index) =>{
		players.push(
			<div>
				<span>{JSON.stringify(player)}</span>
				<Player player={player} key="index" />
			</div>
		)
	})

	return (
		<div className="App">
			<h1>Manadas Web</h1>
			<Board />
			<p>{JSON.stringify(userData, null, 2)}</p>
			{players}
		</div>
	);
}

export default App;
