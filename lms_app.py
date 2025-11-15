import streamlit as st

# Page Config
st.set_page_config(
    page_title="Loan & Profit Calculator",
    page_icon="💰",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Force Light Theme
st.markdown("""
    <script>
        var elements = window.parent.document.querySelectorAll('.stApp');
        elements[0].classList.remove('dark-theme');
        elements[0].classList.add('light-theme');
    </script>
""", unsafe_allow_html=True)

# Clean Simple CSS
st.markdown("""
    <style>
    /* Force Light Mode Override */
    :root {
        --background-color: #f5f5f5;
        --text-color: #000000;
    }

    /* Hide Streamlit Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Light Background - Override Everything */
    body {
        background-color: #f5f5f5 !important;
        color: #000000 !important;
    }

    .stApp {
        background-color: #f5f5f5 !important;
    }

    .main {
        background-color: #f5f5f5 !important;
    }

    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 800px;
        background-color: #f5f5f5 !important;
    }

    /* Override any dark backgrounds */
    section[data-testid="stSidebar"],
    [data-testid="stHeader"],
    .element-container,
    div[class*="css"] {
        background-color: transparent !important;
    }

    /* Titles - Dark and Clear */
    h1 {
        color: #000000 !important;
        font-weight: 700 !important;
        font-size: 2rem !important;
    }

    h2 {
        color: #000000 !important;
        font-weight: 600 !important;
        font-size: 1.4rem !important;
        margin-top: 2rem !important;
        margin-bottom: 1.5rem !important;
    }

    /* Input Labels - Clear Black Text */
    .stTextInput > label {
        color: #000000 !important;
        font-size: 15px !important;
        font-weight: 600 !important;
        margin-bottom: 0.5rem !important;
    }

    /* Input Fields - Simple White with Border */
    .stTextInput > div > div > input {
        background-color: #ffffff !important;
        color: #000000 !important;
        border: 2px solid #d1d5db !important;
        border-radius: 6px !important;
        padding: 0.75rem !important;
        font-size: 16px !important;
        font-weight: 500 !important;
    }

    .stTextInput > div > div > input:focus {
        border-color: #2563eb !important;
        outline: none !important;
        box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1) !important;
    }

    /* Buttons - Simple Blue */
    .stButton > button {
        width: 100%;
        background-color: #2563eb !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 6px !important;
        padding: 0.85rem 1.5rem !important;
        font-size: 16px !important;
        font-weight: 600 !important;
        margin-top: 1.5rem !important;
        cursor: pointer;
    }

    .stButton > button:hover {
        background-color: #1d4ed8 !important;
    }

    /* Success Messages - Green Background, Black Text */
    .stSuccess {
        background-color: #d1fae5 !important;
        border-left: 4px solid #10b981 !important;
        border-radius: 4px !important;
        padding: 1rem !important;
        margin-top: 1rem !important;
    }

    .stSuccess p {
        color: #000000 !important;
        font-size: 16px !important;
        font-weight: 600 !important;
        margin: 0 !important;
    }

    /* Warning Messages - Yellow Background, Black Text */
    .stWarning {
        background-color: #fef3c7 !important;
        border-left: 4px solid #f59e0b !important;
        border-radius: 4px !important;
        padding: 1rem !important;
        margin-top: 1rem !important;
    }

    .stWarning p {
        color: #000000 !important;
        font-size: 15px !important;
        font-weight: 600 !important;
        margin: 0 !important;
    }

    /* Metrics - Clear White Cards */
    [data-testid="metric-container"] {
        background-color: #ffffff !important;
        padding: 1.25rem !important;
        border-radius: 6px !important;
        border: 2px solid #e5e7eb !important;
    }

    [data-testid="stMetricValue"] {
        font-size: 28px !important;
        font-weight: 700 !important;
        color: #000000 !important;
    }

    [data-testid="stMetricLabel"] {
        font-size: 14px !important;
        font-weight: 600 !important;
        color: #000000 !important;
        text-transform: uppercase;
    }

    /* Divider */
    hr {
        margin: 2rem 0 !important;
        border: none !important;
        border-top: 2px solid #e5e7eb !important;
    }

    /* Mobile Responsive */
    @media (max-width: 768px) {
        .main .block-container {
            padding: 1rem;
        }

        h1 {
            font-size: 1.6rem !important;
        }

        h2 {
            font-size: 1.2rem !important;
        }

        .stColumns {
            flex-direction: column;
        }

        .stColumn {
            width: 100% !important;
        }
    }
    </style>
    """, unsafe_allow_html=True)

# Header
st.markdown("<h1 style='text-align: center; color: #000000;'>Tajiran Brep Tanzeem</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #000000; font-size: 16px; margin-top: -0.5rem; margin-bottom: 2.5rem; font-weight: 500;'>Loan & Profit Calculator</p>", unsafe_allow_html=True)

# Helper function to safely convert input to integer
def get_int_input(label, key):
    value = st.text_input(label, "0", key=key)
    try:
        return int(value)
    except ValueError:
        return 0

# Section 1: Profit Sharing
st.markdown("## Profit Sharing")

with st.container():
    col1, col2, col3 = st.columns(3)

    with col1:
        total_amount = get_int_input("Total Amount", key="total")
    with col2:
        member1_contribution = get_int_input("Member Contribution", key="member1")
    with col3:
        profit_percentage = get_int_input("Profit Percentage", key="profit")

    if st.button("Calculate Profit Sharing", key="calc_profit"):
        if total_amount > 0 and member1_contribution > 0:
            profit = (total_amount * profit_percentage) // 100
            member1_share = (member1_contribution * profit) // total_amount

            st.success(f"**Total Profit:** {profit:,}")
            st.success(f"**Member Share:** {member1_share:,}")
        else:
            st.warning("Please enter valid amounts greater than 0")

st.divider()

# Section 2: Loan Return Calculator
st.markdown("## Loan Return Calculator")

with st.container():
    col1, col2 = st.columns(2)

    with col1:
        loan_amount = get_int_input("Loan Amount", key="loan")
    with col2:
        loan_percentage = get_int_input("Interest Rate (%)", key="loan_percent")

    if st.button("Calculate Loan Return", key="calc_loan"):
        if loan_amount > 0:
            interest = (loan_amount * loan_percentage) // 100
            total_return = loan_amount + interest

            col_a, col_b = st.columns(2)
            with col_a:
                st.metric(label="Interest Amount", value=f"{interest:,}")
            with col_b:
                st.metric(label="Total to Return", value=f"{total_return:,}")
        else:
            st.warning("Please enter a valid loan amount greater than 0")

# Footer
st.markdown("")
st.markdown("")
st.markdown(
    "<div style='text-align: center; color: #6b7280; font-size: 14px; margin-top: 3rem; padding-top: 2rem; border-top: 2px solid #e5e7eb; font-weight: 500;'>"
    "Built with Streamlit • Runs 100% Offline"
    "</div>",
    unsafe_allow_html=True
)
