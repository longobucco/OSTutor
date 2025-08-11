import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer

COMPLETED_FILE = "completed.json"


class SimpleHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == "/completato":
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            try:
                data = json.loads(post_data.decode('utf-8'))
                nome = data.get("nome")
                if not nome:
                    self.send_response(400)
                    self._set_cors_headers()
                    self.end_headers()
                    self.wfile.write(b'Nome mancante')
                    return
                if os.path.exists(COMPLETED_FILE):
                    with open(COMPLETED_FILE, "r", encoding="utf-8") as f:
                        completati = json.load(f)
                else:
                    completati = {"completati": []}
                if nome not in completati["completati"]:
                    completati["completati"].append(nome)
                    with open(COMPLETED_FILE, "w", encoding="utf-8") as f:
                        json.dump(completati, f, indent=2, ensure_ascii=False)
                self.send_response(200)
                self._set_cors_headers()
                self.end_headers()
                self.wfile.write(b'OK')
            except Exception as e:
                self.send_response(500)
                self._set_cors_headers()
                self.end_headers()
                self.wfile.write(str(e).encode('utf-8'))
        elif self.path == "/rimuovi_completato":
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            try:
                data = json.loads(post_data.decode('utf-8'))
                nome = data.get("nome")
                if not nome:
                    self.send_response(400)
                    self._set_cors_headers()
                    self.end_headers()
                    self.wfile.write(b'Nome mancante')
                    return
                if os.path.exists(COMPLETED_FILE):
                    with open(COMPLETED_FILE, "r", encoding="utf-8") as f:
                        completati = json.load(f)
                else:
                    completati = {"completati": []}
                if nome in completati["completati"]:
                    completati["completati"].remove(nome)
                    with open(COMPLETED_FILE, "w", encoding="utf-8") as f:
                        json.dump(completati, f, indent=2, ensure_ascii=False)
                self.send_response(200)
                self._set_cors_headers()
                self.end_headers()
                self.wfile.write(b'OK')
            except Exception as e:
                self.send_response(500)
                self._set_cors_headers()
                self.end_headers()
                self.wfile.write(str(e).encode('utf-8'))
        else:
            self.send_response(404)
            self._set_cors_headers()
            self.end_headers()

    def do_GET(self):
        if self.path == "/completed.json":
            if os.path.exists(COMPLETED_FILE):
                with open(COMPLETED_FILE, "r", encoding="utf-8") as f:
                    data = f.read()
                self.send_response(200)
                self._set_cors_headers()
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(data.encode('utf-8'))
            else:
                self.send_response(200)
                self._set_cors_headers()
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(b'{"completati": []}')
        else:
            self.send_response(404)
            self._set_cors_headers()
            self.end_headers()


if __name__ == "__main__":
    server_address = ("", 8080)
    httpd = HTTPServer(server_address, SimpleHandler)
    print("Server avviato su http://localhost:8080 ...")
    httpd.serve_forever()
