from api import db
from passlib.hash import pbkdf2_sha256
class Usuario(db.Model):
    __tablename__= "usuario"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nome = db.Column(db.String(45), nullable=False)
    email = db.Column(db.String(90), nullable=False)
    senha = db.Column(db.String(255), nullable=False)

    def cripto_senha(self):
        self.senha = pbkdf2_sha256.hash(self.senha)

    def decripto_senha(self, senha):
        return pbkdf2_sha256.verify(senha, self.senha)

