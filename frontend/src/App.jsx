import {BrowserRouter, Routes, Route, Navigate} from 'react-router-dom'
import { ProductPage } from "./pages/ProductPage"
import { ChatBotPage } from "./pages/ChatBotPage"
import { ProductCreationPage } from './pages/ProductCreation'
import { Navigation } from './components/Navigation'

function App(){
  return (
    <BrowserRouter>
    <Navigation />
    <Routes>
      <Route path="/products" element={<ProductPage/>}></Route>
      <Route path="/product-creation" element={<ProductCreationPage/>}></Route>
      <Route path="/chat" element={<ChatBotPage/>}></Route>
      <Route path="/" element={<Navigate to="/products"/>}></Route>
    </Routes>
    </BrowserRouter>
  )
}

export default App