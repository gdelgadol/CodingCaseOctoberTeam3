import {Link} from 'react-router-dom'

export function Navigation() {
    return (
        <div>
            <Link to="/products">
            <h1>Makers Tech</h1>
            </Link>
            <Link to="/products">View products</Link>
            <Link to="/chat">ChatBot</Link>
        </div>
    )
}