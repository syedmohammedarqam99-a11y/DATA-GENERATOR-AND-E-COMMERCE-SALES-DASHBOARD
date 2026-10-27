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
        "Inventory Data"
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
    df = pd.read_csv(uploaded_file)

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

    # Convert numeric columns
    df["Quantity"] = pd.to_numeric(
        df["Quantity"],
        errors="coerce"
    )

    df["Price"] = pd.to_numeric(
        df["Price"],
        errors="coerce"
    )

    df["Revenue"] = pd.to_numeric(
        df["Revenue"],
        errors="coerce"
    )

    df = df.dropna()

    # -----------------------------
    # SIDEBAR FILTERS
    # -----------------------------
    st.sidebar.header("🔎 Filters")

    selected_category = st.sidebar.multiselect(
        "Category",
        df["Category"].unique(),
        default=df["Category"].unique()
    )

    selected_city = st.sidebar.multiselect(
        "City",
        df["City"].unique(),
        default=df["City"].unique()
    )

    selected_status = st.sidebar.multiselect(
        "Status",
        df["Status"].unique(),
        default=df["Status"].unique()
    )

    # Apply filters
    filtered_df = df[
        (df["Category"].isin(selected_category)) &
        (df["City"].isin(selected_city)) &
        (df["Status"].isin(selected_status))
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
            title="Revenue by Category"
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
            title="Revenue by City"
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
            .reset_index()
        )

        status_data.columns = [
            "Status",
            "Orders"
        ]

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
            title="Top 10 Products"
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
        use_container_width=True
    )

    # -----------------------------
    # RAW DATA
    # -----------------------------
    with st.expander("📄 View Order Data"):
        st.dataframe(
            filtered_df,
            use_container_width=True
        )

    # -----------------------------
    # DOWNLOAD
    # -----------------------------
    csv = filtered_df.to_csv(index=False)

    st.download_button(
        "⬇️ Download Filtered CSV",
        csv,
        "filtered_ecommerce_sales.csv",
        "text/csv"
    )


# =========================================================
# INVENTORY DASHBOARD
# =========================================================

elif selection == "Inventory Data":

    st.header("📦 Inventory Dashboard")

    # Upload CSV
    uploaded_file = st.file_uploader(
        "Upload your inventory CSV file",
        type=["csv"],
        key="inventory_upload"
    )

    if uploaded_file is None:
        st.info("Please upload a CSV file.")
        st.stop()

    # Read CSV
    df = pd.read_csv(uploaded_file)

    # Required columns
    required_columns = [
        "Product_Name",
        "Category",
        "Stock_Quantity",
        "New_stock Status",
        "Supplier"
    ]

    missing = [
        column for column in required_columns
        if column not in df.columns
    ]

    if missing:
        st.error(
            "Missing columns: " + ", ".join(missing)
        )
        st.stop()

    # Convert stock quantity to numeric
    df["Stock_Quantity"] = pd.to_numeric(
        df["Stock_Quantity"],
        errors="coerce"
    )

    df = df.dropna(
        subset=["Stock_Quantity"]
    )

    # -----------------------------
    # SIDEBAR FILTERS
    # -----------------------------
    st.sidebar.header("🔎 Inventory Filters")

    selected_category = st.sidebar.multiselect(
        "Category",
        df["Category"].unique(),
        default=df["Category"].unique()
    )

    selected_supplier = st.sidebar.multiselect(
        "Supplier",
        df["Supplier"].unique(),
        default=df["Supplier"].unique()
    )

    selected_stock_status = st.sidebar.multiselect(
        "Stock Status",
        df["New_stock Status"].unique(),
        default=df["New_stock Status"].unique()
    )

    # Apply filters
    filtered_inventory = df[
        (df["Category"].isin(selected_category)) &
        (df["Supplier"].isin(selected_supplier)) &
        (df["New_stock Status"].isin(selected_stock_status))
    ]

    # -----------------------------
    # INVENTORY KPIs
    # -----------------------------
    total_products = filtered_inventory["Product_Name"].nunique()

    total_stock = filtered_inventory["Stock_Quantity"].sum()

    total_suppliers = filtered_inventory["Supplier"].nunique()

    out_of_stock = (
        filtered_inventory["Stock_Quantity"] == 0
    ).sum()

    # -----------------------------
    # KPI CARDS
    # -----------------------------
    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "📦 Total Products",
        f"{total_products:,}"
    )

    col2.metric(
        "📊 Total Stock",
        f"{total_stock:,.0f}"
    )

    col3.metric(
        "🚚 Suppliers",
        f"{total_suppliers:,}"
    )

    col4.metric(
        "⚠️ Out of Stock",
        f"{out_of_stock:,}"
    )

    st.divider()

    # -----------------------------
    # STOCK BY CATEGORY
    # -----------------------------
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📊 Stock by Category")

        category_stock = (
            filtered_inventory
            .groupby("Category")["Stock_Quantity"]
            .sum()
            .reset_index()
            .sort_values(
                "Stock_Quantity",
                ascending=False
            )
        )

        fig_category_stock = px.bar(
            category_stock,
            x="Category",
            y="Stock_Quantity",
            title="Stock Quantity by Category"
        )

        st.plotly_chart(
            fig_category_stock,
            use_container_width=True
        )

    # -----------------------------
    # STOCK STATUS
    # -----------------------------
    with col2:
        st.subheader("📦 Stock Status")

        stock_status = (
            filtered_inventory["New_stock Status"]
            .value_counts()
            .reset_index()
        )

        stock_status.columns = [
            "Status",
            "Products"
        ]

        fig_stock_status = px.pie(
            stock_status,
            names="Status",
            values="Products",
            title="Inventory Stock Status"
        )

        st.plotly_chart(
            fig_stock_status,
            use_container_width=True
        )

    # -----------------------------
    # STOCK BY SUPPLIER
    # -----------------------------
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🚚 Stock by Supplier")

        supplier_stock = (
            filtered_inventory
            .groupby("Supplier")["Stock_Quantity"]
            .sum()
            .reset_index()
            .sort_values(
                "Stock_Quantity",
                ascending=False
            )
        )

        fig_supplier = px.bar(
            supplier_stock,
            x="Supplier",
            y="Stock_Quantity",
            title="Stock Quantity by Supplier"
        )

        st.plotly_chart(
            fig_supplier,
            use_container_width=True
        )

    # -----------------------------
    # LOW STOCK PRODUCTS
    # -----------------------------
    with col2:
        st.subheader("⚠️ Low Stock Products")

        low_stock = (
            filtered_inventory
            .sort_values(
                "Stock_Quantity",
                ascending=True
            )
            .head(10)
        )

        fig_low_stock = px.bar(
            low_stock,
            x="Stock_Quantity",
            y="Product_Name",
            orientation="h",
            title="Products with Lowest Stock"
        )

        st.plotly_chart(
            fig_low_stock,
            use_container_width=True
        )

    # -----------------------------
    # INVENTORY TABLE
    # -----------------------------
    st.subheader("📋 Inventory Details")

    inventory_table = (
        filtered_inventory[
            [
                "Product_Name",
                "Category",
                "Stock_Quantity",
                "New_stock Status",
                "Supplier"
            ]
        ]
        .sort_values(
            "Stock_Quantity",
            ascending=True
        )
    )

    st.dataframe(
        inventory_table,
        use_container_width=True
    )

    # -----------------------------
    # RAW INVENTORY DATA
    # -----------------------------
    with st.expander("📄 View Inventory Data"):
        st.dataframe(
            filtered_inventory,
            use_container_width=True
        )

    # -----------------------------
    # DOWNLOAD
    # -----------------------------
    inventory_csv = filtered_inventory.to_csv(
        index=False
    )

    st.download_button(
        "⬇️ Download Filtered Inventory CSV",
        inventory_csv,
        "filtered_inventory.csv",
        "text/csv"
    )