from marshmallow import Schema, fields
#como deben de venir los datos desde el front
class ProductoRequestSchema(Schema):
    nombre = fields.Str(required=True)
    precio = fields.Float(required=True)
    image_url = fields.Str(required=True)
    stock = fields.Int(required=True)
    categoria = fields.Str(required=True)
