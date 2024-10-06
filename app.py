import streamlit as st
import pandas as pd
data_customer_demo=pd.read_csv("C:\\Users\\GOURI SHANKAR KONDRA\\Downloads\\INTERN\\CustomerDemographics.csv")
data_retail1_=pd.read_csv("C:\\Users\\GOURI SHANKAR KONDRA\\Downloads\\INTERN\\Transactional_data_retail_01.csv")
data_retail2_=pd.read_csv("C:\\Users\\GOURI SHANKAR KONDRA\\Downloads\\INTERN\\Transactional_data_retail_02.csv")




st.title("""Demand Forecasting System for Optimizing Inventory and Supply Chain Efficiency Using Historical Sales Data""")

#EDA-1
st.header("Transactional Data_Retail_1")
st.subheader("Exploratory Data Analysis")
st.subheader("Basic descriptive statistics")
st.write(data_retail1_.describe())
st.write("Distribution Of data")
st.subheader("Histograms")
st.bar_chart(data_retail1_, x="Invoice", y="Quantity", stack=False,color="StockCode")
st.subheader("Scatter plot")
st.scatter_chart(data_retail1_,x='Price',y='Quantity',color="StockCode")
st.subheader("Area Chart")
st.area_chart(data_retail1_,x="Price",y="Quantity",color="StockCode")

st.subheader("Statistics")
mean_price=data_retail1_["Price"].mean()
max_price=data_retail1_['Price'].max()
min_price=data_retail1_['Price'].min()
st.write("The AVERAGE price for Transactinal_data-1:",mean_price.round(2))
st.write("The MAX price for Transactinal_data-1:",max_price.round(2))
st.write("The MIN price for Transactinal_data-1:",min_price.round(2))

#EDA-2
st.header("Transactional Data_Retail_2")
st.subheader("Exploratory Data Analysis")
st.subheader("Basic descriptive statistics")
st.write(data_retail2_.describe())
st.write("Distribution Of data")
st.subheader("Histograms")
st.bar_chart(data_retail2_, x="Invoice", y="Quantity", stack=False,color="StockCode")
st.subheader("Scatter plot")
st.scatter_chart(data_retail2_,x='Price',y='Quantity',color="StockCode")
st.subheader("Area Chart")
st.area_chart(data_retail2_,x="Price",y="Quantity",color="StockCode")

st.subheader("Statistics")
mean_price2_=data_retail1_["Price"].mean()
max_price2_=data_retail1_['Price'].max()
min_price2_=data_retail1_['Price'].min()
st.write("The AVERAGE price for Transactinal_data-1:",mean_price2_.round(2))
st.write("The MAX price for Transactinal_data-1:",max_price2_.round(2))
st.write("The MIN price for Transactinal_data-1:",min_price2_.round(2))



#Top 10 Stock codes-Transactionsal-data-1
sorted_data=data_retail1_.sort_values("Quantity",axis=0,ascending=False)
top_codes=sorted_data.iloc[1:11]
print(top_codes["StockCode"])

#Top 10 Top 10 High Revenue Products:
data_retail1_['Product']=data_retail1_["Price"]*data_retail1_['Quantity']
Top_revenue=data_retail1_.sort_values("Product",axis=0,ascending=False)
Revenue=Top_revenue.iloc[1:11]
print(Top_revenue['StockCode'])




#Top 10 Stock codes-Transactionsal-data-2
sorted_data=data_retail2_.sort_values("Quantity",axis=0,ascending=False)
top_code2_=sorted_data.iloc[1:11]
print(top_code2_["StockCode"])

#Top 10 Top 10 High Revenue Products:
data_retail2_['Product']=data_retail2_["Price"]*data_retail2_['Quantity']
Top_revenue2_=data_retail2_.sort_values("Product",axis=0,ascending=False)
Revenue2=Top_revenue2_.iloc[1:11]
print(Top_revenue['StockCode'])

mean_price2_=data_retail2_["Price"].mean()
print(mean_price2_.round(2))







































