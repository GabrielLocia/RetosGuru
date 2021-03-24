from flask import Flask, jsonify, request
from ADN_Secuencias import hasMutation

app = Flask(__name__)

@app.route('/mutation', methods=['POST'])
def mutacion():
    dn = request.json['dna']
    
    if hasMutation(dn):
        return 'Se han encontrado mutaciones', 200, {'Content-Type':'text/plain'}
    else:
         return 'No se encotraron mutacinones', 403, {'Content-Type':'text/plain'}


if __name__ == '__main__':
    app.run(debug=True,port=4000)