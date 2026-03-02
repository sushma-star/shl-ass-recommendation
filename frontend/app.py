import streamlit as st
import requests

st.title("SHL Recommendation System")

API_URL = "http://127.0.0.1:8000/recommend"  

query = st.text_area("Enter Job Description")

if st.button("Search"):
    if query.strip() == "":
        st.warning("Please enter a job description.")
    else:
        try:
            res = requests.get(
                API_URL,
                params={"q": query}
            )

            if res.status_code == 200:
                 data = res.json()
                 results = data["recommendations"]
                 if len(results) == 0:
                        print("⚠ No recommendations returned")
                        st.warning("No recommendations found.")
                 else:
                      st.success(f"Found {len(results)} recommended assessments")
                      if "recommendations" in data:
                           for r in data["recommendations"]:
                                st.write("######", r["name"])
                                st.write(r["url"])
                        # st.write("---")
                      else:
                        st.error("Invalid response format.")
            else:
                st.error("API Error:", res.status_code)

        except Exception as e:
            st.error(f"Connection failed: {e}")
