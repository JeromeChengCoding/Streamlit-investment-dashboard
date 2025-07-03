import streamlit as st
import pandas as pd

def show_stock_info():
    """
    Display stock information to user.
    In a real implementation, you might read from a database or API.
    """
    st.title("股票資訊")
    st.write("此頁面顯示股票清單與詳細資訊。")

    # Example stock data
    data = {
        "Stock Name": ["StockX", "StockY", "StockZ"],
        "Price": [100, 250, 58],
        "PE Ratio": [15.2, 18.4, 12.3],
    }
    df = pd.DataFrame(data)
    st.dataframe(df)

def main():
    show_stock_info()

if __name__ == "__main__":
    main()