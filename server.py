#!/usr/bin/env python3
"""
Simple HTTP server to serve the quiz locally
Run: python server.py
Then open: http://localhost:8000
"""

import http.server
import socketserver
import os
import sys

PORT = 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Aggiungi header CORS per evitare problemi di caricamento JSON
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

    def log_message(self, format, *args):
        # Log più leggibile
        print(f"[{self.log_date_time_string()}] {format % args}")

if __name__ == "__main__":
    # Cambia directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        print(f"✓ Server avviato su http://localhost:{PORT}")
        print(f"✓ Apri il browser e accedi a: http://localhost:{PORT}/Psicologia_test.html")
        print(f"✓ Premi Ctrl+C per stoppare il server")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n✓ Server fermato")
            sys.exit(0)
