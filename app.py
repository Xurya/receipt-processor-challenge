from routes.receipts import receipts_bp
from flask import Flask

app = Flask(__name__)
app.register_blueprint(receipts_bp)

if __name__ == '__main__':
    app.run()