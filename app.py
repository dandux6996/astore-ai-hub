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

# =====================================================
# ESG SCORECARD (NEW - APPEARS ON EVERY TAB)
# =====================================================
def display_esg_scorecard(tab_context="general"):
    """Displays ESG scorecard with estimated KPIs"""
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.metric(
            label="ESG Data Coverage",
            value="62%",
            delta="↗ +4%",
            delta_color="normal",
            help="Percentage of suppliers reporting ESG data (Target: 85% by 2027)"
        )
    
    with col2:
        st.metric(
            label="Spend with ESG Suppliers",
            value="€48M / €92M",
            delta="↗ +12%",
            delta_color="normal",
            help="Spend with ESG-rated suppliers vs total services spend"
        )
    
    with col3:
        st.metric(
            label="Scope 3 Emissions",
            value="1,247 tCO₂e",
            delta="↘ -3%",
            delta_color="inverse",
            help="Services category emissions (Target: 35% reduction by 2028)"
        )
    
    with col4:
        st.metric(
            label="ESG Tenders",
            value="78%",
            delta="↗ +15%",
            delta_color="normal",
            help="% of tenders with ESG criteria (Target: 100%)"
        )
    
    with col5:
        st.metric(
            label="Diversity Suppliers",
            value="14%",
            delta="↗ +2%",
            delta_color="normal",
            help="% spend with diverse/local suppliers (Target: 25%)"
        )
    
    st.markdown("---")

# Call scorecard once at top
display_esg_scorecard("dashboard")

tab1, tab2, tab3, tab4 = st.tabs([
    "Industry & Category Intelligence",
    "Category Strategy",
    "Supplier Intelligence",
    "Tender Preparation Assistant"
])

def call_perplexity(prompt, temperature=0.2):
    try:
        response = requests.post(
            API_URL,
            headers={
                "Authorization": f"Bearer {PPLX_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "sonar-pro",
                "messages": [{"role": "user", "content": prompt}],
                "temperature": temperature
            }
        )
        data = response.json()
        return data["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error calling Perplexity API: {e}"

# =====================================================
# TAB 1 — INDUSTRY & CATEGORY INTELLIGENCE
# =====================================================
with tab1:
    st.header("Industry & Category Intelligence")
    
    # Tab-specific scorecard context
    display_esg_scorecard("intelligence")
    
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
You are a market intelligence analyst for Accor's Astore procurement division. 

Focus area: {focus_area}
Region: {geography}
Timeframe: {timeframe}

Provide 4–5 hospitality-relevant intelligence items covering recent developments, trends, and procurement implications.

For each intelligence item, provide:

**HEADLINE:** Clear, specific title

**WHAT HAPPENED:** Brief summary (2–3 sentences) of the development, trend, or news

**WHY IT MATTERS FOR PROCUREMENT:** Direct implications for Astore category managers
- Cost impact (increase/decrease)
- Supply chain implications
- ESG/sustainability relevance (how does this impact ESG KPIs?)
- Risk considerations
- Opportunity identification

**RECOMMENDED ACTION:** Specific next step (e.g., "Engage suppliers on X", "Monitor Y closely", "Prepare contingency for Z")

**SOURCE:** Cite source and date

**ESG KPI IMPACT:** How does this affect key ESG metrics (data coverage, Scope 3 emissions, supplier diversity)?

Focus on:
- Market trends affecting hospitality services
- Supplier developments (M&A, innovations, challenges)
- Regulatory changes (especially ESG-related)
- Price movements and cost drivers
- Technology and innovation
- Labor market dynamics

Prioritize actionable, procurement-relevant insights. Be specific and current ({timeframe}).
"""
        with st.spinner("Gathering latest intelligence and market insights..."):
            content = call_perplexity(prompt, temperature=0.2)
            st.markdown(content)

# =====================================================
# TAB 2 — CATEGORY STRATEGY
# =====================================================
with tab2:
    st.header("Category Strategy")
    
    # Tab-specific scorecard context
    display_esg_scorecard("strategy")
    
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
name, coverage, strengths, estimated revenue, website, ESG credentials.
Include how each supplier impacts ESG KPIs (data coverage, emissions, diversity).
"""
        else:
            prompt = f"""
Produce a decisive category assessment for Accor's Astore services category.

Category: {category}
Region: {region}
Objective: {objective}
Current status: {current_status}

Output:
CURRENT STATUS (include current ESG KPIs for this category)
KEY GAPS (highlight ESG gaps)
SHORT-TERM ACTIONS (0–6 months) - include ESG actions
LONG-TERM ACTIONS (6–18 months) - include ESG targets
ESTIMATED ESG KPI IMPACT (how this strategy moves the scorecard)

Include ESG and decarbonisation considerations throughout.
"""
        with st.spinner("Generating category strategy..."):
            content = call_perplexity(prompt, temperature=0.2)
            st.markdown(content)

# =====================================================
# TAB 3 — SUPPLIER INTELLIGENCE
# =====================================================
with tab3:
    st.header("Supplier Intelligence & ESG Scoring")
    st.markdown("Deep-dive analysis of supplier capabilities, ESG credentials, and market positioning.")
    
    # Tab-specific scorecard context
    display_esg_scorecard("supplier")
    
    st.subheader("Analyze Existing Supplier")

    supplier_name = st.text_input("Supplier Name", placeholder="E.g., ISS Facility Services, Ecolab, Bunzl")

    col1, col2 = st.columns(2)
    with col1:
        supplier_category = st.selectbox(
            "Service Category",
            [
                "Housekeeping Services",
                "Laundry Services",
                "Energy Management",
                "Waste Management",
                "Cleaning Chemicals",
                "Other / Adjacent Services"
            ],
            key="supplier_category"
        )
    with col2:
        supplier_region = st.selectbox(
            "Region",
            ["DACH", "UK", "Poland", "Europe", "Global"],
            key="supplier_region"
        )

    if st.button("Analyze Supplier", key="supplier_analyze"):
        if not supplier_name.strip():
            st.error("Please enter a supplier name.")
        else:
            prompt = f"""
Provide detailed intelligence on this supplier for Accor Astore procurement:

Supplier: {supplier_name}
Category: {supplier_category}
Region: {supplier_region}

Generate a comprehensive supplier profile:

COMPANY OVERVIEW
SERVICE CAPABILITIES
ESG PERFORMANCE (Critical for 2026)
FINANCIAL STABILITY
HOSPITALITY EXPERIENCE
STRENGTHS & RISKS
NEGOTIATION INSIGHTS
RECOMMENDATION

**ESG KPI IMPACT:** How does this supplier move our ESG scorecard?
- ESG Data Coverage: Does it report PCF, CDP, etc.?
- Scope 3 Emissions: Carbon reduction potential
- Supplier Diversity: Local/SME status
- ESG Tenders: Compliance with our ESG criteria

Use current 2026 data where available. Be specific and cite sources.
"""
            with st.spinner("Gathering supplier intelligence and ESG data..."):
                content = call_perplexity(prompt, temperature=0.25)
                st.markdown(content)

    st.markdown("---")
    st.subheader("Discover New Suppliers")
    
    col3, col4 = st.columns(2)
    with col3:
        discover_category = st.selectbox(
            "Service Category",
            [
                "Housekeeping Services",
                "Laundry Services",
                "Waste Management",
                "Energy Management",
                "Other / Adjacent Services"
            ],
            key="discover_category"
        )
    with col4:
        discover_region = st.selectbox(
            "Region",
            ["DACH", "UK", "Poland", "Europe", "Global"],
            key="discover_region"
        )

    if st.button("Find Suppliers", key="discover_suppliers"):
        prompt = f"""
Identify top suppliers for Accor's Astore procurement:

Category: {discover_category}
Region: {discover_region}

Provide a shortlist of 6–8 suppliers (mix of established and emerging):

For each supplier include:
SUPPLIER NAME
- Coverage: Geographic reach
- Size: Revenue estimate, employee count
- Hospitality Focus: % of business from hotels, key clients
- ESG Credentials: Key certifications, carbon commitments
- Strengths: 2–3 differentiators relevant to hospitality
- Typical Pricing: Premium / Mid-range / Competitive
- Website: URL
- ESG KPI Impact: How it moves our scorecard

Group into:
1. TIER 1: Market Leaders
2. TIER 2: Regional Champions  
3. TIER 3: Emerging/Innovative

Prioritize suppliers with strong ESG credentials and hospitality experience.
"""
        with st.spinner("Searching supplier landscape..."):
            content = call_perplexity(prompt, temperature=0.25)
            st.markdown(content)

# =====================================================
# TAB 4 — TENDER PREPARATION ASSISTANT
# =====================================================
with tab4:
    st.header("AI Tender Preparation Assistant")
    st.markdown("Generate RFI/RFP templates with ESG KPIs and evaluation criteria tailored to your category and region.")
    
    # Tab-specific scorecard context
    display_esg_scorecard("tender")
    
    col1, col2 = st.columns(2)
    with col1:
        tender_category = st.selectbox(
            "Service Category",
            [
                "Housekeeping Services",
                "Laundry & Textile Services",
                "Energy Management Services",
                "Waste Management Services",
                "Other / Adjacent Services"
            ],
            key="tender_category"
        )
    with col2:
        tender_region = st.selectbox(
            "Region",
            ["DACH", "UK", "Poland", "Europe", "Multi-region"],
            key="tender_region"
        )

    tender_type = st.selectbox(
        "Tender Type",
        [
            "RFI (Request for Information)",
            "RFP (Request for Proposal)",
            "Supplier Evaluation Scorecard",
            "ESG Questionnaire"
        ],
        key="tender_type"
    )

    tender_context = st.text_area(
        "Key Requirements & Context",
        height=140,
        placeholder=(
            "E.g., Seeking single supplier for housekeeping across 25 hotels in DACH. "
            "Must have ISO 14001, living wage commitment, and carbon reporting capability. "
            "Contract value €2.5M annually..."
        ),
        key="tender_context"
    )

    if st.button("Generate Tender Document", key="tender_generate"):
        prompt = f"""
Create a professional {tender_type} template for Accor Astore procurement:

Category: {tender_category}
Region: {tender_region}
Requirements / Context: {tender_context}

Generate a complete, ready-to-use document with:

1. INTRODUCTION & BACKGROUND
2. TECHNICAL REQUIREMENTS
3. ESG & SUSTAINABILITY REQUIREMENTS (CRITICAL for 2026)
   - Mandatory ESG KPIs and reporting standards
   - How suppliers will contribute to our ESG scorecard
4. EVALUATION CRITERIA & WEIGHTINGS
   - ESG performance: XX% weight
   - Specific ESG scoring criteria
5. SUPPLIER INFORMATION REQUIRED
6. SUBMISSION REQUIREMENTS
7. KEY QUESTIONS TO ASK SUPPLIERS

**ESG KPI ALIGNMENT:** Ensure the tender drives improvements in:
- ESG Data Coverage (target: 85%)
- Scope 3 Emissions reduction
- Supplier diversity targets

Make it practical, professional, and hospitality-specific.
"""
        with st.spinner("Creating tender documentation..."):
            content = call_perplexity(prompt, temperature=0.2)
            st.info("📋 Tender Document Generated – copy this template and adapt it into Word/PDF for your tender pack.")
            st.markdown(content)
