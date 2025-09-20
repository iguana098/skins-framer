import streamlit as st
import urllib.parse
import requests

st.set_page_config(page_title="Skinsframer", page_icon="images/icon.png"")

emojis = ["( •_•)", "(⌐■_■)", "(｢• ω •)｢", "＼(ﾟ ｰﾟ＼)", "( ﾉ･o･ )ﾉ"]

st.logo("images/horizontal.png", icon_image="images/horizontal.png")
num_forms = st.sidebar.number_input("num forms", label_visibility="visible", min_value=1, max_value=len(emojis), value=1)

for i in range(num_forms):
    emoji = emojis[i % len(emojis)]  # Cycle through emojis in order
    with st.form(f"form_{i}"):
        item_name = st.text_input(
            label=emoji,
            key=f"input_{i}"
        )
        submitted = st.form_submit_button("Search", key=f"submit_{i}")

        if submitted and item_name:
            encoded_item = urllib.parse.quote(item_name)
            url = f"https://steamcommunity.com/market/listings/730/{encoded_item}"
            response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})

            if response.ok:
                st.components.v1.html(response.text, height=650, scrolling=True)
            else:
                raise response.status_code
            
