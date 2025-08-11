from flask import Flask


existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']

app = Flask(__name__)

# Define routes
@app.route('/')
def index():
    return 'Welcome to Flatiron Cars'

# Models route with dynamic model name
@app.route('/<model>')
def models(model):
    if model in existing_models:
        return f'Flatiron {model} is in our fleet!'
    else:
        return f'No models called {model} exists in our catalog'

if __name__ == '__main__':
    app.run(debug=True)