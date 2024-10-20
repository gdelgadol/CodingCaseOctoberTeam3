import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { ProductPage } from './pages/ProductPage';
import { ChatBotPage } from './pages/ChatBotPage';
import { ProductCreationPage } from './pages/ProductCreation';
import { Navigation } from './components/Navigation';
import './App.css'; // Import the CSS styles

function App() {
    return (
        <div className="app-container">
            <header className="page-title">
                    <h1>Makers Tech</h1>
            </header>
            <BrowserRouter>
                <Navigation />
                <div className="content-container">
                    <Routes>
                        <Route path="/products" element={<ProductPage />} />
                        <Route path="/chat" element={<ChatBotPage />} />
                        <Route path="/create-product" element={<ProductCreationPage />} />
                        <Route path="/" element={<Navigate to="/products" />} />
                    </Routes>
                </div>
            </BrowserRouter>
        </div>
    );
}

export default App;

