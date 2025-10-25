from flask import Flask, render_template_string, send_from_directory, jsonify
import random

app = Flask(__name__)

FAKE_NEWS = [
    {"title": "Cientistas descobrem planeta feito de queijo", "body": "Astrônomos ainda investigam se é comestível."},
    {"title": "Governo anuncia proibição de computadores aos domingos", "body": "Medida visa incentivar lazer analógico."},
    {"title": "Nova rede social promete vida eterna digital", "body": "Usuários afirmam sentir saudades do tédio real."},
    {"title": "Aplicativo detecta mentiras com 99% de precisão", "body": "Mas falhou ao testar os próprios criadores."},
    {"title": "Pombo é flagrado usando chip 5G em praça pública", "body": "Teóricos dizem que é apenas o começo."}
]

HTML = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>ClimaEmFoco</title>
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"/>
<style>
body { margin:0; display:flex; height:100vh; font-family:Arial; background:#f5f5f5; }
#left { width:380px; background:white; padding:15px; box-shadow:2px 0 10px rgba(0,0,0,0.1); display:flex; flex-direction:column; height:100vh; overflow-y:auto;}
#fake { border:1px solid #ccc; border-radius:10px; padding:10px; margin-top:10px; background:#fff3f3; }
#map { flex:1; }
button { margin-top:10px; padding:8px; border:none; background:#333; color:white; border-radius:6px; cursor:pointer; }
.selected { margin-top:10px; font-size:14px; padding:8px; border:1px dashed #ccc; border-radius:6px; background:#fafafa; }
</style>
</head>
<body>
<div id="left">
  <h2>Notícias</h2>
  <div id="fake">
    <h3 id="title">{{news[0]['title']}}</h3>
    <p id="body">{{news[0]['body']}}</p>
  </div>
  <div id="fake">
    <h3 id="title">{{news[1]['title']}}</h3>
    <p id="body">{{news[1]['body']}}</p>
  </div>
  <div id="fake">
    <h3 id="title">{{news[2]['title']}}</h3>
    <p id="body">{{news[2]['body']}}</p>
  </div>
  <div id="fake">
    <h3 id="title">{{news[3]['title']}}</h3>
    <p id="body">{{news[3]['body']}}</p>
  </div>
  <!--button onclick="newFake()">Gerar nova notícia</button-->
  <div class="selected"><b>País selecionado:</b> <span id="country">Nenhum</span></div>
</div>
<div id="map"></div>

<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<script>
const fakeSamples = {{news | safe}};

// mapa
const map = L.map('map').setView([20, 0], 2);
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
  maxZoom: 6,
  attribution: '© OpenStreetMap'
}).addTo(map);

// carrega geojson local
fetch('/static/world.geo.json')
  .then(r => r.json())
  .then(data => {
    L.geoJSON(data, {
      style: {color:"#3b82f6", weight:1, fillColor:"#cce5ff", fillOpacity:0.6},
      onEachFeature: function (feature, layer) {
        const name = feature.properties.name;
        layer.on('click', function() {
          layer.bindPopup(name).openPopup();
          document.getElementById('country').textContent = name;
        });
      }
    }).addTo(map);
  });

// gera nova fake news
function newFake(){
  const sample = fakeSamples[Math.floor(Math.random()*fakeSamples.length)];
  document.getElementById('title').textContent = sample.title;
  document.getElementById('body').textContent = sample.body;
}
</script>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML, news=FAKE_NEWS)

if __name__ == "__main__":
    app.run(debug=True)
