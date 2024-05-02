from app import db
from app.model import user

Fonkay = user(username = "fonkyponkay", email= "fonkayp4k@gmail.com", password = "Hithere123")
db.session.add(Fonkay)