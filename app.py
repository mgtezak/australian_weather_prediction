from collections import OrderedDict
import streamlit as st
import config
from tabs import title_page, exploring_and_dataviz, modeling, live_prediction, discussion


st.set_page_config(page_title=config.TITLE, layout="wide", page_icon='🇦🇺')

with open("style.css", "r") as f:
    style = f.read()

st.markdown(f"<style>{style}</style>", unsafe_allow_html=True)

TABS = OrderedDict([(title_page.sidebar_name, title_page),
                    (exploring_and_dataviz.sidebar_name, exploring_and_dataviz),
                    (modeling.sidebar_name, modeling),
                    (live_prediction.sidebar_name, live_prediction),
                    (discussion.sidebar_name, discussion)])

def run():
    st.sidebar.title('Navigation')
    
    st.sidebar.image("https://dst-studio-template.s3.eu-west-3.amazonaws.com/logo-datascientest.png", width=200)
    
    tab_name = st.sidebar.radio("", list(TABS.keys()), 0)
    
    st.sidebar.markdown("---")
    st.sidebar.markdown(f"## {config.PROMOTION}")

    st.sidebar.markdown("### Team members:")
    for member in config.TEAM_MEMBERS:
        st.sidebar.markdown(member.sidebar_markdown(), unsafe_allow_html=True)

    tab = TABS[tab_name]
    tab.run()


if __name__ == "__main__":
    run()
