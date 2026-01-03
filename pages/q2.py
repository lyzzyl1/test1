import streamlit as st
import pandas as pd
import plotly.express as px
import math
import random

st.set_page_config(page_title="第二题 - 单摆探究", layout="wide")

# 在每个页面的开头都添加
st.markdown("""
<style>
    [data-testid="stSidebarNav"] {
        display: none;
    }
</style>
""", unsafe_allow_html=True)

# 页面标题
st.title("第二题：单摆周期影响因素")


# 左侧栏 - 输入控件
with st.sidebar:
    st.header("单摆实验设置")
    
    m = st.slider("小球质量 (g)", 50, 100, 80, step=10, help="选择小球质量")
    l = st.slider("摆线长度 (cm)", 10, 50, 30, step=10, help="选择摆线长度")
    a = st.slider("摆动角度 (°)", 3, 10, 5, step=1, help="选择初始摆动角度")
    
    st.markdown("---")
    run_button = st.button("开始模拟", type="primary", use_container_width=True)

# 主界面
col1, col2=st.columns([1,2])  #两列宽度比

with col1:
    st.header("📝 问题描述")
    st.write("小明在探究单摆的摆动周期与哪些因素有关，请你进行实验挖掘规律。")
    
    answer = st.selectbox(
        "有关因素:",
        ["小球质量", "摆线长度", "摆动角度", "无"]
    ) #下拉选择框
    
    if answer:#绿色成功提示框
        st.success(f"您选择了: **{answer}**")

with col2:
    if run_button:#如果按了该按钮
        
        #开始模拟计算
        # 简化计算逻辑
        time = round( 2*math.pi*math.sqrt(l/9.78)+random.uniform(-0.5, 0.5) ,2)
         
        # 建立图表
        data = pd.DataFrame({
            "指标": ["小球质量", "摆线长度", "摆动角度", "单摆周期"],
            "值": [m, l, a, time]
        })
                
        st.session_state.history.append({
            "小球质量":m, "摆线长度":l, "摆动角度":a, "单摆周期":time
        })
    
    # 历史记录
    if "history" not in st.session_state:
        st.session_state.history = []
    st.header("📊 模拟结果")    
    if "history" in st.session_state:#如果非空
        st.subheader("📈 数据记录")
        df = pd.DataFrame(st.session_state.history[-5:])  # 显示最近5次
        st.dataframe(df)

# 页面底部导航
st.markdown("---")
col_left,col_mid, col_right = st.columns(3)
with col_left:
    if st.button("⬅️返回主页", use_container_width=True):
        st.session_state.history = []
        st.switch_page("home.py")
with col_mid:
    if st.button("⬅️ 上一题", use_container_width=True):
        st.session_state.history = []
        st.switch_page("pages/q1.py")
with col_right:
    if st.button("下一题 ➡️", use_container_width=True):
        st.session_state.history = []
        st.switch_page("pages/q3.py")