--Scripts de los modelos de clases
CREATE TABLE User(
    id varchar(36) PRIMARY KEY NOT NULL,
    email varchar(50) UNIQUE NOT NULL,
    first_name varchar(50) NOT NULL,
    last_name varchar(50) NOT NULL
);

CREATE TABLE Country(
    name varchar(70) NOT NULL,
    code varchar(2) NOT NULL PRIMARY KEY
);

CREATE TABLE City(
    id varchar(36) PRIMARY KEY NOT NULL,
    name varchar(70) NOT NULL,
    country_code varchar(2) NOT NULL
    FOREIGN KEY (country_code) REFERENCES Country(code)
);

CREATE TABLE Place(
    id varchar(36) PRIMARY KEY NOT NULL,
    name varchar(70) NOT NULL,
    description varchar(100) NOT NULL,
    number_of_rooms integer NOT NULL,
    number_of_bathrooms integer NOT NULL,
    max_guest integer NOT NULL,
    price_per_night float NOT NULL,
    latitude float NOT NULL,
    host_id varchar(36) NOT NULL,
    city_id varchar(36) NOT NULL,
    FOREIGN KEY (host_id) REFERENCES User(id),
    FOREIGN KEY (city_id) REFERENCES City(id)
);

CREATE TABLE Amentiy(
    id varchar(36) PRIMARY KEY NOT NULL,
    name varchar(70) NOT NULL
);

CREATE TABLE Place_Amenities(
    id varchar(36) PRIMARY KEY NOT NULL,
    place_id varchar(36) NOT NULL,
    amenity_id varchar(36) NOT NULL,
    FOREIGN KEY (place_id) REFERENCES Place(id),
    FOREIGN KEY (amenity_id) REFERENCES Amenity(id)
);