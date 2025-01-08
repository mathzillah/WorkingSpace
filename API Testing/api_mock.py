from flask import Flask, request, jsonify

my_app = Flask(__name__)

@my_app.route("/get-user/<user_id>")

def get_user(user_id):
    user_data = {
        'user_id': user_id,
        "name": "John Doe",
        "email": "john.doe@example.com"
    }
    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra

    return jsonify(user_data), 200

@my_app.route("/create-user", methods =["POST"])
def create_user():
    data = request.get_json()
    return jsonify(data), 201

if __name__ == "__main__":
    my_app.run(debug=True)
