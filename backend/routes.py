from app import app, db
from flask import request, jsonify
from models import Contact

# get all contacts
@app.route("/api/contacts")
def get_contacts():
      contacts = Contact.query.all()
      result = [contact.to_json() for contact in contacts]
      return jsonify(result)