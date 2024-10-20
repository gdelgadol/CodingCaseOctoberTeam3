import { Link } from 'react-router-dom';
import './Navigation.css'; // Separate CSS file for the navigation

export function Navigation() {
    return (
        <nav className="nav-bar">
            <ul className="nav-links">
                <li><Link to="/products">Products</Link></li>
                <li><Link to="/chat">Chat</Link></li>
            </ul>
        </nav>
    );
}

