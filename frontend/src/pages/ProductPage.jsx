import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './ProductPage.css';

export function ProductPage() {
    const [products, setProducts] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const fetchProducts = async () => {
            try {
                const response = await axios.get('http://localhost:8000/api/product/');
                console.log(response.data)
                setProducts(response.data);
            } catch (error) {
                console.error('Error fetching products:', error);
            } finally {
                setLoading(false);
            }
        };

        fetchProducts();
    }, []);

    if (loading) {
        return <div>Loading...</div>;
    }

    return (
        <div className="product-page">
            <h2>Available Products</h2>
            <div className="product-list">
                {products.map(product => (
                    <div key={product.id} className="product-card">
                        <h3>{product.model_brand.brand_name} {product.model}</h3>
                        <ul>
                            {product.model_features.map(feature => (
                                <li key={feature.id}>{feature.feature}</li>
                            ))}
                        </ul>
                    </div>
                ))}
            </div>
        </div>
    );
}

