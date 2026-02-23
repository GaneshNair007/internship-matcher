import streamlit as st
import pandas as pd
import os
import datetime
import plotly.graph_objects as go

# --- PAGE SETUP ---
st.set_page_config(page_title="Internship Matcher", page_icon="🎯", layout="wide")

# --- CLEAN & MODERN CSS ---
st.markdown("""
    <style>
    .stApp {
        background-color: #000000; 
        color: white;
    }
    section[data-testid="stSidebar"] {
        background-color: #111111 !important;
        border-right: 1px solid #333333;
    }
    .stTextInput > div > div > input {
        background-color: #111111;
        color: white;
        border: 1px solid white; 
    }
    .stExpander {
        background-color: rgba(255, 255, 255, 0.03) !important;
        border: 1px solid white !important;
        border-radius: 8px !important;
    }
    h1, h2, h3, p, span, label {
        color: #ffffff !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- DATA LOADING ---
@st.cache_data
def load_data():
    file_path = 'output(1).csv' 
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        df = df.fillna('')
        return df
    return None

df = load_data()

# --- INITIALIZE VARIABLES (Prevents NameError) ---
match_results = []
user_skills = []

# --- SIDEBAR (User Profile) ---
with st.sidebar:
    st.header("👤 User Profile")
    user_name = st.text_input("Enter your name", key="name_input")
    user_birthday = st.date_input("Birth Date", value=datetime.date(2006, 1, 1), key="date_input")
    
    today = datetime.date.today()
    calc_age = today.year - user_birthday.year - ((today.month, today.day) < (user_birthday.month, user_birthday.day))
    
    st.divider()
    status = "✅ Eligible" if calc_age >= 18 else "❌ Underage"
    st.write(f"**Status:** {status}")
    if user_name:
        st.info(f"Logged in as: {user_name}")
    
    st.divider()
    rating = st.sidebar.slider("Rate our app", 0, 5, 5)

# --- MAIN UI ---
st.title("Internship Matcher")

if calc_age >= 18:
    st.write(f"Welcome **{user_name if user_name else 'Student'}**! Enter your skills to find matches.")
    
    user_input = st.text_input("Your Skills:", placeholder="e.g. Python, SQL, Machine Learning", key="skill_search")

    if user_input:
        user_skills = [s.strip().lower() for s in user_input.split(',')]
        
        if df is not None:
            for index, row in df.iterrows():
                job_tags = str(row['tags']).lower()
                score = sum(1 for skill in user_skills if skill in job_tags)
                
                if score > 0:
                    match_results.append({
                        'Company': row['Company'],
                        'Title': row['Job Title'],
                        'Location': row['Location'],
                        'Skills': row.get('Required Skills', 'Skills not listed'),
                        'Score': score
                    })

            # --- MATCH RESULTS & ANALYTICS ---
            if match_results:
                st.success(f"Found {len(match_results)} matches!")
                
                # Sort results for display
                sorted_results = sorted(match_results, key=lambda x: x['Score'], reverse=True)

                # --- RADAR GRAPH SECTION ---
                st.markdown("### 📊 Skill Gap Analysis")
                company_names = [res['Company'] for res in match_results]
                selected_company = st.selectbox("Select a company to compare your skills:", company_names)

                # Find data for the selected company
                comp_data = next(item for item in match_results if item['Company'] == selected_company)
                
                # Prepare Radar Chart Data
                categories = [s.strip() for s in comp_data['Skills'].split(',')][:6]
                # Ensure we handle empty skill strings
                categories = [c for c in categories if c] 
                
                if categories:
                    user_values = [1 if cat.lower() in [us.lower() for us in user_skills] else 0 for cat in categories]
                    comp_values = [1] * len(categories)

                    fig = go.Figure()
                    fig.add_trace(go.Scatterpolar(r=comp_values, theta=categories, fill='toself', name='Requirement', line_color='#636EFA'))
                    fig.add_trace(go.Scatterpolar(r=user_values, theta=categories, fill='toself', name='Your Skills', line_color='#EF553B'))

                    fig.update_layout(
                        polar=dict(radialaxis=dict(visible=True, range=[0, 1], showticklabels=False), bgcolor="rgba(0,0,0,0)"),
                        showlegend=True,
                        paper_bgcolor='rgba(0,0,0,0)',
                        plot_bgcolor='rgba(0,0,0,0)',
                        font=dict(color="white")
                    )
                    st.plotly_chart(fig, use_container_width=True)
                
                # --- LIST VIEW ---
                st.write(f"### Found {len(match_results)} detailed matches:")
                for item in sorted_results:
                    with st.expander(f"🏢 {item['Company']} — {item['Title']} ({item['Score']} skills match)"):
                        st.write(f"📍 **Location:** {item['Location']}")
                        st.write(f"📝 **Required Skills:** {item['Skills']}")
            else:
                st.warning("No matches found. Try broadening your skill list.")
        else:
            st.error("Error: 'output(1).csv' not found in the folder.")
else:
    st.error(f"Sorry {user_name if user_name else 'User'}, you must be 18 or older to access the internship database.")
    st.info("Please update your birth date in the sidebar once you are eligible.")

st.divider()