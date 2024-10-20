import { useEffect, useState } from "react";
import { getAllProducts } from "../api/products.api";

export function ProductPage(){

    const [products, setProducts] = useState([]);

    useEffect(() => {
        async function loadProducts() {
            const res = await getAllProducts();
            setProducts(res.data)
        }
        loadProducts();
    }, []);

    return <div>
        {products.map(product => (
            <div key={product.id}>
                <h1>{product.model}</h1> 
            </div>
        ))}
    </div>;
}