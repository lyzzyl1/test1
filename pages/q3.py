import streamlit as st
import pandas as pd
import plotly.express as px
import math
import random

st.set_page_config(page_title="第三题 - 生态金字塔", layout="wide")

# 在每个页面的开头都添加
st.markdown("""
<style>
    [data-testid="stSidebarNav"] {
        display: none;
    }
</style>
""", unsafe_allow_html=True)

st.title("第三题：生态系统中的能量流动分析")
st.markdown("---")

# 1. 题干文字
st.markdown("""
### 题目描述

在一个封闭的森林生态系统中，科学家观察到了以下食物链关系：

1. **生产者**：绿色植物（通过光合作用产生能量）
2. **初级消费者**：草食动物（如兔子、鹿）
3. **次级消费者**：肉食动物（如狐狸、狼）
4. **分解者**：真菌和细菌

### 问题

1. 解释为什么能量在食物链中逐级递减
2. 如果这个森林生态系统被开发，会如何影响能量流动？

请根据生态学原理，详细分析上述问题。
""")

# 2. 图片
st.subheader("🔬 生态系统能量金字塔示意图")
/*st.image(
    "pages/p3.PNG",
    caption="图1：典型的生态系统能量金字塔，显示能量在营养级间的递减关系",
    use_container_width=True
)*/

# 3. 用户回答的文本框
st.subheader("📝 请在此输入您的分析回答")

# 使用 st.session_state.history 保存用户输入

# 大文本框供用户输入回答
user_answer = st.text_area(
    "请详细阐述您的分析和计算过程：",
    value=st.session_state.history,
    height=300,
)

# 实时保存用户输入
st.session_state.history = user_answer



# 创建两列布局，使提交按钮居中
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    # 提交按钮
    if st.button("📤 提交答案", type="primary", use_container_width=True):
        if user_answer.strip():
            # 保存到session_state
            st.session_state.q3_answer = user_answer
            st.session_state.q3_submitted = True

            # 显示成功消息
            st.success("✅ 答案提交成功！")           
        else:
            st.error("❌ 答案不能为空，请输入您的分析后再提交。")


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
        st.switch_page("pages/q2.py")
with col_right:
    if st.button("下一题 ➡️", use_container_width=True):
        st.session_state.history = []

        st.switch_page("pages/q3.py")

