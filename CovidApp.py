import streamlit as st
import pandas as pd
from plotly.subplots import make_subplots
# import plotly.express as px
# import plotly.graph_objects as go
import plotly.figure_factory as ff


st.title('Analisi decessi province italiane 2011-2021')

uploaded_file = st.file_uploader(label = "Scegli il file in formato csv", accept_multiple_files = False , type = ["csv"])

if uploaded_file:
	df=pd.read_csv(uploaded_file)
	province = df.columns.tolist()
	st.sidebar.title("Liste delle province")

	province.remove("data")
	province_selezionate = st.sidebar.multiselect(label = "", options=province)

	if province_selezionate:
		check_box=st.checkbox("Crea grafico")
		if check_box:
			rows = len(province_selezionate)
			fig=make_subplots(rows = rows, cols = 1, shared_xaxes = True, subplot_titles=province_selezionate)
			for provincia in province_selezionate:
				fig.add_trace(ff.Scatter( x=df['data'] , y = df[provincia], name=provincia),
							  row=province_selezionate.index(provincia) +1, col=1)
			fig.update_layout(showlegend=False, plot_bgcolor='rgb(255,255,255)')
			fig.update_xaxes(showgrid=True, gridwidth=0.05, gridcolor="LightPink",
			zeroline=True,zerolinewidth=2,zerolinecolor='Black')
			fig.update_yaxes(showgrid=True, gridwidth=0.05, gridcolor="LightPink",
			zeroline=True,zerolinewidth=2,zerolinecolor='Black')
			st.plotly_chart(fig)

#ricorda di installare plotly 
#conda install -c plotly/label/test plotly

#installare stramlit
#pip install streamlit
