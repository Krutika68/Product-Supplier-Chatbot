CREATE TABLE suppliers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    contact_info TEXT,
    product_categories TEXT
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    brand VARCHAR(255),
    price DECIMAL,
    category VARCHAR(255),
    description TEXT,
    supplier_id INTEGER REFERENCES suppliers(id)
);
