import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px
from babel.numbers import format_currency
sns.set(style='dark')

st.set_page_config(page_title='E-Commerce 2017 Review')
st.header('E-Commerce 2017 Data Review')
st.write("""
- Nama: Farrel Rasyad
- Email: farrelrasyad.frr@gmail.com
- Id Dicoding: farrel_rasyad_eypa
- github repo: https://github.com/FrL1902/python-data-analysis-project-dicoding
         """)

df = pd.read_csv('all_df.csv')

st.write("""
#### Berikut adalah review data E-Commerce Tahun 2017
         """)
 

col1, col2 = st.columns(2)

with col1:
    total_orders = len(df)
    st.metric("Total orders", value=total_orders)
 
with col2:
    total_revenue = format_currency(df.payment_value.sum(), "BRL", locale='en_US') 
    st.metric("Total Revenue (Brazilian real)", value=total_revenue)

popular_categories = df['product_category_name_english'].value_counts()

top_categories = popular_categories.head(5)
top_categories['Others'] = popular_categories.iloc[5:].sum()

st.write("""
### 1. Apa saja 5 kategori barang terlaris di tahun 2017? 
         """)

fig1, ax1 = plt.subplots()
ax1.set_title("Best Selling Categories 2017", loc="center", fontsize=30)
ax1.pie(top_categories, labels=top_categories.index, autopct='%1.1f%%', startangle=90)
ax1.legend(top_categories, loc="best")
ax1.axis('equal')

st.pyplot(fig1)

st.write("""
##### Kita bisa lihat 5 kategori terlaris dari piechart diatas yaitu:
1. bed bath table (4316 order)
2. sports leisure (3500 order)
3. health beauty (3280 order)
4. furniture decor (3034 order)
5. computers accessories (2520)
         """)

st.write("""
### 2. Apa saja 5 kategori dengan skor terbaik dan terburuk di tahun 2017?
         """)

category_score = df[['review_score', 'product_category_name_english']]

mean_category_scores = category_score.groupby(by="product_category_name_english").agg({
    "review_score": "mean",
}).sort_values(by="review_score", ascending=False)

scoreDF = pd.DataFrame(mean_category_scores)

category_means = scoreDF.groupby('product_category_name_english')['review_score'].mean()

top_5_categories = category_means.nlargest(5)
bad_5_categories = category_means.nsmallest(5)

scoreDF2 = pd.DataFrame(top_5_categories)

fig, ax = plt.subplots(figsize=(20, 15))
colors = ["#90CAF9", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
sns.barplot(
    x="review_score", 
    y="product_category_name_english",
    data=scoreDF2,
    palette=colors,
    ax=ax
)
ax.set_title("Best Categories by Score 2017", loc="center", fontsize=30)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)
st.pyplot(fig)


scoreDF3 = pd.DataFrame(bad_5_categories)

fig, ax = plt.subplots(figsize=(20, 15))
colors = ["#90CAF9", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
sns.barplot(
    x="review_score", 
    y="product_category_name_english",
    data=scoreDF3,
    palette=colors,
    ax=ax
)
ax.set_title("Worst Categories by Score 2017", loc="center", fontsize=30)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)
st.pyplot(fig)

st.write("""
##### Kita bisa lihat 5 kategori dengan skor terbaik adalah
1. arts and craftmanship
2. fashion childrens clothes
3. la cuisine
4. cds dvds musicals
5. fashion sport
        
         

##### Kita juga bisa lihat 5 kategori dengan skor terburuk adalah
1. diapers and hygiene
2. security and services
3. small appliances home oven and coffee
4. office furniture
5. fashion male clothing
         """)