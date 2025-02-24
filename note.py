from flask import Blueprint, request, jsonify
from models import db, Note
note_bp = Blueprint("note", __name__)

# 모든 메모 조회 (GET)
@note_bp.route("/api/notes", methods=["GET"])
def get_notes():
    page = request.args.get('page', 1, type=int)
    notes = Note.query.paginate(page=page, per_page=10, error_out=False)

    return jsonify({
        "notes":[note.to_dict() for note in notes.items],
        "total_pages": notes.pages
    })

# 메모 추가 (POST)
@note_bp.route("/api/notes", methods=["POST"])
def create_note():
    data = request.get_json()
    if not data or not all(key in data for key in ("title", "content")):
        return jsonify({"error": "제목과 내용을 입력하세요."}), 400
    
    new_note = Note(**data)
    db.session.add(new_note)
    db.session.commit()

    return jsonify(new_note.to_dict()), 201

# 메모 삭제 (DELETE)
@note_bp.route("/api/notes/<int:id>", methods=["DELETE"])
def delete_note(id):
    note = Note.query.get(id)

    if not note:
        return jsonify({"error": "메모를 찾을 수 없습니다."}), 404

    db.session.delete(note)
    db.session.commit()
    
    return jsonify({"message": "메모가 삭제되었습니다."}), 200