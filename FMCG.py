import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from annotated_text import annotated_text

sidebar= st.sidebar
st.markdown("<h1 style='text-align: center'><u>'Trade of FMCG Products'</u></h1>", unsafe_allow_html=True)
option2= sidebar.radio('Select',('Import','Export'))
option1= st.selectbox('Select the Country', ('Morocco','Algeria','Egypt','Sudan','Tunisia','Libya'))
option3= sidebar.radio('Select',('2019','Previous Year','Previous 3 Years', 'Previous 5 Years'))
option4= sidebar.radio('Select', ('Animal Product','Vegetable Product','Animal and Vegetable Bi Product', 'Foodstuffs'))
#----------------------------------------------------------------------------------------------------------------------------------------------

if option2=='Import':   
    if option1== 'Morocco':
        
        df=pd.read_csv('Morocco Import.csv')
        df.drop(columns=['Section ID','HS2 ID','HS4 ID'], inplace=True)
        df.rename(columns={'Trade Value Growth':'Trade Value Growth(%)','Trade Value Growth 1':'TradeValue Growth(%)Pre 1','Trade Value Growth 3':'TradeValue Growth(%)Pre 3','Trade Value Growth 5':'TradeValue Growth(%)Pre 5'},inplace=True)
        st.dataframe(df)

        

        if option3== '2019':
            fig=px.treemap(df, path=[px.Constant('PRODUCTS'),'Section', 'HS2'], values='Trade Value', color='Trade Value Growth(%)',color_continuous_scale='RdBu')
            fig.update_layout(margin= dict(t=50, l=25, r=25, b=25), width =1100,  height=650)
            st.plotly_chart(fig)
        
        if option3=='Previous Year':
            fig=px.treemap(df, path=[px.Constant('PRODUCTS'),'Section', 'HS2'], values='Trade Value Previous 1', color='TradeValue Growth(%)Pre 1',color_continuous_scale='RdBu')
            fig.update_layout(margin= dict(t=50, l=25, r=25, b=25), width =1100,  height=650)
            st.plotly_chart(fig)
        
        if option3=='Previous 3 Years':
            fig=px.treemap(df, path=[px.Constant('PRODUCTS'),'Section', 'HS2'], values='Trade Value Previous 3', color='TradeValue Growth(%)Pre 3',color_continuous_scale='RdBu')
            fig.update_layout(margin= dict(t=50, l=25, r=25, b=25), width =1100,  height=650)
            st.plotly_chart(fig)

        if option3=='Previous 5 Years':
            fig=px.treemap(df, path=[px.Constant('PRODUCTS'),'Section', 'HS2'], values='Trade Value Previous 5', color='TradeValue Growth(%)Pre 5',color_continuous_scale='RdBu')
            fig.update_layout(margin= dict(t=50, l=25, r=25, b=25), width =1100,  height=650)
            st.plotly_chart(fig)

        
  #---------------------------------------------------------------------------------------------      
        
        if option4=='Animal Product':
            if option3=='2019':
                st.plotly_chart(px.histogram(df.head(35), x='HS2' ,y='Trade Value',width =1000,  height=900 , template='plotly_dark',title='Animal Products'))
            if option3=='Previous Year':
                st.plotly_chart(px.histogram(df.head(35), x='HS2' ,y='Trade Value Previous 1',width =1000,  height=900 , template='plotly_dark',title='Animal Products'))
            if option3=='Previous 3 Years':
                st.plotly_chart(px.histogram(df.head(35), x='HS2' ,y='Trade Value Previous 3',width =1000,  height=900 , template='plotly_dark',title='Animal Products'))
            if  option3=='Previous 5 Years':
                st.plotly_chart(px.histogram(df.head(35), x='HS2' ,y='Trade Value Previous 5',width =1000,  height=900 , template='plotly_dark',title='Animal Products'))

            dt=pd.read_csv('Animal Morocco.csv')
            dt.drop(columns=['Section ID','HS2 ID','HS4 ID','HS6 ID' ], inplace=True)
            st.markdown('Tariff on Animal Products')
            st.dataframe(dt)
#-----------------------------------------------------------------------------------

        if option4=='Vegetable Product':
            if option3=='2019':
                st.plotly_chart(px.histogram(df.iloc[36:112], x='HS2' ,y='Trade Value',width =1000,  height=900 , template='plotly_dark',title='Vegetable Products'))
            if option3=='Previous Year':
                st.plotly_chart(px.histogram(df.iloc[36:112], x='HS2' ,y='Trade Value Previous 1',width =1000,  height=900 , template='plotly_dark',title='Vegetable Products'))
            if option3=='Previous 3 Years':
                st.plotly_chart(px.histogram(df.iloc[36:112], x='HS2' ,y='Trade Value Previous 3',width =1000,  height=900 , template='plotly_dark',title='Vegetable Products'))
            if  option3=='Previous 5 Years':
                st.plotly_chart(px.histogram(df.iloc[36:112], x='HS2' ,y='Trade Value Previous 5',width =1000,  height=900 , template='plotly_dark',title='Vegetable Products'))

            dv=pd.read_csv('Vegetable Morocco.csv')
            dv.drop(columns=['Section ID','HS2 ID','HS4 ID','HS6 ID' ], inplace=True)
            st.markdown('Tariff on Vegetable Products')
            st.dataframe(dv)
#---------------------------------------------------------------------------------------

        if option4=='Animal and Vegetable Bi Product':
            if option3=='2019':
                st.plotly_chart(px.histogram(df.iloc[112:131], x='HS2' ,y='Trade Value',width =800,  height=600 , template='plotly_dark',title='Animal and Vegetable Bi Product'))
            if option3=='Previous Year':
                st.plotly_chart(px.histogram(df.iloc[112:131], x='HS2' ,y='Trade Value Previous 1',width =800,  height=600 , template='plotly_dark',title='Animal and Vegetable Bi Product'))
            if option3=='Previous 3 Years':
                st.plotly_chart(px.histogram(df.iloc[112:131], x='HS2' ,y='Trade Value Previous 3',width =800,  height=600 , template='plotly_dark',title='Animal and Vegetable Bi Product'))
            if  option3=='Previous 5 Years':
                st.plotly_chart(px.histogram(df.iloc[112:131], x='HS2' ,y='Trade Value Previous 5',width =800,  height=600 , template='plotly_dark',title='Animal and Vegetable Bi Product'))

            dw=pd.read_csv('Biproduct Morocco.csv')
            dw.drop(columns=['Section ID','HS2 ID','HS4 ID','HS6 ID' ], inplace=True)
            st.markdown('Animal and Vegetable Bi Products')
            st.dataframe(dw)

#--------------------------------------------------------------------------------------------------    
        if option4=='Foodstuffs':
            if option3=='2019':
                st.plotly_chart(px.histogram(df.tail(53), x='HS2' ,y='Trade Value',width =1000,  height=900 , template='plotly_dark',title='Foodstuffs'))
            if option3=='Previous Year':
                st.plotly_chart(px.histogram(df.tail(53), x='HS2' ,y='Trade Value Previous 1',width =1000,  height=900 , template='plotly_dark',title='Foodstuffs'))
            if option3=='Previous 3 Years':
                st.plotly_chart(px.histogram(df.tail(53), x='HS2' ,y='Trade Value Previous 3',width =1000,  height=900 , template='plotly_dark',title='Foodstuffs'))
            if  option3=='Previous 5 Years':
                st.plotly_chart(px.histogram(df.tail(53), x='HS2' ,y='Trade Value Previous 5',width =1000,  height=900 , template='plotly_dark',title='Foodstuffs'))

            dx=pd.read_csv('Foodstuff Morocco.csv')
            dx.drop(columns=['Section ID','HS2 ID','HS4 ID','HS6 ID' ], inplace=True)
            st.markdown('Tariff on Foodstuffs Products')
            st.dataframe(dx)
#----------------------------------------------------------------------------------------

    if option1=='Algeria':
        df=pd.read_csv('Algeria Import.csv')
        df.drop(columns=['Section ID','HS2 ID','HS4 ID'], inplace=True)
        df.rename(columns={'Trade Value Growth':'Trade Value Growth(%)','Trade Value Growth 1':'TradeValue Growth(%)Pre 1','Trade Value Growth 3':'TradeValue Growth(%)Pre 3','Trade Value Growth 5':'TradeValue Growth(%)Pre 5'},inplace=True)
        st.dataframe(df)

        

        if option3== '2019':
            fig=px.treemap(df, path=[px.Constant('PRODUCTS'),'Section', 'HS2'], values='Trade Value', color='Trade Value Growth(%)',color_continuous_scale='RdBu')
            fig.update_layout(margin= dict(t=50, l=25, r=25, b=25), width =1100,  height=650)
            st.plotly_chart(fig)
        
        if option3=='Previous Year':
            fig=px.treemap(df, path=[px.Constant('PRODUCTS'),'Section', 'HS2'], values='Trade Value Previous 1', color='TradeValue Growth(%)Pre 1',color_continuous_scale='RdBu')
            fig.update_layout(margin= dict(t=50, l=25, r=25, b=25), width =1100,  height=650)
            st.plotly_chart(fig)
        
        if option3=='Previous 3 Years':
            fig=px.treemap(df, path=[px.Constant('PRODUCTS'),'Section', 'HS2'], values='Trade Value Previous 3', color='TradeValue Growth(%)Pre 3',color_continuous_scale='RdBu')
            fig.update_layout(margin= dict(t=50, l=25, r=25, b=25), width =1100,  height=650)
            st.plotly_chart(fig)

        if option3=='Previous 5 Years':
            fig=px.treemap(df, path=[px.Constant('PRODUCTS'),'Section', 'HS2'], values='Trade Value Previous 5', color='TradeValue Growth(%)Pre 5',color_continuous_scale='RdBu')
            fig.update_layout(margin= dict(t=50, l=25, r=25, b=25), width =1100,  height=650)
            st.plotly_chart(fig)

        
  #---------------------------------------------------------------------------------------------      
        
        if option4=='Animal Product':
            if option3=='2019':
                st.plotly_chart(px.histogram(df.head(30), x='HS2' ,y='Trade Value',width =1000,  height=900 , template='plotly_dark',title='Animal Products'))
            if option3=='Previous Year':
                st.plotly_chart(px.histogram(df.head(30), x='HS2' ,y='Trade Value Previous 1',width =1000,  height=900 , template='plotly_dark',title='Animal Products'))
            if option3=='Previous 3 Years':
                st.plotly_chart(px.histogram(df.head(30), x='HS2' ,y='Trade Value Previous 3',width =1000,  height=900 , template='plotly_dark',title='Animal Products'))
            if  option3=='Previous 5 Years':
                st.plotly_chart(px.histogram(df.head(30), x='HS2' ,y='Trade Value Previous 5',width =1000,  height=900 , template='plotly_dark',title='Animal Products'))

            dt=pd.read_csv('Animal Algeria.csv')
            dt.drop(columns=['Section ID','HS2 ID','HS4 ID','HS6 ID' ], inplace=True)
            st.markdown('Tariff on Animal Products')
            st.dataframe(dt)
#-----------------------------------------------------------------------------------

        if option4=='Vegetable Product':
            if option3=='2019':
                st.plotly_chart(px.histogram(df.iloc[31:102], x='HS2' ,y='Trade Value',width =1000,  height=900 , template='plotly_dark',title='Vegetable Products'))
            if option3=='Previous Year':
                st.plotly_chart(px.histogram(df.iloc[31:102], x='HS2' ,y='Trade Value Previous 1',width =1000,  height=900 , template='plotly_dark',title='Vegetable Products'))
            if option3=='Previous 3 Years':
                st.plotly_chart(px.histogram(df.iloc[31:102], x='HS2' ,y='Trade Value Previous 3',width =1000,  height=900 , template='plotly_dark',title='Vegetable Products'))
            if  option3=='Previous 5 Years':
                st.plotly_chart(px.histogram(df.iloc[31:102], x='HS2' ,y='Trade Value Previous 5',width =1000,  height=900 , template='plotly_dark',title='Vegetable Products'))

            dv=pd.read_csv('Vegetable Algeria.csv')
            dv.drop(columns=['Section ID','HS2 ID','HS4 ID','HS6 ID' ], inplace=True)
            st.markdown('Tariff on Vegetable Products')
            st.dataframe(dv)
#---------------------------------------------------------------------------------------

        if option4=='Animal and Vegetable Bi Product':
            if option3=='2019':
                st.plotly_chart(px.histogram(df.iloc[102:118], x='HS2' ,y='Trade Value',width =800,  height=600 , template='plotly_dark',title='Animal and Vegetable Bi Product'))
            if option3=='Previous Year':
                st.plotly_chart(px.histogram(df.iloc[102:118], x='HS2' ,y='Trade Value Previous 1',width =800,  height=600 , template='plotly_dark',title='Animal and Vegetable Bi Product'))
            if option3=='Previous 3 Years':
                st.plotly_chart(px.histogram(df.iloc[102:118], x='HS2' ,y='Trade Value Previous 3',width =800,  height=600 , template='plotly_dark',title='Animal and Vegetable Bi Product'))
            if  option3=='Previous 5 Years':
                st.plotly_chart(px.histogram(df.iloc[102:118], x='HS2' ,y='Trade Value Previous 5',width =800,  height=600 , template='plotly_dark',title='Animal and Vegetable Bi Product'))

            dw=pd.read_csv('Biproduct Algeria.csv')
            dw.drop(columns=['Section ID','HS2 ID','HS4 ID','HS6 ID' ], inplace=True)
            st.markdown('Animal and Vegetable Bi Products')
            st.dataframe(dw)

#--------------------------------------------------------------------------------------------------    
        if option4=='Foodstuffs':
            if option3=='2019':
                st.plotly_chart(px.histogram(df.tail(47), x='HS2' ,y='Trade Value',width =1000,  height=900 , template='plotly_dark',title='Foodstuffs'))
            if option3=='Previous Year':
                st.plotly_chart(px.histogram(df.tail(47), x='HS2' ,y='Trade Value Previous 1',width =1000,  height=900 , template='plotly_dark',title='Foodstuffs'))
            if option3=='Previous 3 Years':
                st.plotly_chart(px.histogram(df.tail(47), x='HS2' ,y='Trade Value Previous 3',width =1000,  height=900 , template='plotly_dark',title='Foodstuffs'))
            if  option3=='Previous 5 Years':
                st.plotly_chart(px.histogram(df.tail(47), x='HS2' ,y='Trade Value Previous 5',width =1000,  height=900 , template='plotly_dark',title='Foodstuffs'))

            dx=pd.read_csv('Foodstuff Algeria.csv')
            dx.drop(columns=['Section ID','HS2 ID','HS4 ID','HS6 ID' ], inplace=True)
            st.markdown('Tariff on Foodstuffs Products')
            st.dataframe(dx)
#------------------------------------------------------------------------------------------

    if option1=='Egypt':
        df=pd.read_csv('Egypt Import.csv')
        df.drop(columns=['Section ID','HS2 ID','HS4 ID'], inplace=True)
        df.rename(columns={'Trade Value Growth':'Trade Value Growth(%)','Trade Value Growth 1':'TradeValue Growth(%)Pre 1','Trade Value Growth 3':'TradeValue Growth(%)Pre 3','Trade Value Growth 5':'TradeValue Growth(%)Pre 5'},inplace=True)
        st.dataframe(df)

        

        if option3== '2019':
            fig=px.treemap(df, path=[px.Constant('PRODUCTS'),'Section', 'HS2'], values='Trade Value', color='Trade Value Growth(%)',color_continuous_scale='RdBu')
            fig.update_layout(margin= dict(t=50, l=25, r=25, b=25), width =1100,  height=650)
            st.plotly_chart(fig)
        
        if option3=='Previous Year':
            fig=px.treemap(df, path=[px.Constant('PRODUCTS'),'Section', 'HS2'], values='Trade Value Previous 1', color='TradeValue Growth(%)Pre 1',color_continuous_scale='RdBu')
            fig.update_layout(margin= dict(t=50, l=25, r=25, b=25), width =1100,  height=650)
            st.plotly_chart(fig)
        
        if option3=='Previous 3 Years':
            fig=px.treemap(df, path=[px.Constant('PRODUCTS'),'Section', 'HS2'], values='Trade Value Previous 3', color='TradeValue Growth(%)Pre 3',color_continuous_scale='RdBu')
            fig.update_layout(margin= dict(t=50, l=25, r=25, b=25), width =1100,  height=650)
            st.plotly_chart(fig)

        if option3=='Previous 5 Years':
            fig=px.treemap(df, path=[px.Constant('PRODUCTS'),'Section', 'HS2'], values='Trade Value Previous 5', color='TradeValue Growth(%)Pre 5',color_continuous_scale='RdBu')
            fig.update_layout(margin= dict(t=50, l=25, r=25, b=25), width =1100,  height=650)
            st.plotly_chart(fig)

        
  #---------------------------------------------------------------------------------------------      
        
        if option4=='Animal Product':
            if option3=='2019':
                st.plotly_chart(px.histogram(df.head(36), x='HS2' ,y='Trade Value',width =1000,  height=900 , template='plotly_dark',title='Animal Products'))
            if option3=='Previous Year':
                st.plotly_chart(px.histogram(df.head(36), x='HS2' ,y='Trade Value Previous 1',width =1000,  height=900 , template='plotly_dark',title='Animal Products'))
            if option3=='Previous 3 Years':
                st.plotly_chart(px.histogram(df.head(36), x='HS2' ,y='Trade Value Previous 3',width =1000,  height=900 , template='plotly_dark',title='Animal Products'))
            if  option3=='Previous 5 Years':
                st.plotly_chart(px.histogram(df.head(36), x='HS2' ,y='Trade Value Previous 5',width =1000,  height=900 , template='plotly_dark',title='Animal Products'))

            dt=pd.read_csv('Animal Egypt.csv')
            dt.drop(columns=['Section ID','HS2 ID','HS4 ID','HS6 ID' ], inplace=True)
            st.markdown('Tariff on Animal Products')
            st.dataframe(dt)
#-----------------------------------------------------------------------------------

        if option4=='Vegetable Product':
            if option3=='2019':
                st.plotly_chart(px.histogram(df.iloc[37:114], x='HS2' ,y='Trade Value',width =1000,  height=900 , template='plotly_dark',title='Vegetable Products'))
            if option3=='Previous Year':
                st.plotly_chart(px.histogram(df.iloc[37:114], x='HS2' ,y='Trade Value Previous 1',width =1000,  height=900 , template='plotly_dark',title='Vegetable Products'))
            if option3=='Previous 3 Years':
                st.plotly_chart(px.histogram(df.iloc[37:114], x='HS2' ,y='Trade Value Previous 3',width =1000,  height=900 , template='plotly_dark',title='Vegetable Products'))
            if  option3=='Previous 5 Years':
                st.plotly_chart(px.histogram(df.iloc[37:114], x='HS2' ,y='Trade Value Previous 5',width =1000,  height=900 , template='plotly_dark',title='Vegetable Products'))

            dv=pd.read_csv('Vegetable Egypt.csv')
            dv.drop(columns=['Section ID','HS2 ID','HS4 ID','HS6 ID' ], inplace=True)
            st.markdown('Tariff on Vegetable Products')
            st.dataframe(dv)
#---------------------------------------------------------------------------------------

        if option4=='Animal and Vegetable Bi Product':
            if option3=='2019':
                st.plotly_chart(px.histogram(df.iloc[114:134], x='HS2' ,y='Trade Value',width =800,  height=600 , template='plotly_dark',title='Animal and Vegetable Bi Product'))
            if option3=='Previous Year':
                st.plotly_chart(px.histogram(df.iloc[114:134], x='HS2' ,y='Trade Value Previous 1',width =800,  height=600 , template='plotly_dark',title='Animal and Vegetable Bi Product'))
            if option3=='Previous 3 Years':
                st.plotly_chart(px.histogram(df.iloc[114:134], x='HS2' ,y='Trade Value Previous 3',width =800,  height=600 , template='plotly_dark',title='Animal and Vegetable Bi Product'))
            if  option3=='Previous 5 Years':
                st.plotly_chart(px.histogram(df.iloc[114:134], x='HS2' ,y='Trade Value Previous 5',width =800,  height=600 , template='plotly_dark',title='Animal and Vegetable Bi Product'))

            dw=pd.read_csv('Biproduct Egypt.csv')
            dw.drop(columns=['Section ID','HS2 ID','HS4 ID','HS6 ID' ], inplace=True)
            st.markdown('Animal and Vegetable Bi Products')
            st.dataframe(dw)

#--------------------------------------------------------------------------------------------------    
        if option4=='Foodstuffs':
            if option3=='2019':
                st.plotly_chart(px.histogram(df.tail(53), x='HS2' ,y='Trade Value',width =1000,  height=900 , template='plotly_dark',title='Foodstuffs'))
            if option3=='Previous Year':
                st.plotly_chart(px.histogram(df.tail(53), x='HS2' ,y='Trade Value Previous 1',width =1000,  height=900 , template='plotly_dark',title='Foodstuffs'))
            if option3=='Previous 3 Years':
                st.plotly_chart(px.histogram(df.tail(53), x='HS2' ,y='Trade Value Previous 3',width =1000,  height=900 , template='plotly_dark',title='Foodstuffs'))
            if  option3=='Previous 5 Years':
                st.plotly_chart(px.histogram(df.tail(53), x='HS2' ,y='Trade Value Previous 5',width =1000,  height=900 , template='plotly_dark',title='Foodstuffs'))

            dx=pd.read_csv('Foodstuf Egypt.csv')
            dx.drop(columns=['Section ID','HS2 ID','HS4 ID','HS6 ID' ], inplace=True)
            st.markdown('Tariff on Foodstuffs Products')
            st.dataframe(dx)
#-------------------------------------------------------------------------------------------------
    if option1=='Sudan':
        df=pd.read_csv('Sudan Import.csv')
        df.drop(columns=['Section ID','HS2 ID','HS4 ID'], inplace=True)
        df.rename(columns={'Trade Value Growth':'Trade Value Growth(%)','Trade Value Growth 1':'TradeValue Growth(%)Pre 1','Trade Value Growth 3':'TradeValue Growth(%)Pre 3','Trade Value Growth 5':'TradeValue Growth(%)Pre 5'},inplace=True)
        st.dataframe(df)

        

        if option3== '2019':
            fig=px.treemap(df, path=[px.Constant('PRODUCTS'),'Section', 'HS2'], values='Trade Value', color='Trade Value Growth(%)',color_continuous_scale='RdBu')
            fig.update_layout(margin= dict(t=50, l=25, r=25, b=25), width =1100,  height=650)
            st.plotly_chart(fig)
        
        if option3=='Previous Year':
            fig=px.treemap(df, path=[px.Constant('PRODUCTS'),'Section', 'HS2'], values='Trade Value Previous 1', color='TradeValue Growth(%)Pre 1',color_continuous_scale='RdBu')
            fig.update_layout(margin= dict(t=50, l=25, r=25, b=25), width =1100,  height=650)
            st.plotly_chart(fig)
        
        if option3=='Previous 3 Years':
            fig=px.treemap(df, path=[px.Constant('PRODUCTS'),'Section', 'HS2'], values='Trade Value Previous 3', color='TradeValue Growth(%)Pre 3',color_continuous_scale='RdBu')
            fig.update_layout(margin= dict(t=50, l=25, r=25, b=25), width =1100,  height=650)
            st.plotly_chart(fig)

        if option3=='Previous 5 Years':
            fig=px.treemap(df, path=[px.Constant('PRODUCTS'),'Section', 'HS2'], values='Trade Value Previous 5', color='TradeValue Growth(%)Pre 5',color_continuous_scale='RdBu')
            fig.update_layout(margin= dict(t=50, l=25, r=25, b=25), width =1100,  height=650)
            st.plotly_chart(fig)

        
  #---------------------------------------------------------------------------------------------      
        
        if option4=='Animal Product':
            if option3=='2019':
                st.plotly_chart(px.histogram(df.head(26), x='HS2' ,y='Trade Value',width =1000,  height=900 , template='plotly_dark',title='Animal Products'))
            if option3=='Previous Year':
                st.plotly_chart(px.histogram(df.head(26), x='HS2' ,y='Trade Value Previous 1',width =1000,  height=900 , template='plotly_dark',title='Animal Products'))
            if option3=='Previous 3 Years':
                st.plotly_chart(px.histogram(df.head(26), x='HS2' ,y='Trade Value Previous 3',width =1000,  height=900 , template='plotly_dark',title='Animal Products'))
            if  option3=='Previous 5 Years':
                st.plotly_chart(px.histogram(df.head(26), x='HS2' ,y='Trade Value Previous 5',width =1000,  height=900 , template='plotly_dark',title='Animal Products'))

            dt=pd.read_csv('Animal Sudan.csv')
            dt.drop(columns=['Section ID','HS2 ID','HS4 ID','HS6 ID' ], inplace=True)
            st.markdown('Tariff on Animal Products')
            st.dataframe(dt)
#-----------------------------------------------------------------------------------

        if option4=='Vegetable Product':
            if option3=='2019':
                st.plotly_chart(px.histogram(df.iloc[27:91], x='HS2' ,y='Trade Value',width =1000,  height=900 , template='plotly_dark',title='Vegetable Products'))
            if option3=='Previous Year':
                st.plotly_chart(px.histogram(df.iloc[27:91], x='HS2' ,y='Trade Value Previous 1',width =1000,  height=900 , template='plotly_dark',title='Vegetable Products'))
            if option3=='Previous 3 Years':
                st.plotly_chart(px.histogram(df.iloc[27:91], x='HS2' ,y='Trade Value Previous 3',width =1000,  height=900 , template='plotly_dark',title='Vegetable Products'))
            if  option3=='Previous 5 Years':
                st.plotly_chart(px.histogram(df.iloc[27:91], x='HS2' ,y='Trade Value Previous 5',width =1000,  height=900 , template='plotly_dark',title='Vegetable Products'))

            dv=pd.read_csv('Vegetable Sudan.csv')
            dv.drop(columns=['Section ID','HS2 ID','HS4 ID','HS6 ID' ], inplace=True)
            st.markdown('Tariff on Vegetable Products')
            st.dataframe(dv)
#---------------------------------------------------------------------------------------

        if option4=='Animal and Vegetable Bi Product':
            if option3=='2019':
                st.plotly_chart(px.histogram(df.iloc[91:108], x='HS2' ,y='Trade Value',width =800,  height=600 , template='plotly_dark',title='Animal and Vegetable Bi Product'))
            if option3=='Previous Year':
                st.plotly_chart(px.histogram(df.iloc[91:108], x='HS2' ,y='Trade Value Previous 1',width =800,  height=600 , template='plotly_dark',title='Animal and Vegetable Bi Product'))
            if option3=='Previous 3 Years':
                st.plotly_chart(px.histogram(df.iloc[91:108], x='HS2' ,y='Trade Value Previous 3',width =800,  height=600 , template='plotly_dark',title='Animal and Vegetable Bi Product'))
            if  option3=='Previous 5 Years':
                st.plotly_chart(px.histogram(df.iloc[91:108], x='HS2' ,y='Trade Value Previous 5',width =800,  height=600 , template='plotly_dark',title='Animal and Vegetable Bi Product'))

            dw=pd.read_csv('Biproduct Sudan.csv')
            dw.drop(columns=['Section ID','HS2 ID','HS4 ID','HS6 ID' ], inplace=True)
            st.markdown('Animal and Vegetable Bi Products')
            st.dataframe(dw)

#--------------------------------------------------------------------------------------------------    
        if option4=='Foodstuffs':
            if option3=='2019':
                st.plotly_chart(px.histogram(df.tail(46), x='HS2' ,y='Trade Value',width =1000,  height=900 , template='plotly_dark',title='Foodstuffs'))
            if option3=='Previous Year':
                st.plotly_chart(px.histogram(df.tail(46), x='HS2' ,y='Trade Value Previous 1',width =1000,  height=900 , template='plotly_dark',title='Foodstuffs'))
            if option3=='Previous 3 Years':
                st.plotly_chart(px.histogram(df.tail(46), x='HS2' ,y='Trade Value Previous 3',width =1000,  height=900 , template='plotly_dark',title='Foodstuffs'))
            if  option3=='Previous 5 Years':
                st.plotly_chart(px.histogram(df.tail(46), x='HS2' ,y='Trade Value Previous 5',width =1000,  height=900 , template='plotly_dark',title='Foodstuffs'))

            dx=pd.read_csv('Foodstuf Sudan.csv')
            dx.drop(columns=['Section ID','HS2 ID','HS4 ID','HS6 ID' ], inplace=True)
            st.markdown('Tariff on Foodstuffs Products')
            st.dataframe(dx)

