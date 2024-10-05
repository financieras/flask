import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import algorithmData from "./data/algorithmsExample.js";
import "./Landing.css";


const Landing = () => {

	const algorithms = algorithmData.algorithms;


	const [formValues, updateFormValues] = useState({
		"width": 3,
		"height": 3,
		"nPlayers": 2,
		"foodAmount": "max",
		"players": [
			{ "name": "User A", "algorithm": "" },
			{ "name": "User B", "algorithm": "" }
		]
	})

	const handleChange = (event) => {
		const { name, value } = event.target;

		updateFormValues((prevData) => {
			let newPlayerValues = [...prevData.players];

			if (name === "nPlayers") {
				const newCount = parseInt(value, 10);
				const currentCount = newPlayerValues.length;

				if (newCount > currentCount) {
					for (let i = currentCount; i < newCount; i++) {
						newPlayerValues.push({
							name: "User " + String.fromCharCode(65 + i),
							algorithm: "",
						});
					}
				} else if (newCount < currentCount) {
					newPlayerValues = newPlayerValues.slice(0, newCount);
				}
			}

			return {
				...prevData,
				[name]: value,
				players: newPlayerValues, // Update the players array
			};
		});
	};


	const handleAlgorithmChange = (playerName, algorithm) => {
		updateFormValues((prevValues) => ({
			...prevValues,
			players: prevValues.players.map((player) =>
				player.name === playerName ? { ...player, algorithm: algorithm } : player
			),
		}));
	};

	const navigate = useNavigate();

	/* const handleSubmit = async (event) => { */
	const handleSubmit = (event) => {
		event.preventDefault();
		/* try {
			const response = await fetch("/api/simulation", {
				method: "POST",
				headers: {
					"Content-Type": "application/json",
				},
				body: JSON.stringify(formValues),
			});

			if (response.ok) {
				navigate("/simulation");
			} else {
				console.error("Failed to submit the form");
			}
		} catch (error) {
			console.error("Error submitting the form:", error);
		} */
		navigate("/simulation");
	}

	return (
		<div id="mainContainer">
			<h1>Herds simulation</h1>
			<form onSubmit={handleSubmit}>
				<div>
					<label htmlFor="width">Width of the board</label>
					<input onChange={handleChange} name="width" type="number" min={2} max={500} value={formValues.width} />
				</div>
				<div>
					<label htmlFor="height">Height of the board</label>
					<input onChange={handleChange} name="height" type="number" min={2} max={500} value={formValues.height} />
				</div>
				<div>
					<label htmlFor="nPlayers">Number of players</label>
					<input onChange={handleChange} name="nPlayers" type="number" min={2} max={26} value={formValues.nPlayers} />
				</div>
				<div id="algorithmsTable">
					<label>User Algorithms</label>
					<table className="algorithm-table">
						<thead>
							<tr>
								<th />
								{algorithms.map((algorithm, index) => (
									<th key={index}>{algorithm}</th>
								))}
							</tr>
						</thead>
						<tbody>
							{formValues.players.map((player) => (
								<tr key={player.name}>
									<td>{player.name}</td>
									{algorithms.map((algorithm, index) => (
										<td key={index}>
											<input
												type="radio"
												name={`player-${player.name}-algorithm`}
												value={algorithm}
												checked={player.algorithm === algorithm}
												onChange={() => handleAlgorithmChange(player.name, algorithm)}
											/>
										</td>
									))}
								</tr>
							))}
						</tbody>
					</table>
				</div>
				<div>
					<label htmlFor="">Amount of food</label>
					<select
						name="foodAmount"
						id="foodAmount"
						value={formValues.foodAmount}
						onChange={handleChange}
					>
						<option value="max">Max</option>
						<option value="mid">Mid</option>
						<option value="min">Min</option>
					</select>
				</div>
				<button>Start simulation</button>
			</form>
		</div>
	)
}

export default Landing;
