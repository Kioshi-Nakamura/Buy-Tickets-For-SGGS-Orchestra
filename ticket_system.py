import http.server
import socketserver
from urllib.parse import parse_qs

# Logik tiket berdasarkan kategori
def calculate_ticket_price(category):
    if category == "Pelajar SGGS":
        return 12.00
    elif category == "Guru SGGS":
        return 14.00
    elif category == "Orang Awam (Bawah 12 tahun)":
        return 5.50
    elif category == "Orang Awam (13 hingga 50 tahun)":
        return 20.00
    elif category == "Orang Awam (51 tahun dan ke atas)":
        return 15.00
    return 0.0

# HTML dan CSS untuk laman web
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ms">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sistem Tiket Konsert Orkestra SGGS</title>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Playfair Display', serif;
            background-color: #0F0000;
            color: white;
            margin: 0;
            padding: 0;
        }

        header {
            background-color: #440000;
            padding: 20px;
            text-align: center;
        }

        h1 {
            font-size: 3em;
            color: #F4B3B3;
            margin: 0;
        }

        .container {
            background-color: #002028;
            padding: 20px;
            margin: 20px;
            border-radius: 10px;
        }

        .form-group {
            margin-bottom: 15px;
        }

        label, select {
            font-size: 1.2em;
        }

        select {
            padding: 5px;
            font-size: 1em;
            background-color: #6E1313;
            color: white;
            border: none;
            border-radius: 5px;
            width: 100%;
        }

        button {
            background-color: #6E1313;
            color: white;
            padding: 10px 20px;
            font-size: 1.2em;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }

        button:hover {
            background-color: #F4B3B3;
        }

        .result {
            margin-top: 20px;
            background-color: #440000;
            padding: 15px;
            border-radius: 10px;
            font-size: 1.2em;
        }

        .footer {
            margin-top: 40px;
            background-color: #440000;
            padding: 10px;
            text-align: center;
        }
    </style>
</head>
<body>

<header>
    <h1>Sistem Tiket Konsert Orkestra SGGS</h1>
</header>

<div class="container">
    <h2>Tambah Tiket</h2>
    <form method="GET">
        <div class="form-group">
            <label for="category">Pilih Kategori:</label>
            <select name="category" id="category" required>
                <option value="Pelajar SGGS">Pelajar SGGS - RM12.00</option>
                <option value="Guru SGGS">Guru SGGS - RM14.00</option>
                <option value="Orang Awam (Bawah 12 tahun)">Orang Awam (Bawah 12 tahun) - RM5.50</option>
                <option value="Orang Awam (13 hingga 50 tahun)">Orang Awam (13 hingga 50 tahun) - RM20.00</option>
                <option value="Orang Awam (51 tahun dan ke atas)">Orang Awam (51 tahun dan ke atas) - RM15.00</option>
            </select>
        </div>
        <button type="submit">Tambah Tiket</button>
    </form>

    <h3>Jumlah Tiket: RM{}</h3>

    <form method="GET">
        <div class="form-group">
            <button type="submit" name="clear" value="true">Tutup dan Papar Jumlah</button>
        </div>
    </form>
</div>

<div class="footer">
    <p>&copy; 2024 Sistem Tiket Konsert Orkestra SGGS</p>
</div>

</body>
</html>
"""

# Pengendali untuk permintaan HTTP
class RequestHandler(http.server.BaseHTTPRequestHandler):
    total_price = 0.0
    
    def do_GET(self):
        # Parse parameter dari URL
        query = parse_qs(self.path[2:])
        category = query.get("category", [None])[0]
        clear = query.get("clear", [None])[0]

        if category:
            self.total_price += calculate_ticket_price(category)

        if clear:
            self.total_price = 0.0
        
        # Menyediakan respons dengan HTML
        html_content = HTML_TEMPLATE.format(self.total_price)
        
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(html_content.encode("utf-8"))

# Fungsi utama untuk menjalankan server
def run(server_class=http.server.HTTPServer, handler_class=RequestHandler):
    port = 8080
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Server berjalan di http://localhost:{port}")
    httpd.serve_forever()

# Mulakan server
if __name__ == "__main__":
    run()
