import psycopg2
import os

# Charger les variables d'environnement
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "9OFcMtIEXoQugAAddLbp")
DB_HOST = os.getenv("DB_HOST", "database-1.clkcmqc4qi9v.eu-west-3.rds.amazonaws.com")
DB_NAME = os.getenv("DB_NAME", "my_database")  # Nom de la base de données

# Connexion à PostgreSQL (sans base de données spécifique)
conn = psycopg2.connect(
    dbname="postgres", user=DB_USER, password=DB_PASSWORD, host=DB_HOST
)
conn.autocommit = True  # Nécessaire pour CREATE DATABASE
cur = conn.cursor()

# Vérifier si la base de données existe
cur.execute("SELECT 1 FROM pg_database WHERE datname = %s", (DB_NAME,))
exists = cur.fetchone()

if not exists:
    print(f"📌 Création de la base de données '{DB_NAME}'...")
    cur.execute(f"CREATE DATABASE {DB_NAME}")
else:
    print(f"✅ La base de données '{DB_NAME}' existe déjà.")

# Fermer la connexion initiale
cur.close()
conn.close()

# Se reconnecter à la base de données nouvellement créée
conn = psycopg2.connect(
    dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST
)
cur = conn.cursor()

# Lire et exécuter le fichier schema.sql
with open("schema.sql", "r") as f:
    sql_script = f.read()
    cur.execute(sql_script)

print("✅ Tables créées avec succès !")

# Valider et fermer la connexion
conn.commit()
cur.close()
conn.close()
