import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import numpy as np
from utils.data_generator import DataGenerator
from utils.alert_system import AlertSystem

# Page configuration
st.set_page_config(
    page_title="Manufacturing Scrap Monitor",
    page_icon="🏭",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize data generator and alert system
@st.cache_resource
def get_data_generator():
    return DataGenerator()

@st.cache_resource
def get_alert_system():
    return AlertSystem()

data_gen = get_data_generator()
alert_system = get_alert_system()

# Main dashboard header
st.title("🏭 Manufacturing Scrap Monitoring Dashboard")
st.markdown("---")

# Sidebar for navigation and controls
with st.sidebar:
    st.header("Dashboard Controls")
    
    # Role selection
    user_role = st.selectbox(
        "Select User Role",
        ["Operator", "Engineer", "Management"],
        index=1
    )
    
    # Time range selection
    time_range = st.selectbox(
        "Time Range",
        ["Last Hour", "Last 8 Hours", "Last 24 Hours", "Last Week"],
        index=2
    )
    
    # Machine filter
    machines = data_gen.get_machine_list()
    selected_machines = st.multiselect(
        "Select Machines",
        machines,
        default=machines[:3]
    )
    
    # Auto-refresh toggle
    auto_refresh = st.checkbox("Auto Refresh (30s)", value=True)
    
    if auto_refresh:
        st.empty()  # Placeholder for refresh timer

# Get current data based on selections
current_data = data_gen.get_real_time_data(selected_machines, time_range)

# Alert banner
alerts = alert_system.check_alerts(current_data)
if alerts:
    for alert in alerts:
        if alert['level'] == 'critical':
            st.error(f"🚨 {alert['message']}")
        elif alert['level'] == 'warning':
            st.warning(f"⚠️ {alert['message']}")
        else:
            st.info(f"ℹ️ {alert['message']}")

# Key metrics row
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    scrap_rate = current_data['scrap_quantity'].sum() / current_data['total_production'].sum() * 100
    st.metric(
        label="Overall Scrap Rate",
        value=f"{scrap_rate:.2f}%",
        delta=f"{scrap_rate - 2.5:.2f}%"
    )

with col2:
    scrap_cost = (current_data['scrap_quantity'] * current_data['unit_cost']).sum()
    st.metric(
        label="Scrap Cost",
        value=f"${scrap_cost:,.0f}",
        delta=f"${scrap_cost - 15000:,.0f}"
    )

with col3:
    oee_impact = 100 - (scrap_rate * 2.5)  # Simplified OEE calculation
    st.metric(
        label="OEE Impact",
        value=f"{oee_impact:.1f}%",
        delta=f"{oee_impact - 95:.1f}%"
    )

with col4:
    avg_downtime = current_data['downtime_minutes'].mean()
    st.metric(
        label="Avg Downtime",
        value=f"{avg_downtime:.0f} min",
        delta=f"{avg_downtime - 25:.0f} min"
    )

with col5:
    total_production = current_data['total_production'].sum()
    st.metric(
        label="Total Production",
        value=f"{total_production:,.0f}",
        delta=f"{total_production - 50000:,.0f}"
    )

# Main dashboard content
col_left, col_right = st.columns([2, 1])

with col_left:
    st.subheader("Real-Time Scrap Rate Trend")
    
    # Create time series plot
    fig_trend = px.line(
        current_data,
        x='timestamp',
        y='scrap_rate',
        color='machine_id',
        title="Scrap Rate by Machine Over Time",
        labels={'scrap_rate': 'Scrap Rate (%)', 'timestamp': 'Time'}
    )
    fig_trend.add_hline(y=3.0, line_dash="dash", line_color="red", 
                       annotation_text="Target Threshold (3%)")
    fig_trend.update_layout(height=400)
    st.plotly_chart(fig_trend, use_container_width=True)
    
    # Scrap by machine breakdown
    st.subheader("Scrap Analysis by Machine")
    machine_summary = current_data.groupby('machine_id').agg({
        'scrap_quantity': 'sum',
        'total_production': 'sum',
        'scrap_rate': 'mean'
    }).reset_index()
    
    fig_machine = px.bar(
        machine_summary,
        x='machine_id',
        y='scrap_rate',
        title="Average Scrap Rate by Machine",
        color='scrap_rate',
        color_continuous_scale='RdYlBu_r'
    )
    fig_machine.update_layout(height=300)
    st.plotly_chart(fig_machine, use_container_width=True)

with col_right:
    st.subheader("Top Scrap Root Causes")
    
    # Generate root cause data
    root_causes = data_gen.get_root_causes()
    fig_causes = px.pie(
        root_causes,
        values='count',
        names='cause',
        title="Scrap Root Causes Distribution"
    )
    fig_causes.update_layout(height=300)
    st.plotly_chart(fig_causes, use_container_width=True)
    
    st.subheader("Shift Performance")
    shift_data = data_gen.get_shift_data()
    
    for shift in shift_data:
        with st.container():
            st.write(f"**{shift['shift']}**")
            scrap_pct = shift['scrap_rate']
            if scrap_pct > 4:
                st.error(f"Scrap Rate: {scrap_pct:.1f}%")
            elif scrap_pct > 2.5:
                st.warning(f"Scrap Rate: {scrap_pct:.1f}%")
            else:
                st.success(f"Scrap Rate: {scrap_pct:.1f}%")

# Bottom section - Additional insights
st.markdown("---")
st.subheader("Recent Anomalies & Insights")

col1, col2 = st.columns(2)

with col1:
    st.info("""
    **🔍 Pattern Detection:**
    - Scrap spikes detected after 45+ minutes of downtime
    - Machine M003 showing 15% higher scrap rate than baseline
    - Temperature fluctuations correlating with quality issues
    """)

with col2:
    st.warning("""
    **📈 Predictive Insights:**
    - Forecasted 12% increase in scrap for next shift
    - Recommend calibrating Machine M001 temperature sensors
    - Operator training needed for Product Type B processes
    """)

# Data refresh handling
if auto_refresh:
    import time
    time.sleep(30)
    st.rerun()
