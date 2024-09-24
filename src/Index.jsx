import React, { useState } from "react";
import { useNavigate } from "react-router-dom";


const Index = () => {

	const [formValues, updateFormValues] = useState({
		"width": 3,
		"height": 3,
		"nPlayers": 2,
		"foodAmount": "max"
	})

	const handleChange = (event) => {
		updateFormValues(prevData => {
			return {
				...prevData,
				[event.target.name]: event.target.value
			}
		})
	}

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
		<div>
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
				<div>
					<span>* Table of algorithms *</span>
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

export default Index;
