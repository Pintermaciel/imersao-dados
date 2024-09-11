import datetime
import streamlit as st

import model

def main():
    st.title("Sistema de CRM e Vendas - ZapFlow")
    email = st.text_input("Digite seu email")
    data =st.date_input("Data da venda")
    hora =st.time_input("Hora da venda")
    valor =st.number_input("Valor da venda")
    quantidade =st.number_input("Quantidade vendida")
    produto = st.selectbox(
        "Produto:",
        [
            "ZapFlow - Gemini",
            "ZapFlow - chatGPT",
            "zapFlow - Lhama",
        ]
        )

    if st.button("Finalizar"):

        data_hora = datetime.datetime.combine(data, hora)
        st.write("Email: ", email)
        st.write("Data: ", data_hora)
        st.write("Valor: ", valor)
        st.write("Quantidade: ", quantidade)
        st.write("Produto: ", produto)


if __name__ == "__main__":
    main()