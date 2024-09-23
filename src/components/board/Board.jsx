import React, { useEffect, useRef } from "react";
import colours from "../../data/colours.js";
import './Board.css'


const Board = ({ board }) => {

	const canvasRef = useRef(null);

	const draw = (ctx, width, height) => {
		const rows = board.length;
		const cols = board[0].length;

		const cellWidth = width / cols;
		const cellHeight = height / rows;


		// Clear the canvas
		ctx.clearRect(0, 0, width, height);

		// Draw each cell and its content
		board.forEach((row, rowIndex) => {
			row.forEach((cell, colIndex) => {
				const x = colIndex * cellWidth;
				const y = rowIndex * cellHeight;

				// Draw the cell (a rectangle)
				ctx.strokeStyle = 'white';
				ctx.lineWidth = 1;
				ctx.strokeRect(x, y, cellWidth, cellHeight);

				// Draw the value inside the cell
				if (isNaN(cell))
					ctx.fillStyle = colours[cell.charCodeAt(0) - 65].primary;
				else if (!cell)
					ctx.fillStyle = 'lightgray';
				else
					ctx.fillStyle = 'white';
				ctx.font = `${cellHeight / 2}px Arial`;
				ctx.textAlign = 'center';
				ctx.textBaseline = 'middle';
				ctx.fillText(cell, x + cellWidth / 2, y + cellHeight / 2);
			});
		});
	};

	useEffect(() => {
		const canvas = canvasRef.current;
		const ctx = canvas.getContext('2d');
		const width = canvas.width;
		const height = canvas.height;

		draw(ctx, width, height);
	}, []);

	return (
		<div className="boardContainer">
			<canvas ref={canvasRef} className="boardCanvas" height={board.length * 100} width={board[0].length * 100} />
		</div>
	)
}

export default Board;
