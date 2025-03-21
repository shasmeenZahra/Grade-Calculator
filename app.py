import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from calculations import calculate_percentage, assign_grade
from performance import performance_feedback
from visualization import plot_graph

# 🎨 Page Title
st.title("📊 Student Grade Calculator")

# 📚 Subjects
subjects = ["Math", "Science", "English", "Computer", "History"]
marks = []

# 📥 Input Section
st.header("Enter Your Marks:")
for subject in subjects:
    marks.append(st.number_input(f"Marks in {subject} (out of 100)", min_value=0, max_value=100, step=1))

# 📌 Calculate Button
if st.button("Calculate Result"):
    percentage = calculate_percentage(marks)
    grade = assign_grade(percentage)
    feedback = performance_feedback(percentage)

    # 📝 Display Results
    st.subheader("📄 Result Summary")
    st.write(f"**Total Marks:** {sum(marks)} / 500")
    st.write(f"**Percentage:** {percentage:.2f}%")
    st.write(f"**Grade:** {grade}")
    st.success(feedback)

    # 📈 Graph
    plot_graph(subjects, marks)
