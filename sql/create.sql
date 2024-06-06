CREATE TABLE IF NOT EXISTS Schedule_state (
    state_id INT PRIMARY KEY NOT NULL,
    state_name VARCHAR(20) NOT NULL
);

CREATE TABLE IF NOT EXISTS Schedule (
    schedule_id INT PRIMARY KEY NOT NULL,
    state_id INT NOT NULL,
    master_id INT NOT NULL,
    closing_time TIME NOT NULL,
    opening_time TIME NOT NULL,
    date DATE NOT NULL,
    FOREIGN KEY (master_id) REFERENCES Master(master_id),
    FOREIGN KEY (state_id) REFERENCES Schedule_state(state_id)
);

CREATE TABLE IF NOT EXISTS Master (
    master_id INT PRIMARY KEY NOT NULL,
    last_name VARCHAR(40) NOT NULL,
    first_name VARCHAR(40) NOT NULL,
    middle_name VARCHAR(40),
    gender CHAR(1) NOT NULL,
    phone_number VARCHAR(20) NOT NULL,
    birth_date DATE NOT NULL,
    position_id INT NOT NULL,
    salon_id INT NOT NULL,
    FOREIGN KEY (position_id) REFERENCES Position(position_id),
    FOREIGN KEY (salon_id) REFERENCES Salon(salon_id)
);

CREATE TABLE IF NOT EXISTS Master_Service (
    service_id INT NOT NULL,
    master_id INT NOT NULL,
    PRIMARY KEY (service_id, master_id),
    FOREIGN KEY (service_id) REFERENCES Service(service_id),
    FOREIGN KEY (master_id) REFERENCES Master(master_id)
);

CREATE TABLE IF NOT EXISTS Service (
    service_id INT PRIMARY KEY NOT NULL,
    price DECIMAL(8,2) NOT NULL,
    duration VARCHAR(20) NOT NULL,
    service_name VARCHAR(20) NOT NULL
);

CREATE TABLE IF NOT EXISTS Position (
    position_id INT PRIMARY KEY NOT NULL,
    rate DECIMAL(8,2) NOT NULL,
    position_name VARCHAR(20) NOT NULL
);

CREATE TABLE IF NOT EXISTS Salon (
    salon_id INT PRIMARY KEY NOT NULL,
    address VARCHAR(40) NOT NULL,
    area VARCHAR(20) NOT NULL,
    closing_time TIME NOT NULL,
    opening_time TIME NOT NULL
);
