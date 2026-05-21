import streamlit as st

def setosa():
    with st.expander("Iris Setosa"):
        #setosa
        st.image(r'https://upload.wikimedia.org/wikipedia/commons/a/a7/Irissetosa1.jpg?utm_source=en.wikipedia.org&utm_campaign=index&utm_content=original',caption="Iris Setosa")
        st.write("Iris setosa, known as the beachhead iris, bristle-pointed iris, or a number of other common names, is a species of flowering plant in the genus Iris of the family Iridaceae. It belongs to the subgenus Limniris and the series Tripetalae.")
        st.image(r'https://i.etsystatic.com/20845839/r/il/86ac74/3108398608/il_1080xN.3108398608_6l57.jpg',width="content")

        with st.expander("Physical Features"):
            st.write("Iris setosa is similar in form to a miniature Japanese iris")
            st.image(r'https://www.thespruce.com/thmb/6UCHyHo17OQuMMBEvNGNChiETs0=/4200x0/filters:no_upscale():max_bytes(150000):strip_icc()/how-to-grow-and-care-for-japanese-iris-5077439-hero-bbbd19a517fa4c01a6ec5d7b70e67969.JPG',caption="JAPANESE IRIS")
            
            st.write("I. setosa has branched stems that are very variable in height,ranging from 10 cm (5 inches) to 1 m (3 ft) tall.The larger plants can grow beyond the height of the leaves.The roundish stems are 1.5-9 cm (0.6-4 in) in diameter with 1 to 3 branches.")

            st.write("Iris setosa has grass-like, lanceolate (sword-shaped),[ medium-green leaves with a purple-tinged base.Its leaves can measure 30–60 cm (12–24 in) long by 0.8–2.5 cm (0.3–1 in) wide.The plant bears 3–4 flowers per stem (for a total of 6 and 13 on the whole plant) in groups of 3.")
        with st.expander("Gallery"):
            st.image(r'https://images.squarespace-cdn.com/content/v1/61eeea89d60f57793d9e114b/1706854177704-ZMBZEYAY1ALA6KZRQ6KH/iris%2Bsetosa%2Bmany%2Bedited.jpg?format=1000w')
            st.image(r"https://davisla3.files.wordpress.com/2013/07/iris-setosa.jpg")


def versicolor():
      with st.expander("Iris Versicolor"):
            st.image(r"https://upload.wikimedia.org/wikipedia/commons/2/27/Blue_Flag%2C_Ottawa.jpg",caption="Iris Versicolor")
            st.write("Iris versicolor or Iris versicolour is also commonly known as the blue flag, harlequin blueflag, larger blue flag, northern blue flag, and poison flag, plus other variations of these names.")
            st.write("It is a species of Iris native to North America, in Eastern Canada and the Eastern United States. It is common in sedge meadows, marshes, and along streambanks and shores. The specific epithet versicolor means variously coloured.")
            st.image(r"https://nurserylive.com/cdn/shop/products/nurserylive-plants-iris-versicolor-plant-16968957296780.jpg?v=1634222287")
            with st.expander("Physical Features"):
                st.write("* Iris versicolor is a flowering herbaceous perennial plant, growing 10–80 cm (4–31 in) high. ([1]) It tends to form large clumps from thick, creeping rhizomes.")
                st.write("* The unwinged, erect stems generally have basal leaves that are more than 1 cm (1⁄2 in) wide. Leaves are folded on the midribs so that they form an overlapping flat fan")
                st.write("* The well developed blue flower has six petals and sepals spread out nearly flat and have two forms. The longer sepals are hairless and have a greenish-yellow blotch at their base. The inferior ovary is bluntly angled")
                st.write("* Flowers are usually light to deep blue (purple and violet are not uncommon) and bloom during May to July. Fruit is a three-celled, bluntly angled capsule. The large seeds can be observed floating in fall.")

                st.image(r"https://ask-ayurveda.com/media/uploads/wiki/Iris_versicolour.png")
            
            with st.expander("Gallery"):
                 st.image(r"https://wiki.irises.org/pub/Spec/SpecVersicolor/iversicolor07.jpg")
                 st.image(r"https://thumbs.dreamstime.com/b/iris-versicolor-single-blue-flag-black-background-31834833.jpg")
def virginica():
     with st.expander("Iris Virginica"):
        st.image(r"https://upload.wikimedia.org/wikipedia/commons/9/9f/Iris_virginica.jpg?utm_source=commons.wikimedia.org&utm_campaign=index&utm_content=original",caption="Iris Virginica")
        st.write("")
#setosa()
