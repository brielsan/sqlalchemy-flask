from flask import Blueprint, request, jsonify
from models.contact import Contact
from utils.db import db

contacts = Blueprint("contacts", __name__)


@contacts.route("/get", methods=["GET"])
def get_contacts():
    result = []
    for u in Contact.query.all():
        del u.__dict__["_sa_instance_state"]
        result.append(u.__dict__)
    return jsonify(result)


@contacts.route("/new", methods=["POST"])
def add_contact():
    request_data = request.get_json()

    fullname = request_data["fullname"]
    email = request_data["email"]
    phone = request_data["phone"]

    new_contact = Contact(fullname, email, phone)

    db.session.add(new_contact)
    db.session.commit()

    response = {"msg": "User created successfully"}
    return response


@contacts.route("/update/<id>", methods=["PUT"])
def update_contact(id):
    request_data = request.get_json()

    contact = Contact.query.get(id)

    contact.fullname = request_data["fullname"]
    contact.email = request_data["email"]
    contact.phone = request_data["phone"]

    db.session.commit()

    response = {"msg": "User updated successfully"}
    return response


@contacts.route("/delete/<id>", methods=["DELETE"])
def delete_contact(id):
    contact = Contact.query.get(id)

    db.session.delete(contact)
    db.session.commit()

    response = {"msg": "User deleted successfully"}
    return response
