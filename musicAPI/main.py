from flask import Flask, request, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/musicdb"
mongo = PyMongo(app)

# Endpoint for user registration
@app.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    user = {
        'username': data['username'],
        'email': data['email'],
        'password': data['password']
    }
    users_collection = mongo.db.users
    result = users_collection.insert_one(user)
    return jsonify({'message': 'User registered successfully', 'user_id': str(result.inserted_id)}), 201

# Endpoint for adding a new song
@app.route('/songs', methods=['POST'])
def add_song():
    data = request.get_json()
    song = {
        'title': data['title'],
        'artist': data['artist'],
        'genre': data['genre']
    }
    songs_collection = mongo.db.songs
    result = songs_collection.insert_one(song)
    return jsonify({'message': 'Song added successfully', 'song_id': str(result.inserted_id)}), 201

# Endpoint for getting all songs
@app.route('/songs', methods=['GET'])
def get_songs():
    songs_collection = mongo.db.songs
    songs = songs_collection.find({}, {'_id': False})
    return jsonify({'songs': list(songs)})

if __name__ == '__main__':
    app.run(debug=True)
