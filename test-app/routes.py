from flask import Flask
import controllers.informasi

def register_routes(app: Flask):
    app.add_url_rule('/', view_func=controllers.informasi.index, methods=['GET'])
    app.add_url_rule('/create', view_func=controllers.informasi.create, methods=['GET', 'POST'])
    app.add_url_rule('/show/<int:informasi_id>', view_func=controllers.informasi.show, methods=['GET'])
    app.add_url_rule('/edit/<int:informasi_id>', view_func=controllers.informasi.edit, methods=['GET', 'POST'])
    app.add_url_rule('/delete/<int:informasi_id>', view_func=controllers.informasi.delete, methods=['POST'])