from flask import Flask, jsonify, request

app= Flask(__name__)

playlist = [
    {"id": 1, "titulo": "Shape of You ", "artista": "Ed sheeran", "link": "https://www.youtube.com/watch?v=JGwWNGJdvx8&vl=pt-BR"},
    {"id": 2, "titulo": "Odisseus", "artista": "Jorge Rivera", "link": "https://www.youtube.com/watch?v=XusDFv2wL9U"},
    {"id": 3, "titulo": "Puppeteer", "artista": "Jorge Rivera", "link": "https://www.youtube.com/watch?v=tso8nSWnENM"},
    {"id": 4, "titulo": "God games", "artista": "Jorge Rivera", "link": "https://www.youtube.com/watch?v=z_5Hokpu0vg"},
    {"id": 5, "titulo": "Hold Them Down", "artista": "Jorge Rivera", "link": "https://www.youtube.com/watch?v=oeDDZNKHOVo"},
    {"id": 6, "titulo": "Just a man", "artista": "Jorge Rivera", "link": "https://www.youtube.com/watch?v=glYh3O2Rcz8"}

]

@app.route('/musicas', methods =['GET'])
def get_musicas():
    return jsonify({"playlist": playlist, "total": len(playlist)})
 
@app.route("/musicas", methods= ["POST"])
def add_musica():
    nova_musica = request.json
    nova_musica["id"] = len(playlist) + 1 
    playlist.append(nova_musica)
    return jsonify({"mensagem": "Nova música criada!", "musica": nova_musica}),201

@app.route("/musicas/<int:id>")
def encontrar(id):
    for musica in playlist:
        if id == musica["id"]:
            return musica
    return {"mensagen": "Música não encontrada"},404

app.run(debug=True, host="0.0.0.0" )