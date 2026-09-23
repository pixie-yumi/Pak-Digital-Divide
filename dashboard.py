import streamlit as st
import pandas as pd

st.title("Pakistan Digital Gender Divide")

df = pd.read_csv("digital_divide_dataset.csv")

st.subheader("Raw Data")
st.dataframe(df)

st.subheader("Mobile Ownership Gap by Region")
mobile_df = df[(df["indicator"]=="mobile ownership")]
chart_data = mobile_df.pivot(index="region", columns="group", values="value 2024-25")
st.bar_chart(chart_data, stack=False) 

st.subheader("Internet Use Gap by Region")
internet_df = df[(df["indicator"]=="internet use")]
internet_chart = internet_df.pivot(index="region", columns="group", values="value 2024-25")
st.bar_chart(internet_chart, stack=False)

st.subheader("Household Internet Access: Urban VS Rural")
access_df = df[(df["indicator"]=="internet access")]
access_chart = access_df.pivot(index="region", columns="group",values="value 2024-25")
st.bar_chart(access_chart, stack=False)

st.subheader("Key Takeaway")
st.write("""
The data tells a clear story: Pakistani women aren't excluded from the internet because 
they don't want to use it or don't know how. They're excluded because they don't own the 
device in the first place. Once a woman gets access, by any means, she uses it as much as 
men do, and in cities, more. The real gap is ownership, not skill.

Rural women have it worst on both fronts: the biggest ownership gap and the weakest internet 
infrastructure. Nationally, 76% of people still have no financial account at all, and just 
9% use mobile money, meaning most of the population, women especially, are also locked out 
of the digital economy that phone ownership would unlock.

If this data were used to guide anything, it wouldn't be another "digital literacy" workshop. 
It would be getting rural women their own phones, paired with access to mobile banking, since 
ownership alone opens the door to both connectivity and financial inclusion at once.
""")
