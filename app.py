import streamlit.components.v1 as components
import streamlit as st
import pandas as pd

st.set_page_config(page_title="青春提案所", page_icon="💡", layout="wide")

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;500;700;800&display=swap');

    :root {
        --primary: #739072;
        --primary-deep: #5a775a;
        --background: #FAF7F2;
        --secondary-bg: #EAE6DF;
        --text: #4A443C;
        --card: #FFFDFB;
        --line: #D9D1C5;
        --soft: #9AAE96;
        --highlight: #F2E7D2;
    }

    .stApp {
        background:
            radial-gradient(circle at top left, rgba(115, 144, 114, 0.12), transparent 24%),
            linear-gradient(180deg, #F9F5F0 0%, var(--background) 100%);
        color: var(--text);
    }

    .block-container {
        max-width: 1220px;
        padding: 3rem 2.2rem 4rem;
    }

    h1, h2, h3, p, span, label, button, [data-testid="stMarkdownContainer"], [data-testid="stExpander"] {
        font-family: 'Noto Sans TC', sans-serif;
    }

    h1 {
        color: var(--text);
        font-size: clamp(2.6rem, 5vw, 4.1rem);
        font-weight: 900;
        line-height: 0.96;
        letter-spacing: -0.06em;
        margin: 0.2rem 0 0.7rem;
    }

    h2, h3 {
        color: var(--text);
        font-weight: 800;
    }

    [data-testid="stCaptionContainer"] {
        color: var(--primary-deep);
        font-weight: 800;
        letter-spacing: 0.12em;
        text-transform: uppercase;
    }

    [data-testid="stImage"] img {
        border-radius: 18px;
        border: 3px solid rgba(115, 144, 114, 0.18);
        box-shadow: 0 14px 32px rgba(74, 68, 60, 0.08);
    }

    [data-testid="stExpander"] {
        background: rgba(255,255,255,0.38);
        border: 1px solid var(--line);
        border-radius: 14px;
        margin-top: 0.7rem;
    }

    [data-testid="stExpander"] summary p {
        color: var(--text);
        font-weight: 700;
    }

    .stLinkButton a {
        background: linear-gradient(135deg, var(--primary), var(--primary-deep));
        border: 0;
        border-radius: 999px;
        color: #fff;
        font-weight: 700;
        padding: 0.7rem 1.2rem;
        box-shadow: 0 10px 22px rgba(90, 119, 90, 0.22);
    }

    .stLinkButton a:hover {
        background: linear-gradient(135deg, var(--primary-deep), var(--primary));
        color: white;
    }

    [data-testid="column"] {
        background: linear-gradient(180deg, rgba(255,255,255,0.85), rgba(255,255,255,0.72));
        border: 1px solid rgba(115, 144, 114, 0.18);
        border-radius: 22px;
        padding: 1.2rem 1.25rem 0.9rem;
        box-shadow: 0 16px 40px rgba(74, 68, 60, 0.08);
    }

    [data-testid="column"] > div {
        position: relative;
    }

    [data-testid="column"] h3 {
        background: var(--highlight);
        display: inline-block;
        padding: 0.35rem 0.7rem;
        border-radius: 999px;
        border: 1px solid rgba(115, 144, 114, 0.18);
    }

    hr {
        border-color: rgba(115, 144, 114, 0.18);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("<div style='color:#739072;font-size:0.8rem;font-weight:800;letter-spacing:0.16em;'>CAMPUS UTOPIA / 2026</div>", unsafe_allow_html=True)
st.title("青春提案所")
st.markdown("<div style='background:#EAE6DF; padding:0.8rem 1rem; border-left:6px solid #739072; border-radius:10px; font-size:1.1rem; color:#4A443C; font-weight:700; margin-bottom:0.8rem;'>打破框架的 N 個校園點子</div>", unsafe_allow_html=True)
st.markdown("歡迎來到校園烏托邦特展。點開各組提案，看看不同立場的討論，想想哪個提案最可行？")
st.divider()

# 1. 模擬表單資料 (已全面更新為：學生、教師、家長、校長、部長、教授)
@st.cache_data
def load_data():
    data = pd.DataFrame({
        "組別名稱": ["第 1 組：科技共存派", "第 2 組：睡眠革命軍"],
        "議題類別": ["📱 科技與界線 (手機)", "⏰ 作息與空間 (早自習)"],
        "圖片網址": ["https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=500", "https://images.unsplash.com/photo-1455619452474-d2be8b1e70cd?w=500"],
        "一句話痛點": ["手機鎖起來，我們的數位焦慮卻被放大了。", "7:30 到校，我們只是坐在教室裡夢遊。"],
        
        "角色1_學生": [
            "我們需要查資料、安排補習時間，沒收手機等於切斷了我們的數位自主權...", 
            "睡眠不足導致我們上課根本無法集中，早自習考試的效益極低..."
        ],
        "角色2_教師": [
            "上課偷滑手機嚴重干擾教學節奏，且引發網路霸凌事件，班級經營難度極高...", 
            "早自習是安定班級心情的重要時刻，若取消，第一節課學生往往心浮氣躁..."
        ],
        "角色3_家長": [
            "雖然怕他們近視，但如果發生緊急事件（如地震），聯絡不到孩子我會非常焦慮...", 
            "雙薪家庭早上必須配合上班時間送小孩，若延後上學，家長接送會有極大困難..."
        ],
        "角色4_校長": [
            "我必須兼顧校園安全與學校聲譽。若開放手機導致偷拍或作弊事件，學校會面臨極大的輿論與家長壓力...", 
            "延後到校牽涉到校車班次的全面調度，以及鄰近交通尖峰時刻的壅塞問題，不能只看單一班級的意願..."
        ],
        "角色5_部長": [
            "中央法規賦予學校因地制宜的管理權，但政策必須符合《兒童及少年福利與權益保障法》，保障學生的表意權...", 
            "配合 108 課綱精神，我們鼓勵學校將早自習還給學生自主規劃，但同時要確保城鄉差距與弱勢學生的照顧..."
        ],
        "角色6_教授": [
            "大學端看重的是『自我調節能力』。高中把學生管得太死，上大學沒人管就全面失控，這不是我們要的未來人才...", 
            "只會早起考試的機器人無法適應高等教育。我們希望看到學生有精神地參與討論，而不是在課堂上補眠..."
        ]
    })
    return data

df = load_data()

# 2. 提案展示大廳 (2欄式)
cols = st.columns(2)

for index, row in df.iterrows():
    with cols[index % 2]:
        st.subheader(row["組別名稱"])
        st.caption(f"🏷️ 議題：{row['議題類別']}")
        st.image(row["圖片網址"], use_container_width=True)
        st.markdown(f"**🔥 我們的痛點：** {row['一句話痛點']}")
        
        # --- 核心改動：6 個全新角色的 Tabs ---
        with st.expander("📖 展開觀看各方角色觀點與政策細節"):
            tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
                "🧑‍🎓 學生", "👨‍🏫 教師", "👪 家長", "🧑‍💼 校長", "🏛️ 部長", "🎓 教授"
            ])
            
            with tab1:
                st.markdown("**【學生代表 觀點】**")
                st.write(row["角色1_學生"])
            with tab2:
                st.markdown("**【教師代表 觀點】**")
                st.write(row["角色2_教師"])
            with tab3:
                st.markdown("**【家長代表 觀點】**")
                st.write(row["角色3_家長"])
            with tab4:
                st.markdown("**【校長 觀點】**")
                st.write(row["角色4_校長"])
            with tab5:
                st.markdown("**【教育部長 觀點】**")
                st.write(row["角色5_部長"])
            with tab6:
                st.markdown("**【大學教授 觀點】**")
                st.write(row["角色6_教授"])
        
        # 互動按鈕
        # 把原本的按鈕替換成這段鑲嵌程式碼：
st.markdown("### 💬 政策質詢與留言區")
# 這裡貼上妳 Padlet 的專屬分享網址
components.iframe("https://padlet.com/embed/https://padlet.com/merry81027/padlet-iipny64x1ou2s45t", height=400, scrolling=True)
st.divider()

