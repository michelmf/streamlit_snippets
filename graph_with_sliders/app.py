"""
Playing with multiple sliders.
"""
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def main():
    df = px.data.iris()
    st.title("Soma dos Sliders")

    # Crie 3 colunas com um slider em cada uma
    col1, col2, col3 = st.columns(3)

    with col1:
        slider1 = st.slider("Head Main B 1st Stage Compressor", min_value=0, max_value=5, value=0, step=1)
    with col2:
        slider2 = st.slider("Head Main B 2nd Stage Compressor", min_value=0, max_value=5, value=0, step=1)
    with col3:
        slider3 = st.slider("Head Reinjection Compressor", min_value=4.5, max_value=8.0, value=4.5, step=0.5)

    # Calcule a soma dos valores dos sliders
    # total = slider1 + slider2 + slider3
    # x = pd.DataFrame(index=[list(range(0,301,1))])
    # Exiba a soma dos valores dos sliders no centro da página
    # st.write(f"## Soma dos valores dos sliders: {total}")
    # st.line_chart(x)

    # fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")
    
    # fig.add_trace(go.Scatter(x=(slider1+slider2), y=(slider3)), marker=dict(color="red", size=12), name="Slider")
    # fig.show()
    fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")
    fig.add_trace(go.Scatter(x=[slider1+slider2], y=[slider3], marker=dict(color="red", size=12), name="Slider"))
    
    with col1:
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    main()