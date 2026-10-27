
import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="E-Commerce Dashboard",
    page_icon="🛒",
    layout="wide"
)

st.title("🛒 E-Commerce Dashboard")

# -----------------------------
# DASHBOARD SELECTION
# -----------------------------
selection = st.selectbox(
    "Select the type of dashboard:",
    [
        "E-commerce Sales Data",
        "Inventory Data 🚧 (Coming Soon)"
    ]
)

# =========================================================
# E-COMMERCE SALES DASHBOARD
# =========================================================

if selection == "E-commerce Sales Data":

    st.header("📊 E-Commerce Sales Dashboard")

    # Upload CSV
    uploaded_file = st.file_uploader(
        "Upload your e-commerce CSV file",
        type=["csv"],
        key="sales_upload"
    )

    if uploaded_file is None:
        st.info("Please upload a CSV file.")
        st.stop()

    # Read CSV
    try:
        df = pd.read_csv(uploaded_file)
    except Exception as e:
        st.error(f"Unable to read the CSV file: {e}")
        st.stop()

    # Check required columns
    required_columns = [
        "Order_ID",
        "Product",
        "Category",
        "Quantity",
        "Price",
        "City",
        "Status",
        "Revenue"
    ]

    missing = [
        column for column in required_columns
        if column not in df.columns
    ]

    if missing:
        st.error("Missing columns: " + ", ".join(missing))
        st.stop()

    if df.empty:
        st.warning("The uploaded CSV file contains no data.")
        st.stop()

    # Convert numeric columns
    for column in ["Quantity", "Price", "Revenue"]:
        df[column] = pd.to_numeric(
            df[column],
            errors="coerce"
        )

    # Remove rows with missing required values
    df = df.dropna(subset=required_columns)

    if df.empty:
        st.warning("No valid records found in the uploaded CSV.")
        st.stop()

    # -----------------------------
    # SIDEBAR FILTERS
    # -----------------------------
    st.sidebar.header("🔎 Filters")

    selected_category = st.sidebar.multiselect(
        "Category",
        options=sorted(df["Category"].unique().tolist()),
        default=sorted(df["Category"].unique().tolist())
    )

    selected_city = st.sidebar.multiselect(
        "City",
        options=sorted(df["City"].unique().tolist()),
        default=sorted(df["City"].unique().tolist())
    )

    selected_status = st.sidebar.multiselect(
        "Status",
        options=sorted(df["Status"].unique().tolist()),
        default=sorted(df["Status"].unique().tolist())
    )

    # Apply filters
    filtered_df = df[
        df["Category"].isin(selected_category)
        & df["City"].isin(selected_city)
        & df["Status"].isin(selected_status)
    ]

    # -----------------------------
    # KPI CALCULATIONS
    # -----------------------------
    total_revenue = filtered_df["Revenue"].sum()

    total_orders = filtered_df["Order_ID"].nunique()

    total_quantity = filtered_df["Quantity"].sum()

    average_order_value = (
        total_revenue / total_orders
        if total_orders > 0
        else 0
    )

    # -----------------------------
    # KPI CARDS
    # -----------------------------
    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "💰 Total Revenue",
        f"₹{total_revenue:,.0f}"
    )

    col2.metric(
        "📦 Total Orders",
        f"{total_orders:,}"
    )

    col3.metric(
        "🛒 Quantity Sold",
        f"{total_quantity:,.0f}"
    )

    col4.metric(
        "💵 Average Order Value",
        f"₹{average_order_value:,.0f}"
    )

    st.divider()

    # -----------------------------
    # REVENUE BY CATEGORY
    # -----------------------------
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📊 Revenue by Category")

        category_data = (
            filtered_df
            .groupby("Category")["Revenue"]
            .sum()
            .reset_index()
        )

        fig_category = px.bar(
            category_data,
            x="Category",
            y="Revenue",
            title="Revenue by Category",
            labels={
                "Category": "Category",
                "Revenue": "Revenue (₹)"
            }
        )

        st.plotly_chart(
            fig_category,
            use_container_width=True
        )

    # -----------------------------
    # REVENUE BY CITY
    # -----------------------------
    with col2:
        st.subheader("🏙️ Revenue by City")

        city_data = (
            filtered_df
            .groupby("City")["Revenue"]
            .sum()
            .reset_index()
            .sort_values(
                "Revenue",
                ascending=False
            )
        )

        fig_city = px.bar(
            city_data,
            x="City",
            y="Revenue",
            title="Revenue by City",
            labels={
                "City": "City",
                "Revenue": "Revenue (₹)"
            }
        )

        st.plotly_chart(
            fig_city,
            use_container_width=True
        )

    # -----------------------------
    # ORDER STATUS
    # -----------------------------
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🚚 Order Status")

        status_data = (
            filtered_df["Status"]
            .value_counts()
            .rename_axis("Status")
            .reset_index(name="Orders")
        )

        fig_status = px.pie(
            status_data,
            names="Status",
            values="Orders",
            title="Order Status"
        )

        st.plotly_chart(
            fig_status,
            use_container_width=True
        )

    # -----------------------------
    # TOP PRODUCTS
    # -----------------------------
    with col2:
        st.subheader("🏆 Top Products")

        product_data = (
            filtered_df
            .groupby("Product")["Revenue"]
            .sum()
            .reset_index()
            .sort_values(
                "Revenue",
                ascending=False
            )
            .head(10)
        )

        fig_product = px.bar(
            product_data,
            x="Revenue",
            y="Product",
            orientation="h",
            title="Top 10 Products",
            labels={
                "Revenue": "Revenue (₹)",
                "Product": "Product"
            }
        )

        # Display the highest-revenue product at the top
        fig_product.update_layout(
            yaxis={"categoryorder": "total ascending"}
        )

        st.plotly_chart(
            fig_product,
            use_container_width=True
        )

    # -----------------------------
    # PRODUCT TABLE
    # -----------------------------
    st.subheader("📋 Product Performance")

    product_table = (
        filtered_df
        .groupby("Product")
        .agg(
            Quantity_Sold=("Quantity", "sum"),
            Revenue=("Revenue", "sum"),
            Orders=("Order_ID", "nunique")
        )
        .reset_index()
        .sort_values(
            "Revenue",
            ascending=False
        )
    )

    st.dataframe(
        product_table,
        use_container_width=True,
        hide_index=True
    )

    # -----------------------------
    # RAW DATA
    # -----------------------------
    with st.expander("📄 View Order Data"):

        st.dataframe(
            filtered_df,
            use_container_width=True,
            hide_index=True
        )

    # -----------------------------
    # DOWNLOAD FILTERED DATA
    # -----------------------------
    csv = filtered_df.to_csv(index=False)

    st.download_button(
        label="⬇️ Download Filtered CSV",
        data=csv,
        file_name="filtered_ecommerce_sales.csv",
        mime="text/csv"
    )

# =========================================================
# INVENTORY DASHBOARD - UNDER DEVELOPMENT
# =========================================================

elif selection == "Inventory Data 🚧 (Coming Soon)":

    st.header("📦 Inventory Dashboard")

    st.info(
        "🚧 This section is currently under development. "
        "The Inventory Dashboard will be available in a future update."
    )

    st.markdown(
        """
        ### Planned Features

        The following features are planned for the
        Inventory Dashboard:

        - 📦 **Stock Overview:** Track total products
          and available stock.
        - 📊 **Category Analysis:** Analyze stock levels
          across product categories.
        - 🚚 **Supplier Performance:** View stock distribution
          by supplier.
        - ⚠️ **Low Stock Alerts:** Identify products
          that require restocking.
        - 📈 **Stock Status Analysis:** Monitor inventory
          availability and stock conditions.
        - 📋 **Inventory Reports:** View inventory records
          and export filtered data.
        """
    )

    st.divider()

    st.subheader("Development Status")

    st.progress(0.25)

    st.caption(
        "Inventory Dashboard — Work in Progress. "
        "Features are planned and implementation is ongoing."
    )
