import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import { Link } from 'react-router-dom';
import Simulation from "./Simulation";
import Index from "./Index.jsx";


function App() {
	return (
		<Router>
			<Routes>
				<Route path="/" element={<Index />} />
				<Route path="/simulation" element={<Simulation />} />
				{/* 404 page */}
				<Route path='*' element={
					<center>
						<h1>404 | Page not found :(</h1>
						<p>Sorry, the page you are looking for could not be found.</p>
						<Link to="/">
							<a>Go back to home</a>
						</Link>
					</center>
				} />
			</Routes>
		</Router>
	);
}

export default App;
