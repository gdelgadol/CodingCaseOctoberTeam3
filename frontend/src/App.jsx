import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { ProductPage } from './pages/ProductPage';
import { ChatBotPage } from './pages/ChatBotPage';
import { ProductCreationPage } from './pages/ProductCreation';
import { Navigation } from './components/Navigation';
import './App.css';
import { Header } from './components/Header';
import { Footer } from './components/Footer';

function App() {
    return (
        <div className="app-container">
            <Header />
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
            <Footer />
        </div>
    );
}

export default App;

