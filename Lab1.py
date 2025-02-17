from flask import Flask

# Название приложения - lab
app = Flask("lab")

@app.route('/')
def hello():
    return "Hello, Docker!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
