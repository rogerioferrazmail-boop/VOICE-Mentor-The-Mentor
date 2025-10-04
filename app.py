import streamlit as st

# Dados iniciais
mentores = ["Mentor 1", "Mentor 2", "Mentor 3", "Mentor 4", "Mentor 5", "Mentor 6"]
max_pessoas = 5

if 'reservas' not in st.session_state:
    st.session_state['reservas'] = {mentor: [] for mentor in mentores}

st.title("Sistema de Reservas de Sessões com Mentores")
st.write("Escolha um mentor e reserve sua vaga (máximo 5 pessoas por sessão)")

mentor_escolhido = st.selectbox("Escolha um mentor:", mentores)
nome = st.text_input("Digite seu nome:")

if st.button("Reservar"):
    if nome == "":
        st.warning("Por favor, digite seu nome.")
    elif len(st.session_state['reservas'][mentor_escolhido]) >= max_pessoas:
        st.error("Essa sessão já está cheia!")
    elif nome in st.session_state['reservas'][mentor_escolhido]:
        st.warning("Você já reservou essa sessão.")
    else:
        st.session_state['reservas'][mentor_escolhido].append(nome)
        st.success(f"Reserva confirmada para {mentor_escolhido}!")

st.subheader("Reservas atuais")
for mentor, participantes in st.session_state['reservas'].items():
    st.write(f"{mentor}: {participantes} ({len(participantes)}/{max_pessoas})")