import streamlit as st

st.title("Coba")

tab1, tab2, tab3 = st.tabs(["1", "2", "3"])

with tab1:
    st.image("https://www.google.com/url?sa=i&url=https%3A%2F%2Fhdqwalls.com%2Fswitzerland-landscape-4k-wallpaper&psig=AOvVaw3sGjymhFZSrXD1u6wvUp89&ust=1680492667738000&source=images&cd=vfe&ved=0CBAQjRxqFwoTCOCTm5ihiv4CFQAAAAAdAAAAABAD.jpg")

with tab2:
    col1, col2, col3 = st.columns(3)

    with col1:
        st.success("coy")

    with col2:
        st.balloons()

with tab3:
    with st.container():
        st.write("This is inside the container")

        st.image("https://www.google.com/url?sa=i&url=https%3A%2F%2Fhdqwalls.com%2Fswitzerland-landscape-4k-wallpaper&psig=AOvVaw3sGjymhFZSrXD1u6wvUp89&ust=1680492667738000&source=images&cd=vfe&ved=0CBAQjRxqFwoTCOCTm5ihiv4CFQAAAAAdAAAAABAD.jpg")

        A = st.button("ok")

    st.write("This is outside the container")