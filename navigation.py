import streamlit as st
import base64
# import matplotlib.pyplot as plt 
import pandas as pd
import csv

# ================ Background image ===

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('2.jpg')


def navigation():
    try:
        path = st.experimental_get_query_params()['p'][0]
    except Exception as e:
        st.error('Please use the main app.')
        return None
    return path


if navigation() == "home":
    st.title(" Malware Detection Using Machine Learning")
    st.write("Malware is one of the most frequent cyberattacks, with its prevalence growing daily across the network. Malware traffic is always asymmetrical compared to benign traffic, which is always symmetrical. Fortunately, there are many artificial intelligence techniques that can be used to detect malware and distinguish it from normal activities. However, the problem of dealing with large and high-dimensional data has not been addressed enough. In this paper, a high-performance malware detection system using machine learnings such as NAIVE BAYES and RANDOM FOREST ")

    
elif navigation()=='login':
    st.title("Welcome Login Page !!!")

    
    
    if "visibility" not in st.session_state:
        st.session_state.visibility = "visible"
        st.session_state.disabled = False
    
    col1, col2 = st.columns(2)
    
    
        
    with col1:
    
        UR1 = st.text_input("Login User Name",key="username")
        psslog = st.text_input("Password",key="password",type="password")

        agree = st.checkbox('LOGIN')
        
        if agree:
            try:
                
                df = pd.read_csv(UR1+'.csv')
                U_P1 = df['User'][0]
                U_P2 = df['Password'][0]
                if str(UR1) == str(U_P1) and str(psslog) == str(U_P2):
                    st.success('Successfully Login !!!')    

                    import pandas as pd
                    
                    def hyperlink(url):
                        return f'<a target="_blank" href="{url}">{url}</a>'
                    
                    dff = pd.DataFrame(columns=['page'])
                    dff['page'] = ['Predicting']
                    dff['page'] = dff['page'].apply(hyperlink)
                    dff = dff.to_html(escape=False)
    
                    st.write(dff, unsafe_allow_html=True)        
    
                else:
                    st.write('Login Failed!!!')
            except:
                st.write('Login Failed!!!')                 
    with col2:
        UR = st.text_input("Register User Name",key="username1")
        pss1 = st.text_input("First Password",key="password1",type="password")
        pss2 = st.text_input("Confirm Password",key="password2",type="password")
            
    
        if pss1 == pss2 and len(str(pss1)) > 2:
            import pandas as pd
            
                 
            # field names 
            fields = ['User', 'Password'] 
            
            
            # st.text(temp_user)
            old_row = [[UR,pss1]]
            
            # writing to csv file 
            with open(UR+'.csv', 'w') as csvfile: 
                # creating a csv writer object 
                csvwriter = csv.writer(csvfile) 
                    
                # writing the fields 
                csvwriter.writerow(fields) 
                    
                # writing the data rows 
                csvwriter.writerows(old_row)
            st.success('Successfully Registered !!!')
        else:
            
            st.write('Registeration Failed !!!')     

elif navigation() == "view":
    st.title("View Our Input Data Hete !!!")
    aa=st.button('VIEW DATA')
    if aa:
        import pandas as pd
        df=pd.read_csv("Malware dataset.csv")
        df1=df.head(20)
  
        st.table(df1)
      
 
elif navigation() == "results":
    st.title('Results ')
    st.text("-----------------------")
    st.text("Performance Analysis")
    st.text("-----------------------")
    st.text(" ")
    st.image("graph.png")  

