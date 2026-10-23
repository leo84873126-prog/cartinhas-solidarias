import streamlit as st
import json
import os

# Configuração da página
st.set_page_config(
    page_title="Mural do Afeto - Doação de Itens de Higiene",
    page_icon="🌸",
    layout="wide"
)

# Arquivo JSON para salvar os pedidos para TODOS os usuários (compartilhado)
DATA_FILE = "pedidos.json"

def carregar_pedidos():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return []
    return []

def salvar_pedidos(pedidos):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(pedidos, f, ensure_ascii=False, indent=4)

# Estilização visual no estilo Papelaria Fofa (Grid, Gradiente Rosa/Roxo)
st.markdown("""
    <style>
    /* Fundo degradê rosa/roxo suave com estampa de papel quadriculado */
    .stApp {
        background-color: #fce4ec !important;
        background-image: 
            linear-gradient(135deg, rgba(255, 230, 242, 0.85) 0%, rgba(243, 229, 245, 0.85) 100%),
            linear-gradient(to right, rgba(240, 180, 210, 0.2) 1px, transparent 1px),
            linear-gradient(to bottom, rgba(240, 180, 210, 0.2) 1px, transparent 1px) !important;
        background-size: 100% 100%, 24px 24px, 24px 24px !important;
        color: #3d0012 !important;
    }

    /* Cores de texto gerais */
    h1, h2, h3, h4, h5, h6, p, span, label, div {
        color: #3d0012 !important;
    }

    /* Campos de texto e números com fundo branco e borda suave */
    input, textarea, div[data-baseweb="input"] div, div[data-baseweb="base-input"] {
        background-color: #ffffff !important;
        color: #3d0012 !important;
        -webkit-text-fill-color: #3d0012 !important;
    }

    input, textarea {
        border: 2px solid #f8bbd0 !important;
        border-radius: 12px !important;
    }

    /* Estilo do Card / Cartinha estilo papelaria/adesivo */
    .card {
        background: #ffffff;
        border-radius: 20px;
        padding: 24px;
        border: 2px solid #f48fb1;
        margin-bottom: 20px;
        box-shadow: 0px 6px 16px rgba(206, 147, 216, 0.25);
        position: relative;
        overflow: hidden;
    }

    /* Detalhe floral decorativo no canto das cartinhas */
    .card::before {
        content: "🌸";
        position: absolute;
        top: 10px;
        right: 15px;
        font-size: 1.5rem;
        opacity: 0.8;
    }

    .card-title {
        color: #7b1fa2 !important;
        font-weight: bold;
        font-size: 1.25rem;
    }

    .card-text {
        color: #2b000d !important;
        background: #fdf0f7;
        padding: 12px;
        border-radius: 12px;
        border-left: 4px solid #ab47bc;
        font-size: 1.05rem;
    }

    .badge {
        background-color: #ec407a;
        color: #ffffff !important;
        padding: 6px 14px;
        border-radius: 15px;
        font-size: 0.95rem;
        font-weight: bold;
    }

    /* Banner fofo de cabeçalho estilo sticker de papel */
    .banner-fofo {
        background: #ffffff;
        border-radius: 18px;
        padding: 16px;
        text-align: center;
        border: 2px dashed #ce93d8;
        color: #6a1b9a !important;
        font-weight: bold;
        font-size: 1.1rem;
        margin-bottom: 25px;
        box-shadow: 0px 4px 10px rgba(225, 190, 231, 0.4);
    }

    /* Caixa do Popover (Janela de Resgate) */
    div[data-testid="stPopoverBody"] {
        background-color: #ffffff !important;
        border: 2px solid #ab47bc !important;
        border-radius: 18px !important;
        box-shadow: 0px 6px 20px rgba(0,0,0,0.12) !important;
    }

    div[data-testid="stPopoverBody"] * {
        color: #3d0012 !important;
    }

    /* Estilização dos botões (Tom Rosa/Roxo fofo) */
    .stButton>button, div.stFormSubmitButton > button, [data-testid="stPopover"] button {
        background: linear-gradient(135deg, #ec407a 0%, #ab47bc 100%) !important;
        color: #ffffff !important;
        -webkit-text-fill-color: #ffffff !important;
        border-radius: 22px !important;
        border: none !important;
        font-weight: bold !important;
        font-size: 1rem !important;
        box-shadow: 0px 3px 8px rgba(171, 71, 188, 0.3) !important;
    }
    </style>
""", unsafe_allow_html=True)

# Carrega os pedidos salvos no servidor para todos verem igual
if 'pedidos' not in st.session_state:
    st.session_state.pedidos = carregar_pedidos()

# Cabeçalho Principal
st.markdown("""
    <div style="text-align: center; padding: 10px 0;">
        <h1 style="color: #6a1b9a !important; font-size: 2.3rem;">🌸✨ Mural do Afeto & Solidariedade ✨🌸</h1>
        <p style="color: #4a148c !important; font-size: 1.15rem; font-weight: 600;">
            Um cantinho seguro, acolhedor e cheio de carinho para apoiar quem precisa de itens de higiene menstrual. 🎀
        </p>
    </div>
""", unsafe_allow_html=True)

# Mensagem fofa
st.markdown("""
    <div class="banner-fofo">
        🌷 <i>"Pequenos gestos de carinho florescem em grandes sorrisos. Seja bem-vinda(o) ao nosso jardim de afeto!"</i> 🌷
    </div>
""", unsafe_allow_html=True)

# Métricas e Contadores dinâmicos compartilhados
total_pedidos = len(st.session_state.pedidos)
resgatados = sum(1 for p in st.session_state.pedidos if p.get('resgatado', False))
pendentes = total_pedidos - resgatados

col_m1, col_m2, col_m3 = st.columns(3)
col_m1.metric("Total de Cartinhas 💌", total_pedidos)
col_m2.metric("Aguardando Amor 🌸", pendentes)
col_m3.metric("Pedidos Resgatados ❤️", resgatados)

st.write("---")

# Abas da interface
aba1, aba2 = st.tabs(["🌸 Adotar uma Cartinha", "🌷 Escrever um Pedido"])

# --- ABA 1: MURAL DE CARTINHAS ---
with aba1:
    st.markdown("### 🌼 Cartinhas no Mural")
    st.write("Clique abaixo para filtrar e ver as cartinhas enviadas:")
    
    filtro_visualizacao = st.radio(
        "Exibir cartinhas:",
        ["💌 Ver Todas as Cartinhas", "🌸 Aguardando Amor (Pendentes)", "❤️ Pedidos Resgatados"],
        horizontal=True
    )
    
    st.write("")
    
    if total_pedidos == 0:
        st.info("🌸 O mural ainda está vazio. Seja a primeira pessoa a escrever uma cartinha na aba 'Escrever um Pedido'!")
    else:
        grid_cols = st.columns(2)
        pedidos_exibidos = 0
        
        for i, pedido in enumerate(st.session_state.pedidos):
            is_resgatado = pedido.get("resgatado", False)
            
            if "Aguardando" in filtro_visualizacao and is_resgatado:
                continue
            if "Resgatados" in filtro_visualizacao and not is_resgatado:
                continue
                
            pedidos_exibidos += 1
            col = grid_cols[pedidos_exibidos % 2]
            
            with col:
                status_tag = "✅ Resgatado com Amor!" if is_resgatado else "⏳ Aguardando Resgate"
                serie_info = f" • {pedido['serie']}" if pedido.get('serie') else ""
                
                # Montagem segura do HTML da cartinha
                card_html = (
                    f"<div class=\"card\">"
                    f"<div class=\"card-title\">🌸 Cartinha de {pedido['nome']} ({pedido['idade']} anos{serie_info})</div>"
                    f"<small style=\"color: #6a1b9a; font-weight: bold;\">📍 {pedido['cidade']}</small><br><br>"
                    f"<p class=\"card-text\">\"{pedido['historia']}\"</p>"
                    f"<hr style=\"border: 0.5px dashed #ce93d8; margin: 10px 0;\">"
                    f"<b style=\"color: #3d0012;\">📦 Item necessário:</b> <span class=\"badge\">{pedido['item']}</span><br><br>"
                    f"<small style=\"color: #3d0012;\">Status: <b>{status_tag}</b></small>"
                    f"</div>"
                )
                st.markdown(card_html, unsafe_allow_html=True)
                
                # Botão para marcar como resgatado
                if not is_resgatado:
                    with st.popover(f"🎁 Resgatar pedido de {pedido['nome']}"):
                        st.write(f"💖 **Você vai ajudar {pedido['nome']}!**")
                        st.write(f"Item necessário: **{pedido['item']}**")
                        
                        nome_doador = st.text_input("Seu nome ou apelido (opcional):", key=f"nome_{pedido['id']}")
                        
                        if st.button("Marcar pedido como resgatado ❤️", key=f"btn_{pedido['id']}"):
                            doador = nome_doador.strip() if nome_doador.strip() else "Anônimo(a)"
                            pedido["resgatado"] = True
                            pedido["padrinho"] = doador
                            salvar_pedidos(st.session_state.pedidos)
                            st.success(f"Pedido marcado como resgatado por {doador}! Obrigado por ajudar! 💕")
                            st.rerun()
                else:
                    st.info(f"Pedido resgatado por: **{pedido.get('padrinho', 'Anônimo')}** 💖")
                
                # Botão para excluir cartinha
                if st.button("🗑️ Excluir Cartinha", key=f"del_{pedido['id']}"):
                    st.session_state.pedidos = [p for p in st.session_state.pedidos if p['id'] != pedido['id']]
                    salvar_pedidos(st.session_state.pedidos)
                    st.success("Cartinha excluída com sucesso! 🌸")
                    st.rerun()
                
                st.markdown("<br>", unsafe_allow_html=True)
        
        if pedidos_exibidos == 0:
            st.info("Nenhuma cartinha encontrada para este filtro no momento. 💕")

# --- ABA 2: ADICIONAR NOVO PEDIDO ---
with aba2:
    st.markdown("### 📝 Escrever uma nova Cartinha 🌹")
    st.write("Sinta-se acolhida(o). Preencha os dados abaixo para publicar seu pedido no mural para todos.")
    
    with st.form("form_novo_pedido"):
        nome = st.text_input("Seu Nome ou Iniciais:")
        col_f1, col_f2 = st.columns(2)
        with col
