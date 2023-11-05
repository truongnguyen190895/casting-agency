import json
from flask import request, _request_ctx_stack, jsonify
from functools import wraps
from jose import jwt
from urllib.request import urlopen
from jose.backends import RSAKey
from jose.exceptions import JWTClaimsError, ExpiredSignatureError
import os
# from settings import AUTH0_DOMAIN, ALGORITHMS, API_AUDIENCE

## AuthError Exception
"""
AuthError Exception
A standardized way to communicate auth failure modes
"""
AUTH0_DOMAIN = os.environ["AUTH0_DOMAIN"]
ALGORITHMS = os.environ["ALGORITHMS"]
API_AUDIENCE = os.environ["API_AUDIENCE"]

class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code


## Auth Header


def get_token_auth_header():
    # Attempt to get the Authorization header from the request
    auth_header = request.headers.get("Authorization", None)

    if not auth_header:
        # Raise an AuthError if no header is present
        raise AuthError(
            {
                "code": "authorization_header_missing",
                "description": "Authorization header is expected.",
            },
            401,
        )

    # Attempt to split the header into "bearer" and the token
    header_parts = auth_header.split()

    if len(header_parts) != 2 or header_parts[0].lower() != "bearer":
        # Raise an AuthError if the header is malformed
        raise AuthError(
            {
                "code": "invalid_header",
                "description": 'Authorization header must be in the format "Bearer token".',
            },
            401,
        )

    # Return the token part of the header
    return header_parts[1]


def check_permissions(permission, payload):
    if "permissions" not in payload:
        # Raise an AuthError if permissions are not included in the payload
        raise AuthError(
            {
                "code": "missing_permissions",
                "description": "Permissions not included in the token.",
            },
            400,
        )

    if permission not in payload["permissions"]:
        # Raise an AuthError if the requested permission is not in the payload permissions array
        raise AuthError(
            {
                "code": "unauthorized",
                "description": "Permission not found in the token.",
            },
            403,
        )

    return True


def verify_decode_jwt(token):
    # Retrieve Auth0's JWKS (JSON Web Key Set)
    jwks_url = f"https://{AUTH0_DOMAIN}/.well-known/jwks.json"
    jwks_response = urlopen(jwks_url)
    jwks_data = json.loads(jwks_response.read())

    # Decode and verify the token using Auth0's JWKS
    rsa_key = RSAKey(key=jwks_data["keys"][0], algorithm="RS256")

    try:
        # Decode the JWT and verify its claims
        payload = jwt.decode(
            token,
            rsa_key,
            algorithms=ALGORITHMS,
            audience=API_AUDIENCE,
            issuer=f"https://{AUTH0_DOMAIN}/",
        )

        return payload

    except ExpiredSignatureError:
        raise AuthError(
            {"code": "token_expired", "description": "Token has expired."}, 401
        )

    except JWTClaimsError as e:
        raise AuthError(
            {
                "code": "invalid_claims",
                "description": "Incorrect claims. Please, check the audience and issuer.",
                "jwt_claims_error": str(e),
            },
            401,
        )

    except Exception as e:
        raise AuthError(
            {
                "code": "invalid_token",
                "description": "Unable to parse authentication token.",
                "exception_message": str(e),
            },
            401,
        )


def requires_auth(permission=""):
    def requires_auth_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            try:
                token = get_token_auth_header()
                payload = verify_decode_jwt(token)
                check_permissions(permission, payload)

                # If the permissions check passes, call the decorated function
                return f(*args, **kwargs)

            except AuthError as e:
                # Handle AuthError exceptions
                return (
                    jsonify(
                        {
                            "success": False,
                            "error": e.error["code"],
                            "message": e.error["description"],
                        }
                    ),
                    e.status_code,
                )

        return wrapper

    return requires_auth_decorator
