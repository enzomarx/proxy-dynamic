# create the interface web to manage the proxy
from flask import Flask, request, render_template, redirect, url_for
import json

app = Flask(__name__)

def load_config():
  with open('config.json') as f:
    return json.load(f)

def save_config(config):
  with open('config.json', 'w') as f:
    json.dump(config, f, indent=1)

@app.route('/')
def index():
  config = load_config()
  return render_template('index.html', routes=config['routes'])

@app.route('/add_route', methods=['POST'])
def add_route():
  config = load_config()
  new_route = {
  'host': request.form['host'],
  'scheme': request.form['scheme'],
  'target_host': request.form['target_host'],
  'target_port': int(request.form['target_host']
}
config['routes'].append(new_route)
save_config(config)
return redirect(url_for('index'))

@app.route('/delete_route/<int:route_id>', methods=['POST'])
def delete_route(route_id):
  config = load_config()
  config['routes'].pop(route_id)
  save_config(config)
  return redirect(url_for('index'))

if __name__ == '__main__':
  app.run(port=5000)
