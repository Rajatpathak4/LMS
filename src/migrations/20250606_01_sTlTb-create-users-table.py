 CREATE TABLE public.login (
            id SERIAL PRIMARY KEY,
            token VARCHAR(100) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            created_by INT

 )