import streamlit as st

# Page Config
st.set_page_config(page_title="Loan & Profit Calculator", page_icon="💰", layout="centered")

# Title
st.markdown("<h1 style='text-align: center; color: #2E86C1;'>💰 Tajiran Brep Tanzeem Calculator</h1>", unsafe_allow_html=True)
st.write("---")

# Helper function to safely convert input to integer
def get_int_input(label, key):
    value = st.text_input(label, "0", key=key)
    try:
        return int(value)
    except ValueError:
        return 0

# ==============================
# Section 1: Profit Sharing
# ==============================
st.markdown("## 📊 Profit Sharing")

with st.container():
    col1, col2, col3 = st.columns(3)

    with col1:
        total_amount = get_int_input("💵 Total Amount After Loaning", key="total")
    with col2:
        member1_contribution = get_int_input("👤 Member 1 Contribution", key="member1")
    with col3:
        profit_percentage = get_int_input("📈 Profit Percentage (%)", key="profit")

    if st.button("🔍 Calculate Profit Sharing"):
        if total_amount > 0 and member1_contribution > 0:
            profit = (total_amount * profit_percentage) // 100
            member1_share = (member1_contribution * profit) // total_amount

            
            st.info(f"💰 **Total Profit:** {profit}")
            st.info(f"👤 **Member 1's Share:** {member1_share}")
        else:
            st.warning("⚠️ Please enter valid amounts greater than 0.")

st.write("---")

# ==============================
# Section 2: Loan Return Calculator
# ==============================
st.markdown("## 💸 Loan Return Calculator")

with st.container():
    col1, col2 = st.columns(2)

    with col1:
        loan_amount = get_int_input("🏦 Loan Amount", key="loan")
    with col2:
        loan_percentage = get_int_input("📊 Loan Interest (%)", key="loan_percent")

    if st.button("🔍 Calculate Loan Return"):
        if loan_amount > 0:
            total_return = loan_amount + (loan_amount * loan_percentage) // 100

            
            st.info(f"📌 **Total Amount to Return:** {total_return}")
        else:
            st.warning("⚠️ Please enter a valid loan amount greater than 0.")
