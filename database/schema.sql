-- TODO: Definir las tablas del sistema

-- Tabla de usuarios
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(80) UNIQUE NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla de productos  
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    price NUMERIC(10, 2) NOT NULL,
    stock INTEGER DEFAULT 0,
    image_url VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla de carritos
CREATE TABLE carts (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla de items del carrito
CREATE TABLE cart_items (
    id SERIAL PRIMARY KEY,
    cart_id INTEGER NOT NULL REFERENCES carts(id) ON DELETE CASCADE,
    product_id INTEGER NOT NULL REFERENCES products(id) ON DELETE CASCADE,
    quantity INTEGER NOT NULL DEFAULT 1,
    added_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Agregar índices para optimizar consultas
CREATE INDEX idx_users_username ON users(username);
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_products_name ON products(name);
CREATE INDEX idx_carts_user_id ON carts(user_id);
CREATE INDEX idx_cart_items_cart_id ON cart_items(cart_id);
CREATE INDEX idx_cart_items_product_id ON cart_items(product_id);

-- Insertar datos de prueba
INSERT INTO users (username, email, password_hash, is_active) VALUES
('admin', 'admin@tienda.com', 'hashed_password_admin', TRUE),
('usuario1', 'usuario1@tienda.com', 'hashed_password_1', TRUE),
('usuario2', 'usuario2@tienda.com', 'hashed_password_2', TRUE);

INSERT INTO products (name, description, price, stock, image_url) VALUES
('Laptop', 'Laptop de alto rendimiento', 1500.00, 10, '/static/images/laptop.jpg'),
('Mouse', 'Mouse inalámbrico ergonómico', 25.50, 50, '/static/images/mouse.jpg'),
('Teclado', 'Teclado mecanico RGB', 89.99, 30, '/static/images/keyboard.jpg'),
('Monitor', 'Monitor 4K 27 pulgadas', 399.99, 5, '/static/images/monitor.jpg'),
('Headphones', 'Audífonos profesionales', 149.99, 20, '/static/images/headphones.jpg');
