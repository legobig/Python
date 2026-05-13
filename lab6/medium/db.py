import psycopg2
from datetime import datetime

conn = psycopg2.connect(
    dbname="geometry_db",
    user="postgres",
    password="12345",
    host="localhost",
    port="5432"
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS calculations (
    id SERIAL PRIMARY KEY,
    figure TEXT,
    a NUMERIC,
    b NUMERIC,
    c NUMERIC,
    area NUMERIC,
    r_out NUMERIC,
    r_in NUMERIC,
    created_at TIMESTAMP
)
""")

conn.commit()


def save_result(figure, a=None, b=None, c=None, area=None, r_out=None, r_in=None):
    cursor.execute("""
        INSERT INTO calculations
        (figure, a, b, c, area, r_out, r_in, created_at)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
    """, (
        figure, a, b, c, area, r_out, r_in, datetime.now()
    ))
    conn.commit()
