import streamlit as st
import time
import pandas as pd


def main():
    st.file_uploader(
        "Upload a file",
        type=["xlsx", "xls"],
        key="file",
    )

    if st.session_state.file is not None:
        if st.button(
            "Run",
            type="primary",
        ):
            start_time = time.time()
            st.progress(0, "Testing...")
            file_df = pd.read_excel(st.session_state.file)
            for idx, row in file_df.iterrows():
                time.sleep(15)
                end_time = time.time()
                st.write(row)
                st.progress(
                    idx / len(file_df), f"Total Time: {round(end_time - start_time)} seconds..."
                )


if __name__ == "__main__":
    main()
