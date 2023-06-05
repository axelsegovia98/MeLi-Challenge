CREATE SCHEMA meli;

CREATE TABLE IF NOT EXISTS meli.Customer (
  `custm_id` BIGINT AUTO_INCREMENT PRIMARY KEY, -- Identificador único del usuario
  `custm_user` VARCHAR(20) NOT NULL UNIQUE, -- Nombre de usuario
  `email` VARCHAR(40) NOT NULL UNIQUE, -- Email del usuario
  `first_name` VARCHAR(50) NOT NULL, -- Primer nombre del usuario
  `last_name` VARCHAR(50) NOT NULL, -- Apellido del usuario
  `gender` CHAR(1), -- Género del usuario
  `address` VARCHAR(60), -- Dirección del usuario
  `b_date` DATE NOT NULL, -- Fecha de nacimiento del usuario
  `phone` VARCHAR(15) -- Teléfono de contacto del usuario
);

CREATE TABLE IF NOT EXISTS meli.Category (
  `catg_id` INT AUTO_INCREMENT PRIMARY KEY, -- Identificador único de la categoría
  `catg_path` VARCHAR(100) NOT NULL, -- Path de la categoría
  `catg_name` VARCHAR(40) NOT NULL -- Nombre de la categoría
);

CREATE TABLE IF NOT EXISTS meli.Item (
  `item_id` BIGINT AUTO_INCREMENT PRIMARY KEY, -- Identificador único del item
  `item_name` VARCHAR(60) NOT NULL, -- Nombre del item
  `item_value` FLOAT NOT NULL DEFAULT 0.0, -- Valor del item
  `item_status` CHAR(1) NOT NULL DEFAULT '1', -- Estatus del item [0 Inactivo, 1 Activo]
  `id_seller` BIGINT NOT NULL, -- Identificador único del vendedor que ofrece el item
  `catg_id` INT, -- Identificador único de la categoría del item
  `catg_name` VARCHAR(40) NOT NULL, -- Nombre de la categoría del item
  FOREIGN KEY (`catg_id`) REFERENCES `Category`(`catg_id`)
);

CREATE TABLE IF NOT EXISTS meli.Order (
  `order_id` BIGINT AUTO_INCREMENT PRIMARY KEY, -- Identificador único de la orden
  `order_date` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, -- Fecha de creación de la orden
  `order_value` FLOAT NOT NULL DEFAULT 0.0, -- Valor total de la orden
  `item_id` BIGINT NOT NULL, -- Identificador único del item vendido
  `item_q` INT NOT NULL DEFAULT 1, -- Cantidad de items vendido por orden
  `id_buyer` BIGINT, -- Identificador único del comprador del item
  `address` VARCHAR(60), -- Dirección a la que se va a enviar el item.
  `id_seller` BIGINT, -- Identificador único del vendedor del item
  FOREIGN KEY (`item_id`) REFERENCES `Item`(`item_id`)
  FOREIGN KEY (`id_buyer`) REFERENCES `Customer`(`custm_id`)
);

