from flask import Flask, render_template, jsonify
import dfs_interactivo
import dfs_recursivo
import dijsktra
import Puzzle_lineal_3601
import vuelos_bfs

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dfs-interactivo', methods=['GET'])
def dfs():
    resultado_dfs_interactivo= dfs_interactivo.imprimir()
    return jsonify({"resultado": resultado_dfs_interactivo})

@app.route('/dfs-recursivo', methods=['GET'])
def dfs2():
    resultado_dfs_recursivo= dfs_recursivo.imprimir()
    return jsonify({"resultado": resultado_dfs_recursivo})

@app.route('/dijsktra', methods=['GET'])
def dfs3():
    resultado_dijsktra= dijsktra.imprimir()
    return jsonify({"resultado": resultado_dijsktra})

@app.route('/puzzle-lineal', methods=['GET'])
def dfs4():
    resultado_puzzle_lineal = Puzzle_lineal_3601.imprimir()
    return jsonify({"resultado": resultado_puzzle_lineal})

@app.route('/vuelos-bfs', methods=['GET'])
def dfs5():
    resultado_vuelos_bfs= vuelos_bfs.imprimir()
    return jsonify({"resultado": resultado_vuelos_bfs})




if __name__ == '__main__':
    app.run(debug=True)
