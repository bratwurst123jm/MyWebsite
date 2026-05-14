"""
Modern Template — Python HTTP Server
Serves the enhanced Link-in-Bio template locally.
"""

from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

HOST = "0.0.0.0"
PORT = 27000
BASE_DIR = Path(__file__).resolve().parent
PUBLIC_URL = f"http://localhost:{PORT}"


class ReusableThreadingHTTPServer(ThreadingHTTPServer):
    allow_reuse_address = True


def main() -> None:
    handler = partial(SimpleHTTPRequestHandler, directory=str(BASE_DIR))
    server = ReusableThreadingHTTPServer((HOST, PORT), handler)
    print(f"🚀 Modern Template Server running on {PUBLIC_URL}")
    print(f"   Öffne {PUBLIC_URL} im Browser")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 Server stopped.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
