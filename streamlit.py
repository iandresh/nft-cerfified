import streamlit as st

def main():
    st.title("Boot Camp Certificate Minter")
    st.write("Choose an account to get started")
    contract_address = st.text_input("Type Contract Address")
    st.write('\n') # Adding some spacing between the input boxes
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

