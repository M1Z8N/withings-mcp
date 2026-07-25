from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

class tripleTLovesMe(BaseHTTPRequestHandler):
    result = None

    def do_GET(self) -> None:
        parsed_path = urlparse(self.path)

        # make sure its callback not like anything else
        if parsed_path.path != "/callback":
            self.send_error(404)
            return

        query_params = parse_qs(parsed_path.query)

        code_value = query_params.get("code")
        state_value = query_params.get("state")

        if not code_value or not state_value:
            print("yo... bruh ur missing code or state :(")
            return

        code = code_value[0]
        returned_state = state_value[0]

        type(self).result = {
            "code": code,
            "state": returned_state
        }
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(b"Authorization Received. You can close this tab lil bro.")
