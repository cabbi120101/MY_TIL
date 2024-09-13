import mysql.connector

def get_db_connection():
    # MySQL에 연결하기 위한 설정을 입력합니다.
    return mysql.connector.connect(
        host="localhost",  # MySQL 서버 주소
        user="ssafy",  # MySQL 사용자 이름
        password="1234",  # MySQL 비밀번호
        database="face_recognition_db"  # 사용할 데이터베이스 이름
    )