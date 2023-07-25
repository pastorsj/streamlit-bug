import streamlit as st
import time
import pandas as pd


def main():
    if st.button(
        "Run",
        type="primary",
    ):
        start_time = time.time()
        st.progress(0, "Testing...")
        idx = 0
        while idx < 100:
            time.sleep(15)
            end_time = time.time()
            st.progress(
                (idx + 1) / 100,
                f"Total Time: {round(end_time - start_time)} seconds...",
            )
            idx += 1


if __name__ == "__main__":
    main()
