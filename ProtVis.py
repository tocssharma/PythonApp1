import streamlit as st
import streamlit.components.v1 as components
id=st.text_input("Enter the PDB Id:")
if id:
  components.html(
    """ <script src="https://3Dmol.org/build/3Dmol.js" async></script>
        <div style="height: 400px; width: 400px; position: relative;"
        class='viewer_3Dmol.js' darta-pdb={}
        data-style1='cartoon:color=spectrum' data-spin='axis:y;speed:3>>/div>
    """.format(id),height=800,
    )
