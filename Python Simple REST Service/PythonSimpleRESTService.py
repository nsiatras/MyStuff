from flask import Flask, jsonify, request
  
app = Flask(__name__)

@app.route('/testme', methods=['GET'])
def testme():
    if(request.method == 'GET'):
        data = {"#1": "Welcome to my python Rest Service!", "#2":"Data","#3":"More data..."}
        return jsonify(data)
  
  
if __name__ == '__main__':
    app.run(debug=True)