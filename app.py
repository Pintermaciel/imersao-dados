import datetime
import streamlit as st
from pydantic import ValidationError

from model import Vendas

def main():
    st.title("Sistema de CRM e Vendas - ZapFlow")
    email = st.text_input("Digite seu email")
    data =st.date_input("Data da venda")
    hora =st.time_input("Hora da venda")
    valor =st.number_input("Valor da venda")
    quantidade =st.number_input(
        "Quantidade vendida",
        min_value=1,)
    produto = st.selectbox(
        "Produto:",
        [
            "ZapFlow - Gemini",
            "ZapFlow - chatGPT",
            "zapFlow - Lhama",
        ]
        )

    if st.button("Finalizar"):
        try:
            
            data_hora = datetime.datetime.combine(data, hora)
            venda = Vendas(
            email=email,
            data=data_hora,
            valor=valor,
            quantidade=quantidade,
            produto=produto
            )
            st.write(venda)
        except ValidationError as e:
            st.error(
                f"Por favor, preencha todos os campos corretamente {e}"
                )


if __name__ == "__main__":
    main()