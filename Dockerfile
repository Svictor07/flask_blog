# Utiliser une image officielle de Python comme base
FROM python:3.11-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier le fichier des dépendances et les installer
COPY requirements.txt .

# Installer les dépendances, y compris Gunicorn
RUN pip install --no-cache-dir -r requirements.txt gunicorn

# Copier le code source de l'application
COPY . .

# Exposer le port sur lequel Flask tourne
EXPOSE 5000

# Utiliser Gunicorn pour exécuter l’application Flask
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:50", "app:app"]

