---> set the Role
USE ROLE accountadmin;

---> set the Warehouse
USE WAREHOUSE compute_wh;

CREATE OR REPLACE SCHEMA sql_edu.staging;

---> create the Raw Menu Table
CREATE OR REPLACE TABLE sql_edu.staging.customers
(
    name VARCHAR(100),            -- Name of the customer
    first_purchase DATE,          -- Date of the first purchase
    country VARCHAR(50),          -- Country of the customer
    company VARCHAR(100)          -- Company the customer is associated with
);

INSERT INTO sql_edu.staging.customers (name, first_purchase, country, company)
SELECT c2, c3, c4, c5
FROM sql_edu.public.raw_l
WHERE c1 = 'customers_raw';
