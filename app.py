import streamlit as st
import requests

def buscar_link_musica(id):
    try:
      resposta = requests.get(f"http://127.0.0.1:5000/musicas/{id}")
    except:
       with area_video:
          st.warning("Serviço de vídeos fora do ar.")
       return None
    else:
      if resposta.status_code == 200:
          musica = resposta.json()
          return musica.get("link")
      return None
    
def listar_musicas():
    resposta = requests.get("http://127.0.0.1:5000/musicas")
    corpo_resposta = resposta.json()
    musicas = corpo_resposta.get("playlist")
    return musicas



# Configuração básica da página
st.set_page_config(page_title="Yfitops - Home", page_icon="🎵", layout="wide")

# ====== CSS SIMPLES (injetado direto aqui para ser 1 arquivo só) ======
CSS = """
:root{
  --bg: #0f1115;
  --panel: #161a22;
  --muted: #a6adbb;
  --text: #e7e9ee;
  --accent: #1dbf73;
  --accent-2: #1aa363;
}
html, body, .stApp {
  background-color: var(--bg) !important;
  color: var(--text) !important;
  font-family: system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial;
}

/* Barra do topo */
.topbar{
  display:flex; align-items:center; justify-content:space-between;
  padding:12px 16px; border-bottom:1px solid rgba(255,255,255,0.08);
  background: linear-gradient(180deg, #0f1115 0%, #0f111500 100%);
}
.topbar .brand{
  font-weight:800; font-size:22px; color:var(--accent); letter-spacing:.5px;
}

/* Botões */
.stButton>button{
  background: var(--accent); color:#06130c; border:none;
  border-radius:999px; padding:8px 16px; font-weight:700;
}
.stButton>button:hover{ background: var(--accent-2); }

/* Placeholder de vídeo */
.video-placeholder{
  width:100%; aspect-ratio:16/9; border-radius:12px;
  border:1px dashed rgba(255,255,255,0.25);
  display:grid; place-items:center; color:var(--muted); background:#12151c;
}

/* Espaçadores */
.spacer-8 {height:8px;}
.spacer-16 {height:16px;}
.spacer-24 {height:24px;}
"""
st.markdown(f"<style>{CSS}</style>", unsafe_allow_html=True)

# ====== TOPO: marca ======
st.markdown(
    """
    <div class="topbar">
        <img src="https://cdn-icons-png.flaticon.com/512/2111/2111624.png" height="50px">
        <div class="brand">Yfitops 🎶</div>
    </div>
    """,
    unsafe_allow_html=True
)
# # ====== VÍDEO (PLACEHOLDER) ======




st.subheader("🎬 Vídeo em destaque")
st.info("Espaço reservado para um vídeo. No futuro use: st.video('URL do YouTube ou arquivo')")

area_video = st.container()


# ====== LISTA DE MÚSICAS (FUTURA API) ======
musicas = listar_musicas()
for musica in musicas:
   st.markdown(f"{musica.get("titulo")} ☞ {musica.get("artista")}", unsafe_allow_html=True)
   if st.button(f"{musica.get('titulo')}",musica["id"]):
      with area_video:
         st.video(musica["link"])
   
