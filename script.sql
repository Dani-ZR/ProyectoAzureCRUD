CREATE TABLE estudiantes(

    id INT PRIMARY KEY IDENTITY(1,1),

    nombre VARCHAR(100) NOT NULL,

    correo VARCHAR(100) NOT NULL,

    edad INT NOT NULL,

    carrera VARCHAR(100) NOT NULL

);

INSERT INTO estudiantes(nombre, correo, edad, carrera)
VALUES
('Daniela Zambrano', 'daniela@ucc.edu.co', 23, 'Ingeniería'),

('Carlos Lopez', 'carlos@ucc.edu.co', 22, 'Sistemas'),

('Laura Florez', 'laura@ucc.edu.co', 20, 'Electrónica');