import streamlit as st
import species
import frontend

def intro():
    st.header("WELCOME TO THE WORLD OF IRIS",text_alignment="center")
    st.image(r'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Iris_sanguinea_cultivar%2C_Wakehurst_Place%2C_UK_-_Diliff.jpg/500px-Iris_sanguinea_cultivar%2C_Wakehurst_Place%2C_UK_-_Diliff.jpg',caption="Iris sibirica")

    st.text("Iris is a flowering plant genus of 310 accepted species with showy flowers. As well as being the scientific name, iris is also widely used as a common name for all Iris species, as well as some  belonging to other closely related genera.")

    st.image(r"https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Parts_of_an_iris_flower.jpg/500px-Parts_of_an_iris_flower.jpg",caption="Illustration of an iris flower with highlighted parts of the flower")

    st.write("Irises are perennial plants, growing from creeping rhizomes (rhizomatous irises) or, in drier climates, from bulbs (bulbous irises). They have long, erect flowering stems which may be simple or branched, solid or hollow, and flattened or have a circular cross-section. The rhizomatous species usually have 3-10 basal sword-shaped leaves growing in dense clumps.The bulbous species also have 2-10 narrow leaves growing from the bulb.")
    t1,t2=st.tabs(["Species","Predict Your  Iris"])
    with t1:
        species.setosa()
        species.versicolor()
        species.virginica()
    with t2:
        frontend.predcition()

intro()