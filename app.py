import streamlit as st
from streamlit_apexjs import st_apexcharts

options = {
    "chart": {
        "id": "lol",
        "toolbar": {
            "show": False
        }
    },

    "labels": [1991, 1992, 1993, 1994, 1995]
    ,
    "legend": {
        "show": True,
        "position": "bottom",
    }
}

options2 = {
    "chart": {
        "id": "lol2",
        "toolbar": {
            "show": False
        }
    },

    "xaxis": {
        "categories":
            [1991, 1992, 1993, 1994, 1995]
    }
    ,
    "legend": {
        "show": True,
        "position": "bottom",
    }
}

options3 = {
    "chart": {
        "id": "lol3",
        "toolbar": {
            "show": False
        }
    },

    "labels": [1991, 1992, 1993, 1994, 1995]
    ,
    "legend": {
        "show": True,
        "position": "bottom",
    }
}

series = [44, 55, 41, 17, 15]
series2 = [{
    "name": 'example',
    "data": [44, 55, 41, 17, 15]
}]

with st.container():
    col1, col2 = st.columns(2)

    with col1:
        st_apexcharts(options, series, 'donut', '100%', 'Title 1')

    with col2:
        st_apexcharts(options2, series2, 'bar', '100%', 'Title 2')

with st.container():
    st_apexcharts(options3, series2, 'line', '700', 'Title 3')
