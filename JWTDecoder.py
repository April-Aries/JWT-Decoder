import jwt

def decode_jwt(token, secret_key, algorithms=['HS256']):
    try:
        decoded_data = jwt.decode(token, secret_key, algorithms=algorithms)
        return decoded_data
    except jwt.ExpiredSignatureError:
        return "Token has expired"
    except jwt.InvalidTokenError:
        return "Invalid token"

ct = input( "Please input the encoded JSON Web Token: " )
secret = input( "Please input the secret: " )

ctList = ct.split('.')

decoded_data = decode_jwt(ct, secret)

if isinstance(decoded_data, dict):
    print("Decoded JSON Web Token Data:")
    for key, value in decoded_data.items():
        print(f"{key}: {value}")
else:
    print(decoded_data)
