from flask import Flask, jsonify, request, render_template
import pymysql.cursors
from ADN_Secuencias import hasMutation

app = Flask(__name__)
cont = [0,0];

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/mutation', methods=['POST'])
def mutacion():
    #Conexion a la base de datos 
    connection  = pymysql.connect(user='locia@mutationserver',
                       password='Gal14695238',
                       database='mutations',
                       host='mutationserver.mysql.database.azure.com',
                       cursorclass=pymysql.cursors.DictCursor,
                       ssl= {'ca':'C:/ssl/BaltimoreCyberTrustRoot.crt.pem'})

    
    dn = request.json['dna'] #obtiene el archivo json de la url 
    #comprueba si el adn tiene mutaciones
    mutations, cout_mutations, cout_no_mutations = hasMutation(dn)

    cont[0] = cont[0] + cout_mutations #posicion 0 para mutaciones
    cont[1] = cont[1] + cout_no_mutations #posicion 1 para no mutaciones

    Stradn = "".join(dn)    
   

    if mutations:
        with connection:
            with connection.cursor() as cursor:
                cursor.execute('INSERT INTO adn(id,DNA,Mutation) VALUES(%s,%s,%s)',(0,Stradn,cout_mutations))
            connection.commit()
        return 'Se han encontrado mutaciones', 200, {'Content-Type':'text/plain'}
    else:
        with connection:
            with connection.cursor() as cursor:
                cursor.execute('INSERT INTO adn(id,DNA,Mutation) VALUES(%s,%s,%s)',(0,Stradn,cout_mutations))
            connection.commit()
        return 'No se encotraron mutacinones', 403, {'Content-Type':'text/plain'}
   

@app.route('/status')
def status():

    ratio = 0.0
    if cont[1] != 0:
        ratio = float(cont[0])/float(cont[1])
    
    Status = [
       {"count_mutation":cont[0],
        "count_no_mutation":cont[1],
        "ratio": ratio
       } 
    ]
    return  jsonify(Status)


if __name__ == '__main__':
    app.run(debug=True,port=4000)