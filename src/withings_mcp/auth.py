import os
import secrets

import requests
from dotenv import load_dotenv

#oauth flow state, vcode exchange and token refresh

load_dotenv()

clientID = os.getenv("clientID")
clientSecret = os.getenv("clientSecret")
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

def xChangeCode(authorization_code: str):
    url = "https://wbsapi.withings.net/v2/oauth2"

    data = {
          "action" : "requesttoken",
          "grant_type" : "authorization_code",
          "client_id" : clientID,
          "client_secret": clientSecret,
          "code": authorization_code,
          "redirect_uri" : redirect_uri
      }

    xChangeRes = requests.post(
        url,
        data=data,
        timeout=15,
    )

    xChangeRes.raise_for_status()

    payload = xChangeRes.json()
    body = payload.get("body")

    r_fields = {
        "userid",
        "access_token",
        "refresh_token",
        "expires_in",
        "token_type",
    }

    missing = r_fields - body.keys()

    if missing:
        raise RuntimeError(
            f"Token response missing {sorted(missing)}"
        )

    return body
