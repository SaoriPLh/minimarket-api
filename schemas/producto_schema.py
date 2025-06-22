from marshmallow import Schema, fields
#como deben de venir los datos desde el front con ciertas reglas 
class ProductoRequestSchema(Schema): #hereda de schema con sus funciones como validar y selecalizar 
    nombre = fields.Str(required=True) # fields son los atributos que definen cada campo 
    precio = fields.Float(required=True) #requited indica q el campo es obligatorio si falta el hacer load que es el q valida los campos lanza error
    image_url = fields.Str(required=True)
    stock = fields.Int(required=True)
    categoria = fields.Str(required=True)


#dump_onlu = true es para campos que se usara para respuestas (salidas) no para validacion de entrada

#load_only = true el campo se usa al recibir datos osea q no la devolvemos como salida en una respuesta