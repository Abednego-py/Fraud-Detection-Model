import streamlit as st
from model import prediction
from enum import Enum


class Transaction_Type(Enum):
    DEBIT = "debit"
    CREDIT = "credit"

Channels_map  = {
    'web' : 4,
    'android' : 0,
    'ios' : 2,
    'pay later' : 3,
    'checkout' : 1
}

Provider_map = {
    'ProviderId_1': 0,
    'ProviderId_2': 1,
    'ProviderId_3': 2,
    'ProviderId_4': 3,
    'ProviderId_5': 4,
    'ProviderId_6': 5
}


Product_map = {
    'ProductId_1': 0,
    'ProductId_10': 1,
    'ProductId_11': 2,
    'ProductId_12': 3,
    'ProductId_13': 4,
    'ProductId_14': 5,
    'ProductId_15': 6,
    'ProductId_16': 7,
    'ProductId_17': 8,
    'ProductId_18': 9,
    'ProductId_19': 10,
    'ProductId_2': 11,
    'ProductId_20': 12,
    'ProductId_21': 13,
    'ProductId_22': 14,
    'ProductId_23': 15,
    'ProductId_24': 16,
    'ProductId_25': 17,
    'ProductId_26': 18,
    'ProductId_27': 19,
    'ProductId_3': 20,
    'ProductId_4': 21,
    'ProductId_5': 22,
    'ProductId_6': 23,
    'ProductId_7': 24,
    'ProductId_8': 25,
    'ProductId_9': 26
}

Product_category_map = {
    'airtime': 0,
    'data_bundles': 1,
    'financial_services': 2,
    'movies': 3,
    'other': 4,
    'retail': 5,
    'ticket': 6,
    'transport': 7,
    'tv': 8,
    'utility_bill': 9
}




def main():
    st.title("Fraud Detection Model Deployment")

    st.image("../fraud_detection.jpg", caption="Fraud detection image", use_column_width=True)

    provider_id = st.selectbox("Select source provider of items bought", (i for i in Provider_map.keys()), placeholder="Provider ID")
    product_id = st.selectbox("Select item name",(i for i in Product_map.keys()), placeholder="Product ID")
    Product_category = st.selectbox("Select product category", (i for i in Product_category_map.keys()), placeholder="Product Category")
    channel_id = st.selectbox("Select channel", ('web', 'android', 'ios', 'pay later', 'checkout'), placeholder="Product Category")
    transaction_type = st.selectbox("Select transaction type", ('debit', 'credit'), placeholder='select transaction type')
    amount = st.text_input("Amount :  ")
    pricing_strategy = st.text_input("Enter integer values between 0 and 4: ")
    
    if(transaction_type == Transaction_Type.CREDIT.value):
        amount = - int(amount)
    
    channel_id = Channels_map[channel_id]
    provider_id = Provider_map[provider_id]
    product_id = Product_map[product_id]
    Product_category = Product_category_map[Product_category]
    result = ''

    if st.button("Predict"):
        result = prediction(int(provider_id), int(product_id), int(Product_category), int(channel_id),
                            int(amount), int(pricing_strategy))
        
        if result[0] == 0:
            st.success('This doesn"t look like a fraud case')
        else:
            st.error('This looks like a fraud case')


if __name__=='__main__':
    main()