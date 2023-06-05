/* 
Listar los usuarios que cumplan años el día de hoy cuya cantidad de ventas
realizadas en enero 2020 sea superior a 1500. 
*/

SELECT
    -- Campos de interes para analizar
    Custm.custm_id,
    Custm.b_date,
    COUNT(Order.id_seller) AS q_sales -- Total de ventas
FROM meli.Customer AS Custm
-- Se cruzan los datos con la tabla de transacciones buscando traer cada transaccion por cliente
INNER JOIN meli.Order AS Order
ON Custm.custm_id = Order.id_seller
-- Se filtran datos en base a los usuarios que cumplan años el día de hoy 
-- CURDATE() Nos devuelve la fecha de hoy en formato yyyy-MM-dd
WHERE Custm.b_date = CURDATE()
-- Se filtran las ordenes que sucedieron en el mes de Enero de 2020
AND Order.order_date >= '2020-01-01'
AND Order.order_date <= '2020-01-31'
-- A razón del COUNT() sobre la cantidad de ordenes por cliente se realiza un GROUP BY.
GROUP BY Order.id_seller
-- Se reducen los resultados a los clientes que tengan más de 1500 ventas.
HAVING COUNT(Order.id_seller) > 1500
;




/*
Por cada mes del 2020, se solicita el top 5 de usuarios que más vendieron($) en la
categoría Celulares. Se requiere el mes y año de análisis, nombre y apellido del
vendedor, cantidad de ventas realizadas, cantidad de productos vendidos y el monto
total transaccionado
*/

SELECT * FROM (
	SELECT
        -- Campos de interes para analizar
		Custm.custm_id,
		DATE_FORMAT(Orders.order_date, '%m') AS month,
		DATE_FORMAT(Orders.order_date, '%Y') AS year,
		Custm.first_name,
		Custm.last_name,
		COUNT(Orders.id_seller) AS q_sales, --Total de ventas
		SUM(Orders.item_q) AS q_products, --Total de productos
		SUM(Orders.order_value) AS total_amount, --Monto total vendido
        /* 
        Para obtener un TOP 5 de usuarios en base a sus ventas se optó por usar un DENSE_RANK()
        Este tiene como objetivo evitar enumerar resultados de forma secuencial e interpretar
        los datos de forma que se identifique los meses como distintas particiones a las que enumerar
        y posterior a eso la forma de enumerarlos 
        sea en base a el mes, el monto total, el total de ventas y el total de productos vendidos
        a razón de intentar evitar más de 5 usuarios par el TOP 5
        */
        DENSE_RANK() OVER (
			PARTITION BY DATE_FORMAT(Orders.order_date, '%m')
            ORDER BY
				DATE_FORMAT(Orders.order_date, '%m'),
                SUM(Orders.order_value) DESC,
				COUNT(Orders.id_seller) DESC,
                SUM(Orders.item_q) DESC)
		AS top_ranked
	FROM meli.Customer AS Custm
    -- Se cruzan los datos con la tabla de transacciones buscando traer cada transaccion por cliente
	INNER JOIN meli.Order AS Orders
	ON Custm.custm_id = Orders.id_seller
    -- Se cruzan los datos con la tabla de items buscando traer cada item y filtrarlo por la categoria celulares
    INNER JOIN meli.item AS Items
    ON Orders.item_id = Items.item_id
    AND Items.catg_name = 'Celulares'
    -- Se filtran los datos dejan solo los del 202
	WHERE DATE_FORMAT(Orders.order_date, '%Y') = '2020'
    -- A razón del COUNT() sobre la cantidad de ordenes por cliente, y por los campos transformados se realiza un GROUP BY.
	GROUP BY Orders.id_seller, month, year
    ) AS TEMP
-- Se filtran los datos en base a el resultado del DENSE_RANK con el objetivo de quedarse
-- solo con los que esten en el TOP 5.
WHERE top_ranked  <= 5
;




/*
Se solicita poblar una nueva tabla con el precio y estado de los Ítems a fin del día.
Tener en cuenta que debe ser reprocesable. Vale resaltar que en la tabla Item,
vamos a tener únicamente el último estado informado por la PK definida. (Se puede
resolver a través de StoredProcedure)
*/

CREATE PROCEDURE GetActiveItems(IN ItemStatusTable VARCHAR(50))
-- El parametro ItemStatusTable espera recibir el nombre de la tabla que va a ser poblada
BEGIN
    -- Se limpia la tabla para tener posteriormente el último dato del item
    SET @sql = CONCAT('TRUNCATE TABLE ', ItemStatusTable);
    PREPARE stmt FROM @sql;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;

    -- Se cargan los datos en la tabla incluyendo ID del item, el precio y el status
    INSERT INTO ItemStatusTable (item_id, item_price, item_status)
    SELECT item_id, item_price, item_status
    FROM meli.Item;
END