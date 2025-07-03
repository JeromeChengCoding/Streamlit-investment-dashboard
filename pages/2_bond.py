import streamlit as st
import pandas as pd

def show_bond_info():
    """
    Display bond information to user.
    In a real implementation, you might read from a database or API.
    """
    st.title("債券資訊")
    st.write("此頁面顯示債券清單與詳細資訊。")

    # Example bond data
    data = {
        "Bond Name": ["BondA", "BondB", "BondC"],
        "Yield": [2.5, 3.0, 2.8],
        "Duration": [5, 10, 7],
    }
    df = pd.DataFrame(data)
    st.dataframe(df)

def main():
    show_bond_info()

if __name__ == "__main__":
    main()