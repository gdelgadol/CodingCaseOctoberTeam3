# Coding Case (Chatbot)

This is the result of a 24-hour challenge, the Coding Case:

Your task is to assist a technology e-commerce company named 'Makers Tech' in creating a ChatBot that responds to and informs users through a graphical interface about the inventory, features, and prices of the products currently available. This is based on the question asked, for example:

- Client: How many computers are currently available?
- ChatBot: At the moment, we have 4 computers; we have 2 HP, 1 Dell, and the other one is Apple. Which one would you like to purchase?
- Client: Tell me more about the Dell computer?

# Installation

## 1. Clone the repository:

```bash
git clone https://github.com/gdelgadol/CodingCaseOctoberTeam3.git
cd CodingCaseOctoberTeam3
```

## 2. **Create a virtual environment (optional)**

### Start it with Python:

```bash
python -m venv venv
```

### Execute or start using it:

- Linux/Mac

```bash
source venv/bin/activate
```

- Windows

```bash
venv\Scripts\activate
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 4. Install the LLM model (Llama 3.2 META)

Go to https://ollama.com/ and download the version of Ollama that suits your system. Once installed, use the console to run `ollama run llama3.2`. The model (2.0 GB) will be downloaded automatically.

## 5. PostgreSQL Scrip for DB

These are values for testing out the ChatBot

```
-- Insert brands into the Brand table
INSERT INTO public."MakersTechApp_brand" (brand_name) VALUES
('Dell'),
('HP'),
('Apple'),
('Lenovo'),
('Acer'),
('Asus'),
('Microsoft'),
('Razer'),
('Samsung'),
('Toshiba');

-- Insert specific features into the Feature table
INSERT INTO public."MakersTechApp_feature" (feature) VALUES
('Intel Core i5 9600K'),
('Intel Core i7 10750H'),
('AMD Ryzen 5 4600H'),
('16 GB RAM'),
('32 GB RAM'),
('1 TB SSD'),
('512 GB SSD'),
('$1000'),
('$1500'),
('$2000'),
('$2500'),
('NVIDIA GeForce GTX 1650'),
('NVIDIA GeForce RTX 3060'),
('Intel Iris Plus Graphics'),
('15.6" Full HD Display'),
('4 hours battery life'),
('8 hours battery life'),
('2.5 kg weight'),
('1.2 kg weight');

-- Insert products into the Product table
INSERT INTO public."MakersTechApp_product" (model, model_brand_id) VALUES
('XPS 13', (SELECT id FROM public."MakersTechApp_brand" WHERE brand_name = 'Dell')),
('Pavilion 15', (SELECT id FROM public."MakersTechApp_brand" WHERE brand_name = 'HP')),
('MacBook Pro 14', (SELECT id FROM public."MakersTechApp_brand" WHERE brand_name = 'Apple')),
('ThinkPad X1 Carbon', (SELECT id FROM public."MakersTechApp_brand" WHERE brand_name = 'Lenovo')),
('Aspire 5', (SELECT id FROM public."MakersTechApp_brand" WHERE brand_name = 'Acer')),
('ROG Zephyrus G14', (SELECT id FROM public."MakersTechApp_brand" WHERE brand_name = 'Asus')),
('Surface Laptop 4', (SELECT id FROM public."MakersTechApp_brand" WHERE brand_name = 'Microsoft')),
('Blade 15', (SELECT id FROM public."MakersTechApp_brand" WHERE brand_name = 'Razer')),
('Galaxy Book Pro', (SELECT id FROM public."MakersTechApp_brand" WHERE brand_name = 'Samsung')),
('Satellite C55', (SELECT id FROM public."MakersTechApp_brand" WHERE brand_name = 'Toshiba'));

-- Insert specific features for each product
-- XPS 13 Features
INSERT INTO public."MakersTechApp_product_model_features" (product_id, feature_id) 
SELECT 
    (SELECT id FROM public."MakersTechApp_product" WHERE model = 'XPS 13'),
    id
FROM public."MakersTechApp_feature"
WHERE feature IN ('Intel Core i7 10750H', '16 GB RAM', '1 TB SSD', '$1500');

-- Pavilion 15 Features
INSERT INTO public."MakersTechApp_product_model_features" (product_id, feature_id) 
SELECT 
    (SELECT id FROM public."MakersTechApp_product" WHERE model = 'Pavilion 15'),
    id
FROM public."MakersTechApp_feature"
WHERE feature IN ('AMD Ryzen 5 4600H', '16 GB RAM', '512 GB SSD', '$1000');

-- MacBook Pro 14 Features
INSERT INTO public."MakersTechApp_product_model_features" (product_id, feature_id) 
SELECT 
    (SELECT id FROM public."MakersTechApp_product" WHERE model = 'MacBook Pro 14'),
    id
FROM public."MakersTechApp_feature"
WHERE feature IN ('Intel Core i7 10750H', '32 GB RAM', '1 TB SSD', '$2000');

-- ThinkPad X1 Carbon Features
INSERT INTO public."MakersTechApp_product_model_features" (product_id, feature_id) 
SELECT 
    (SELECT id FROM public."MakersTechApp_product" WHERE model = 'ThinkPad X1 Carbon'),
    id
FROM public."MakersTechApp_feature"
WHERE feature IN ('Intel Core i5 9600K', '16 GB RAM', '512 GB SSD', '$1500');

-- Aspire 5 Features
INSERT INTO public."MakersTechApp_product_model_features" (product_id, feature_id) 
SELECT 
    (SELECT id FROM public."MakersTechApp_product" WHERE model = 'Aspire 5'),
    id
FROM public."MakersTechApp_feature"
WHERE feature IN ('AMD Ryzen 5 4600H', '16 GB RAM', '1 TB SSD', '$1000');

-- ROG Zephyrus G14 Features
INSERT INTO public."MakersTechApp_product_model_features" (product_id, feature_id) 
SELECT 
    (SELECT id FROM public."MakersTechApp_product" WHERE model = 'ROG Zephyrus G14'),
    id
FROM public."MakersTechApp_feature"
WHERE feature IN ('AMD Ryzen 7 4800HS', '32 GB RAM', '1 TB SSD', '$2500');

-- Surface Laptop 4 Features
INSERT INTO public."MakersTechApp_product_model_features" (product_id, feature_id) 
SELECT 
    (SELECT id FROM public."MakersTechApp_product" WHERE model = 'Surface Laptop 4'),
    id
FROM public."MakersTechApp_feature"
WHERE feature IN ('Intel Core i5 1135G7', '16 GB RAM', '512 GB SSD', '$1200');

-- Blade 15 Features
INSERT INTO public."MakersTechApp_product_model_features" (product_id, feature_id) 
SELECT 
    (SELECT id FROM public."MakersTechApp_product" WHERE model = 'Blade 15'),
    id
FROM public."MakersTechApp_feature"
WHERE feature IN ('Intel Core i7 10875H', '16 GB RAM', '1 TB SSD', '$2500');

-- Galaxy Book Pro Features
INSERT INTO public."MakersTechApp_product_model_features" (product_id, feature_id) 
SELECT 
    (SELECT id FROM public."MakersTechApp_product" WHERE model = 'Galaxy Book Pro'),
    id
FROM public."MakersTechApp_feature"
WHERE feature IN ('Intel Core i5 1135G7', '16 GB RAM', '512 GB SSD', '$1400');

-- Satellite C55 Features
INSERT INTO public."MakersTechApp_product_model_features" (product_id, feature_id) 
SELECT 
    (SELECT id FROM public."MakersTechApp_product" WHERE model = 'Satellite C55'),
    id
FROM public."MakersTechApp_feature"
WHERE feature IN ('Intel Core i3 1005G1', '8 GB RAM', '1 TB HDD', '$700');
```
