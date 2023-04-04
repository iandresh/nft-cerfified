import streamlit as st

def main():
    st.title("Bootcamp Certificate Minter")
st.write("Choose an account to get started")
accounts = 0xfFa2994F451c0342aF46e055DAC924b8fe302285
address = st.selectbox("Select Account", options=accounts)
st.markdown("---")

# ADD CERTIFICATE
st.markdown("## Mint Bootcamp Certificate")

tab1 = st.tabs(["Individual"])

# INDIVIDUAL
with tab1:
    name = st.text_input("Full Name")
    completion_date = st.text_input("Completion Date")
    certificate_template = st.file_uploader("Upload Certificate Template")
    if certificate_template is not None:
        st.write("Template Uploaded!")
    if st.button("Register Certificate"):
        # Here you can add code to process the user input and generate the certificate
        st.write("Certificate Registered!")
        
if __name__ == '__main__':
    main()
