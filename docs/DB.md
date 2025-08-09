MEMBUAT DATABASE

# Masuk ke psql:

psql -U postgres

# Lalu di dalam psql:

# -- Buat user baru dengan password

CREATE USER dbname_user WITH PASSWORD 'dbname123';

# -- Buat database baru kalau belum ada

CREATE DATABASE dbname_db;

# -- Kasih hak akses ke user baru untuk database itu

GRANT ALL PRIVILEGES ON DATABASE dbname_db TO dbname_user;

# -- (Opsional) Jadikan dia owner

ALTER DATABASE dbname_db OWNER TO dbname_user;

# Lalu keluar dari psql:

\q

# Contoh hasil url db

DATABASE_URL = postgresql://dbname_user:dbname123@localhost:5432/dbname_db
