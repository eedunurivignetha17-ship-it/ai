from flask import Blueprint, request, jsonify
from services.ai_service import get_ai_response

ai_bp = Blueprint("ai", __name__)

@ai_bp.route("/chat", methods=["POST"])
def chat():

    data = request.json
    message = data.get("message")

    response = get_ai_response(message)

    return jsonify({
        "response": response
    })