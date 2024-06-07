# ADM-DB

## Overview
This repository contains scripts and data for generating and managing a salon management database. The database is designed to handle various aspects of salon operations, including client information, service offerings, staff schedules, promotions, and transaction receipts.

## Table of Contents
- [Project Structure](#project-structure)
- [Dependencies](#dependencies)
- [Database Schema](#database-schema)
- [Data Generation](#data-generation)
- [Master Data](#master-data)

## Project Structure
The repository is organized as follows:

├── csv/ # Directory containing CSV files <br>
├── sql/ # Directory containing SQL scripts  <br>
├── \*script*.py # Directory containing Python scripts for data generation
├── salon_management.db # SQLite database file
├── README.md # This README file
├── Master Data.ipynb # Master Data notebook with Golden Records

## Dependencies
The project requires the following Python packages:
- `pandas`
- `faker`
- `sqlite3`

## Database Schema
The database schema consists of the following tables:
- `Client`: Stores information about salon clients.
- `Service`: Lists available services and their details.
- `Registration`: Records client registrations for services.
- `Service_Registration`: Links services to registrations.
- `Promotion`: Contains promotion details.
- `Receipt`: Stores transaction receipts.

For detailed schema definitions, refer to the `sql/create.sql` file.

## Data Generation
The data used to populate the database is generated using various Python scripts located in the `scripts` directory. Each script is responsible for generating data for specific tables and saving it to corresponding CSV files in the `csv` directory. The scripts use libraries such as `pandas`, `random`, `datetime`, and `faker` to create realistic and diverse data.

- **Clients.py**: Generates client data.
- **Master_serv.py**: Assigns services to masters.
- **Masters.py**: Generates master (staff) data.
- **Position.py**: Creates position data.
- **Promo.py**: Generates promotion data.
- **Receipts.py**: Creates receipt data.
- **Salon.py**: Generates salon location data.
- **Schedule.py**: Creates schedule data for masters.
- **Service_Registration.py**: Links services to registrations.
- **Services.py**: Generates data for available services.

## Master Data
This script loads data from CSV files, normalizes phone numbers and formats addresses. The cleaned data is then saved back to the original CSV files.
