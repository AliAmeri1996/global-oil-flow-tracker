import streamlit as st
import plotly.graph_objects as go
import requests 
import pandas as pd



st.set_page_config(page_title="Global Oil Flow Tracker", layout="wide")
st.markdown("<h1 style='text-align: center;'>Global Oil Flow Tracker</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Explore global oil production, consumption and trade flows in real time.</p>", unsafe_allow_html=True)


# all the countries that produce oil in the world 
producers = {
    'USA': {'lat': 37.09, 'lon': -95.71, 'production': 13.3},
    'Saudi Arabia': {'lat': 23.89, 'lon': 45.08, 'production': 10.5},
    'Russia': {'lat': 61.52, 'lon': 105.31, 'production': 10.1},
    'Canada': {'lat': 56.13, 'lon': -106.34, 'production': 5.6},
    'Iraq': {'lat': 33.22, 'lon': 43.67, 'production': 4.5},
    'China': {'lat': 35.86, 'lon': 104.19, 'production': 4.2},
    'UAE': {'lat': 23.42, 'lon': 53.84, 'production': 4.0},
    'Iran': {'lat': 32.42, 'lon': 53.68, 'production': 3.8},
    'Brazil': {'lat': -14.23, 'lon': -51.92, 'production': 3.5},
    'Kuwait': {'lat': 29.31, 'lon': 47.48, 'production': 2.9},
    'Mexico': {'lat': 23.63, 'lon': -102.55, 'production': 1.9},
    'Kazakhstan': {'lat': 48.01, 'lon': 66.92, 'production': 1.9},
    'Norway': {'lat': 60.47, 'lon': 8.46, 'production': 1.8},
    'Nigeria': {'lat': 9.08, 'lon': 8.67, 'production': 1.5},
    'Libya': {'lat': 26.33, 'lon': 17.22, 'production': 1.2},
    'Angola': {'lat': -11.20, 'lon': 17.87, 'production': 1.1},
    'Oman': {'lat': 21.51, 'lon': 55.92, 'production': 1.1},
    'Algeria': {'lat': 28.03, 'lon': 1.65, 'production': 1.0},
    'India': {'lat': 20.59, 'lon': 78.96, 'production': 0.8},
    'Venezuela': {'lat': 6.42, 'lon': -66.58, 'production': 0.8},
    'Colombia': {'lat': 4.57, 'lon': -74.29, 'production': 0.8},
    'UK': {'lat': 55.37, 'lon': -3.43, 'production': 0.8},
    'Azerbaijan': {'lat': 40.14, 'lon': 47.57, 'production': 0.7},
    'Argentina': {'lat': -38.41, 'lon': -63.61, 'production': 0.7},
    'Malaysia': {'lat': 4.21, 'lon': 108.96, 'production': 0.6},
    'Qatar': {'lat': 25.35, 'lon': 51.18, 'production': 0.6},
    'Egypt': {'lat': 26.82, 'lon': 30.80, 'production': 0.6},
    'Indonesia': {'lat': -0.78, 'lon': 113.92, 'production': 0.6},
    'Ecuador': {'lat': -1.83, 'lon': -78.18, 'production': 0.5},
    'Australia': {'lat': -25.27, 'lon': 133.77, 'production': 0.4},
    'Turkmenistan': {'lat': 38.96, 'lon': 59.55, 'production': 0.3},
    'Thailand': {'lat': 15.87, 'lon': 100.99, 'production': 0.3},
    'Congo': {'lat': -0.22, 'lon': 15.82, 'production': 0.3},
    'Vietnam': {'lat': 14.05, 'lon': 108.27, 'production': 0.2},
    'Ghana': {'lat': 7.94, 'lon': -1.02, 'production': 0.2},
    'Bahrain': {'lat': 26.00, 'lon': 50.55, 'production': 0.2},
    'Peru': {'lat': -9.18, 'lon': -75.01, 'production': 0.1},
    'Trinidad and Tobago': {'lat': 10.69, 'lon': -61.22, 'production': 0.1},
    'Denmark': {'lat': 56.26, 'lon': 9.50, 'production': 0.1},
    'Gabon': {'lat': -0.80, 'lon': 11.60, 'production': 0.2},
    'Equatorial Guinea': {'lat': 1.65, 'lon': 10.26, 'production': 0.1},
    'Brunei': {'lat': 4.53, 'lon': 114.72, 'production': 0.1},
    'Chad': {'lat': 15.45, 'lon': 18.73, 'production': 0.1},
    'Sudan': {'lat': 12.86, 'lon': 30.21, 'production': 0.1},
    'South Sudan': {'lat': 6.87, 'lon': 31.30, 'production': 0.1},
    'Romania': {'lat': 45.94, 'lon': 24.96, 'production': 0.07},
    'Ukraine': {'lat': 48.37, 'lon': 31.16, 'production': 0.07},
    'Uzbekistan': {'lat': 41.37, 'lon': 64.58, 'production': 0.1},
    'Cameroon': {'lat': 3.84, 'lon': 11.50, 'production': 0.07},
    'Bolivia': {'lat': -16.29, 'lon': -63.58, 'production': 0.05},
    'Yemen': {'lat': 15.55, 'lon': 48.51, 'production': 0.05},
    'Syria': {'lat': 34.80, 'lon': 38.99, 'production': 0.05},
    'Tunisia': {'lat': 33.88, 'lon': 9.53, 'production': 0.05},
    'Papua New Guinea': {'lat': -6.31, 'lon': 143.95, 'production': 0.05},
}




# the countries that consume the oil the most 
consumers = {
    'USA': {'lat': 37.09, 'lon': -95.71, 'consumption': 20.0},
    'China': {'lat': 35.86, 'lon': 104.19, 'consumption': 15.2},
    'India': {'lat': 20.59, 'lon': 78.96, 'consumption': 5.2},
    'Japan': {'lat': 36.20, 'lon': 138.25, 'consumption': 3.2},
    'Saudi Arabia': {'lat': 23.89, 'lon': 45.08, 'consumption': 3.1},
    'Russia': {'lat': 61.52, 'lon': 105.31, 'consumption': 3.0},
    'South Korea': {'lat': 35.90, 'lon': 127.76, 'consumption': 2.8},
    'Canada': {'lat': 56.13, 'lon': -106.34, 'consumption': 2.5},
    'Brazil': {'lat': -14.23, 'lon': -51.92, 'consumption': 2.4},
    'Germany': {'lat': 51.16, 'lon': 10.45, 'consumption': 2.1},
    'Mexico': {'lat': 23.63, 'lon': -102.55, 'consumption': 1.9},
    'Iran': {'lat': 32.42, 'lon': 53.68, 'consumption': 1.8},
    'UAE': {'lat': 23.42, 'lon': 53.84, 'consumption': 1.0},
    'UK': {'lat': 55.37, 'lon': -3.43, 'consumption': 1.5},
    'France': {'lat': 46.22, 'lon': 2.21, 'consumption': 1.5},
    'Italy': {'lat': 41.87, 'lon': 12.56, 'consumption': 1.2},
    'Spain': {'lat': 40.46, 'lon': -3.74, 'consumption': 1.2},
    'Indonesia': {'lat': -0.78, 'lon': 113.92, 'consumption': 1.6},
    'Australia': {'lat': -25.27, 'lon': 133.77, 'consumption': 1.0},
    'Thailand': {'lat': 15.87, 'lon': 100.99, 'consumption': 1.3},
    'Turkey': {'lat': 38.96, 'lon': 35.24, 'consumption': 1.0},
    'Netherlands': {'lat': 52.13, 'lon': 5.29, 'consumption': 0.9},
    'Malaysia': {'lat': 4.21, 'lon': 108.96, 'consumption': 0.8},
    'Argentina': {'lat': -38.41, 'lon': -63.61, 'consumption': 0.7},
    'Pakistan': {'lat': 30.37, 'lon': 69.34, 'consumption': 0.6},
    'Egypt': {'lat': 26.82, 'lon': 30.80, 'consumption': 0.6},
    'Poland': {'lat': 51.91, 'lon': 19.14, 'consumption': 0.6},
    'Belgium': {'lat': 50.50, 'lon': 4.46, 'consumption': 0.6},
    'Vietnam': {'lat': 14.05, 'lon': 108.27, 'consumption': 0.5},
    'Philippines': {'lat': 12.87, 'lon': 121.77, 'consumption': 0.5},
    'Colombia': {'lat': 4.57, 'lon': -74.29, 'consumption': 0.4},
    'Venezuela': {'lat': 6.42, 'lon': -66.58, 'consumption': 0.4},
    'Kuwait': {'lat': 29.31, 'lon': 47.48, 'consumption': 0.4},
    'Nigeria': {'lat': 9.08, 'lon': 8.67, 'consumption': 0.4},
    'Algeria': {'lat': 28.03, 'lon': 1.65, 'consumption': 0.4},
    'Sweden': {'lat': 60.12, 'lon': 18.64, 'consumption': 0.3},
    'Norway': {'lat': 60.47, 'lon': 8.46, 'consumption': 0.3},
    'Romania': {'lat': 45.94, 'lon': 24.96, 'consumption': 0.3},
    'Czech Republic': {'lat': 49.81, 'lon': 15.47, 'consumption': 0.2},
    'Hungary': {'lat': 47.16, 'lon': 19.50, 'consumption': 0.2},
    'Greece': {'lat': 39.07, 'lon': 21.82, 'consumption': 0.3},
    'Portugal': {'lat': 39.39, 'lon': -8.22, 'consumption': 0.2},
    'Austria': {'lat': 47.51, 'lon': 14.55, 'consumption': 0.2},
    'Switzerland': {'lat': 46.81, 'lon': 8.22, 'consumption': 0.2},
    'Bangladesh': {'lat': 23.68, 'lon': 90.35, 'consumption': 0.1},
    'Chile': {'lat': -35.67, 'lon': -71.54, 'consumption': 0.3},
    'Peru': {'lat': -9.18, 'lon': -75.01, 'consumption': 0.2},
    'Ecuador': {'lat': -1.83, 'lon': -78.18, 'consumption': 0.2},
    'Morocco': {'lat': 31.79, 'lon': -7.09, 'consumption': 0.2},
    'Israel': {'lat': 31.04, 'lon': 34.85, 'consumption': 0.2},
    'Singapore': {'lat': 1.35, 'lon': 103.81, 'consumption': 1.3},
    'Kazakhstan': {'lat': 48.01, 'lon': 66.92, 'consumption': 0.3},
    'Ukraine': {'lat': 48.37, 'lon': 31.16, 'consumption': 0.2},
    'New Zealand': {'lat': -40.90, 'lon': 174.88, 'consumption': 0.2},
    'Denmark': {'lat': 56.26, 'lon': 9.50, 'consumption': 0.2},
    'Finland': {'lat': 61.92, 'lon': 25.74, 'consumption': 0.2},
    'Iraq': {'lat': 33.22, 'lon': 43.67, 'consumption': 0.8},
    'Oman': {'lat': 21.51, 'lon': 55.92, 'consumption': 0.2},
    'Qatar': {'lat': 25.35, 'lon': 51.18, 'consumption': 0.3},
    'Myanmar': {'lat': 21.91, 'lon': 95.95, 'consumption': 0.1},
    'Sri Lanka': {'lat': 7.87, 'lon': 80.77, 'consumption': 0.1},
    'Kenya': {'lat': -0.02, 'lon': 37.90, 'consumption': 0.1},
    'Ethiopia': {'lat': 9.14, 'lon': 40.48, 'consumption': 0.1},
    'Ghana': {'lat': 7.94, 'lon': -1.02, 'consumption': 0.1},
    'Tanzania': {'lat': -6.36, 'lon': 34.88, 'consumption': 0.1},
    'Ivory Coast': {'lat': 7.53, 'lon': -5.54, 'consumption': 0.1},
    'Cameroon': {'lat': 3.84, 'lon': 11.50, 'consumption': 0.1},
    'Bolivia': {'lat': -16.29, 'lon': -63.58, 'consumption': 0.1},
    'Paraguay': {'lat': -23.44, 'lon': -58.44, 'consumption': 0.1},
    'Uruguay': {'lat': -32.52, 'lon': -55.76, 'consumption': 0.1},
    'Cuba': {'lat': 21.52, 'lon': -77.78, 'consumption': 0.1},
    'Jordan': {'lat': 30.58, 'lon': 36.23, 'consumption': 0.1},
    'Lebanon': {'lat': 33.85, 'lon': 35.86, 'consumption': 0.1},
    'Tunisia': {'lat': 33.88, 'lon': 9.53, 'consumption': 0.1},
    'Libya': {'lat': 26.33, 'lon': 17.22, 'consumption': 0.2},
    'Sudan': {'lat': 12.86, 'lon': 30.21, 'consumption': 0.1},
    'Angola': {'lat': -11.20, 'lon': 17.87, 'consumption': 0.1},
    'Azerbaijan': {'lat': 40.14, 'lon': 47.57, 'consumption': 0.1},
    'Uzbekistan': {'lat': 41.37, 'lon': 64.58, 'consumption': 0.1},
    'Turkmenistan': {'lat': 38.96, 'lon': 59.55, 'consumption': 0.1},
}


# the check points data
chokepoints = {
    'Strait of Hormuz': {'lat': 26.57, 'lon': 56.25, 'barrels': 21, 'percentage': 20, 'description': '20% of global oil supply passes through here daily — key Middle East export route'},
    'Suez Canal': {'lat': 30.42, 'lon': 32.34, 'barrels': 9, 'percentage': 9, 'description': 'Connects Red Sea to Mediterranean — vital for Middle East to Europe flows'},
    'Strait of Malacca': {'lat': 2.50, 'lon': 101.20, 'barrels': 16, 'percentage': 15, 'description': 'Key route from Middle East to China, Japan and South Korea'},
    'Bosphorus Strait': {'lat': 41.12, 'lon': 29.07, 'barrels': 3, 'percentage': 3, 'description': 'Only exit for Russian and Caspian oil into Mediterranean'},
    'Cape of Good Hope': {'lat': -34.35, 'lon': 18.47, 'barrels': 6, 'percentage': 6, 'description': 'Alternative route avoiding Suez Canal — used when Suez is blocked or too costly'},
    'Danish Straits': {'lat': 57.50, 'lon': 10.50, 'barrels': 3, 'percentage': 3, 'description': 'Key route for Russian oil exports from Baltic Sea ports'},
    'Panama Canal': {'lat': 9.08, 'lon': -79.68, 'barrels': 1, 'percentage': 1, 'description': 'Connects Pacific and Atlantic — used for US and Latin American oil flows'},
}

#major trade routes

trade_routes = [
    {'from': 'Saudi Arabia', 'to': 'China', 'barrels': 1.7},
    {'from': 'Saudi Arabia', 'to': 'Japan', 'barrels': 1.2},
    {'from': 'Saudi Arabia', 'to': 'South Korea', 'barrels': 0.9},
    {'from': 'Saudi Arabia', 'to': 'India', 'barrels': 0.8},
    {'from': 'Russia', 'to': 'China', 'barrels': 2.0},
    {'from': 'Russia', 'to': 'Germany', 'barrels': 0.7},
    {'from': 'Russia', 'to': 'India', 'barrels': 1.5},
    {'from': 'Iraq', 'to': 'China', 'barrels': 1.2},
    {'from': 'Iraq', 'to': 'India', 'barrels': 0.9},
    {'from': 'UAE', 'to': 'Japan', 'barrels': 0.8},
    {'from': 'UAE', 'to': 'China', 'barrels': 0.7},
    {'from': 'USA', 'to': 'China', 'barrels': 0.5},
    {'from': 'USA', 'to': 'Japan', 'barrels': 0.4},
    {'from': 'Canada', 'to': 'USA', 'barrels': 3.5},
    {'from': 'Nigeria', 'to': 'India', 'barrels': 0.3},
    {'from': 'Angola', 'to': 'China', 'barrels': 0.6},
]


st.markdown("---")
# sidebar for view selection
view=st.sidebar.radio("Select View", ["Oil Producers","Oil Consumers", "Trade Routes", "Chokepoints"])

fig=go.Figure()

if view == "Oil Producers":
    total_production = sum(d['production'] for d in producers.values())
    st.sidebar.markdown("### Production Stats")
    for country, data in producers.items():
        percentage = (data['production'] / total_production) * 100
        st.sidebar.markdown(f"**{country}:** {data['production']}M bpd ({percentage:.1f}%)")
        fig.add_trace(go.Scattergeo(
            lat=[data['lat']],
            lon=[data['lon']],
            text=f"{country}<br>Production: {data['production']}M bpd ({percentage:.1f}%)",
            marker=dict(size=data['production']*3, color='red', opacity=0.7),
            name=country,
            mode='markers'
        ))


elif view == "Oil Producers":
    total_production = sum(d['production'] for d in producers.values())
    st.sidebar.markdown("### Production Stats")
    for country, data in producers.items():
        percentage = (data['production'] / total_production) * 100
        st.sidebar.markdown(f"**{country}:** {data['production']}M bpd ({percentage:.1f}%)")


elif view == "Oil Consumers":
    total_consumption = sum(d['consumption'] for d in consumers.values())
    st.sidebar.markdown("### Consumption Stats")
    for country, data in consumers.items():
        percentage = (data['consumption'] / total_consumption) * 100
        st.sidebar.markdown(f"**{country}:** {data['consumption']}M bpd ({percentage:.1f}%)")
        fig.add_trace(go.Scattergeo(
            lat=[data['lat']],
            lon=[data['lon']],
            text=f"{country}<br>Consumption: {data['consumption']}M bpd ({percentage:.1f}%)",
            marker=dict(size=data['consumption']*3, color='blue', opacity=0.7),
            name=country,
            mode='markers'
        ))


elif view == "Chokepoints":
    for name, data in chokepoints.items():
        fig.add_trace(go.Scattergeo(
            lat=[data['lat']],
            lon=[data['lon']],
            text=f"{name}<br>Oil flow: {data['barrels']}M bpd<br>{data['percentage']}% of global supply<br>{data['description']}",
            marker=dict(size=15, color='orange', symbol='diamond', opacity=0.9),
            name=name,
            mode='markers'
        ))




fig.update_layout(
    geo=dict(
        showframe=False,
        showcoastlines=True,
        showland=True,
        landcolor='lightgray',
        showocean=True,
        oceancolor='lightblue',
        showlakes=True,
        lakecolor='lightblue',
        showrivers=True,
        rivercolor='lightblue',
        showcountries=True,
        countrycolor='white',
        countrywidth=0.5,
        projection_type='natural earth'
    ),
    height=600,
    margin=dict(l=0, r=0, t=0, b=0)
)

st.plotly_chart(fig, use_container_width=True)