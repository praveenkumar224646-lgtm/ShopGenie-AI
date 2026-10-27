import streamlit as st
import requests
from rag.product_comparator import compare_products
from rag.search_history import save_search, get_search_history, clear_search_history
# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="ShopGenie AI",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# PREMIUM LUXURY CSS
# ============================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600&family=Playfair+Display:wght@400;500;600&display=swap');

/* ---------- GLOBAL ---------- */

.stApp {
    background:
        radial-gradient(circle at 80% 10%, rgba(184, 148, 72, 0.08), transparent 30%),
        radial-gradient(circle at 10% 80%, rgba(255, 255, 255, 0.025), transparent 25%),
        #0b0b0a;
    color: #f1eee7;
    font-family: 'DM Sans', sans-serif;
}

.main .block-container {
    max-width: 1400px;
    padding-top: 3rem;
    padding-bottom: 4rem;
}

/* ---------- SIDEBAR ---------- */

[data-testid="stSidebar"] {
    background: #080807;
    border-right: 1px solid rgba(255,255,255,0.08);
}

[data-testid="stSidebar"] > div:first-child {
    padding: 2rem 1.3rem;
}

.sidebar-brand {
    font-family: 'Playfair Display', serif;
    font-size: 25px;
    letter-spacing: 1px;
    color: #f2eee5;
    margin-bottom: 4px;
}

.sidebar-sub {
    color: #8d8a82;
    font-size: 11px;
    letter-spacing: 2px;
    text-transform: uppercase;
}

.nav-label {
    color: #77736b;
    font-size: 10px;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-top: 35px;
    margin-bottom: 10px;
}

/* ---------- RADIO ---------- */

.stRadio > label {
    display: none;
}

.stRadio div[role="radiogroup"] {
    gap: 4px;
}

.stRadio div[role="radiogroup"] label {
    border-radius: 7px;
    padding: 10px 12px;
    color: #a9a69e;
    transition: 0.25s;
}

.stRadio div[role="radiogroup"] label:hover {
    background: rgba(255,255,255,0.05);
    color: #eee9df;
}

.stRadio div[role="radiogroup"] label[data-checked="true"] {
    background: rgba(184,148,72,0.12);
    color: #d5b56b;
}

/* ---------- HERO ---------- */

.eyebrow {
    color: #b89550;
    font-size: 11px;
    letter-spacing: 4px;
    text-transform: uppercase;
    margin-bottom: 15px;
}

.hero-title {
    font-family: 'Playfair Display', serif;
    font-size: clamp(48px, 6vw, 82px);
    line-height: 0.98;
    font-weight: 400;
    letter-spacing: -2px;
    color: #f4f0e8;
    margin: 0;
}

.hero-title span {
    color: #b89550;
}

.hero-subtitle {
    color: #99958c;
    font-size: 17px;
    line-height: 1.7;
    max-width: 650px;
    margin-top: 25px;
}

.hero-line {
    height: 1px;
    background: linear-gradient(
        90deg,
        #b89550,
        rgba(184,148,72,0.15),
        transparent
    );
    margin: 45px 0;
}

/* ---------- SECTION ---------- */

.section-label {
    color: #b89550;
    font-size: 10px;
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-bottom: 8px;
}

.section-title {
    font-family: 'Playfair Display', serif;
    font-size: 34px;
    color: #eeeae2;
    margin-bottom: 25px;
}

/* ---------- FEATURE CARDS ---------- */

.lux-card {
    min-height: 190px;
    padding: 28px;
    background: linear-gradient(
        145deg,
        rgba(255,255,255,0.045),
        rgba(255,255,255,0.015)
    );
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 4px;
    transition: all 0.3s ease;
}

.lux-card:hover {
    transform: translateY(-4px);
    border-color: rgba(184,148,72,0.45);
    background: rgba(184,148,72,0.045);
}

.card-number {
    color: #b89550;
    font-size: 11px;
    letter-spacing: 2px;
    margin-bottom: 28px;
}

.card-title {
    font-family: 'Playfair Display', serif;
    font-size: 25px;
    color: #eeeae2;
    margin-bottom: 12px;
}

.card-text {
    color: #88857d;
    font-size: 14px;
    line-height: 1.7;
}

/* ---------- SEARCH PANEL ---------- */

.search-panel {
    background: #10100e;
    border: 1px solid rgba(255,255,255,0.09);
    padding: 35px;
    border-radius: 5px;
    margin-top: 15px;
}

.search-heading {
    font-family: 'Playfair Display', serif;
    font-size: 30px;
    color: #eeeae2;
    margin-bottom: 8px;
}

.search-caption {
    color: #77746d;
    font-size: 13px;
    margin-bottom: 25px;
}

/* ---------- INPUTS ---------- */

.stTextInput label,
.stNumberInput label,
.stSelectbox label {
    color: #aaa69d !important;
    font-size: 12px !important;
    letter-spacing: 0.5px;
}

.stTextInput input,
.stNumberInput input,
.stSelectbox div[data-baseweb="select"] {
    background: #0b0b0a !important;
    color: #eeeae2 !important;
    border: 1px solid #2a2925 !important;
    border-radius: 3px !important;
}

.stTextInput input:focus,
.stNumberInput input:focus {
    border-color: #b89550 !important;
    box-shadow: 0 0 0 1px #b89550 !important;
}

/* ---------- BUTTON ---------- */

.stButton > button {
    width: 100%;
    min-height: 46px;
    background: #b89550 !important;
    color: #0b0b0a !important;
    border: none !important;
    border-radius: 3px !important;
    font-weight: 600 !important;
    letter-spacing: 0.5px;
    transition: all 0.25s ease;
}

.stButton > button:hover {
    background: #d0ad62 !important;
    transform: translateY(-1px);
}

/* ---------- RESULT ---------- */

.result-box {
    margin-top: 25px;
    padding: 25px;
    border: 1px solid rgba(184,148,72,0.35);
    background: rgba(184,148,72,0.045);
    border-radius: 4px;
}

.result-label {
    color: #b89550;
    font-size: 10px;
    letter-spacing: 3px;
    text-transform: uppercase;
}

.result-value {
    color: #eeeae2;
    font-size: 17px;
    margin-top: 7px;
}

/* ---------- PAGE HEADER ---------- */

.page-eyebrow {
    color: #b89550;
    font-size: 10px;
    letter-spacing: 3px;
    text-transform: uppercase;
}

.page-title {
    font-family: 'Playfair Display', serif;
    font-size: 48px;
    font-weight: 400;
    color: #eeeae2;
    margin-top: 5px;
}

.page-description {
    color: #85827a;
    max-width: 650px;
    line-height: 1.7;
}

/* ---------- FOOTER ---------- */

.footer {
    margin-top: 80px;
    padding-top: 20px;
    border-top: 1px solid rgba(255,255,255,0.06);
    color: #57544e;
    font-size: 10px;
    letter-spacing: 2px;
    text-align: center;
    text-transform: uppercase;
}

/* ---------- HIDE STREAMLIT DEFAULT ---------- */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    background: transparent !important;
}

/* ---------- LUXURY PRODUCT CARDS ---------- */

.product-card {
    position: relative;
    padding: 28px;
    margin: 8px 0 28px 0;
    background: linear-gradient(145deg, #141411, #0b0b0a 75%);
    border: 1px solid rgba(184, 148, 72, 0.28);
    border-radius: 8px;
    transition: all 0.3s ease;
}

.product-card:hover {
    border-color: #b89550;
    transform: translateY(-3px);
    box-shadow: 0 12px 35px rgba(0, 0, 0, 0.22);
}

.product-option {
    color: #b89550;
    font-size: 10px;
    letter-spacing: 3px;
    margin-bottom: 14px;
}

.product-name {
    color: #f4f0e8;
    font-family: 'Playfair Display', serif;
    font-size: 28px;
    margin-bottom: 10px;
}

.product-price {
    color: #d5b56b;
    font-size: 30px;
    font-weight: 600;
    margin: 15px 0 24px 0;
}

.product-divider {
    height: 1px;
    background: rgba(255, 255, 255, 0.10);
    margin: 22px 0;
}

.product-spec-label {
    color: #8d8a82;
    font-size: 10px;
    letter-spacing: 2px;
    margin-bottom: 8px;
}

.product-spec-value {
    color: #eeeae2;
    font-size: 14px;
}

.product-description {
    color: #b6b1a7;
    font-size: 14px;
    line-height: 1.8;
    overflow-wrap: anywhere;
}
</style>
""", unsafe_allow_html=True)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        """
        <div class="sidebar-brand">SHOPGENIE</div>
        <div class="sidebar-sub">Intelligent Commerce</div>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<div class="nav-label">Explore</div>', unsafe_allow_html=True)

    page = st.radio(
        "Navigation",
        [
            "🏠 Home",
            "🔍 Product Search",
            "⚖️ Compare Products",
            "⭐ Recommendations",
            "📝 Review Summary",
            "📜 Search History"
        ],
        label_visibility="collapsed"
    )

    st.markdown(
        """
        <div style="
            position: fixed;
            bottom: 25px;
            color: #55524c;
            font-size: 10px;
            letter-spacing: 1.5px;
            line-height: 1.7;
        ">
        GENAI · RAG · AGENTIC AI<br>
        POWERED BY INTELLIGENCE
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# HOME
# ============================================================

if page == "🏠 Home":

    st.markdown(
        '<div class="eyebrow">THE INTELLIGENT WAY TO SHOP</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="hero-title">Shopping,<br><span>reimagined.</span></div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="hero-subtitle">
        ShopGenie AI brings together intelligent search, product intelligence,
        review analysis and personalized recommendations in one refined
        shopping experience.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<div class="hero-line"></div>', unsafe_allow_html=True)

    # FEATURES

    st.markdown(
        '<div class="section-label">01 — CAPABILITIES</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-title">Intelligence behind every choice.</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3, gap="large")

    with col1:
        st.markdown(
            """
            <div class="lux-card">
                <div class="card-number">01 / SEARCH</div>
                <div class="card-title">Smart Discovery</div>
                <div class="card-text">
                Describe what you need naturally. ShopGenie understands
                your requirements, budget and preferences.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div class="lux-card">
                <div class="card-number">02 / ANALYSE</div>
                <div class="card-title">Deep Comparison</div>
                <div class="card-text">
                Compare products through specifications, pricing and
                customer insights instead of browsing endlessly.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            """
            <div class="lux-card">
                <div class="card-number">03 / DECIDE</div>
                <div class="card-title">Personal Guidance</div>
                <div class="card-text">
                Receive explainable recommendations tailored to what
                actually matters to you.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # SEARCH AREA

    st.markdown(
        '<div class="section-label">02 — DISCOVER</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="search-panel">
            <div class="search-heading">What are you looking for?</div>
            <div class="search-caption">
            Tell ShopGenie what you need. Let intelligence do the rest.
            </div>
        """,
        unsafe_allow_html=True
    )

    query = st.text_input(
        "Product requirement",
        placeholder="e.g. Premium laptop for coding under ₹70,000",
        label_visibility="collapsed"
    )

    col1, col2 = st.columns(2, gap="medium")

    with col1:
        budget = st.number_input(
            "Maximum Budget (₹)",
            min_value=0,
            value=50000,
            step=1000
        )

    with col2:
        category = st.selectbox(
            "Category",
            [
                "All",
                "Laptop",
                "Mobile",
                "Headphones",
                "Smartwatch",
                "Camera",
                "Other"
            ],
            index=0,
            key="discover_category"
        )

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("EXPLORE PRODUCTS  →", use_container_width=True):

        if query:

            payload = {
                "query": query,
                "budget": budget,
                "category": category
            }

            try:

                response = requests.post(
                    "http://127.0.0.1:8000/search",
                    json=payload,
                    timeout=120
                )

                if response.status_code == 200:

                    result = response.json()
                    save_search(
                        query=result["query"],
                        budget=result["budget"],
                        category=result["category"]
                    )

                    st.markdown(
                        """
                        <div class="result-box">
                            <div class="result-label">
                            SHOPGENIE RESPONSE
                            </div>
                        """,
                        unsafe_allow_html=True
                    )

                    st.markdown(
                        f"""
                        <div class="result-value">
                        Requirement &nbsp; — &nbsp; {result['query']}
                        </div>

                        <div class="result-value">
                        Budget &nbsp; — &nbsp; ₹{result['budget']:,.0f}
                        </div>

                        <div class="result-value">
                        Category &nbsp; — &nbsp; {result['category']}
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                    st.markdown("</div>", unsafe_allow_html=True)

                    st.markdown("### ✦ AI Recommendation")
                    st.write(result.get("answer", "No AI answer was returned."))

                    sources = result.get("sources", [])
                    if sources:
                        with st.expander("View retrieved product information"):
                            st.json(sources)

                else:
                    st.error(f"Backend returned {response.status_code}: {response.text}")

            except requests.exceptions.ReadTimeout:
                st.error("The AI is taking too long to respond. Please try again in a moment.")
            except requests.exceptions.ConnectionError:
                st.error("Backend is not running. Start FastAPI first.")
            except requests.exceptions.RequestException as error:
                st.error(f"Request failed: {error}")

        else:

            st.warning("Please enter what you are looking for.")

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown(
        """
        <div class="footer">
        SHOPGENIE AI · INTELLIGENT COMMERCE
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# PRODUCT SEARCH
# ============================================================

elif page == "🔍 Product Search":

    st.markdown(
        '<div class="page-eyebrow">01 — DISCOVERY</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="page-title">Product Search</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="page-description">Search for products using natural language and define the budget that matters to you.</div>',
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    query = st.text_input(
        "Product requirement",
        placeholder="Gaming laptop under ₹70,000"
    )

    budget = st.number_input(
        "Maximum Budget (₹)",
        min_value=0,
        value=50000,
        step=5000,
        key="product_budget"
    )



    category = st.selectbox(
        "Category",
        [
            "All",
            "Laptop",
            "Mobile",
            "Headphones",
            "Smartwatch",
            "Camera",
            "Other"
        ],
        index=0,
        key="product_category"
    )

    if st.button("SEARCH PRODUCTS  →"):


        if query:

            payload = {
                "query": query,
                "budget": budget,
                "category": category
            }

            try:

                response = requests.post(
                    "http://127.0.0.1:8000/search",
                    json=payload,
                    timeout=120
                )

                if response.status_code == 200:

                    result = response.json()
                    save_search(
                        query=result["query"],
                        budget=result["budget"],
                        category=result["category"]
                    )
                    st.session_state["recommendation_data"] = result.get("sources", [])

                    st.success("Search request processed.")

                    st.write(f"**Requirement:** {result['query']}")
                    st.write(f"**Budget:** ₹{result['budget']:,.0f}")
                    st.write(f"**Category:** {result['category']}")
                    st.markdown("### ✦ AI Recommendation")
                    st.write(result.get("answer", "No AI answer was returned."))

                    sources = result.get("sources", [])
                    if sources:
                        with st.expander("View retrieved product information"):
                            st.json(sources)

                else:
                    st.error(f"Backend returned {response.status_code}: {response.text}")

            except requests.exceptions.ReadTimeout:
                st.error("The AI is taking too long to respond. Please try again in a moment.")
            except requests.exceptions.ConnectionError:
                st.error("Backend is not running. Start FastAPI first.")
            except requests.exceptions.RequestException as error:
                st.error(f"Request failed: {error}")

        else:
            st.warning("Please enter your requirement.")


# ============================================================
# COMPARE
# ============================================================



elif page == "⚖️ Compare Products":

    st.markdown(
        '<div class="page-eyebrow">02 — ANALYSIS</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="page-title">Compare Products</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="page-description">Compare catalog prices and available specifications side by side.</div>',
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        product1 = st.text_input(
            "FIRST PRODUCT",
            placeholder="e.g. ASUS Vivobook 15",
            key="compare_product1"
        )

    with col2:
        product2 = st.text_input(
            "SECOND PRODUCT",
            placeholder="e.g. HP Victus 15",
            key="compare_product2"
        )

    if st.button("COMPARE PRODUCTS →", use_container_width=True):

        if not product1.strip() or not product2.strip():
            st.warning("Please enter both product names.")

        elif product1.strip().lower() == product2.strip().lower():
            st.warning("Please enter two different products.")

        else:
            with st.spinner("Comparing products..."):
                result = compare_products(product1, product2)

            if "error" in result:
                st.warning(result["error"])

            else:
                first = result["product1"]
                second = result["product2"]
                comparison = result["comparison"]

                st.markdown("### ✦ Product Comparison")

                col1, col2 = st.columns(2)

                for col, product in [
                    (col1, first),
                    (col2, second)
                ]:
                    with col:
                        st.markdown("#### " + product["product"])

                        price = product.get("price")

                        if price is not None:
                            st.metric("Price", f"₹{price:,.0f}")
                        else:
                            st.metric("Price", "Not available")

                        st.write("**Category:**", product.get("category", "Unknown"))
                        st.write("**RAM:**", product.get("ram", "Not available"))
                        st.write("**Storage:**", product.get("storage", "Not available"))
                        st.write("**Processor:**", product.get("processor", "Not available"))

                        with st.expander("Product description and source"):
                            st.write(product.get("description", ""))
                            st.caption("Source: " + product.get("source", "Unknown"))

                st.markdown("---")
                st.markdown("### ✦ Final Verdict")

                difference = comparison.get("price_difference")

                if difference is not None:
                    st.metric("Price Difference", f"₹{difference:,.0f}")

                st.success(
                    "Cheaper product: " + comparison["cheaper_product"]
                )

                st.caption(
                    "Comparison uses recorded catalog data. "
                    "Unavailable specifications are not assumed."
                )




# ============================================================
# RECOMMENDATIONS
# ============================================================
elif page == "⭐ Recommendations":

    st.markdown(
        '<div class="page-eyebrow">03 — PERSONALIZED AI</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="page-title">Recommendations</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="page-description">Find the right products based on your needs and budget.</div>',
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    query = st.text_input(
        "What are you looking for?",
        placeholder="e.g. Best laptop for coding",
        key="recommendation_query"
    )

    budget = st.number_input(
        "Maximum Budget (₹)",
        min_value=0,
        value=50000,
        step=5000,
        key="recommendation_budget"
    )

    category = st.selectbox(
        "Category",
        [
            "All",
            "Laptop",
            "Mobile",
            "Headphones",
            "Smartwatch",
            "Camera",
            "Other"
        ],
        key="recommendation_category"
    )

    if st.button("GET RECOMMENDATIONS →"):

        if query.strip():

            payload = {
                "query": query,
                "budget": budget,
                "category": category
            }

            try:
                response = requests.post(
                    "http://127.0.0.1:8000/search",
                    json=payload,
                    timeout=120
                )

                if response.status_code == 200:
                    result = response.json()
                    save_search(
                        query=result["query"],
                        budget=result["budget"],
                        category=result["category"]
                    )

                    st.markdown("### ✦ AI Recommendation")

                    st.write(
                        result.get(
                            "answer",
                            "No recommendation was returned."
                        )
                    )

                    sources = result.get("sources", [])

                    if sources:
                        with st.expander("View product details"):
                            st.json(sources)

                else:
                    st.error(
                        f"Backend error: {response.status_code}"
                    )

            except requests.exceptions.ConnectionError:
                st.error("Backend is not running. Start FastAPI first.")

            except requests.exceptions.RequestException as error:
                st.error(f"Request failed: {error}")

        else:
            st.warning("Please enter your product requirement.")


elif page == "📜 Search History":
    st.markdown(
        '<div class="page-title">Search History</div>',
        unsafe_allow_html=True
    )

    st.write("Your recent product searches")

    history = get_search_history()

    if history:
        for item in history:
            search_id, query, budget, category, searched_at = item

            with st.container(border=True):
                st.markdown(f"**{query}**")
                st.write(f"Budget: ₹{budget:,.0f}" if budget is not None else "Budget: Not set")
                st.write(f"Category: {category or 'All'}")
                st.caption(searched_at)

        if st.button("CLEAR SEARCH HISTORY"):
            clear_search_history()
            st.success("Search history cleared.")
            st.rerun()
    else:
        st.info("No search history yet. Search for a product first.")
