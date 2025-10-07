from flask import Flask, render_template
from models import Base  # importa Base desde __init__.py de tu carpeta models
from config.database import engine  # tu engine de SQLAlchemy

app = Flask(__name__)

# Crear tablas de base de datos
Base.metadata.create_all(bind=engine)


@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
