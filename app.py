from flask import Flask, jsonify, request, send_from_directory

from config import SQLALCHEMY_DATABASE_URI, SECRET_KEY
from models import db, Note
from note import note_bp
import os

def create_app():
    app = Flask(__name__)

    # 환경 변수 설정
    app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
    app.config["SECRET_KEY"] = SECRET_KEY

    # DB 초기화
    db.init_app(app)

    # 블루프린트 등록
    app.register_blueprint(note_bp)

    # 데이터베이스 테이블 생성
    with app.app_context():
        if not os.path.exists("instance/database.db"):
            db.create_all()
            print("데이터베이스가 생성되었습니다.")

    @app.route("/")
    def index():
        return send_from_directory("static", "index.html")

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=1328, debug=True)