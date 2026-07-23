import streamlit as st
import pandas as pd
import plotly.express as px

# Page Configuration
st.set_page_config(
    page_title="Insurance Complaint Root Cause Analyzer",
    page_icon="📊",
    layout="wide"
)

st.markdown("""
<style>

/* Main Background */
.stApp{
    background-color:#F4F7FC;
}

/* Main Content */
.main .block-container{
    padding-top:2rem;
    padding-bottom:2rem;
    padding-left:2rem;
    padding-right:2rem;
}

/* Sidebar */
[data-testid="stSidebar"]{
    background:#0F172A;
}

[data-testid="stSidebar"] *{
    color:white;
}

/* Headers */
h1{
    color:#0F172A;
    font-weight:700;
}

h2,h3{
    color:#1E3A8A;
}

/* Metric Cards */
[data-testid="metric-container"]{
    background:white;
    border-radius:15px;
    padding:18px;
    border-left:6px solid #2563EB;
    box-shadow:0px 3px 12px rgba(0,0,0,0.08);
}

/* Tables */
[data-testid="stDataFrame"]{
    border-radius:12px;
    background:white;
}

/* Buttons */
.stButton>button{
    background:#2563EB;
    color:white;
    border-radius:8px;
    border:none;
}

.stButton>button:hover{
    background:#1D4ED8;
}

/* Select Boxes */
.stSelectbox{
    background:white;
    border-radius:8px;
}

</style>
""", unsafe_allow_html=True)



st.markdown("""
<style>

.main{
    background-color:#f5f7fa;
}

h1{
    color:#0B5ED7;
}

h2{
    color:#0B5ED7;
}

.stMetric{
    border-radius:12px;
    padding:15px;
    background:white;
    box-shadow:0 2px 8px rgba(0,0,0,0.1);
}

</style>
""", unsafe_allow_html=True)

# Load Data

@st.cache_data
def load_data():
    df = pd.read_csv("final_insurance_rootcause.csv")
    root_df = pd.read_csv("root_cause_analysis.csv")
    return df, root_df

df, root_df = load_data()


# Sidebar

st.sidebar.title("📂 Navigation")

page = st.sidebar.radio(
    "Select Page",
    [
        "Dashboard",
        "Complaint Analytics",
        "Root Cause Analysis",
        "AI Recommendations",
        "Company Insights",
        "About"
    ]
)

st.sidebar.header("🔍 Filters")

coverage_filter = st.sidebar.multiselect(
    "Coverage Type",
    sorted(df["Coverage type"].dropna().unique())
)

company_filter = st.sidebar.multiselect(
    "Insurance Company",
    sorted(df["Complaint filed against"].dropna().unique())
)

filtered_df = df.copy()

if coverage_filter:
    filtered_df = filtered_df[
        filtered_df["Coverage type"].isin(coverage_filter)
    ]

if company_filter:
    filtered_df = filtered_df[
        filtered_df["Complaint filed against"].isin(company_filter)
    ]


# Dashboard Page

if page == "Dashboard":

    st.title("🏥 Insurance Complaint Root Cause Analyzer")
    st.markdown(
        "### LLM Analytics for Insurance Complaint Root Cause Identification"
    )

    st.markdown("---")

    # KPI Cards
    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Total Complaints",
        f"{len(df):,}"
    )

    col2.metric(
        "Insurance Companies",
        df["Complaint filed against"].nunique()
    )

    col3.metric(
        "Coverage Types",
        df["Coverage type"].nunique()
    )

    col4.metric(
        "Root Cause Categories",
        df["Root_Cause"].nunique()
    )

    st.markdown("---")

    st.subheader("📄 Dataset Preview")

    st.dataframe(df.head(20), use_container_width=True)

    st.markdown("---")

    st.subheader("Dataset Summary")

    col1, col2 = st.columns(2)

    with col1:
        st.write(f"**Total Records:** {len(filtered_df):,}")
        st.write(f"**Insurance Companies:** {filtered_df['Complaint filed against'].nunique()}")

    with col2:
        st.write(f"**Coverage Types:** {filtered_df['Coverage type'].nunique()}")
        st.write(f"**Average Resolution Days:** {filtered_df['Resolution_Days'].mean():.2f}")


# Placeholder Pages

if page == "Complaint Analytics":

    st.title("📊 Complaint Analytics")

    st.markdown("### Overall Complaint Statistics")

    # Complaint Reasons

    st.subheader("Top Complaint Reasons")

    complaint_reason = (
        filtered_df["Reason complaint filed"]
        .value_counts()
        .head(10)
        .reset_index()
    )

    complaint_reason.columns = [
        "Complaint Reason",
        "Count"
    ]

    fig = px.bar(
        complaint_reason,
        x="Complaint Reason",
        y="Count",
        color="Count",
        title="Top 10 Complaint Reasons"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.markdown("---")

    # Coverage
    st.subheader("Coverage Type Distribution")

    coverage = (
        filtered_df["Coverage type"]
        .value_counts()
        .head(10)
        .reset_index()
    )

    coverage.columns = [
        "Coverage",
        "Count"
    ]

    fig = px.pie(
    coverage,
    values="Count",
    names="Coverage",
    hole=0.5
)

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.markdown("---")
       
    # Companies
    st.subheader("Top Insurance Companies")

    company = (
        filtered_df["Complaint filed against"]
        .value_counts()
        .head(10)
        .reset_index()
    )

    company.columns = [
        "Company",
        "Complaints"
    ]

    fig = px.bar(
        company,
        x="Company",
        y="Complaints",
        color="Complaints",
        title="Top Companies by Complaints"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.markdown("---")

    # Resolution Time

    if "Resolution_Days" in df.columns:

        st.subheader("Resolution Time")

        fig = px.histogram(
            df,
            x="Resolution_Days",
            nbins=40,
            title="Complaint Resolution Time"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    st.markdown("---")

    # Root Causes

    st.subheader("Root Cause Distribution")

    root = (
        df["Root_Cause"]
        .value_counts()
        .reset_index()
    )

    root.columns = [
        "Root Cause",
        "Count"
    ]

    fig = px.bar(
        root,
        x="Root Cause",
        y="Count",
        color="Count",
        title="Root Cause Categories"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

elif page == "Root Cause Analysis":

    st.title("🧠 Root Cause Analysis")

    st.markdown("### Explore Complaint Root Causes")

    # Root Cause Selection
    selected_root = st.selectbox(
        "Select a Root Cause",
        sorted(df["Root_Cause"].dropna().unique())
    )

    filtered_df = df[df["Root_Cause"] == selected_root]

    st.metric(
        "Number of Complaints",
        len(filtered_df)
    )

    st.markdown("---")

    st.subheader("Top Complaint Reasons")

    reason = (
        filtered_df["Reason complaint filed"]
        .value_counts()
        .head(10)
        .reset_index()
    )

    reason.columns = [
        "Complaint Reason",
        "Count"
    ]

    fig = px.bar(
        reason,
        x="Complaint Reason",
        y="Count",
        color="Count",
        title="Top Complaint Reasons"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    st.subheader("Coverage Types")

    coverage = (
        filtered_df["Coverage type"]
        .value_counts()
        .head(10)
        .reset_index()
    )

    coverage.columns = [
        "Coverage",
        "Count"
    ]

    fig = px.pie(
        coverage,
        values="Count",
        names="Coverage",
        title="Coverage Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    st.subheader("Sample Complaints")

    st.dataframe(
        filtered_df[
            [
                "Complaint filed against",
                "Reason complaint filed",
                "Coverage type",
                "How resolved"
            ]
        ].head(20),
        use_container_width=True
    )

elif page == "AI Recommendations":

    st.title("🤖 AI Recommendations")

    st.markdown("### LLM Generated Process Improvements")

    if "Analysis" in root_df.columns:

        cluster = st.selectbox(
            "Select Cluster",
            root_df["Cluster"]
        )

        analysis = root_df[
            root_df["Cluster"] == cluster
        ]["Analysis"].iloc[0]

        with st.expander(
            "LLM Analysis",
            expanded=True
        ):
            st.write(analysis)

    else:

        st.warning(
            "Analysis column not found in root_cause_analysis.csv"
        )

elif page == "Company Insights":

    st.title("🏢 Company Insights")

    company = st.selectbox(
        "Select Insurance Company",
        sorted(df["Complaint filed against"].dropna().unique())
    )

    company_df = df[df["Complaint filed against"] == company]

    col1, col2 = st.columns(2)

    col1.metric("Complaints", len(company_df))

    if "Resolution_Days" in company_df.columns:
        avg_days = company_df["Resolution_Days"].dropna().mean()
        col2.metric(
            "Avg Resolution Days",
            f"{avg_days:.1f}" if pd.notna(avg_days) else "N/A"
        )

    st.subheader("Top Complaint Reasons")

    company_reason = (
        company_df["Reason complaint filed"]
        .value_counts()
        .head(10)
        .reset_index()
    )

    company_reason.columns = [
        "Reason",
        "Count"
    ]

    fig = px.bar(
        company_reason,
        x="Reason",
        y="Count",
        color="Count",
        color_continuous_scale="Blues"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.subheader("Complaint Records")

    st.dataframe(company_df, use_container_width=True)

elif page == "About":

    st.title("ℹ️ About Project")

    st.markdown("""
# Insurance Complaint Root Cause Analyzer

### Problem Statement (PS087)

Create an LLM complaint analyzer that groups insurance grievances by root cause and recommends process changes.

---

### Technologies

- Python
- Pandas
- Sentence Transformers
- KMeans Clustering
- OpenRouter LLM
- Streamlit
- Plotly

---

### AI Pipeline

Insurance Dataset

    ↓

Data Cleaning

    ↓

Sentence Embeddings

    ↓

KMeans Clustering

    ↓

LLM Analytics

    ↓

Root Cause Dashboard

---

Developed using NLP + Machine Learning + LLM Analytics.
""")
    

st.divider()

st.caption(
    "Insurance Complaint Root Cause Analyzer | PS087 | LLM Analytics | Developed using NLP, KMeans & OpenRouter"
)
