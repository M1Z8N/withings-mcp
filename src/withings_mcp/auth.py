import os
import requests
import secrets
from dotenv import load_dotenv

#oauth flow state, vcode exchange and token refresh

load_dotenv()

clientID = os.getenv("clientID")
redirect_uri = os.getenv("redirect_uri")
scope = "user.metrics"

def authAttempt():

    state = secrets.token_urlsafe(32)

    authURL = "https://account.withings.com/oauth2_user/authorize2"

    params = {
        "response_type" : "code",
        "client_id" : clientID,
        "scope" : scope,
        "redirect_uri" : redirect_uri,
        "state" : state
    }

    authRequest = requests.Request(method="GET", url=authURL, params=params)
    authRequest = authRequest.prepare()

    return authRequest.url, state
