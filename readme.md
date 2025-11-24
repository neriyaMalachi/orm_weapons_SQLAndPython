# FastAPI + SQLModel Demo

## Quick Start
1. Create virtualenv and install deps:
   ```bash
   pip install -r requirements.txt


for create data

   ```bash

CREATE TABLE IF NOT EXISTS customer (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    country VARCHAR(50) DEFAULT 'IL'
);
        INSERT INTO customer (name, country) VALUES
        ('Amit Cohen', 'IL'),
        ('Dana Levy', 'IL'),
        ('Yossi Peretz', 'IL'),
        ('Noa Bar', 'US'),
        ('David Katz', 'UK'),
        ('Shir Azulay', 'IL'),
        ('Roi Shlomi', 'IL'),
        ('Michael Levi', 'CA'),
        ('Or Tal', 'IL'),
        ('Lior Shaked', 'IL'),
        ('Hila Ron', 'IL'),
        ('Yaron Mor', 'FR'),
        ('Yael Ben Harush', 'IL'),
        ('Tom Avraham', 'IL'),
        ('Niv Hadar', 'IL'),
        ('Tal Engel', 'US'),
        ('Omer Gold', 'IL'),
        ('Moshe Sharabi', 'IL'),
        ('Gal Cohen', 'IL'),
        ('Sarah Klein', 'DE');






CREATE TABLE IF NOT EXISTS `order` (
    id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    total DECIMAL(10,2) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customer(id)
);

        INSERT INTO `order` (customer_id, total, created_at) VALUES
        (1, 120.50, '2024-12-01 10:22:00'),
        (1, 499.90, '2024-12-05 14:10:00'),
        (2, 250.00, '2024-12-03 09:45:00'),
        (2, 1299.00, '2024-12-10 11:31:00'),
        (3, 59.90, '2024-12-02 16:05:00'),
        (3, 89.90, '2024-12-02 17:20:00'),
        (3, 700.00, '2024-12-12 19:04:00'),
        (4, 220.00, '2024-12-04 13:55:00'),
        (5, 780.00, '2024-12-06 12:20:00'),
        (6, 650.00, '2024-12-07 08:20:00'),
        (6, 150.00, '2024-12-08 10:12:00'),
        (7, 320.00, '2024-12-09 13:45:00'),
        (7, 420.00, '2024-12-11 11:10:00'),
        (8, 999.00, '2024-12-11 14:15:00'),
        (9, 45.00, '2024-12-02 09:01:00'),
        (9, 180.00, '2024-12-03 15:20:00'),
        (10, 2000.00, '2024-12-15 18:00:00'),
        (10, 250.00, '2024-12-16 12:21:00'),
        (11, 50.00, '2024-12-01 11:11:00'),
        (12, 760.00, '2024-12-02 13:37:00'),
        (13, 120.00, '2024-12-04 10:10:00'),
        (13, 130.00, '2024-12-05 11:55:00'),
        (14, 450.00, '2024-12-07 17:20:00'),
        (15, 250.00, '2024-12-08 16:40:00'),
        (15, 330.00, '2024-12-10 19:20:00'),
        (16, 899.00, '2024-12-11 20:10:00'),
        (17, 140.00, '2024-12-01 07:00:00'),
        (17, 300.00, '2024-12-03 14:00:00'),
        (17, 500.00, '2024-12-15 18:00:00'),
        (18, 100.00, '2024-12-03 10:10:00'),
        (19, 230.00, '2024-12-09 12:12:00'),
        (19, 150.00, '2024-12-10 13:13:00'),
        (20, 500.00, '2024-12-14 08:00:00'),
        (20, 600.00, '2024-12-15 09:00:00'),
        (20, 1600.00, '2024-12-16 10:00:00'),
        (1, 999.99, '2024-12-20 16:00:00'),
        (4, 1100.00, '2024-12-18 14:10:00'),
        (6, 2200.00, '2024-12-19 19:40:00'),
        (10, 3000.00, '2024-12-21 21:00:00');
