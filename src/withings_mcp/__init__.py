from withings_mcp.auth import authAttempt
import webbrowser

def main() -> None:
    authorizationURL, expectedState = authAttempt()

    print("Hello from withings-mcp!")

    webbrowser.open(str(authorizationURL))
