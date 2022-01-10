import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title='NA Countries Trade Data Representation', page_icon='LV.jpg')
sidebar= st.sidebar
st.write('*based on latest data available online')
st.markdown("<h1 style='text-align: center'><u>Trade of FMCG Products in</u></h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center'><u>'Northern African Countries'</u></h1>", unsafe_allow_html=True) 
sidebar.image('Lever Bridge.jpeg')
option1= st.selectbox('Select the Country', ('Morocco','Algeria','Egypt','Sudan','Tunisia','Libya'))
option2= st.radio('Select',('Import','Export','Tariff','Service Trade'))
option3= sidebar.radio('Select',('2019','2018','2016-2018', '2014-2018'))

with st.spinner('| Just a sec |'):
    if option1=='Morocco': 
        st.markdown("<h2 style='text-align: center'><u>Morocco</u></h1>", unsafe_allow_html=True) 
        if option2== 'Import':
            st.markdown("<h3 style='text-align: center'>[Imports]</h3>", unsafe_allow_html=True)
            df=pd.read_csv('Morocco Import.csv')
            df.drop(columns=['Section ID','HS2 ID','HS4 ID'], inplace=True)
            df.rename(columns={'Trade Value Growth':'Trade Value Growth(%)','Trade Value Growth 1':'TradeValue Growth(%)Pre 1','Trade Value Growth 3':'TradeValue Growth(%)Pre 3','Trade Value Growth 5':'TradeValue Growth(%)Pre 5'},inplace=True)
            st.dataframe(df)

            if option3== '2019':
                fig=px.treemap(df, path=[px.Constant('PRODUCTS'),'Section', 'HS2','HS4'], values='Trade Value', color='Trade Value', hover_data=['Trade Value Growth(%)'],color_continuous_scale='rdbu')
                fig.update_layout(margin= dict(t=50, l=25, r=25, b=25), width =1100,  height=650)
                st.plotly_chart(fig)
                col1, col2=st.columns(2)
                col1.plotly_chart(px.histogram(df.head(35), x='HS2' ,y='Trade Value',width =650,  height=650 , template='plotly_dark',title='Animal Products'))
                col2.plotly_chart(px.histogram(df.iloc[36:112], x='HS2' ,y='Trade Value',width =650,  height=650 , template='plotly_dark',title='Vegetable Products'))
                col1.plotly_chart(px.histogram(df.iloc[112:131], x='HS2' ,y='Trade Value',width =500,  height=550 , template='plotly_dark',title='Animal and Vegetable Bi Product'))
                col2.plotly_chart(px.histogram(df.tail(53), x='HS2' ,y='Trade Value',width =700,  height=700 , template='plotly_dark',title='Foodstuffs'))

            
            if option3=='2018':
                fig=px.treemap(df, path=[px.Constant('PRODUCTS'),'Section', 'HS2','HS4'], values='Trade Value Previous 1', color='Trade Value Previous 1', hover_data=['TradeValue Growth(%)Pre 1'],color_continuous_scale='RdBu')
                fig.update_layout(margin= dict(t=50, l=25, r=25, b=25), width =1100,  height=650)
                st.plotly_chart(fig)
                col1, col2=st.columns(2)
                col1.plotly_chart(px.histogram(df.head(35), x='HS2' ,y='Trade Value Previous 1',width =650,  height=650 , template='plotly_dark',title='Animal Products'))
                col2.plotly_chart(px.histogram(df.iloc[36:112], x='HS2' ,y='Trade Value Previous 1',width =650,  height=650 , template='plotly_dark',title='Vegetable Products'))
                col1.plotly_chart(px.histogram(df.iloc[112:131], x='HS2' ,y='Trade Value Previous 1',width =500,  height=550 , template='plotly_dark',title='Animal and Vegetable Bi Product'))
                col2.plotly_chart(px.histogram(df.tail(53), x='HS2' ,y='Trade Value Previous 1',width =700,  height=700 , template='plotly_dark',title='Foodstuffs'))
            
            if option3=='2016-2018':
                fig=px.treemap(df, path=[px.Constant('PRODUCTS'),'Section', 'HS2','HS4'], values='Trade Value Previous 3', color='Trade Value Previous 3', hover_data=['TradeValue Growth(%)Pre 3'],color_continuous_scale='RdBu')
                fig.update_layout(margin= dict(t=50, l=25, r=25, b=25), width =1100,  height=650)
                st.plotly_chart(fig)
                col1, col2=st.columns(2)
                col1.plotly_chart(px.histogram(df.head(35), x='HS2' ,y='Trade Value Previous 3',width =650,  height=650 , template='plotly_dark',title='Animal Products'))
                col2.plotly_chart(px.histogram(df.iloc[36:112], x='HS2' ,y='Trade Value Previous 3',width =650,  height=650 , template='plotly_dark',title='Vegetable Products'))
                col1.plotly_chart(px.histogram(df.iloc[112:131], x='HS2' ,y='Trade Value Previous 3',width =500,  height=550 , template='plotly_dark',title='Animal and Vegetable Bi Product'))
                col2.plotly_chart(px.histogram(df.tail(53), x='HS2' ,y='Trade Value Previous 3',width =700,  height=700 , template='plotly_dark',title='Foodstuffs'))

            if option3=='2014-2018':
                fig=px.treemap(df, path=[px.Constant('PRODUCTS'),'Section', 'HS2','HS4'], values='Trade Value Previous 5', color='Trade Value Previous 5', hover_data=['TradeValue Growth(%)Pre 5'],color_continuous_scale='RdBu')
                fig.update_layout(margin= dict(t=50, l=25, r=25, b=25), width =1100,  height=650)
                st.plotly_chart(fig)
                col1, col2=st.columns(2)
                col1.plotly_chart(px.histogram(df.head(35), x='HS2' ,y='Trade Value Previous 5',width =650,  height=650 , template='plotly_dark',title='Animal Products'))
                col2.plotly_chart(px.histogram(df.iloc[36:112], x='HS2' ,y='Trade Value Previous 5',width =650,  height=650 , template='plotly_dark',title='Vegetable Products'))
                col1.plotly_chart(px.histogram(df.iloc[112:131], x='HS2' ,y='Trade Value Previous 5',width =500,  height=550 , template='plotly_dark',title='Animal and Vegetable Bi Product'))
                col2.plotly_chart(px.histogram(df.tail(53), x='HS2' ,y='Trade Value Previous 5',width =700,  height=700 , template='plotly_dark',title='Foodstuffs'))

        if option2== 'Export':
            st.markdown("<h3 style='text-align: center'>[Exports]</h3>", unsafe_allow_html=True)
            df=pd.read_csv('Morocco Export.csv')
            df.drop(columns=['Section ID','HS2 ID','HS4 ID'], inplace=True)
            df.rename(columns={'Trade Value Growth':'Trade Value Growth(%)','Trade Value Growth 1':'TradeValue Growth(%)Pre 1','Trade Value Growth 3':'TradeValue Growth(%)Pre 3','Trade Value Growth 5':'TradeValue Growth(%)Pre 5'},inplace=True)
            st.dataframe(df)

            if option3== '2019':
                fig=px.treemap(df, path=[px.Constant('PRODUCTS'),'Section', 'HS2','HS4'], values='Trade Value', color='Trade Value',hover_data=['Trade Value Growth(%)'],color_continuous_scale='RdBu')
                fig.update_layout(margin= dict(t=50, l=25, r=25, b=25), width =1100,  height=650)
                st.plotly_chart(fig)
                col1, col2=st.columns(2)
                col1.plotly_chart(px.histogram(df.head(30), x='HS2' ,y='Trade Value',width =650,  height=650 , template='plotly_dark',title='Animal Products'))
                col2.plotly_chart(px.histogram(df.iloc[31:102], x='HS2' ,y='Trade Value',width =650,  height=650 , template='plotly_dark',title='Vegetable Products'))
                col1.plotly_chart(px.histogram(df.iloc[102:120], x='HS2' ,y='Trade Value',width =500,  height=550 , template='plotly_dark',title='Animal and Vegetable Bi Product'))
                col2.plotly_chart(px.histogram(df.tail(51), x='HS2' ,y='Trade Value',width =700,  height=700 , template='plotly_dark',title='Foodstuffs'))

            if option3=='2018':
                fig=px.treemap(df, path=[px.Constant('PRODUCTS'),'Section', 'HS2','HS4'], values='Trade Value Previous 1', color='Trade Value Previous 1',hover_data=['TradeValue Growth(%)Pre 1'],color_continuous_scale='RdBu')
                fig.update_layout(margin= dict(t=50, l=25, r=25, b=25), width =1100,  height=650)
                st.plotly_chart(fig)
                col1, col2=st.columns(2)
                col1.plotly_chart(px.histogram(df.head(30), x='HS2' ,y='Trade Value Previous 1',width =650,  height=650 , template='plotly_dark',title='Animal Products'))
                col2.plotly_chart(px.histogram(df.iloc[31:102], x='HS2' ,y='Trade Value Previous 1',width =650,  height=650 , template='plotly_dark',title='Vegetable Products'))
                col1.plotly_chart(px.histogram(df.iloc[102:120], x='HS2' ,y='Trade Value Previous 1',width =500,  height=550 , template='plotly_dark',title='Animal and Vegetable Bi Product'))
                col2.plotly_chart(px.histogram(df.tail(51), x='HS2' ,y='Trade Value Previous 1',width =700,  height=700 , template='plotly_dark',title='Foodstuffs'))
            

            if option3=='2016-2018':
                fig=px.treemap(df, path=[px.Constant('PRODUCTS'),'Section', 'HS2','HS4'], values='Trade Value Previous 3', color='Trade Value Previous 3',hover_data=['TradeValue Growth(%)Pre 3'],color_continuous_scale='RdBu')
                fig.update_layout(margin= dict(t=50, l=25, r=25, b=25), width =1100,  height=650)
                st.plotly_chart(fig)
                col1, col2=st.columns(2)
                col1.plotly_chart(px.histogram(df.head(30), x='HS2' ,y='Trade Value Previous 3',width =650,  height=650 , template='plotly_dark',title='Animal Products'))
                col2.plotly_chart(px.histogram(df.iloc[31:102], x='HS2' ,y='Trade Value Previous 3',width =650,  height=650 , template='plotly_dark',title='Vegetable Products'))
                col1.plotly_chart(px.histogram(df.iloc[102:120], x='HS2' ,y='Trade Value Previous 3',width =500,  height=550 , template='plotly_dark',title='Animal and Vegetable Bi Product'))
                col2.plotly_chart(px.histogram(df.tail(51), x='HS2' ,y='Trade Value Previous 3',width =700,  height=700 , template='plotly_dark',title='Foodstuffs'))

            if option3=='2014-2018':
                fig=px.treemap(df, path=[px.Constant('PRODUCTS'),'Section', 'HS2','HS4'], values='Trade Value Previous 5', color='Trade Value Previous 5',hover_data=['TradeValue Growth(%)Pre 5'],color_continuous_scale='RdBu')
                fig.update_layout(margin= dict(t=50, l=25, r=25, b=25), width =1100,  height=650)
                st.plotly_chart(fig)
                col1, col2=st.columns(2)
                col1.plotly_chart(px.histogram(df.head(30), x='HS2' ,y='Trade Value Previous 5',width =650,  height=650 , template='plotly_dark',title='Animal Products'))
                col2.plotly_chart(px.histogram(df.iloc[31:102], x='HS2' ,y='Trade Value Previous 5',width =650,  height=650 , template='plotly_dark',title='Vegetable Products'))
                col1.plotly_chart(px.histogram(df.iloc[102:120], x='HS2' ,y='Trade Value Previous 5',width =500,  height=550 , template='plotly_dark',title='Animal and Vegetable Bi Product'))
                col2.plotly_chart(px.histogram(df.tail(51), x='HS2' ,y='Trade Value Previous 5',width =700,  height=700 , template='plotly_dark',title='Foodstuffs'))
            
        if option2=='Tariff':
            st.markdown("<h3 style='text-align: center'>[Tariff]</h3>", unsafe_allow_html=True)

            da=pd.read_csv('Animal Morocco.csv')
            da.drop(columns=['Section ID','HS2 ID','HS4 ID','HS6 ID' ], inplace=True)
            da.rename(columns={'Tariff':'Tariff(%)'},inplace=True)
            st.markdown('Tariff on Animal Products')
            st.dataframe(da)
            st.markdown('---')

            db=pd.read_csv('Vegetable Morocco.csv')
            db.drop(columns=['Section ID','HS2 ID','HS4 ID','HS6 ID' ], inplace=True)
            db.rename(columns={'Tariff':'Tariff(%)'},inplace=True)
            st.markdown('Tariff on Vegetable Products')
            st.dataframe(db)
            st.markdown('---')

            dc=pd.read_csv('Biproduct Morocco.csv')
            dc.drop(columns=['Section ID','HS2 ID','HS4 ID','HS6 ID' ], inplace=True)
            dc.rename(columns={'Tariff':'Tariff(%)'},inplace=True)
            st.markdown('Tariff on Animal and Vegetable Bi Products')
            st.dataframe(dc)
            st.markdown('---')

            dd=pd.read_csv('Foodstuff Morocco.csv')
            dd.drop(columns=['Section ID','HS2 ID','HS4 ID','HS6 ID' ], inplace=True)
            dd.rename(columns={'Tariff':'Tariff(%)'},inplace=True)
            st.markdown('Tariff on Foodstuffs')
            st.dataframe(dd)
            st.markdown('---')

        if option2== 'Service Trade':
            st.markdown("<h3 style='text-align: center'>[Service Trade]</h3>", unsafe_allow_html=True)
            
            dz=pd.read_csv('Morocco serviceimports.csv')
            dz.drop(columns=['Parent Service ID','Service ID' ], inplace=True)
            st.markdown('Service Imports 2019')
            st.dataframe(dz)
            st.plotly_chart(px.histogram(dz, x='Service' ,y='Service Value',width =650,  height=650 , template='plotly_dark'))
            
            dy=pd.read_csv('Morocco serviceexports.csv')
            dy.drop(columns=['Parent Service ID','Service ID' ], inplace=True)
            st.markdown('Service Exports 2019')
            st.dataframe(dy)
            st.plotly_chart(px.histogram(dy, x='Service' ,y='Service Value',width =650,  height=650 , template='plotly_dark'))         
    #***********************************************************************************************************************************************
    #***********************************************************************************************************************************************
    if option1=='Algeria':  
        st.markdown("<h2 style='text-align: center'><u>Algeria</u></h1>", unsafe_allow_html=True)
        if option2== 'Import':
            st.markdown("<h3 style='text-align: center'>[Imports]</h3>", unsafe_allow_html=True)
            df=pd.read_csv('Algeria Import.csv')
            df.drop(columns=['Section ID','HS2 ID','HS4 ID'], inplace=True)
            df.rename(columns={'Trade Value Growth':'Trade Value Growth(%)','Trade Value Growth 1':'TradeValue Growth(%)Pre 1','Trade Value Growth 3':'TradeValue Growth(%)Pre 3','Trade Value Growth 5':'TradeValue Growth(%)Pre 5'},inplace=True)
            st.dataframe(df)

            if option3== '2019':
                fig=px.treemap(df, path=[px.Constant('PRODUCTS'),'Section', 'HS2','HS4'], values='Trade Value', color='Trade Value',hover_data=['Trade Value Growth(%)'],color_continuous_scale='RdBu')
                fig.update_layout(margin= dict(t=50, l=25, r=25, b=25), width =1100,  height=650)
                st.plotly_chart(fig)
                col1, col2=st.columns(2)
                col1.plotly_chart(px.histogram(df.head(30), x='HS2' ,y='Trade Value',width =650,  height=650 , template='plotly_dark',title='Animal Products'))
                col2.plotly_chart(px.histogram(df.iloc[31:102], x='HS2' ,y='Trade Value',width =650,  height=650 , template='plotly_dark',title='Vegetable Products'))
                col1.plotly_chart(px.histogram(df.iloc[102:118], x='HS2' ,y='Trade Value',width =500,  height=550 , template='plotly_dark',title='Animal and Vegetable Bi Product'))
                col2.plotly_chart(px.histogram(df.tail(48), x='HS2' ,y='Trade Value',width =700,  height=700 , template='plotly_dark',title='Foodstuffs'))

            
            if option3=='2018':
                fig=px.treemap(df, path=[px.Constant('PRODUCTS'),'Section', 'HS2','HS4'], values='Trade Value Previous 1', color='Trade Value Previous 1',hover_data=['TradeValue Growth(%)Pre 1'],color_continuous_scale='RdBu')
                fig.update_layout(margin= dict(t=50, l=25, r=25, b=25), width =1100,  height=650)
                st.plotly_chart(fig)
                col1, col2=st.columns(2)
                col1.plotly_chart(px.histogram(df.head(30), x='HS2' ,y='Trade Value Previous 1',width =650,  height=650 , template='plotly_dark',title='Animal Products'))
                col2.plotly_chart(px.histogram(df.iloc[31:102], x='HS2' ,y='Trade Value Previous 1',width =650,  height=650 , template='plotly_dark',title='Vegetable Products'))
                col1.plotly_chart(px.histogram(df.iloc[102:118], x='HS2' ,y='Trade Value Previous 1',width =500,  height=550 , template='plotly_dark',title='Animal and Vegetable Bi Product'))
                col2.plotly_chart(px.histogram(df.tail(48), x='HS2' ,y='Trade Value Previous 1',width =700,  height=700 , template='plotly_dark',title='Foodstuffs'))
            
            if option3=='2016-2018':
                fig=px.treemap(df, path=[px.Constant('PRODUCTS'),'Section', 'HS2','HS4'], values='Trade Value Previous 3', color='Trade Value Previous 3',hover_data=['TradeValue Growth(%)Pre 3'],color_continuous_scale='RdBu')
                fig.update_layout(margin= dict(t=50, l=25, r=25, b=25), width =1100,  height=650)
                st.plotly_chart(fig)
                col1, col2=st.columns(2)
                col1.plotly_chart(px.histogram(df.head(30), x='HS2' ,y='Trade Value Previous 3',width =650,  height=650 , template='plotly_dark',title='Animal Products'))
                col2.plotly_chart(px.histogram(df.iloc[31:102], x='HS2' ,y='Trade Value Previous 3',width =650,  height=650 , template='plotly_dark',title='Vegetable Products'))
                col1.plotly_chart(px.histogram(df.iloc[102:118], x='HS2' ,y='Trade Value Previous 3',width =500,  height=550 , template='plotly_dark',title='Animal and Vegetable Bi Product'))
                col2.plotly_chart(px.histogram(df.tail(48), x='HS2' ,y='Trade Value Previous 3',width =700,  height=700 , template='plotly_dark',title='Foodstuffs'))

            if option3=='2014-2018':
                fig=px.treemap(df, path=[px.Constant('PRODUCTS'),'Section', 'HS2','HS4'], values='Trade Value Previous 5', color='Trade Value Previous 5',hover_data=['TradeValue Growth(%)Pre 5'],color_continuous_scale='RdBu')
                fig.update_layout(margin= dict(t=50, l=25, r=25, b=25), width =1100,  height=650)
                st.plotly_chart(fig)
                col1, col2=st.columns(2)
                col1.plotly_chart(px.histogram(df.head(30), x='HS2' ,y='Trade Value Previous 5',width =650,  height=650 , template='plotly_dark',title='Animal Products'))
                col2.plotly_chart(px.histogram(df.iloc[31:102], x='HS2' ,y='Trade Value Previous 5',width =650,  height=650 , template='plotly_dark',title='Vegetable Products'))
                col1.plotly_chart(px.histogram(df.iloc[102:118], x='HS2' ,y='Trade Value Previous 5',width =500,  height=550, template='plotly_dark',title='Animal and Vegetable Bi Product'))
                col2.plotly_chart(px.histogram(df.tail(48), x='HS2' ,y='Trade Value Previous 5',width =700,  height=700 , template='plotly_dark',title='Foodstuffs'))
            
        if option2== 'Export':
            st.markdown("<h3 style='text-align: center'>[Exports]</h3>", unsafe_allow_html=True)
            df=pd.read_csv('Algeria Export.csv')
            df.drop(columns=['Section ID','HS2 ID','HS4 ID'], inplace=True)
            df.rename(columns={'Trade Value Growth':'Trade Value Growth(%)','Trade Value Growth 1':'TradeValue Growth(%)Pre 1','Trade Value Growth 3':'TradeValue Growth(%)Pre 3','Trade Value Growth 5':'TradeValue Growth(%)Pre 5'},inplace=True)
            st.dataframe(df)

            if option3=='2019':
                fig=px.treemap(df, path=[px.Constant('PRODUCTS'),'Section', 'HS2','HS4'], values='Trade Value', color='Trade Value',hover_data=['Trade Value Growth(%)'],color_continuous_scale='rdbu')
                fig.update_layout(margin= dict(t=50, l=25, r=25, b=25), width =1100,  height=650)
                st.plotly_chart(fig)
                col1, col2=st.columns(2)
                col1.plotly_chart(px.histogram(df.head(16), x='HS2' ,y='Trade Value',width =650,  height=650 , template='plotly_dark',title='Animal Products'))
                col2.plotly_chart(px.histogram(df.iloc[17:65], x='HS2' ,y='Trade Value',width =650,  height=650 , template='plotly_dark',title='Vegetable Products'))
                col1.plotly_chart(px.histogram(df.iloc[65:75], x='HS2' ,y='Trade Value',width =500,  height=550 , template='plotly_dark',title='Animal and Vegetable Bi Product'))
                col2.plotly_chart(px.histogram(df.tail(39), x='HS2' ,y='Trade Value',width =700,  height=700 , template='plotly_dark',title='Foodstuffs'))

            if option3=='2018':
                fig=px.treemap(df, path=[px.Constant('PRODUCTS'),'Section', 'HS2','HS4'], values='Trade Value Previous 1', color='Trade Value Previous 1',hover_data=['TradeValue Growth(%)Pre 1'],color_continuous_scale='RdBu')
                fig.update_layout(margin= dict(t=50, l=25, r=25, b=25), width =1100,  height=650)
                st.plotly_chart(fig)
                col1, col2=st.columns(2)
                col1.plotly_chart(px.histogram(df.head(16), x='HS2' ,y='Trade Value Previous 1',width =650,  height=650 , template='plotly_dark',title='Animal Products'))
                col2.plotly_chart(px.histogram(df.iloc[17:65], x='HS2' ,y='Trade Value Previous 1',width =650,  height=650 , template='plotly_dark',title='Vegetable Products'))
                col1.plotly_chart(px.histogram(df.iloc[65:75], x='HS2' ,y='Trade Value Previous 1',width =500,  height=550 , template='plotly_dark',title='Animal and Vegetable Bi Product'))
                col2.plotly_chart(px.histogram(df.tail(39), x='HS2' ,y='Trade Value Previous 1',width =700,  height=700 , template='plotly_dark',title='Foodstuffs'))
            

            if option3=='2016-2018':
                fig=px.treemap(df, path=[px.Constant('PRODUCTS'),'Section', 'HS2','HS4'], values='Trade Value Previous 3', color='Trade Value Previous 3',hover_data=['TradeValue Growth(%)Pre 3'],color_continuous_scale= 'RdBu')
                fig.update_layout(margin= dict(t=50, l=25, r=25, b=25), width =1100,  height=650)
                st.plotly_chart(fig)
                col1, col2=st.columns(2)
                col1.plotly_chart(px.histogram(df.head(16), x='HS2' ,y='Trade Value Previous 3',width =650,  height=650 , template='plotly_dark',title='Animal Products'))
                col2.plotly_chart(px.histogram(df.iloc[17:65], x='HS2' ,y='Trade Value Previous 3',width =650,  height=650 , template='plotly_dark',title='Vegetable Products'))
                col1.plotly_chart(px.histogram(df.iloc[65:75], x='HS2' ,y='Trade Value Previous 3',width =500,  height=550 , template='plotly_dark',title='Animal and Vegetable Bi Product'))
                col2.plotly_chart(px.histogram(df.tail(39), x='HS2' ,y='Trade Value Previous 3',width =700,  height=700 , template='plotly_dark',title='Foodstuffs'))

            if option3=='2014-2018':
                fig=px.treemap(df, path=[px.Constant('PRODUCTS'),'Section', 'HS2','HS4'], values='Trade Value Previous 5', color='Trade Value Previous 5',hover_data=['TradeValue Growth(%)Pre 5'],color_continuous_scale='RdBu')
                fig.update_layout(margin= dict(t=50, l=25, r=25, b=25), width =1100,  height=650)
                st.plotly_chart(fig)
                col1, col2=st.columns(2)
                col1.plotly_chart(px.histogram(df.head(16), x='HS2' ,y='Trade Value Previous 5',width =650,  height=650 , template='plotly_dark',title='Animal Products'))
                col2.plotly_chart(px.histogram(df.iloc[17:65], x='HS2' ,y='Trade Value Previous 5',width =650,  height=650 , template='plotly_dark',title='Vegetable Products'))
                col1.plotly_chart(px.histogram(df.iloc[65:75], x='HS2' ,y='Trade Value Previous 5',width =500,  height=550 , template='plotly_dark',title='Animal and Vegetable Bi Product'))
                col2.plotly_chart(px.histogram(df.tail(39), x='HS2' ,y='Trade Value Previous 5',width =700,  height=700 , template='plotly_dark',title='Foodstuffs'))

        if option2=='Tariff':
            st.markdown("<h3 style='text-align: center'>[Tariff]</h3>", unsafe_allow_html=True)

            da=pd.read_csv('Animal Algeria.csv')
            da.drop(columns=['Section ID','HS2 ID','HS4 ID','HS6 ID' ], inplace=True)
            da.rename(columns={'Tariff':'Tariff(%)'},inplace=True)
            st.markdown('Tariff on Animal Products')
            st.dataframe(da)
            st.markdown('---')

            db=pd.read_csv('Vegetable Algeria.csv')
            db.drop(columns=['Section ID','HS2 ID','HS4 ID','HS6 ID' ], inplace=True)
            db.rename(columns={'Tariff':'Tariff(%)'},inplace=True)
            st.markdown('Tariff on Vegetable Products')
            st.dataframe(db)
            st.markdown('---')

            dc=pd.read_csv('Biproduct Algeria.csv')
            dc.drop(columns=['Section ID','HS2 ID','HS4 ID','HS6 ID' ], inplace=True)
            dc.rename(columns={'Tariff':'Tariff(%)'},inplace=True)
            st.markdown('Tariff on Animal and Vegetable Bi Products')
            st.dataframe(dc)
            st.markdown('---')

            dd=pd.read_csv('Foodstuff Algeria.csv')
            dd.drop(columns=['Section ID','HS2 ID','HS4 ID','HS6 ID' ], inplace=True)
            dd.rename(columns={'Tariff':'Tariff(%)'},inplace=True)
            st.markdown('Tariff on Foodstuffs')
            st.dataframe(dd)
            st.markdown('---')

        if option2== 'Service Trade':
            st.markdown("<h3 style='text-align: center'>[Service Trade]</h3>", unsafe_allow_html=True)
            
            dz=pd.read_csv('Algeria serviceimports.csv')
            dz.drop(columns=['Parent Service ID','Service ID' ], inplace=True)
            st.markdown('Service Imports 2016')
            st.dataframe(dz)
            st.plotly_chart(px.histogram(dz, x='Service' ,y='Service Value',width =650,  height=650 , template='plotly_dark'))
            
            dy=pd.read_csv('Algeria serviceexports.csv')
            dy.drop(columns=['Parent Service ID','Service ID' ], inplace=True)
            st.markdown('Service Exports 2016')
            st.dataframe(dy)
            st.plotly_chart(px.histogram(dy, x='Service' ,y='Service Value',width =650,  height=650 , template='plotly_dark'))    
    #************************************************************************************************************************************************
    #**************************************************************************************************************************************************
    if option1=='Egypt':  
        st.markdown("<h2 style='text-align: center'><u>Egypt</u></h2>", unsafe_allow_html=True) 
        if option2== 'Import':
            st.markdown("<h3 style='text-align: center'>[Imports]</h3>", unsafe_allow_html=True)
            df=pd.read_csv('Egypt Import.csv')
            df.drop(columns=['Section ID','HS2 ID','HS4 ID'], inplace=True)
            df.rename(columns={'Trade Value Growth':'Trade Value Growth(%)','Trade Value Growth 1':'TradeValue Growth(%)Pre 1','Trade Value Growth 3':'TradeValue Growth(%)Pre 3','Trade Value Growth 5':'TradeValue Growth(%)Pre 5'},inplace=True)
            st.dataframe(df)

            if option3== '2019':
                fig=px.treemap(df, path=[px.Constant('PRODUCTS'),'Section', 'HS2','HS4'], values='Trade Value', color='Trade Value',hover_data=['Trade Value Growth(%)'],color_continuous_scale='rdbu')
                fig.update_layout(margin= dict(t=50, l=25, r=25, b=25), width =1100,  height=650)
                st.plotly_chart(fig)
                col1, col2=st.columns(2)
                col1.plotly_chart(px.histogram(df.head(36), x='HS2' ,y='Trade Value',width =650,  height=650 , template='plotly_dark',title='Animal Products'))
                col2.plotly_chart(px.histogram(df.iloc[37:114], x='HS2' ,y='Trade Value',width =650,  height=650 , template='plotly_dark',title='Vegetable Products'))
                col1.plotly_chart(px.histogram(df.iloc[114:134], x='HS2' ,y='Trade Value',width =500,  height=550 , template='plotly_dark',title='Animal and Vegetable Bi Product'))
                col2.plotly_chart(px.histogram(df.tail(53), x='HS2' ,y='Trade Value',width =700,  height=700 , template='plotly_dark',title='Foodstuffs'))

            
            if option3=='2018':
                fig=px.treemap(df, path=[px.Constant('PRODUCTS'),'Section', 'HS2','HS4'], values='Trade Value Previous 1', color='Trade Value Previous 1',hover_data=['TradeValue Growth(%)Pre 1'],color_continuous_scale='RdBu')
                fig.update_layout(margin= dict(t=50, l=25, r=25, b=25), width =1100,  height=650)
                st.plotly_chart(fig)
                col1, col2=st.columns(2)
                col1.plotly_chart(px.histogram(df.head(36), x='HS2' ,y='Trade Value Previous 1',width =650,  height=650 , template='plotly_dark',title='Animal Products'))
                col2.plotly_chart(px.histogram(df.iloc[37:114], x='HS2' ,y='Trade Value Previous 1',width =650,  height=650 , template='plotly_dark',title='Vegetable Products'))
                col1.plotly_chart(px.histogram(df.iloc[114:134], x='HS2' ,y='Trade Value Previous 1',width =500,  height=550 , template='plotly_dark',title='Animal and Vegetable Bi Product'))
                col2.plotly_chart(px.histogram(df.tail(53), x='HS2' ,y='Trade Value Previous 1',width =700,  height=700 , template='plotly_dark',title='Foodstuffs'))
            
            if option3=='2016-2018':
                fig=px.treemap(df, path=[px.Constant('PRODUCTS'),'Section', 'HS2','HS4'], values='Trade Value Previous 3', color='Trade Value Previous 3',hover_data=['TradeValue Growth(%)Pre 3'],color_continuous_scale='RdBu')
                fig.update_layout(margin= dict(t=50, l=25, r=25, b=25), width =1100,  height=650)
                st.plotly_chart(fig)
                col1, col2=st.columns(2)
                col1.plotly_chart(px.histogram(df.head(36), x='HS2' ,y='Trade Value Previous 3',width =650,  height=650 , template='plotly_dark',title='Animal Products'))
                col2.plotly_chart(px.histogram(df.iloc[37:114], x='HS2' ,y='Trade Value Previous 3',width =650,  height=650 , template='plotly_dark',title='Vegetable Products'))
                col1.plotly_chart(px.histogram(df.iloc[114:134], x='HS2' ,y='Trade Value Previous 3',width =500,  height=550 , template='plotly_dark',title='Animal and Vegetable Bi Product'))
                col2.plotly_chart(px.histogram(df.tail(53), x='HS2' ,y='Trade Value Previous 3',width =700,  height=700 , template='plotly_dark',title='Foodstuffs'))

            if option3=='2014-2018':
                fig=px.treemap(df, path=[px.Constant('PRODUCTS'),'Section', 'HS2','HS4'], values='Trade Value Previous 5', color='Trade Value Previous 5',hover_data=['TradeValue Growth(%)Pre 5'],color_continuous_scale='RdBu')
                fig.update_layout(margin= dict(t=50, l=25, r=25, b=25), width =1100,  height=650)
                st.plotly_chart(fig)
                col1, col2=st.columns(2)
                col1.plotly_chart(px.histogram(df.head(36), x='HS2' ,y='Trade Value Previous 5',width =650,  height=650 , template='plotly_dark',title='Animal Products'))
                col2.plotly_chart(px.histogram(df.iloc[37:114], x='HS2' ,y='Trade Value Previous 5',width =650,  height=650 , template='plotly_dark',title='Vegetable Products'))
                col1.plotly_chart(px.histogram(df.iloc[114:134], x='HS2' ,y='Trade Value Previous 5',width =500,  height=550 , template='plotly_dark',title='Animal and Vegetable Bi Product'))
                col2.plotly_chart(px.histogram(df.tail(53), x='HS2' ,y='Trade Value Previous 5',width =700,  height=700 , template='plotly_dark',title='Foodstuffs'))
            
        if option2== 'Export':
            st.markdown("<h3 style='text-align: center'>[Exports]</h3>", unsafe_allow_html=True)
            df=pd.read_csv('Egypt Export.csv')
            df.drop(columns=['Section ID','HS2 ID','HS4 ID'], inplace=True)
            df.rename(columns={'Trade Value Growth':'Trade Value Growth(%)','Trade Value Growth 1':'TradeValue Growth(%)Pre 1','Trade Value Growth 3':'TradeValue Growth(%)Pre 3','Trade Value Growth 5':'TradeValue Growth(%)Pre 5'},inplace=True)
            st.dataframe(df)

            if option3== '2019':
                fig=px.treemap(df, path=[px.Constant('PRODUCTS'),'Section', 'HS2','HS4'], values='Trade Value', color='Trade Value',hover_data=['Trade Value Growth(%)'],color_continuous_scale='RdBu')
                fig.update_layout(margin= dict(t=50, l=25, r=25, b=25), width =1100,  height=650)
                st.plotly_chart(fig)
                col1, col2=st.columns(2)
                col1.plotly_chart(px.histogram(df.head(34), x='HS2' ,y='Trade Value',width =650,  height=650 , template='plotly_dark',title='Animal Products'))
                col2.plotly_chart(px.histogram(df.iloc[35:112], x='HS2' ,y='Trade Value',width =650,  height=650 , template='plotly_dark',title='Vegetable Products'))
                col1.plotly_chart(px.histogram(df.iloc[112:134], x='HS2' ,y='Trade Value',width =500,  height=550 , template='plotly_dark',title='Animal and Vegetable Bi Product'))
                col2.plotly_chart(px.histogram(df.tail(52), x='HS2' ,y='Trade Value',width =700,  height=700 , template='plotly_dark',title='Foodstuffs'))

            if option3=='2018':
                fig=px.treemap(df, path=[px.Constant('PRODUCTS'),'Section', 'HS2','HS4'], values='Trade Value Previous 1', color='Trade Value Previous 1',hover_data=['TradeValue Growth(%)Pre 1'],color_continuous_scale='RdBu')
                fig.update_layout(margin= dict(t=50, l=25, r=25, b=25), width =1100,  height=650)
                st.plotly_chart(fig)
                col1, col2=st.columns(2)
                col1.plotly_chart(px.histogram(df.head(34), x='HS2' ,y='Trade Value Previous 1',width =650,  height=650 , template='plotly_dark',title='Animal Products'))
                col2.plotly_chart(px.histogram(df.iloc[35:112], x='HS2' ,y='Trade Value Previous 1',width =650,  height=650 , template='plotly_dark',title='Vegetable Products'))
                col1.plotly_chart(px.histogram(df.iloc[112:134], x='HS2' ,y='Trade Value Previous 1',width =500,  height=550 , template='plotly_dark',title='Animal and Vegetable Bi Product'))
                col2.plotly_chart(px.histogram(df.tail(52), x='HS2' ,y='Trade Value Previous 1',width =700,  height=700 , template='plotly_dark',title='Foodstuffs'))
            

            if option3=='2016-2018':
                fig=px.treemap(df, path=[px.Constant('PRODUCTS'),'Section', 'HS2','HS4'], values='Trade Value Previous 3', color='Trade Value Previous 3',hover_data=['TradeValue Growth(%)Pre 3'],color_continuous_scale='RdBu')
                fig.update_layout(margin= dict(t=50, l=25, r=25, b=25), width =1100,  height=650)
                st.plotly_chart(fig)
                col1, col2=st.columns(2)
                col1.plotly_chart(px.histogram(df.head(34), x='HS2' ,y='Trade Value Previous 3',width =650,  height=650 , template='plotly_dark',title='Animal Products'))
                col2.plotly_chart(px.histogram(df.iloc[35:112], x='HS2' ,y='Trade Value Previous 3',width =650,  height=650 , template='plotly_dark',title='Vegetable Products'))
                col1.plotly_chart(px.histogram(df.iloc[112:134], x='HS2' ,y='Trade Value Previous 3',width =500,  height=550 , template='plotly_dark',title='Animal and Vegetable Bi Product'))
                col2.plotly_chart(px.histogram(df.tail(52), x='HS2' ,y='Trade Value Previous 3',width =700,  height=700 , template='plotly_dark',title='Foodstuffs'))

            if option3=='2014-2018':
                fig=px.treemap(df, path=[px.Constant('PRODUCTS'),'Section', 'HS2','HS4'], values='Trade Value Previous 5', color='Trade Value Previous 5',hover_data=['TradeValue Growth(%)Pre 5'],color_continuous_scale='RdBu')
                fig.update_layout(margin= dict(t=50, l=25, r=25, b=25), width =1100,  height=650)
                st.plotly_chart(fig)
                col1, col2=st.columns(2)
                col1.plotly_chart(px.histogram(df.head(34), x='HS2' ,y='Trade Value Previous 5',width =650,  height=650 , template='plotly_dark',title='Animal Products'))
                col2.plotly_chart(px.histogram(df.iloc[35:112], x='HS2' ,y='Trade Value Previous 5',width =650,  height=650 , template='plotly_dark',title='Vegetable Products'))
                col1.plotly_chart(px.histogram(df.iloc[112:134], x='HS2' ,y='Trade Value Previous 5',width =500,  height=550 , template='plotly_dark',title='Animal and Vegetable Bi Product'))
                col2.plotly_chart(px.histogram(df.tail(52), x='HS2' ,y='Trade Value Previous 5',width =700,  height=700 , template='plotly_dark',title='Foodstuffs'))

        if option2=='Tariff':
            st.markdown("<h3 style='text-align: center'>[Tariff]</h3>", unsafe_allow_html=True)

            da=pd.read_csv('Animal Egypt.csv')
            da.drop(columns=['Section ID','HS2 ID','HS4 ID','HS6 ID' ], inplace=True)
            da.rename(columns={'Tariff':'Tariff(%)'},inplace=True)
            st.markdown('Tariff on Animal Products')
            st.dataframe(da)
            st.markdown('---')

            db=pd.read_csv('Vegetable Egypt.csv')
            db.drop(columns=['Section ID','HS2 ID','HS4 ID','HS6 ID' ], inplace=True)
            db.rename(columns={'Tariff':'Tariff(%)'},inplace=True)
            st.markdown('Tariff on Vegetable Products')
            st.dataframe(db)
            st.markdown('---')

            dc=pd.read_csv('Biproduct Egypt.csv')
            dc.drop(columns=['Section ID','HS2 ID','HS4 ID','HS6 ID' ], inplace=True)
            dc.rename(columns={'Tariff':'Tariff(%)'},inplace=True)
            st.markdown('Tariff on Animal and Vegetable Bi Products')
            st.dataframe(dc)
            st.markdown('---')

            dd=pd.read_csv('Foodstuf Egypt.csv')
            dd.drop(columns=['Section ID','HS2 ID','HS4 ID','HS6 ID' ], inplace=True)
            dd.rename(columns={'Tariff':'Tariff(%)'},inplace=True)
            st.markdown('Tariff on Foodstuffs')
            st.dataframe(dd)
            st.markdown('---')

        if option2== 'Service Trade':
            st.markdown("<h3 style='text-align: center'>[Service Trade]</h3>", unsafe_allow_html=True)
            
            dz=pd.read_csv('Egypt serviceimports.csv')
            dz.drop(columns=['Parent Service ID','Service ID' ], inplace=True)
            st.markdown('Service Imports 2019')
            st.dataframe(dz)
            st.plotly_chart(px.histogram(dz, x='Service' ,y='Service Value',width =650,  height=650 , template='plotly_dark'))
            
            dy=pd.read_csv('Egypt serviceexports.csv')
            dy.drop(columns=['Parent Service ID','Service ID' ], inplace=True)
            st.markdown('Service Exports 2019')
            st.dataframe(dy)
            st.plotly_chart(px.histogram(dy, x='Service' ,y='Service Value',width =650,  height=650 , template='plotly_dark'))
    #**********************************************************************************************************************************************
    #************************************************************************************************************************************************
    if option1=='Sudan':   
        st.markdown("<h2 style='text-align: center'><u>Sudan</u></h2>", unsafe_allow_html=True)
        if option2== 'Import':
            st.markdown("<h3 style='text-align: center'>[Imports]</h3>", unsafe_allow_html=True)
            df=pd.read_csv('Sudan Import.csv')
            df.drop(columns=['Section ID','HS2 ID','HS4 ID'], inplace=True)
            df.rename(columns={'Trade Value Growth':'Trade Value Growth(%)','Trade Value Growth 1':'TradeValue Growth(%)Pre 1','Trade Value Growth 3':'TradeValue Growth(%)Pre 3','Trade Value Growth 5':'TradeValue Growth(%)Pre 5'},inplace=True)
            st.dataframe(df)

            if option3== '2019':
                fig=px.treemap(df, path=[px.Constant('PRODUCTS'),'Section', 'HS2','HS4'], values='Trade Value', color='Trade Value',hover_data=['Trade Value Growth(%)'],color_continuous_scale='rdbu')
                fig.update_layout(margin= dict(t=50, l=25, r=25, b=25), width =1100,  height=650)
                st.plotly_chart(fig)
                col1, col2=st.columns(2)
                col1.plotly_chart(px.histogram(df.head(26), x='HS2' ,y='Trade Value',width =650,  height=650 , template='plotly_dark',title='Animal Products'))
                col2.plotly_chart(px.histogram(df.iloc[27:91], x='HS2' ,y='Trade Value',width =650,  height=650 , template='plotly_dark',title='Vegetable Products'))
                col1.plotly_chart(px.histogram(df.iloc[91:108], x='HS2' ,y='Trade Value',width =500,  height=550 , template='plotly_dark',title='Animal and Vegetable Bi Product'))
                col2.plotly_chart(px.histogram(df.tail(46), x='HS2' ,y='Trade Value',width =700,  height=700 , template='plotly_dark',title='Foodstuffs'))

            
            if option3=='2018':
                fig=px.treemap(df, path=[px.Constant('PRODUCTS'),'Section', 'HS2','HS4'], values='Trade Value Previous 1', color='Trade Value Previous 1',hover_data=['TradeValue Growth(%)Pre 1'],color_continuous_scale='RdBu')
                fig.update_layout(margin= dict(t=50, l=25, r=25, b=25), width =1100,  height=650)
                st.plotly_chart(fig)
                col1, col2=st.columns(2)
                col1.plotly_chart(px.histogram(df.head(26), x='HS2' ,y='Trade Value Previous 1',width =650,  height=650 , template='plotly_dark',title='Animal Products'))
                col2.plotly_chart(px.histogram(df.iloc[27:91], x='HS2' ,y='Trade Value Previous 1',width =650,  height=650 , template='plotly_dark',title='Vegetable Products'))
                col1.plotly_chart(px.histogram(df.iloc[91:108], x='HS2' ,y='Trade Value Previous 1',width =500,  height=550 , template='plotly_dark',title='Animal and Vegetable Bi Product'))
                col2.plotly_chart(px.histogram(df.tail(46), x='HS2' ,y='Trade Value Previous 1',width =700,  height=700 , template='plotly_dark',title='Foodstuffs'))
            
            if option3=='2016-2018':
                fig=px.treemap(df, path=[px.Constant('PRODUCTS'),'Section', 'HS2','HS4'], values='Trade Value Previous 3', color='Trade Value Previous 3',hover_data=['TradeValue Growth(%)Pre 3'],color_continuous_scale='RdBu')
                fig.update_layout(margin= dict(t=50, l=25, r=25, b=25), width =1100,  height=650)
                st.plotly_chart(fig)
                col1, col2=st.columns(2)
                col1.plotly_chart(px.histogram(df.head(26), x='HS2' ,y='Trade Value Previous 3',width =650,  height=650 , template='plotly_dark',title='Animal Products'))
                col2.plotly_chart(px.histogram(df.iloc[27:91], x='HS2' ,y='Trade Value Previous 3',width =650,  height=650 , template='plotly_dark',title='Vegetable Products'))
                col1.plotly_chart(px.histogram(df.iloc[91:108], x='HS2' ,y='Trade Value Previous 3',width =500,  height=550 , template='plotly_dark',title='Animal and Vegetable Bi Product'))
                col2.plotly_chart(px.histogram(df.tail(46), x='HS2' ,y='Trade Value Previous 3',width =700,  height=700 , template='plotly_dark',title='Foodstuffs'))

            if option3=='2014-2018':
                fig=px.treemap(df, path=[px.Constant('PRODUCTS'),'Section', 'HS2','HS4'], values='Trade Value Previous 5', color='Trade Value Previous 5',hover_data=['TradeValue Growth(%)Pre 5'],color_continuous_scale='RdBu')
                fig.update_layout(margin= dict(t=50, l=25, r=25, b=25), width =1100,  height=650)
                st.plotly_chart(fig)
                col1, col2=st.columns(2)
                col1.plotly_chart(px.histogram(df.head(26), x='HS2' ,y='Trade Value Previous 5',width =650,  height=650 , template='plotly_dark',title='Animal Products'))
                col2.plotly_chart(px.histogram(df.iloc[27:91], x='HS2' ,y='Trade Value Previous 5',width =650,  height=650 , template='plotly_dark',title='Vegetable Products'))
                col1.plotly_chart(px.histogram(df.iloc[91:108], x='HS2' ,y='Trade Value Previous 5',width =500,  height=550 , template='plotly_dark',title='Animal and Vegetable Bi Product'))
                col2.plotly_chart(px.histogram(df.tail(46), x='HS2' ,y='Trade Value Previous 5',width =700,  height=700 , template='plotly_dark',title='Foodstuffs'))
            
        if option2== 'Export':
            st.markdown("<h3 style='text-align: center'>[Exports]</h3>", unsafe_allow_html=True)
            df=pd.read_csv('Sudan Export.csv')
            df.drop(columns=['Section ID','HS2 ID','HS4 ID'], inplace=True)
            df.rename(columns={'Trade Value Growth':'Trade Value Growth(%)','Trade Value Growth 1':'TradeValue Growth(%)Pre 1','Trade Value Growth 3':'TradeValue Growth(%)Pre 3','Trade Value Growth 5':'TradeValue Growth(%)Pre 5'},inplace=True)
            st.dataframe(df)

            if option3== '2019':
                fig=px.treemap(df, path=[px.Constant('PRODUCTS'),'Section', 'HS2','HS4'], values='Trade Value', color='Trade Value',hover_data=['Trade Value Growth(%)'],color_continuous_scale='RdBu')
                fig.update_layout(margin= dict(t=50, l=25, r=25, b=25), width =1100,  height=650)
                st.plotly_chart(fig)
                col1, col2=st.columns(2)
                col1.plotly_chart(px.histogram(df.head(22), x='HS2' ,y='Trade Value',width =650,  height=650 , template='plotly_dark',title='Animal Products'))
                col2.plotly_chart(px.histogram(df.iloc[23:71], x='HS2' ,y='Trade Value',width =650,  height=650 , template='plotly_dark',title='Vegetable Products'))
                col1.plotly_chart(px.histogram(df.iloc[71:77], x='HS2' ,y='Trade Value',width =500,  height=550 , template='plotly_dark',title='Animal and Vegetable Bi Product'))
                col2.plotly_chart(px.histogram(df.tail(26), x='HS2' ,y='Trade Value',width =700,  height=700 , template='plotly_dark',title='Foodstuffs'))

            if option3=='2018':
                fig=px.treemap(df, path=[px.Constant('PRODUCTS'),'Section', 'HS2','HS4'], values='Trade Value Previous 1', color='Trade Value Previous 1',hover_data=['TradeValue Growth(%)Pre 1'],color_continuous_scale='RdBu')
                fig.update_layout(margin= dict(t=50, l=25, r=25, b=25), width =1100,  height=650)
                st.plotly_chart(fig)
                col1, col2=st.columns(2)
                col1.plotly_chart(px.histogram(df.head(22), x='HS2' ,y='Trade Value Previous 1',width =650,  height=650 , template='plotly_dark',title='Animal Products'))
                col2.plotly_chart(px.histogram(df.iloc[23:71], x='HS2' ,y='Trade Value Previous 1',width =650,  height=650 , template='plotly_dark',title='Vegetable Products'))
                col1.plotly_chart(px.histogram(df.iloc[71:77], x='HS2' ,y='Trade Value Previous 1',width =500,  height=550 , template='plotly_dark',title='Animal and Vegetable Bi Product'))
                col2.plotly_chart(px.histogram(df.tail(26), x='HS2' ,y='Trade Value Previous 1',width =700,  height=700 , template='plotly_dark',title='Foodstuffs'))
            

            if option3=='2016-2018':
                fig=px.treemap(df, path=[px.Constant('PRODUCTS'),'Section', 'HS2','HS4'], values='Trade Value Previous 3', color='Trade Value Previous 3',hover_data=['TradeValue Growth(%)Pre 3'],color_continuous_scale='RdBu')
                fig.update_layout(margin= dict(t=50, l=25, r=25, b=25), width =1100,  height=650)
                st.plotly_chart(fig)
                col1, col2=st.columns(2)
                col1.plotly_chart(px.histogram(df.head(22), x='HS2' ,y='Trade Value Previous 3',width =650,  height=650 , template='plotly_dark',title='Animal Products'))
                col2.plotly_chart(px.histogram(df.iloc[23:71], x='HS2' ,y='Trade Value Previous 3',width =650,  height=650 , template='plotly_dark',title='Vegetable Products'))
                col1.plotly_chart(px.histogram(df.iloc[71:77], x='HS2' ,y='Trade Value Previous 3',width =500,  height=550 , template='plotly_dark',title='Animal and Vegetable Bi Product'))
                col2.plotly_chart(px.histogram(df.tail(26), x='HS2' ,y='Trade Value Previous 3',width =700,  height=700 , template='plotly_dark',title='Foodstuffs'))

            if option3=='2014-2018':
                fig=px.treemap(df, path=[px.Constant('PRODUCTS'),'Section', 'HS2','HS4'], values='Trade Value Previous 5', color='Trade Value Previous 5',hover_data=['TradeValue Growth(%)Pre 5'],color_continuous_scale='RdBu')
                fig.update_layout(margin= dict(t=50, l=25, r=25, b=25), width =1100,  height=650)
                st.plotly_chart(fig)
                col1, col2=st.columns(2)
                col1.plotly_chart(px.histogram(df.head(22), x='HS2' ,y='Trade Value Previous 5',width =650,  height=650 , template='plotly_dark',title='Animal Products'))
                col2.plotly_chart(px.histogram(df.iloc[23:71], x='HS2' ,y='Trade Value Previous 5',width =650,  height=650 , template='plotly_dark',title='Vegetable Products'))
                col1.plotly_chart(px.histogram(df.iloc[71:77], x='HS2' ,y='Trade Value Previous 5',width =500,  height=550 , template='plotly_dark',title='Animal and Vegetable Bi Product'))
                col2.plotly_chart(px.histogram(df.tail(26), x='HS2' ,y='Trade Value Previous 5',width =700,  height=700 , template='plotly_dark',title='Foodstuffs'))

        if option2=='Tariff':
            st.markdown("<h3 style='text-align: center'>[Tariff]</h3>", unsafe_allow_html=True)

            da=pd.read_csv('Animal Sudan.csv')
            da.drop(columns=['Section ID','HS2 ID','HS4 ID','HS6 ID' ], inplace=True)
            da.rename(columns={'Tariff':'Tariff(%)'},inplace=True)
            st.markdown('Tariff on Animal Products')
            st.dataframe(da)
            st.markdown('---')

            db=pd.read_csv('Vegetable Sudan.csv')
            db.drop(columns=['Section ID','HS2 ID','HS4 ID','HS6 ID' ], inplace=True)
            db.rename(columns={'Tariff':'Tariff(%)'},inplace=True)
            st.markdown('Tariff on Vegetable Products')
            st.dataframe(db)
            st.markdown('---')

            dc=pd.read_csv('Biproduct Sudan.csv')
            dc.drop(columns=['Section ID','HS2 ID','HS4 ID','HS6 ID' ], inplace=True)
            dc.rename(columns={'Tariff':'Tariff(%)'},inplace=True)
            st.markdown('Tariff on Animal and Vegetable Bi Products')
            st.dataframe(dc)
            st.markdown('---')

            dd=pd.read_csv('Foodstuf Sudan.csv')
            dd.drop(columns=['Section ID','HS2 ID','HS4 ID','HS6 ID' ], inplace=True)
            dd.rename(columns={'Tariff':'Tariff(%)'},inplace=True)
            st.markdown('Tariff on Foodstuffs')
            st.dataframe(dd)
            st.markdown('---')
        
        if option2== 'Service Trade':
            st.markdown("<h3 style='text-align: center'>[Service Trade]</h3>", unsafe_allow_html=True)
            
            dz=pd.read_csv('Sudan serviceimports.csv')
            dz.drop(columns=['Parent Service ID','Service ID' ], inplace=True)
            st.markdown('Service Imports 2015')
            st.dataframe(dz)
            st.plotly_chart(px.histogram(dz, x='Service' ,y='Service Value',width =650,  height=650 , template='plotly_dark'))
            
            dy=pd.read_csv('Sudan serviceexports.csv')
            dy.drop(columns=['Parent Service ID','Service ID' ], inplace=True)
            st.markdown('Service Exports 2015')
            st.dataframe(dy)
            st.plotly_chart(px.histogram(dy, x='Service' ,y='Service Value',width =650,  height=650 , template='plotly_dark'))
    #********************************************************************************************************************************************
    #***************************************************************************************************************************************************
    if option1=='Tunisia':
        st.markdown("<h2 style='text-align: center'><u>Tunisia</u></h2>", unsafe_allow_html=True)   
        if option2== 'Import':
            st.markdown("<h3 style='text-align: center'>[Imports]</h3>", unsafe_allow_html=True)
            df=pd.read_csv('Tunisia Import.csv')
            df.drop(columns=['Section ID','HS2 ID','HS4 ID'], inplace=True)
            df.rename(columns={'Trade Value Growth':'Trade Value Growth(%)','Trade Value Growth 1':'TradeValue Growth(%)Pre 1','Trade Value Growth 3':'TradeValue Growth(%)Pre 3','Trade Value Growth 5':'TradeValue Growth(%)Pre 5'},inplace=True)
            st.dataframe(df)

            if option3== '2019':
                fig=px.treemap(df, path=[px.Constant('PRODUCTS'),'Section', 'HS2','HS4'], values='Trade Value', color='Trade Value',hover_data=['Trade Value Growth(%)'],color_continuous_scale='rdbu')
                fig.update_layout(margin= dict(t=50, l=25, r=25, b=25), width =1100,  height=650)
                st.plotly_chart(fig)
                col1, col2=st.columns(2)
                col1.plotly_chart(px.histogram(df.head(37), x='HS2' ,y='Trade Value',width =650,  height=650 , template='plotly_dark',title='Animal Products'))
                col2.plotly_chart(px.histogram(df.iloc[38:108], x='HS2' ,y='Trade Value',width =650,  height=650 , template='plotly_dark',title='Vegetable Products'))
                col1.plotly_chart(px.histogram(df.iloc[108:129], x='HS2' ,y='Trade Value',width =500,  height=550 , template='plotly_dark',title='Animal and Vegetable Bi Product'))
                col2.plotly_chart(px.histogram(df.tail(52), x='HS2' ,y='Trade Value',width =700,  height=700 , template='plotly_dark',title='Foodstuffs'))

            
            if option3=='2018':
                fig=px.treemap(df, path=[px.Constant('PRODUCTS'),'Section', 'HS2','HS4'], values='Trade Value Previous 1', color='Trade Value Previous 1',hover_data=['TradeValue Growth(%)Pre 1'],color_continuous_scale='RdBu')
                fig.update_layout(margin= dict(t=50, l=25, r=25, b=25), width =1100,  height=650)
                st.plotly_chart(fig)
                col1, col2=st.columns(2)
                col1.plotly_chart(px.histogram(df.head(37), x='HS2' ,y='Trade Value Previous 1',width =650,  height=650 , template='plotly_dark',title='Animal Products'))
                col2.plotly_chart(px.histogram(df.iloc[38:108], x='HS2' ,y='Trade Value Previous 1',width =650,  height=650 , template='plotly_dark',title='Vegetable Products'))
                col1.plotly_chart(px.histogram(df.iloc[108:129], x='HS2' ,y='Trade Value Previous 1',width =500,  height=550 , template='plotly_dark',title='Animal and Vegetable Bi Product'))
                col2.plotly_chart(px.histogram(df.tail(52), x='HS2' ,y='Trade Value Previous 1',width =700,  height=700 , template='plotly_dark',title='Foodstuffs'))
            
            if option3=='2016-2018':
                fig=px.treemap(df, path=[px.Constant('PRODUCTS'),'Section', 'HS2','HS4'], values='Trade Value Previous 3', color='Trade Value Previous 3',hover_data=['TradeValue Growth(%)Pre 3'],color_continuous_scale='RdBu')
                fig.update_layout(margin= dict(t=50, l=25, r=25, b=25), width =1100,  height=650)
                st.plotly_chart(fig)
                col1, col2=st.columns(2)
                col1.plotly_chart(px.histogram(df.head(37), x='HS2' ,y='Trade Value Previous 3',width =650,  height=650 , template='plotly_dark',title='Animal Products'))
                col2.plotly_chart(px.histogram(df.iloc[38:108], x='HS2' ,y='Trade Value Previous 3',width =650,  height=650 , template='plotly_dark',title='Vegetable Products'))
                col1.plotly_chart(px.histogram(df.iloc[108:129], x='HS2' ,y='Trade Value Previous 3',width =500,  height=550 , template='plotly_dark',title='Animal and Vegetable Bi Product'))
                col2.plotly_chart(px.histogram(df.tail(52), x='HS2' ,y='Trade Value Previous 3',width =700,  height=700 , template='plotly_dark',title='Foodstuffs'))

            if option3=='2014-2018':
                fig=px.treemap(df, path=[px.Constant('PRODUCTS'),'Section', 'HS2','HS4'], values='Trade Value Previous 5', color='Trade Value Previous 5',hover_data=['TradeValue Growth(%)Pre 5'],color_continuous_scale='RdBu')
                fig.update_layout(margin= dict(t=50, l=25, r=25, b=25), width =1100,  height=650)
                st.plotly_chart(fig)
                col1, col2=st.columns(2)
                col1.plotly_chart(px.histogram(df.head(37), x='HS2' ,y='Trade Value Previous 5',width =650,  height=650 , template='plotly_dark',title='Animal Products'))
                col2.plotly_chart(px.histogram(df.iloc[38:108], x='HS2' ,y='Trade Value Previous 5',width =650,  height=650 , template='plotly_dark',title='Vegetable Products'))
                col1.plotly_chart(px.histogram(df.iloc[108:129], x='HS2' ,y='Trade Value Previous 5',width =500,  height=550 , template='plotly_dark',title='Animal and Vegetable Bi Product'))
                col2.plotly_chart(px.histogram(df.tail(52), x='HS2' ,y='Trade Value Previous 5',width =700,  height=700 , template='plotly_dark',title='Foodstuffs'))
            
        if option2== 'Export':
            st.markdown("<h3 style='text-align: center'>[Exports]</h3>", unsafe_allow_html=True)
            df=pd.read_csv('Tunisia Export.csv')
            df.drop(columns=['Section ID','HS2 ID','HS4 ID'], inplace=True)
            df.rename(columns={'Trade Value Growth':'Trade Value Growth(%)','Trade Value Growth 1':'TradeValue Growth(%)Pre 1','Trade Value Growth 3':'TradeValue Growth(%)Pre 3','Trade Value Growth 5':'TradeValue Growth(%)Pre 5'},inplace=True)
            st.dataframe(df)

            if option3== '2019':
                fig=px.treemap(df, path=[px.Constant('PRODUCTS'),'Section', 'HS2','HS4'], values='Trade Value', color='Trade Value',hover_data=['Trade Value Growth(%)'],color_continuous_scale='RdBu')
                fig.update_layout(margin= dict(t=50, l=25, r=25, b=25), width =1100,  height=650)
                st.plotly_chart(fig)
                col1, col2=st.columns(2)
                col1.plotly_chart(px.histogram(df.head(25), x='HS2' ,y='Trade Value',width =650,  height=650 , template='plotly_dark',title='Animal Products'))
                col2.plotly_chart(px.histogram(df.iloc[26:91], x='HS2' ,y='Trade Value',width =650,  height=650 , template='plotly_dark',title='Vegetable Products'))
                col1.plotly_chart(px.histogram(df.iloc[91:110], x='HS2' ,y='Trade Value',width =500,  height=550 , template='plotly_dark',title='Animal and Vegetable Bi Product'))
                col2.plotly_chart(px.histogram(df.tail(46), x='HS2' ,y='Trade Value',width =700,  height=700 , template='plotly_dark',title='Foodstuffs'))

            if option3=='2018':
                fig=px.treemap(df, path=[px.Constant('PRODUCTS'),'Section', 'HS2','HS4'], values='Trade Value Previous 1', color='Trade Value Previous 1',hover_data=['TradeValue Growth(%)Pre 1'],color_continuous_scale='RdBu')
                fig.update_layout(margin= dict(t=50, l=25, r=25, b=25), width =1100,  height=650)
                st.plotly_chart(fig)
                col1, col2=st.columns(2)
                col1.plotly_chart(px.histogram(df.head(25), x='HS2' ,y='Trade Value Previous 1',width =650,  height=650 , template='plotly_dark',title='Animal Products'))
                col2.plotly_chart(px.histogram(df.iloc[26:91], x='HS2' ,y='Trade Value Previous 1',width =650,  height=650 , template='plotly_dark',title='Vegetable Products'))
                col1.plotly_chart(px.histogram(df.iloc[91:110], x='HS2' ,y='Trade Value Previous 1',width =500,  height=550 , template='plotly_dark',title='Animal and Vegetable Bi Product'))
                col2.plotly_chart(px.histogram(df.tail(46), x='HS2' ,y='Trade Value Previous 1',width =700,  height=700 , template='plotly_dark',title='Foodstuffs'))
            

            if option3=='2016-2018':
                fig=px.treemap(df, path=[px.Constant('PRODUCTS'),'Section', 'HS2','HS4'], values='Trade Value Previous 3', color='Trade Value Previous 3',hover_data=['TradeValue Growth(%)Pre 3'],color_continuous_scale='RdBu')
                fig.update_layout(margin= dict(t=50, l=25, r=25, b=25), width =1100,  height=650)
                st.plotly_chart(fig)
                col1, col2=st.columns(2)
                col1.plotly_chart(px.histogram(df.head(25), x='HS2' ,y='Trade Value Previous 3',width =650,  height=650 , template='plotly_dark',title='Animal Products'))
                col2.plotly_chart(px.histogram(df.iloc[26:91], x='HS2' ,y='Trade Value Previous 3',width =650,  height=650 , template='plotly_dark',title='Vegetable Products'))
                col1.plotly_chart(px.histogram(df.iloc[91:110], x='HS2' ,y='Trade Value Previous 3',width =500,  height=550 , template='plotly_dark',title='Animal and Vegetable Bi Product'))
                col2.plotly_chart(px.histogram(df.tail(46), x='HS2' ,y='Trade Value Previous 3',width =700,  height=700 , template='plotly_dark',title='Foodstuffs'))

            if option3=='2014-2018':
                fig=px.treemap(df, path=[px.Constant('PRODUCTS'),'Section', 'HS2','HS4'], values='Trade Value Previous 5', color='Trade Value Previous 5',hover_data=['TradeValue Growth(%)Pre 5'],color_continuous_scale='RdBu')
                fig.update_layout(margin= dict(t=50, l=25, r=25, b=25), width =1100,  height=650)
                st.plotly_chart(fig)
                col1, col2=st.columns(2)
                col1.plotly_chart(px.histogram(df.head(25), x='HS2' ,y='Trade Value Previous 5',width =650,  height=650 , template='plotly_dark',title='Animal Products'))
                col2.plotly_chart(px.histogram(df.iloc[26:91], x='HS2' ,y='Trade Value Previous 5',width =650,  height=650 , template='plotly_dark',title='Vegetable Products'))
                col1.plotly_chart(px.histogram(df.iloc[91:110], x='HS2' ,y='Trade Value Previous 5',width =500,  height=550 , template='plotly_dark',title='Animal and Vegetable Bi Product'))
                col2.plotly_chart(px.histogram(df.tail(46), x='HS2' ,y='Trade Value Previous 5',width =700,  height=700 , template='plotly_dark',title='Foodstuffs'))

        if option2=='Tariff':
            st.markdown("<h3 style='text-align: center'>[Tariff]</h3>", unsafe_allow_html=True)

            da=pd.read_csv('Animal Tunisia.csv')
            da.drop(columns=['Section ID','HS2 ID','HS4 ID','HS6 ID' ], inplace=True)
            da.rename(columns={'Tariff':'Tariff(%)'},inplace=True)
            st.markdown('Tariff on Animal Products')
            st.dataframe(da)
            st.markdown('---')

            db=pd.read_csv('Vegetable Tunisia.csv')
            db.drop(columns=['Section ID','HS2 ID','HS4 ID','HS6 ID' ], inplace=True)
            db.rename(columns={'Tariff':'Tariff(%)'},inplace=True)
            st.markdown('Tariff on Vegetable Products')
            st.dataframe(db)
            st.markdown('---')

            dc=pd.read_csv('Biproduct Tunisia.csv')
            dc.drop(columns=['Section ID','HS2 ID','HS4 ID','HS6 ID' ], inplace=True)
            dc.rename(columns={'Tariff':'Tariff(%)'},inplace=True)
            st.markdown('Tariff on Animal and Vegetable Bi Products')
            st.dataframe(dc)
            st.markdown('---')

            dd=pd.read_csv('Foodstuff Tunisia.csv')
            dd.drop(columns=['Section ID','HS2 ID','HS4 ID','HS6 ID' ], inplace=True)
            dd.rename(columns={'Tariff':'Tariff(%)'},inplace=True)
            st.markdown('Tariff on Foodstuffs')
            st.dataframe(dd)
            st.markdown('---')
        
        if option2== 'Service Trade':
            st.markdown("<h3 style='text-align: center'>[Service Trade]</h3>", unsafe_allow_html=True)
            
            dz=pd.read_csv('Tunisia serviceimports.csv')
            dz.drop(columns=['Parent Service ID','Service ID' ], inplace=True)
            st.markdown('Service Imports 2018')
            st.dataframe(dz)
            st.plotly_chart(px.histogram(dz, x='Service' ,y='Service Value',width =650,  height=650 , template='plotly_dark'))
            
            dy=pd.read_csv('Tunisia serviceexports.csv')
            dy.drop(columns=['Parent Service ID','Service ID' ], inplace=True)
            st.markdown('Service Exports 2018')
            st.dataframe(dy)
            st.plotly_chart(px.histogram(dy, x='Service' ,y='Service Value',width =650,  height=650 , template='plotly_dark'))
    #**********************************************************************************************************************************************
    #***********************************************************************************************************************************************
    if option1=='Libya':   
        st.markdown("<h2 style='text-align: center'><u>Libya</u></h2>", unsafe_allow_html=True)
        if option2== 'Import':
            st.markdown("<h3 style='text-align: center'>[Imports]</h3>", unsafe_allow_html=True)
            df=pd.read_csv('Libya Import.csv')
            df.drop(columns=['Section ID','HS2 ID','HS4 ID'], inplace=True)
            df.rename(columns={'Trade Value Growth':'Trade Value Growth(%)','Trade Value Growth 1':'TradeValue Growth(%)Pre 1','Trade Value Growth 3':'TradeValue Growth(%)Pre 3','Trade Value Growth 5':'TradeValue Growth(%)Pre 5'},inplace=True)
            st.dataframe(df)

            if option3== '2019':
                fig=px.treemap(df, path=[px.Constant('PRODUCTS'),'Section', 'HS2','HS4'], values='Trade Value', color='Trade Value',hover_data=['Trade Value Growth(%)'],color_continuous_scale='rdbu')
                fig.update_layout(margin= dict(t=50, l=25, r=25, b=25), width =1100,  height=650)
                st.plotly_chart(fig)
                col1, col2=st.columns(2)
                col1.plotly_chart(px.histogram(df.head(32), x='HS2' ,y='Trade Value',width =650,  height=650 , template='plotly_dark',title='Animal Products'))
                col2.plotly_chart(px.histogram(df.iloc[33:103], x='HS2' ,y='Trade Value',width =650,  height=650 , template='plotly_dark',title='Vegetable Products'))
                col1.plotly_chart(px.histogram(df.iloc[103:120], x='HS2' ,y='Trade Value',width =500,  height=550 , template='plotly_dark',title='Animal and Vegetable Bi Product'))
                col2.plotly_chart(px.histogram(df.tail(49), x='HS2' ,y='Trade Value',width =700,  height=700 , template='plotly_dark',title='Foodstuffs'))

            
            if option3=='2018':
                fig=px.treemap(df, path=[px.Constant('PRODUCTS'),'Section', 'HS2','HS4'], values='Trade Value Previous 1', color='Trade Value Previous 1',hover_data=['TradeValue Growth(%)Pre 1'],color_continuous_scale='RdBu')
                fig.update_layout(margin= dict(t=50, l=25, r=25, b=25), width =1100,  height=650)
                st.plotly_chart(fig)
                col1, col2=st.columns(2)
                col1.plotly_chart(px.histogram(df.head(32), x='HS2' ,y='Trade Value Previous 1',width =650,  height=650 , template='plotly_dark',title='Animal Products'))
                col2.plotly_chart(px.histogram(df.iloc[33:103], x='HS2' ,y='Trade Value Previous 1',width =650,  height=650 , template='plotly_dark',title='Vegetable Products'))
                col1.plotly_chart(px.histogram(df.iloc[103:120], x='HS2' ,y='Trade Value Previous 1',width =500,  height=550 , template='plotly_dark',title='Animal and Vegetable Bi Product'))
                col2.plotly_chart(px.histogram(df.tail(49), x='HS2' ,y='Trade Value Previous 1',width =700,  height=700 , template='plotly_dark',title='Foodstuffs'))
            
            if option3=='2016-2018':
                fig=px.treemap(df, path=[px.Constant('PRODUCTS'),'Section', 'HS2','HS4'], values='Trade Value Previous 3', color='Trade Value Previous 3',hover_data=['TradeValue Growth(%)Pre 3'],color_continuous_scale='RdBu')
                fig.update_layout(margin= dict(t=50, l=25, r=25, b=25), width =1100,  height=650)
                st.plotly_chart(fig)
                col1, col2=st.columns(2)
                col1.plotly_chart(px.histogram(df.head(32), x='HS2' ,y='Trade Value Previous 3',width =650,  height=650 , template='plotly_dark',title='Animal Products'))
                col2.plotly_chart(px.histogram(df.iloc[33:103], x='HS2' ,y='Trade Value Previous 3',width =650,  height=650 , template='plotly_dark',title='Vegetable Products'))
                col1.plotly_chart(px.histogram(df.iloc[103:120], x='HS2' ,y='Trade Value Previous 3',width =500,  height=550 , template='plotly_dark',title='Animal and Vegetable Bi Product'))
                col2.plotly_chart(px.histogram(df.tail(49), x='HS2' ,y='Trade Value Previous 3',width =700,  height=700 , template='plotly_dark',title='Foodstuffs'))

            if option3=='2014-2018':
                fig=px.treemap(df, path=[px.Constant('PRODUCTS'),'Section', 'HS2','HS4'], values='Trade Value Previous 5', color='Trade Value Previous 5',hover_data=['TradeValue Growth(%)Pre 5'],color_continuous_scale='RdBu')
                fig.update_layout(margin= dict(t=50, l=25, r=25, b=25), width =1100,  height=650)
                st.plotly_chart(fig)
                col1, col2=st.columns(2)
                col1.plotly_chart(px.histogram(df.head(32), x='HS2' ,y='Trade Value Previous 5',width =650,  height=650 , template='plotly_dark',title='Animal Products'))
                col2.plotly_chart(px.histogram(df.iloc[33:103], x='HS2' ,y='Trade Value Previous 5',width =650,  height=650 , template='plotly_dark',title='Vegetable Products'))
                col1.plotly_chart(px.histogram(df.iloc[103:120], x='HS2' ,y='Trade Value Previous 5',width =500,  height=550 , template='plotly_dark',title='Animal and Vegetable Bi Product'))
                col2.plotly_chart(px.histogram(df.tail(49), x='HS2' ,y='Trade Value Previous 5',width =700,  height=700 , template='plotly_dark',title='Foodstuffs'))
            
        if option2== 'Export':
            st.markdown("<h3 style='text-align: center'>[Exports]</h3>", unsafe_allow_html=True)
            df=pd.read_csv('Libya Export.csv')
            df.drop(columns=['Section ID','HS2 ID','HS4 ID'], inplace=True)
            df.rename(columns={'Trade Value Growth':'Trade Value Growth(%)','Trade Value Growth 1':'TradeValue Growth(%)Pre 1','Trade Value Growth 3':'TradeValue Growth(%)Pre 3','Trade Value Growth 5':'TradeValue Growth(%)Pre 5'},inplace=True)
            st.dataframe(df)

            if option3== '2019':
                fig=px.treemap(df, path=[px.Constant('PRODUCTS'),'Section', 'HS2','HS4'], values='Trade Value', color='Trade Value',hover_data=['Trade Value Growth(%)'],color_continuous_scale='RdBu')
                fig.update_layout(margin= dict(t=50, l=25, r=25, b=25), width =1100,  height=650)
                st.plotly_chart(fig)
                col1, col2=st.columns(2)
                col1.plotly_chart(px.histogram(df.head(10), x='HS2' ,y='Trade Value',width =650,  height=650 , template='plotly_dark',title='Animal Products'))
                col2.plotly_chart(px.histogram(df.iloc[11:28], x='HS2' ,y='Trade Value',width =650,  height=650 , template='plotly_dark',title='Vegetable Products'))
                col1.plotly_chart(px.histogram(df.iloc[28:31], x='HS2' ,y='Trade Value',width =500,  height=550 , template='plotly_dark',title='Animal and Vegetable Bi Product'))
                col2.plotly_chart(px.histogram(df.tail(20), x='HS2' ,y='Trade Value',width =700,  height=700 , template='plotly_dark',title='Foodstuffs'))

            if option3=='2018':
                fig=px.treemap(df, path=[px.Constant('PRODUCTS'),'Section', 'HS2','HS4'], values='Trade Value Previous 1', color='Trade Value Previous 1',hover_data=['TradeValue Growth(%)Pre 1'],color_continuous_scale='RdBu')
                fig.update_layout(margin= dict(t=50, l=25, r=25, b=25), width =1100,  height=650)
                st.plotly_chart(fig)
                col1, col2=st.columns(2)
                col1.plotly_chart(px.histogram(df.head(10), x='HS2' ,y='Trade Value Previous 1',width =650,  height=650 , template='plotly_dark',title='Animal Products'))
                col2.plotly_chart(px.histogram(df.iloc[11:28], x='HS2' ,y='Trade Value Previous 1',width =650,  height=650 , template='plotly_dark',title='Vegetable Products'))
                col1.plotly_chart(px.histogram(df.iloc[28:31], x='HS2' ,y='Trade Value Previous 1',width =500,  height=550 , template='plotly_dark',title='Animal and Vegetable Bi Product'))
                col2.plotly_chart(px.histogram(df.tail(20), x='HS2' ,y='Trade Value Previous 1',width =700,  height=700 , template='plotly_dark',title='Foodstuffs'))
            

            if option3=='2016-2018':
                fig=px.treemap(df, path=[px.Constant('PRODUCTS'),'Section', 'HS2','HS4'], values='Trade Value Previous 3', color='Trade Value Previous 3',hover_data=['TradeValue Growth(%)Pre 3'],color_continuous_scale='RdBu')
                fig.update_layout(margin= dict(t=50, l=25, r=25, b=25), width =1100,  height=650)
                st.plotly_chart(fig)
                col1, col2=st.columns(2)
                col1.plotly_chart(px.histogram(df.head(10), x='HS2' ,y='Trade Value Previous 3',width =650,  height=650 , template='plotly_dark',title='Animal Products'))
                col2.plotly_chart(px.histogram(df.iloc[11:28], x='HS2' ,y='Trade Value Previous 3',width =650,  height=650 , template='plotly_dark',title='Vegetable Products'))
                col1.plotly_chart(px.histogram(df.iloc[28:31], x='HS2' ,y='Trade Value Previous 3',width =500,  height=550 , template='plotly_dark',title='Animal and Vegetable Bi Product'))
                col2.plotly_chart(px.histogram(df.tail(20), x='HS2' ,y='Trade Value Previous 3',width =700,  height=700 , template='plotly_dark',title='Foodstuffs'))

            if option3=='2014-2018':
                fig=px.treemap(df, path=[px.Constant('PRODUCTS'),'Section', 'HS2','HS4'], values='Trade Value Previous 5', color='Trade Value Previous 5',hover_data=['TradeValue Growth(%)Pre 5'],color_continuous_scale='RdBu')
                fig.update_layout(margin= dict(t=50, l=25, r=25, b=25), width =1100,  height=650)
                st.plotly_chart(fig)
                col1, col2=st.columns(2)
                col1.plotly_chart(px.histogram(df.head(10), x='HS2' ,y='Trade Value Previous 5',width =650,  height=650 , template='plotly_dark',title='Animal Products'))
                col2.plotly_chart(px.histogram(df.iloc[11:28], x='HS2' ,y='Trade Value Previous 5',width =650,  height=650 , template='plotly_dark',title='Vegetable Products'))
                col1.plotly_chart(px.histogram(df.iloc[28:31], x='HS2' ,y='Trade Value Previous 5',width =500,  height=550 , template='plotly_dark',title='Animal and Vegetable Bi Product'))
                col2.plotly_chart(px.histogram(df.tail(20), x='HS2' ,y='Trade Value Previous 5',width =700,  height=700 , template='plotly_dark',title='Foodstuffs'))
        
        if option2=='Tariff':
            st.write('No Data Available')

        if option2== 'Service Trade':
            st.markdown("<h3 style='text-align: center'>[Service Trade]</h3>", unsafe_allow_html=True)
            
            dz=pd.read_csv('Libya serviceimports.csv')
            dz.drop(columns=['Parent Service ID','Service ID' ], inplace=True)
            st.markdown('Service Imports 2018')
            st.dataframe(dz)
            st.plotly_chart(px.histogram(dz, x='Service' ,y='Service Value',width =650,  height=650 , template='plotly_dark'))
            
            dy=pd.read_csv('Libya serviceexports.csv')
            dy.drop(columns=['Parent Service ID','Service ID' ], inplace=True)
            st.markdown('Service Exports 2018')
            st.dataframe(dy)
            st.plotly_chart(px.histogram(dy, x='Service' ,y='Service Value',width =650,  height=650 , template='plotly_dark'))
    st.markdown('---') 
    #------------------------------------------------------------------------------------------------------------------------------------------------
    #**********************************************************************************************************************************************
    #------------------------------------------------------------------------------------------------------------------------------------------------
    #***********************************************************************************************************************************************
