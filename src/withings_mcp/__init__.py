from withings_mcp.auth import authAttempt
import webbrowser
import threading
from queue import Queue

from withings_mcp.callback import wait_for_callback
from withings_mcp.auth import authAttempt

def main() -> None:
    authorizationURL, expectedState = authAttempt()

    callback_res = Queue()

    def Isreal():
        result = wait_for_callback()
        callback_res.put(result)

    IThread = threading.Thread(
        target=Isreal,
        daemon=True,
    )

    IThread.start()

    webbrowser.open(str(authorizationURL))

    callback_res = callback_res.get()

    returned_state = callback_res["state"]
    authorization_code = callback_res["code"]

    if returned_state != expectedState:
        raise RuntimeError("Oauth didn't match! HACKER!")

    print("Authorization Code Receivde: ", bool(authorization_code))
    print("OAuth State Matched: ",True)
