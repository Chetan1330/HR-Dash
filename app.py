import streamlit as st # web development
import numpy as np # np mean, np random 
import pandas as pd # read csv, df manipulation
import time # to simulate a real time data, time loop 
import plotly.express as px # interactive charts 
import plotly.graph_objects as go

# read csv from a github repo
df = pd.read_csv("https://raw.githubusercontent.com/Lexie88rus/bank-marketing-analysis/master/bank.csv")
df1 = pd.read_excel("dashboard_chetan_UI.xlsx")

data_frame = pd.read_excel("dashboard_chetan_UI.xlsx", 
    usecols='A:M')
# df = df.apply (pd.to_numeric, errors='coerce')
# df = df.dropna()
# print("df1 is ", df1)

st.set_page_config(
    page_title = 'HR Dashboard',
    page_icon = '✅',
    layout = 'wide'
)

# dashboard title


st.title("HR Dashboard")

# top-level filters 

job_filter = st.selectbox("Select Date", filter(lambda x: x.startswith('Date'), sorted(df1)))

# print("Column names:", df1.columns.values)

# print("Column names:", sorted(df1))
# pie_chart = px.pie(df1, title='No.of Pass', )sorted(df)
# creating a single-element container.
placeholder = st.empty()

# dataframe filter 

df = df1[job_filter]

pass_count = 0
fail_count = 0

for i in df.values:
    if i == 'Pass':
        pass_count+= 1
    if i == 'Fail':
        fail_count+= 1

print("Pass count is:", pass_count)
print("Fail count is:", fail_count)
print("Total count is:", pass_count + fail_count)
print("  ")
# print("Dataframe:", df.values)

labels = ['Pass', 'Fail']
values = [pass_count, fail_count]

# fig3 = go.Figure(data=[go.Pie(labels=labels, values=values,
#                       texttemplate=("Pass %i" % 1))])
# fig3.update_traces(textinfo='value')

color_map={'Pass':'cyan',
'Fail':'rgb(255,0,0)',
}

fig3 = px.pie(values=values, 
    names=labels,
    color_discrete_map=px.colors.sequential.RdBu, width=500,height=400)
# fig3.update_layout(title="<b>Pie Chart</b>")


rows = st.columns(2)
rows[0].markdown("### Data Table")
rows[0].dataframe(df, 500,500)
rows[1].markdown("### Pie Chart")
rows[1].plotly_chart(fig3)


# col1, col2 = st.columns([3, 1])

# col1, col2 = st.columns([2, 3])
# col1.markdown("### Real data1")
# col1.write(df)

# col2.markdown("### Real data2")
# col2.plotly_chart(fig3)


# st.dataframe(df, 500,500)
# st.plotly_chart(fig3, width=100,height=100)
# pie_chart = px.pie(df1, title='No.of Pass', )sorted(df)

rows1 = st.columns(1)
rows1[0].markdown("### Data Table")
rows1[0].dataframe(data_frame)
# st.dataframe(data_frame)
# near real-time / live feed simulation 

# for seconds in range(200):
# #while True: 
    
#     df['age_new'] = df['age'] * np.random.choice(range(1,5))
#     df['balance_new'] = df['balance'] * np.random.choice(range(1,5))

#     # creating KPIs 
#     avg_age = np.mean(df['age_new']) 

#     count_married = int(df[(df["marital"]=='married')]['marital'].count() + np.random.choice(range(1,30)))
    
#     balance = np.mean(df['balance_new'])

#     with placeholder.container():
#         # create three columns
#         kpi1, kpi2, kpi3 = st.columns(3)

#         # fill in those three columns with respective metrics or KPIs 
#         kpi1.metric(label="Age ⏳", value=round(avg_age), delta= round(avg_age) - 10)
#         kpi2.metric(label="Married Count 💍", value= int(count_married), delta= - 10 + count_married)
#         kpi3.metric(label="A/C Balance ＄", value= f"$ {round(balance,2)} ", delta= - round(balance/count_married) * 100)

#         # create two columns for charts 

#         fig_col1, fig_col2 = st.columns(2)
#         with fig_col1:
#             st.markdown("### First Chart")
#             fig = px.density_heatmap(data_frame=df, y = 'age_new', x = 'marital')
#             st.write(fig)
#         with fig_col2:
#             st.markdown("### Second Chart")
#             fig2 = px.histogram(data_frame = df, x = 'age_new')
#             st.write(fig2)
#         st.markdown("### Detailed Data View")
#         st.dataframe(df)
#         time.sleep(1)
#     #placeholder.empty()


