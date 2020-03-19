from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/form', methods=['POST'])
def echoResponse():
    json_data = request.get_json()
    name = json_data['name']
    return jsonify(response="Hello, {}".format(name))

if __name__ == '__main__':
    app.run(debug=True, port=3000)
