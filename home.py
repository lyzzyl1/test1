import streamlit as st

st.set_page_config(page_title="跑步模拟系统", layout="wide", page_icon="🏃")

# 在每个页面的开头都添加
st.markdown("""
<style>
    [data-testid="stSidebarNav"] {
        display: none;
    }
</style>
""", unsafe_allow_html=True)

st.title("科学推理能力测试")
st.markdown("---")

# 欢迎信息
st.header("科学推理能力测试")
st.write("""
## 本测试通过创设一系列科学情境，测试您的科学推理能力。

""")

# 显示两个题目链接
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 开始测试")
    if st.button("前往第一题", use_container_width=True):
        st.session_state.history = []
        st.switch_page("pages/q1.py")


