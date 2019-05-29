from flask_restful import Resource, Api, reqparse
from models.user import User 



class Login(Resource): 
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email', required=True, type=str, help='Mail cannot be blank!')
        parser.add_argument('password', required=True, type=str, help='Password cannot be blank!')
        args = parser.parse_args()

        u = User.get(email=args.get("email"))

        if(u != None and args.get('password') == u.password):
            return {'user': {'id': u.id, 'email': u.email }, 'token': u.auth_token}
        else:
            return {}, 401