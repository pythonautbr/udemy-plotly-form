from dataset import ecom_sales_new
import plotly.express as px

bar_fig = px.bar(
    data_frame=ecom_sales_new,
    x='TotalSales (R$)',
    y='Country',
    orientation='h',
    title='Total Sales by Country'
)

bar_fig.show()
