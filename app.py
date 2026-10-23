import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Mural do Afeto - Doação de Itens de Higiene",
    page_icon="🌸",
    layout="wide"
)

# Estilização visual com alto contraste para leitura perfeita
st.markdown("""
    <style>
    /* Fundo da página em rosa claro com estampa de bolinhas */
    .stApp {
        background-color: #fff0f5;
        background-image: radial-gradient(#ffb6c1 15%, transparent 16%), radial-gradient(#ffc0cb 15%, transparent 16%);
        background-size: 60px 60px;
        background-position: 0 0, 30px 30px;
        color: #3d0012 !important;
    }

    /* Forçar cores de texto gerais no Streamlit com contorno de legibilidade */
    h1, h2, h3, h4, h5, h6, p, span, label, div {
        color: #3d0012 !important;
        text-shadow: 0.5px 0.5px 1px rgba(255, 255, 255, 0.9);
    }

    /* Estilo do Card / Cartinha com texto bem escuro e legível */
    .card {
        background: linear-gradient(135deg, #ffffff 0%, #fff0f5 100%);
        border-radius: 18px;
        padding: 22px;
        border: 2px dashed #ff4d6d;
        margin-bottom: 20px;
        box-shadow: 0px 4px 12px rgba(255, 182, 193, 0.5);
    }

    .card-title {
        color: #800f2f !important;
        font-weight: bold;
        font-size: 1.3rem;
        font-family: 'Comic Sans MS', cursive, sans-serif;
    }

    .card-text {
        color: #2b000d !important;
        font-style: italic;
        background: #ffe6eb;
        padding: 12px;
        border-radius: 10px;
        border-left: 5px solid #ff4d6d;
        font-size: 1.05rem;
        font-weight: 500;
    }

    .badge {
        background-color: #ff4d6d;
        color: #ffffff !important;
        padding: 6px 12px;
        border-radius: 12px;
        font-size: 0.95rem;
        font-weight: bold;
        text-shadow: none !important;
    }

    /* Banner fofo destacado */
    .banner-fofo {
        background: #ffffff;
        border-radius: 15px;
        padding: 15px;
        text-align: center;
        border: 2px solid #ff4d6d;
        color: #590d22 !important;
        font-weight: bold;
        font-size: 1.1rem;
        margin-bottom: 25px;
        box-shadow: 0px 2px 8px rgba(0,0,0,0.05);
    }

    /* Estilização dos botões */
    .stButton>button {
        background-color: #ff4d6d !important;
        color: white !important;
        border-radius: 20px !important;
        border: none !important;
        font-weight: bold !important;
        font-size: 1rem !important;
        text-shadow: none !important;
    }
    </style>
""", unsafe_allow_html=True)

# Estado inicial da aplicação (Vazio)
if 'pedidos' not in st.session_state:
    st.session_state.pedidos = []

# Cabeçalho Principal
st.markdown("<h1 style='text-align: center; color: #800f2f !important;'>🌸 🌺 Mural do Afeto & Solidariedade 🌺 🌸</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #590d22 !important; font-size: 1.15rem; font-weight: bold;'>Um cantinho seguro e cheio de amor para apoiar quem precisa de itens essenciais de higiene menstrual. ✨</p>", unsafe_allow_html=True)

# Mensagem fofa de boas-vindas
st.markdown("""
    <div class="banner-fofo">
        🌷 <i>"Pequenos gestos de carinho florescem em grandes sorrisos. Seja bem-vinda(o) ao nosso jardim de afeto!"</i> 🌷
    </div>
""", unsafe_allow_html=True)

# Contador / Métricas
total_pedidos = len(st.session_state.pedidos)
resgatados = sum(1 for p in st.session_state.pedidos if p['resgatado'])
pendentes = total_pedidos - resgatados

col_m1, col_m2, col_m3 = st.columns(3)
col_m1.metric("Total de Cartinhas 💌", total_pedidos)
col_m2.metric("Aguardando Amor 🌸", pendentes)
col_m3.metric("Pedidos Resgatados ❤️", resgatados)

st.write("---")

# Abas da interface
aba1, aba2 = st.tabs(["✉️ Adotar uma Cartinha", "➕ Escrever um Pedido"])

# --- ABA 1: MURAL DE CARTINHAS ---
with aba1:
    st.markdown("### 🌼 Cartinhas no Jardim")
    
    if total_pedidos == 0:
        st.info("🌸 O mural ainda está vazio. Seja a primeira pessoa a escrever uma cartinha na aba 'Escrever um Pedido'!")
    else:
        mostrar_resgatados = st.checkbox("Mostrar também cartinhas já adotadas com carinho 💕", value=False)
        
        grid_cols = st.columns(2)
        pedidos_exibidos = 0
        
        for i, pedido in enumerate(st.session_state.pedidos):
            if not mostrar_resgatados and pedido["resgatado"]:
                continue
                
            pedidos_exibidos += 1
            col = grid_cols[i % 2]
            
            with col:
                status_tag = "✅ Adotado com Amor!" if pedido["resgatado"] else "⏳ Aguardando Padrinho/Madrinha"
                
                st.markdown(f"""
                    <div class="card">
                        <div class="card-title">🌸 Cartinha de {pedido['nome']} ({pedido['idade']} anos)</div>
                        <small style="color: #590d22; font-weight: bold;">📍 {pedido['cidade']}</small><br><br>
                        <p class="card-text">"{pedido['historia']}"</p>
                        <hr style="border: 0.5px dashed #ff4d6d; margin: 10px 0;">
                        <b style="color: #3d0012;">📦 Necessidade:</b> <span class="badge">{pedido['item']}</span><br><br>
                        <small style="color: #3d0012;">Status: <b>{status_tag}</b></small>
                    </div>
                """, unsafe_allow_html=True)
                
                # Botão de Ação / Resgate
                if not pedido["resgatado"]:
                    with st.popover(f"🎁 Resgatar cartinha de {pedido['nome']}"):
                        st.write(f"💖 **Você está prestes a fazer o dia de {pedido['nome']} mais feliz!**")
                        st.write(f"Item necessário: **{pedido['item']}**")
                        
                        nome_doador = st.text_input("Seu nome ou apelido (opcional):", key=f"nome_{pedido['id']}")