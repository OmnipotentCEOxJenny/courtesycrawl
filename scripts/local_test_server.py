# Local test server for CourtesyCrawl: robots.txt with Disallow /private and Crawl-delay 1;
# first request (and /always429) answers 429 with Retry-After: 1. Run: python local_test_server.py
import http.server
n={'c':0}
class H(http.server.BaseHTTPRequestHandler):
    def do_GET(s):
        if s.path=='/robots.txt':
            s.send_response(200);s.end_headers();s.wfile.write(b"User-agent: *\nDisallow: /private\nCrawl-delay: 1\n");return
        n['c']+=1
        if s.path=='/always429' or n['c']==1:
            s.send_response(429);s.send_header('Retry-After','1');s.end_headers();return
        s.send_response(200);s.end_headers();s.wfile.write(b'hello')
    def log_message(s,*a):pass
http.server.HTTPServer(('127.0.0.1',8765),H).serve_forever()
