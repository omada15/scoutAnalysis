import streamlit as st
import pandas as pd

tab1, tab2 = st.tabs(["Data", "ranker"])
df = pd.DataFrame(pd.read_csv("avgs.csv"))

criteria_mapping = {
    "auto points": "avgAutoFuel",
    "auto climb": "autoClimbPercent",
    "transition": "avgTransitionFuel",
    "first shift": "avgFirstActiveHubFuel",
    "second shift": "avgSecondActiveHubFuel",
    "Endgame Points": "avgEndgameFuel",
    "Climb": "endgameAvgClimbPoints",
}

import time

extra_df = pd.DataFrame(pd.read_csv("custom.csv"))


def update( m1, m2, m3, m4,m5,m6):
    row = {
        "multiplier1": m1,
        "multiplier2": m2,
        "multiplier3": m3,
        "multiplier4": m4,
        "multiplier5": m5,
        "multiplier6": m6

    }
    extra_df = pd.read_csv("custom.csv")
    extra_df = pd.concat([extra_df, pd.DataFrame([row])], ignore_index=True)
    extra_df.to_csv("custom.csv", index=False)


max_rows = len(df[["teamNumber"]])

with tab1:
    col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
    st.write("work in progress")
with tab2:

    col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
    label = "multiplier"
    with col1:
        if st.button("run"):
            update(
                st.session_state["multiplier_1"],
                st.session_state["multiplier_2"],
                st.session_state["multiplier_3"],
                st.session_state["multiplier_4"],
                st.session_state["multiplier_5"],
                st.session_state["multiplier_6"]
            )
            extra_df = pd.DataFrame(pd.read_csv("custom.csv"))
            df["avgAutoFuel"]=df["avgAutoFuel"].astype(object) * extra_df.iloc[-1][f"multiplier1"]
            df["avgTransitionFuel"]=df["avgTransitionFuel"].astype(object) * extra_df.iloc[-1][f"multiplier2"]
            df["avgFirstActiveHubFuel"]=df["avgFirstActiveHubFuel"].astype(object) * extra_df.iloc[-1][f"multiplier3"]
            df["avgSecondActiveHubFuel"]=df["avgSecondActiveHubFuel"].astype(object) * extra_df.iloc[-1][f"multiplier4"]
            df["avgEndgameFuel"]=df["avgEndgameFuel"].astype(object) * extra_df.iloc[-1][f"multiplier5"]
            df["avgTotalFuel"]=df["avgTotalFuel"].astype(object) * extra_df.iloc[-1][f"multiplier6"]

    with col3:
        selector_1_multiplier = st.text_input(label, key="multiplier_1")
    with col4:
        selector_2_multiplier = st.text_input(label, key="multiplier_2")
    with col5:
        selector_3_multiplier = st.text_input(label, key="multiplier_3")
    with col6:
        selector_4_multiplier = st.text_input(label, key="multiplier_4")
    with col7:
        selector_4_multiplier = st.text_input(label, key="multiplier_5")
    with col8:
        selector_4_multiplier = st.text_input(label, key="multiplier_6")

    st.data_editor(
        df,
        column_order=(
            "teamNumber",
            "entries",
            "avgAutoFuel",
            "avgTransitionFuel",
            "avgFirstActiveHubFuel",
            "avgSecondActiveHubFuel",
            "avgEndgameFuel",
            "avgTotalFuel"
        ),
        hide_index=True,
        disabled=["widgets"],
        key="chud"
    )
    