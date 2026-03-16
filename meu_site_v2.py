import streamlit as st

# 1. Configuração da Página
st.set_page_config(page_title="João Marcos | Portfolio Profissional", layout="wide")

# 2. Estilização Master
st.markdown("""
    <style>
    .stApp { background-color: #050a12; }
    .main-title { color: #ffffff; font-size: 3.5rem !important; font-weight: 800; margin-bottom: 0px; }
    .subtitle { color: #00d4ff; font-size: 1.6rem; font-weight: 400; margin-bottom: 30px; }
    .section-title { color: #00d4ff; border-left: 4px solid #00d4ff; padding-left: 15px; margin-top: 30px; margin-bottom: 20px; font-size: 1.8rem; }
    p, li { color: #b0bccb; font-size: 1.25rem; line-height: 1.8; text-align: justify; }
    .project-card { 
        background-color: #0e1621; 
        padding: 30px; 
        border-radius: 20px; 
        border: 1px solid #1d2939; 
    }
    </style>
    """, unsafe_allow_html=True)

# --- BARRA LATERAL ---
st.sidebar.markdown("### Contato Profissional")
st.sidebar.write("📧 [jmarcos.fbarros@gmail.com](mailto:jmarcos.fbarros@gmail.com)")
st.sidebar.write("🔗 [LinkedIn](https://www.linkedin.com/in/joão-marcos-347311230)")

# --- CABEÇALHO ---
st.markdown('<h1 class="main-title">João Marcos Fonseca</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Analista de Dados Orientado a Negócios</p>', unsafe_allow_html=True)

st.write("""
Estrategista de dados focado em transformar fluxos complexos em ativos de decisão. 
Especialista em unir a precisão técnica do código (Python/SQL) com a agressividade comercial 
necessária para blindar margens de contribuição e otimizar operações de larga escala.
""")

st.divider()

# --- ESTRUTURA PRINCIPAL ---
col_main, col_spacer, col_sidebar = st.columns([2, 0.1, 1])

with col_main:
    st.markdown('<h2 class="section-title">Sobre Minha Atuação</h2>', unsafe_allow_html=True)
    st.write("""
    Minha trajetória é consolidada na ponte entre a operação real e a inteligência de dados. Com um background robusto no setor de refrigeração e serviços, aprendi que a tecnologia deve servir ao lucro, e não o contrário.

Hoje, atuo como um tradutor: converto fluxos complexos de informação e bancos de dados subutilizados em ecossistemas de Business Intelligence. Minha visão de dono me permite identificar onde o dinheiro está 'vazando' e como a arquitetura de dados pode ser escalável para suportar decisões que impactam diretamente o faturamento e a saúde financeira da empresa.
    """)
    
    st.markdown('<h2 class="section-title">Como eu trabalho</h2>', unsafe_allow_html=True)
    st.write("""
    Minha metodologia foca na entrega de clareza absoluta sobre os indicadores que realmente movem o ponteiro do negócio:

Ciclo Financeiro & CCL (Capital de Giro): Análise detalhada do Ciclo Financeiro e da Necessidade de Capital de Giro (NCG), garantindo que o faturamento se transforme em caixa real e não fique preso em estoques ou prazos de recebimento ineficientes.

Fluxo de Caixa & EBITDA: Monitoramento em tempo real da geração de caixa operacional. Estruturo visões que permitem ao gestor antecipar cenários e medir a lucratividade antes de juros, impostos, depreciação e amortização.

Margem de Contribuição e Lucro Líquido: Diferenciação clara entre faturamento bruto e margem real por unidade de negócio, identificando quais serviços ou produtos estão drenando a rentabilidade da operação.

Engenharia de Dados & ETL: Automação de pipelines via Python e SQL para que o dado chegue limpo e confiável, eliminando erros manuais e garantindo integridade para o suporte à decisão executiva.
    """)

with col_sidebar:
    st.markdown('<div class="project-card">', unsafe_allow_html=True)
    st.markdown('<h3 style="color:#ffffff; margin-top:0;">📂 Portfólio de Soluções</h3>', unsafe_allow_html=True)
    st.write("Selecione para explorar o detalhamento:")
    
    if st.button("📈 Performance Comercial (R$ 53M)", use_container_width=True):
        st.session_state.projeto_atual = "53M"
    
    if st.button("⚡ Smart Grid: Eletromobilidade", use_container_width=True):
        st.session_state.projeto_atual = "SmartGrid"
        
    if st.button("❄️ FrostTech: Inteligência em Refrigeração", use_container_width=True):
        st.session_state.projeto_atual = "Refri"
        
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# --- SEÇÃO DE DETALHAMENTO ÚNICA ---
if 'projeto_atual' in st.session_state:
    if st.session_state.projeto_atual == "53M":
        st.markdown('<h2 class="section-title">Case: Inteligência Comercial Nacional (> R$ 53 Mi)</h2>', unsafe_allow_html=True)
        img_col1, img_col2 = st.columns(2)
        with img_col1:
            st.image("projeto_comercial.png", caption="Visão Executiva de Rentabilidade", use_container_width=True)
        with img_col2:
            st.image("comercial_2.png", caption="Análise Detalhada de Break-even point", use_container_width=True)
        st.write("""
        * **Engenharia:** Scripts em Python para carga massiva de dados e modelagem relacional no Supabase.
        * **Business Intelligence:** Utilização de DAX avançado para cálculo de margem líquida real.
        * **Impacto:** Identificação de falhas de escala e custos ocultos que afetavam o EBITDA.
        """)
        
    elif st.session_state.projeto_atual == "SmartGrid":
        st.markdown('<h2 class="section-title">Case: Monitoramento de Smart Grid - Metro City</h2>', unsafe_allow_html=True)
        st.image("eletro_.png", use_container_width=True)
        st.write("""
        ### ⚡ A cidade tem 45 milhões de kWh consumidos. A rede aguenta?
        Fui atrás do problema escondido na infraestrutura de eletropostos.
        **O que os dados revelaram:** O gargalo não é volume — é gestão de demanda. O carregamento *Fast* gera proporcionalmente mais risco de sobrecarga (246 ocorrências críticas).
        **Conclusão Estratégica:** A solução real é a precificação dinâmica e incentivo ao carregamento fora de pico.
        """)

    elif st.session_state.projeto_atual == "Refri":
        st.markdown('<h2 class="section-title">Case: FrostTech - Inteligência Financeira e Otimização de Lucro</h2>', unsafe_allow_html=True)
        st.image("refri_ana.png", use_container_width=True)
        st.write("""
        ### De dados brutos a decisões estratégicas
        Como utilizei SQL, Python e Power BI para maximizar a rentabilidade de uma operação de refrigeração.
        
        **🎯 O Problema de Negócio:**
        Muitas empresas de serviços faturam alto, mas não sabem para onde o dinheiro está indo. O objetivo deste projeto foi auditar uma operação de manutenção de refrigeração para identificar gargalos de custos, produtos subfaturados e o real impacto das garantias no lucro líquido.
        
        **Tecnologias Utilizadas:** SQL para extração, Python para tratamento e Power BI para a visualização dos insights estratégicos.
        """)
else:
    st.markdown('<p style="text-align:center; opacity:0.5;">Selecione um projeto ao lado para visualizar os resultados.</p>', unsafe_allow_html=True)