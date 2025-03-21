import streamlit as st
import matplotlib.pyplot as plt

def plot_graph(subjects, marks):
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(subjects, marks, color=['blue', 'green', 'red', 'purple', 'orange'])
    ax.set_xlabel("Subjects")
    ax.set_ylabel("Marks")
    ax.set_title("📊 Student Marks Visualization")
    ax.set_ylim(0, 100)
    
    st.pyplot(fig)
