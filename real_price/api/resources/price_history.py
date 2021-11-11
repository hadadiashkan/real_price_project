from flask import request
from flask_jwt_extended import jwt_required
from flask_restful import Resource

from real_price.api.schemas import UserSchema
from real_price.extensions import db
from real_price.models import User


class PriceHistoryResource(Resource):
    """Single object resource

    ---
    get:
      tags:
        - api
      summary: Get a price of Dollar or Euro
      description: Get a single price by name
      parameters:
        - in: path
          name: name
          schema:
            type: integer
      responses:
        200:
          content:
            application/json:
              schema:
                type: object
                properties:
                  price_history: PriceHistorySchema
        404:
          description: price history does not exists
    put:
      tags:
        - api
      summary: Update a user
      description: Update a single user by ID
      parameters:
        - in: path
          name: user_id
          schema:
            type: integer
      requestBody:
        content:
          application/json:
            schema:
              UserSchema
      responses:
        200:
          content:
            application/json:
              schema:
                type: object
                properties:
                  msg:
                    type: string
                    example: user updated
                  user: UserSchema
        404:
          description: user does not exists
    delete:
      tags:
        - api
      summary: Delete a user
      description: Delete a single user by ID
      parameters:
        - in: path
          name: user_id
          schema:
            type: integer
      responses:
        200:
          content:
            application/json:
              schema:
                type: object
                properties:
                  msg:
                    type: string
                    example: user deleted
        404:
          description: user does not exists
    """

    method_decorators = []

    def get(self, currency_name):
        schema = UserSchema()
        user = User.query.get_or_404(user_id)
        return {"user": schema.dump(user)}

    def put(self, user_id):
        schema = UserSchema(partial=True)
        user = User.query.get_or_404(user_id)
        user = schema.load(request.json, instance=user)

        db.session.commit()

        return {"msg": "user updated", "user": schema.dump(user)}

    def delete(self, user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()

        return {"msg": "user deleted"}
