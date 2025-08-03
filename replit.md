# Overview

A comprehensive manufacturing scrap monitoring dashboard built with Streamlit that provides real-time monitoring, predictive analytics, and alert management for manufacturing operations. The system tracks scrap rates, production metrics, machine performance, and costs across multiple manufacturing lines with role-based access control for operators, engineers, and management.

# User Preferences

Preferred communication style: Simple, everyday language.

# System Architecture

## Frontend Architecture
- **Framework**: Streamlit with multi-page application structure
- **Layout**: Wide layout with sidebar navigation and role-based controls
- **Visualization**: Plotly Express and Plotly Graph Objects for interactive charts and real-time data visualization
- **Pages**: Modular page structure with separate modules for real-time monitoring, predictive analytics, alerts management, and historical analysis
- **State Management**: Streamlit's native caching with `@st.cache_resource` decorators for performance optimization

## Backend Architecture
- **Data Generation**: Custom `DataGenerator` class simulating real manufacturing data with realistic patterns and variations
- **Machine Learning**: `ScrapPredictor` class using scikit-learn with multiple model types (Random Forest, Linear Regression, Neural Networks, Ensemble)
- **Alert System**: Comprehensive `AlertSystem` class with configurable thresholds, escalation rules, and notification management
- **Data Processing**: Pandas for data manipulation and NumPy for numerical computations

## Data Management
- **Data Sources**: Simulated manufacturing data including machine metrics, production rates, scrap rates, temperatures, pressures, and operator information
- **Time Series Data**: Real-time data streams with configurable refresh rates and historical data analysis
- **Feature Engineering**: Automated feature creation for machine learning models including lag features, rolling averages, and time-based features

## User Interface Components
- **Role-Based Access**: Different views and controls for Operators, Engineers, and Management
- **Real-Time Monitoring**: Live KPIs, machine status indicators, and streaming data visualization
- **Predictive Analytics**: ML-powered forecasting with confidence intervals and feature importance analysis
- **Alert Configuration**: Customizable thresholds, notification settings, and escalation workflows
- **Historical Analysis**: Deep-dive analytics with various grouping options and trend analysis

## Security and Performance
- **Caching Strategy**: Resource-level caching for data generators and model instances
- **Performance Optimization**: Efficient data processing with vectorized operations and optimized chart rendering
- **Modular Design**: Separated concerns with utility classes for different functional areas

# External Dependencies

## Python Libraries
- **streamlit**: Web application framework for the dashboard interface
- **pandas**: Data manipulation and analysis library
- **plotly**: Interactive visualization library for charts and graphs
- **numpy**: Numerical computing library for mathematical operations
- **scikit-learn**: Machine learning library for predictive models and data preprocessing
- **datetime**: Standard library for time and date operations

## Data Dependencies
- **Simulated Data**: Self-contained data generation system that doesn't require external databases
- **Machine Learning Models**: In-memory model training and prediction without external ML services
- **Alert System**: Self-contained notification and escalation system

## Potential Integrations
- **Email/SMS Services**: Currently simulated but designed for integration with notification providers
- **Database Systems**: Architecture supports future integration with manufacturing databases
- **External APIs**: Extensible design for connecting to real manufacturing equipment APIs
- **Authentication Systems**: Framework ready for enterprise authentication integration