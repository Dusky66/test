# Importovanie Flask modulu
from flask import Flask

# Vytvorenie inštancie aplikácie
app = Flask(__name__)

# Definovanie cesty a príslušnej funkcie
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Spustenie aplikácie
if __name__ == '__main__':
    app.run(debug=True)
