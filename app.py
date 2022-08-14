from flask import Flask, request, jsonify

from aistuff import aistuff
app = Flask(__name__)

@app.route("/api", methods=['GET'])
def home():
    turn = float(request.args['turn'])
    p1h = float(request.args['p1h'])
    p1i = float(request.args['p1i'])
    p2h = float(request.args['p2h'])
    p2i = float(request.args['p2i'])
    p1t0 = request.args['p1t0']
    p1t1 = request.args['p1t1']
    p1t2 = request.args['p1t2']
    p2t0 = request.args['p2t0']
    p2t1 = request.args['p2t1']
    p2t2 = request.args['p2t2']
    ai = aistuff()
    result = ai.getPredictions(turn,p1h,p1i,p2h,p2i,p1t0,p1t1,p1t2,p2t0,p2t1,p2t2)
    jsonObj = {
        "a": str(result[0]),
        "b": str(result[1]),
        "c": str(result[2]),
        "d": str(result[3]),
        "e": str(result[4])
    }
    return jsonify(jsonObj)

@app.route("/")
def default():
    return "App is live. make Api call @ /api"

if __name__ == '__main__':
    app.run()