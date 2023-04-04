
import streamlit as st


# cert editing imports
from PIL import Image, ImageDraw, ImageFont

# Streamlit App UI
col1, col2, col3 = st.columns([1, 3, 1])
with col1:
    st.write("")
with col2:
    st.image("images/Logo.png")
with col3:
    st.write("")


st.title("Bootcamp Certificate Minter")
st.write("Choose an account to get started")
accounts = w3.eth.accounts
address = st.selectbox("Select Account", options=accounts)
st.markdown("---")

# ADD CERTIFICATE
st.markdown("## Mint Bootcamp Certificate")

tab1, tab2 = st.tabs(["Individual", "Batch (Teacher Mode)"])

# INDIVIDUAL
with tab1:
    student_name = st.text_input("Enter full name")
    completion_date = st.text_input(
        "Enter the completion date", value="December 2022")

    # Use the Streamlit `file_uploader` function create the list of digital image file types(jpg, jpeg, or png) that will be uploaded to Pinata.
    file = st.file_uploader("Upload Certificate", type=["jpg", "jpeg", "png"])

    name_font = ImageFont.truetype(
        'template_auto_generator/Open_Sans/OpenSans-Italic-VariableFont_wdth,wght.ttf', size=30)

    date_font = ImageFont.truetype(
        'template_auto_generator/Open_Sans/OpenSans-Medium.ttf', size=25)

    if st.button("Register Certificate"):
        certificate_img = generate_individual_certificate_png(
            student_name, completion_date, file)
        # Use the `pin_certificate` helper function to pin the file to IPFS
        certificate_ipfs_hash, token_json = pin_certificate(
            student_name, certificate_img)

        certificate_uri = f"ipfs://{certificate_ipfs_hash}"

        tx_hash = contract.functions.registerCertificate(
            address,
            student_name,
            completion_date,
            certificate_uri,
            token_json['image']
        ).transact({'from': address, 'gas': 1000000})
        receipt = w3.eth.waitForTransactionReceipt(tx_hash)
        st.balloons()
        st.markdown("# CONGRATULATIONS!")
        st.markdown('##### You have successfully registered your certificate!')
        st.image(certificate_img)
        st.write("Transaction receipt mined:")
        st.write(dict(receipt))
        st.write(
            "You can view the pinned metadata file with the following IPFS Gateway Link")
        st.markdown(
            f"[Certificate IPFS Gateway Link](https://ipfs.io/ipfs/{certificate_ipfs_hash})")
        st.markdown(
            f"[Certificate IPFS Image Link](https://ipfs.io/ipfs/{token_json['image']})")