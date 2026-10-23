import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Mural do Afeto - Doação de Itens de Higiene",
    page_icon="🌸",
    layout="wide"
)

# Estilização visual: Fundo magnólia/rosa suave e letras bem legíveis
st.markdown("""
    <style>
    /* Fundo suave em tom rosa magnólia / rosa sólido claro */
    .stApp {
        background-color: #fbf0f5 !important;
        color: #3d0012 !important;
    }

    /* Cores de texto gerais */
    h1, h2, h3, h4, h5, h6, p, span, label, div {
        color: #3d0012 !important;
    }

    /* Estilo do Card / Cartinha */
    .card {
        background: #ffffff;
        border-radius: 18px;
        padding: 22px;
        border: 2px solid #ffb3c1;
        margin-bottom: 20px;
        box-shadow: 0px 4px 12px rgba(230, 180, 200, 0.3);
    }

    .card-title {
        color: #800f2f !important;
        font-weight: bold;
        font-size: 1.25rem;
    }

    .card-text {
        color: #2b000d !important;
        background: #fff0f5;
        padding: 12px;
        border-radius: 10px;
        border-left: 4px solid #ff4d6d;
        font-size: 1.05rem;
    }

    .badge {
        background-color: #ff4d6d;
        color: #ffffff !important;
        padding: 6px 12px;
        border-radius: 12px;
        font-size: 0.95rem;
        font-weight: bold;
    }

    /* Banner de mensagens fofas */
    .banner-fofo {
        background: #ffffff;
        border-radius: 15px;
        padding: 15px;
        text-align: center;
        border: 2px solid #ffb3c1;
        color: #590d22 !important;
        font-weight: bold;
        font-size: 1.05rem;
        margin-bottom: 25px;
    }

    /* Estilização dos botões */
    .stButton>button {
        background-color: #ff4d6d !important;
        color: white !important;
        border-radius: 20px !important;
        border: none !important;
        font-weight: bold !important;
        font-size: 1rem !important;
    }
    </style>
""", unsafe_allow_html=True)

# Estado inicial da aplicação (Vazio)
if 'pedidos' not in st.session_state:
    st.session_state.pedidos = []

# Cabeçalho Principal (Sem as flores verdes)
st.markdown("<h1 style='text-align: center; color: #800f2f !important;'>Mural do Afeto & Solidariedade</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #590d22 !important; font-size: 1.15rem; font-weight: bold;'>Um cantinho seguro e cheio de amor para apoiar quem precisa de itens essenciais de higiene menstrual. ✨</p>", unsafe_allow_html=True)

# Mensagem fofa
st.markdown("""
    <div class="banner-fofo">
        <i>"Pequenos gestos de carinho florescem em grandes sorrisos. Seja bem-vinda(o) ao nosso jardim de afeto!"</i>
    </div>
""", unsafe_allow_html=True)

# Métricas e Contadores dinâmicos
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
    st.markdown("### Cartinhas no Mural")
    
    if total_pedidos == 0:
        st.info("O mural ainda está vazio. Seja a primeira pessoa a escrever uma cartinha na aba 'Escrever um Pedido'!")
    else:
        mostrar_resgatados = st.checkbox("Mostrar também cartinhas já resgatadas 💕", value=False)
        
        grid_cols = st.columns(2)
        pedidos_exibidos = 0
        
        for i, pedido in enumerate(st.session_state.pedidos):
            if not mostrar_resgatados and pedido["resgatado"]:
                continue
                
            pedidos_exibidos += 1
            col = grid_cols[i % 2]
            
            with col:
                status_tag = "✅ Resgatado com Amor!" if pedido["resgatado"] else "⏳ Aguardando Resgate"
                
                serie_info = f" • {pedido['serie']}" if pedido.get('serie') else ""
                
                st.markdown(f"""
                    <div class="card">
                        <div class="card-title">Cartinha de {pedido['nome']} ({pedido['idade']} anos{serie_info})</div>
                        <small style="color: #590d22; font-weight: bold;">📍 {pedido['cidade']}</small><br><br>
                        <p class="card-text">"{pedido['historia']}"</p>
                        <hr style="border: 0.5px dashed #ffb3c1; margin: 10px 0;">
                        <b style="color: #3d0012;">📦 Item necessário:</b> <span class="badge">{pedido['item']}</span><br><br>
                        <small style="color: #3d0012;">Status: <b>{status_tag}</b></small>
                    </div>
                """, unsafe_allow_html=True)
                
                # Botão para responder / marcar como resgatado
                if not pedido["resgatado"]:
                    with st.popover(f"🎁 Resgatar pedido de {pedido['nome']}"):
                        st.write(f"💖 **Você vai ajudar {pedido['nome']}!**")
                        st.write(f"Item necessário: **{pedido['item']}**")
                        
                        nome_doador = st.text_input("Seu nome ou apelido (opcional):", key=f"nome_{pedido['id']}")
                        
                        if st.button("Marcar pedido como resgatado ❤️", key=f"btn_{pedido['id']}"):
                            doador = nome_doador.strip() if nome_doador.strip() else "Anônimo(a)"
                            pedido["resgatado"] = True
                            pedido["padrinho"] = doador
                            st.success(f"Pedido marcado como resgatado por {doador}! Obrigado por ajudar! 💕")
                            st.rerun()
                else:
                    st.info(f"Pedido resgatado por: **{pedido['padrinho']}** 💖")
                
                st.markdown("<br>", unsafe_allow_html=True)
        
        if pedidos_exibidos == 0 and not mostrar_resgatados:
            st.success("Todas as cartinhas atuais já foram resgatadas! 💕 Marque a opção acima para visualizá-las.")

# --- ABA 2: ADICIONAR NOVO PEDIDO ---
with aba2:
    st.markdown("### 📝 Escrever uma nova Cartinha")
    st.write("Sinta-se acolhida(o). Preencha os dados abaixo para publicar seu pedido no mural.")
    
    with st.form("form_novo_pedido"):
        nome = st.text_input("Seu Nome ou Iniciais:")
        col_f1, col_f2 = st.columns(2)
        with col_f1:
            idade = st.number_input("Sua Idade:", min_value=10, max_value=100, value=15)
        with col_f2:
            serie = st.text_input("Qual série/ano você cursa?", placeholder="Ex: 3ª série / 3º ano")
            
        cidade = st.text_input("Sua Cidade / Estado:", value="Minaçu - GO")
        item = st.text_input("Qual item ou kit de higiene você precisa?", placeholder="Ex: 2 Pacotes de absorventes com abas + Sabonete neutro")
        historia = st.text_area("Escreva seu pedido / mensagem:", placeholder="Conta um pouquinho do seu pedido... Lembre-se: este é um espaço seguro e sem julgamentos! 💕")
        
        submitted = st.form_submit_button("Enviar Cartinha ao Mural 💌")
        
        if submitted:
            if nome and item and historia:
                novo_id = len(st.session_state.pedidos) + 1
                st.session_state.pedidos.append({
                    "id": novo_id,
                    "nome": nome,
                    "idade": idade,
                    "serie": serie,
                    "cidade": cidade,
                    "item": item,
                    "historia": historia,
                    "resgatado": False,
                    "padrinho": None
                })
                st.success("Sua cartinha foi enviada ao mural com sucesso! ✨")
                st.rerun()
            else:
                st.error("Por favor, preencha o nome, o item necessário e a mensagem para enviar seu pedido.")
