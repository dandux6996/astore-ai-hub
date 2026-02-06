import streamlit as st
import requests
import json
import os
from datetime import datetime

# =============================
# CONFIG
# =============================
PPLX_API_KEY = "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"
API_URL = "https://api.perplexity.ai/chat/completions"
NEGOTIATION_DB = "negotiation_learnings.json"

st.set_page_config(
    page_title="AI (Astore Insights) Hub",
    layout="wide"
)

st.title("AI (Astore Insights) Hub")

tab1, tab2, tab3, tab4 = st.tabs([
    "Industry & Category Intelligence",
    "Category Strategy",
    "Supplier Evaluation",
    "Negotiation Intelligence"
])

# =====================================================
# TAB 1 — INDUSTRY & CATEGORY INTELLIGENCE (UNCHANGED)
# =====================================================
with tab1:
    st.header("Industry & Category Intelligence")

    focus_area = st.selectbox(
        "Focus area",
        [
            "Hospitality Market & Hotels",
            "Procurement & Sourcing",
            "Housekeeping & Cleaning Services",
            "Laundry & Textile Services",
            "Energy & Utilities",
            "Waste Management & Circular Economy",
            "ESG, Sustainability & Decarbonisation",
            "Regulation & Policy",
            "Labour & Outsourced Services"
        ],
        key="int_focus"
    )

    geography = st.selectbox(
        "Geographic scope",
        ["Global", "Europe", "UK", "DACH", "Poland"],
        key="int_geo"
    )

    timeframe = st.selectbox(
        "Time horizon",
        ["Last 24 hours", "Last 7 days", "Last 30 days"],
        key="int_time"
    )

    if st.button("Generate Intelligence Brief", key="int_generate"):
        prompt = f"""
Fetch up to 4 hospitality-relevant intelligence items.

Focus: {focus_area}
Region: {geography}
Timeframe: {timeframe}

Return RAW JSON ONLY with:
headline, gist, sourcing_implication, source_url
"""

        response = requests.post(
            API_URL,
            headers={"Authorization": f"Bearer {PPLX_API_KEY}", "Content-Type": "application/json"},
            json={"model": "sonar-pro", "messages": [{"role": "user", "content": prompt}], "temperature": 0.2}
        )

        content = response.json()["choices"][0]["message"]["content"]
        content = content.replace("```json", "").replace("```", "").strip()

        try:
            items = json.loads(content)
        except:
            items = []

        for item in items:
            st.markdown(f"### {item['headline']}")
            st.write(f"**Gist:** {item['gist']}")
            st.write(f"**Why it matters:** {item['sourcing_implication']}")
            st.markdown(f"[Read more]({item['source_url']})")
            st.divider()

# =====================================================
# TAB 2 — CATEGORY STRATEGY (UNCHANGED)
# =====================================================
with tab2:
    st.header("Category Strategy")

    category = st.selectbox(
        "Service Category",
        [
            "Housekeeping Services",
            "Laundry Services",
            "Energy Management Services",
            "Waste Management Services",
            "Other / Adjacent Services"
        ],
        key="cat_category"
    )

    region = st.selectbox("Region", ["Europe", "UK", "DACH", "Poland", "Global"], key="cat_region")

    objective = st.selectbox(
        "Primary objective",
        [
            "Cost optimization",
            "Supplier consolidation",
            "Supplier expansion / diversification",
            "Standardization",
            "Service quality improvement",
            "Risk reduction",
            "ESG improvement",
            "Find Suppliers"
        ],
        key="cat_objective"
    )

    current_status = st.text_area("Current category status", height=120, key="cat_status")

    if st.button("Generate Output", key="cat_generate"):
        if objective == "Find Suppliers":
            prompt = f"""
List hospitality-relevant suppliers for:
Category: {category}
Region: {region}

Group as Local/Regional and International.
For each supplier include:
name, coverage, strengths, estimated revenue, website.
"""
        else:
            prompt = f"""
Produce a decisive category assessment.

Category: {category}
Region: {region}
Objective: {objective}
Current status: {current_status}

Output:
CURRENT STATUS
KEY GAPS
SHORT-TERM ACTIONS (0–6 months)
LONG-TERM ACTIONS (6–18 months)
"""

        response = requests.post(
            API_URL,
            headers={"Authorization": f"Bearer {PPLX_API_KEY}", "Content-Type": "application/json"},
            json={"model": "sonar-pro", "messages": [{"role": "user", "content": prompt}], "temperature": 0.2}
        )

        st.markdown(response.json()["choices"][0]["message"]["content"])

# =====================================================
# TAB 3 — SUPPLIER EVALUATION (REDESIGNED)
# =====================================================
with tab3:
    st.header("Supplier Evaluation")

    eval_mode = st.radio(
        "Evaluation approach",
        [
            "Define KPIs & Weightages",
            "Compare Suppliers"
        ],
        key="eval_mode_new"
    )

    # -------------------------------------------------
    # MODE 1 — KPI DEFINITION
    # -------------------------------------------------
    if eval_mode == "Define KPIs & Weightages":
        category = st.selectbox(
            "Service category",
            [
                "Housekeeping Services",
                "Laundry Services",
                "Energy Management Services",
                "Waste Management Services",
                "Other / Adjacent Services"
            ],
            key="kpi_category"
        )

        region = st.selectbox(
            "Region",
            ["Europe", "UK", "DACH", "Poland", "Global"],
            key="kpi_region"
        )

        status = st.text_area(
            "Current category context (e.g. no. of suppliers, tender stage, pain points)",
            height=120,
            key="kpi_status"
        )

        if st.button("Generate KPIs & Weightages", key="kpi_generate"):
            prompt = f"""
You are supporting an Astore Category Manager.

Category: {category}
Region: {region}
Current context: {status}

Task:
Define the MOST RELEVANT KPIs to evaluate suppliers.

Output requirements:
- 6–10 KPIs only
- Each KPI must include:
  • KPI name
  • Why it matters
  • Suggested weightage (%)
- Total weightage must equal 100%

KPIs must reflect:
- Service continuity
- Labour dependency
- Cost structure
- ESG & compliance
- Regional maturity
"""

            response = requests.post(
                API_URL,
                headers={"Authorization": f"Bearer {PPLX_API_KEY}", "Content-Type": "application/json"},
                json={"model": "sonar-pro", "messages": [{"role": "user", "content": prompt}], "temperature": 0.2}
            )

            st.markdown(response.json()["choices"][0]["message"]["content"])

    # -------------------------------------------------
    # MODE 2 — SUPPLIER COMPARISON
    # -------------------------------------------------
    else:
        supplier_count = st.number_input(
            "Number of suppliers to compare",
            min_value=1,
            max_value=10,
            value=3,
            step=1,
            key="cmp_count"
        )

        suppliers = []
        for i in range(int(supplier_count)):
            st.subheader(f"Supplier {i+1}")
            name = st.text_input("Supplier name", key=f"cmp_name_{i}")
            score_input = st.text_area(
                "Supplier performance notes / scores vs KPIs",
                height=80,
                key=f"cmp_notes_{i}"
            )
            suppliers.append({"name": name, "notes": score_input})

        if st.button("Compare Suppliers", key="cmp_generate"):
            prompt = f"""
Compare suppliers for an Astore services category.

Supplier inputs:
{suppliers}

Task:
- Rank suppliers
- Highlight trade-offs
- Identify preferred supplier(s)
- Flag key risks
- Recommend next steps
"""

            response = requests.post(
                API_URL,
                headers={"Authorization": f"Bearer {PPLX_API_KEY}", "Content-Type": "application/json"},
                json={"model": "sonar-pro", "messages": [{"role": "user", "content": prompt}], "temperature": 0.25}
            )

            st.markdown(response.json()["choices"][0]["message"]["content"])

# =====================================================
# TAB 4 — NEGOTIATION INTELLIGENCE (UNCHANGED)
# =====================================================
with tab4:
    st.header("Negotiation Intelligence")

    neg_mode = st.radio(
        "Negotiation stage",
        ["Pre-Negotiation Intelligence", "Post-Negotiation Learning"],
        key="neg_mode"
    )

    if neg_mode == "Pre-Negotiation Intelligence":
        supplier = st.text_input("Supplier name", key="neg_supplier")
        service = st.selectbox(
            "Service category",
            ["Housekeeping", "Laundry", "Energy Management", "Waste Management", "Other Services"],
            key="neg_service"
        )
        region = st.selectbox("Region", ["Europe", "UK", "DACH", "Poland", "Global"], key="neg_region")

        if st.button("Generate Negotiation Intelligence", key="neg_pre_btn"):
            prompt = f"""
Provide negotiation intelligence for:
Supplier: {supplier}
Service: {service}
Region: {region}

Include:
- Company overview
- Hospitality relevance
- Market position
- Leverage points
- Risks
- Suggested negotiation posture
"""

            response = requests.post(
                API_URL,
                headers={"Authorization": f"Bearer {PPLX_API_KEY}", "Content-Type": "application/json"},
                json={"model": "sonar-pro", "messages": [{"role": "user", "content": prompt}], "temperature": 0.2}
            )
            st.markdown(response.json()["choices"][0]["message"]["content"])

    else:
        category = st.selectbox(
            "Service category",
            [
                "Housekeeping Services",
                "Laundry Services",
                "Energy Management Services",
                "Waste Management Services",
                "Other / Adjacent Services"
            ],
            key="neg_post_category"
        )
        region = st.selectbox("Region", ["Europe", "UK", "DACH", "Poland", "Global"], key="neg_post_region")
        worked = st.text_area("What worked", key="neg_worked")
        didnt = st.text_area("What didn’t work", key="neg_didnt")

        if st.button("Save Negotiation Learning", key="neg_save"):
            entry = {
                "date": datetime.now().isoformat(),
                "category": category,
                "region": region,
                "worked": worked,
                "didnt": didnt
            }

            if os.path.exists(NEGOTIATION_DB):
                with open(NEGOTIATION_DB, "r") as f:
                    data = json.load(f)
            else:
                data = []

            data.append(entry)

            with open(NEGOTIATION_DB, "w") as f:
                json.dump(data, f, indent=2)

            prompt = f"""
Based on the negotiation experience below, suggest improvements.

Worked:
{worked}

Did not work:
{didnt}
"""

            response = requests.post(
                API_URL,
                headers={"Authorization": f"Bearer {PPLX_API_KEY}", "Content-Type": "application/json"},
                json={"model": "sonar-pro", "messages": [{"role": "user", "content": prompt}], "temperature": 0.2}
            )

            st.success("Negotiation learning saved.")
            st.markdown(response.json()["choices"][0]["message"]["content"])
