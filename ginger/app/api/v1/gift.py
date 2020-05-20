from flask import g

from app.libs.error_code import Success, DuplicateGift
from app.libs.redprint import Redprint
from app.models.base import db
from app.models.book import Book
from app.models.gift import Gift

api = Redprint('gift')


@api.route('/<isbn>',methods=['POST'])
def create(isbn):
    uid = g.user.id
    with db.auto_commit():
        Book.query.filter_by(isbn=isbn).first_or_404()
        gift = Gift.query.filter_by(uid = uid,isbn=isbn).first()
        if not gift:
            raise DuplicateGift()
        gift = Gift()
        gift.uid = uid
        gift.isbn = isbn
        db.session.add(gift)

    return Success()


