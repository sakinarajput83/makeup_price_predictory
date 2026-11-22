import streamlit as st
import pickle
import numpy as np
import pandas as pd

with open('makeup_model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("Makeup Price Predictor")

# 2 Hisse kar diye - Left me Box, Right me Graph
left, right = st.columns([1, 1])

with left:
    product_name = st.text_input("1. Product Name")
    brand_rating = st.number_input("2. Brand Rating (1 to 5)", min_value=1.0, max_value=5.0, value=4.0)
    weight = st.number_input("3. Weight (in grams)", min_value=10, max_value=500, value=100)
    spf = st.number_input("4. SPF (0 to 50)", min_value=0, max_value=50, value=15)
    customer_rating = st.number_input("5. Customer Rating (1 to 5)", min_value=1.0, max_value=5.0, value=4.0)

    if st.button("Predict Price"):
        if product_name == "":
            st.warning("Please Enter Product Name!")
        else:
            data = np.array([[brand_rating, weight, spf, customer_rating]])
            price = model.predict(data)[0]
            st.success(f"{product_name} Price is: Rs. {price:.2f}")

with right:
    st.subheader("Live Graph")
    st.write("Tum kuch bharo ya na bharo, graph yahi rahega")

    chart_data = pd.DataFrame({
        "Feature": ["Brand Rating", "Weight", "SPF", "Customer Rating"],
        "Value": [brand_rating, weight, spf, customer_rating]
    })
    st.bar_chart(chart_data.set_index("Feature"))

    st.subheader("Price vs Weight Graph")
    weights = [10, 50, 100, 200, 300, 400, 500]
    prices = []
    for w in weights:
        p = model.predict(np.array([[brand_rating, w, spf, customer_rating]]))[0]
        prices.append(p)
    
    price_data = pd.DataFrame({"Weight": weights, "Price": prices})
    st.line_chart(price_data.set_index("Weight"))