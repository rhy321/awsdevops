from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from the Dockerized Flask App on AWS EC2!"

if __name__ == '__main__':
    # It's crucial for Flask to listen on 0.0.0.0 for it to be accessible
    # outside the container (e.g., from the EC2 host).
    app.run(host='0.0.0.0', port=5000)

