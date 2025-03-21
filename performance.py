def performance_feedback(percentage):
    if percentage >= 90:
        return "🌟 Outstanding! Keep it up! 🎉"
    elif percentage >= 80:
        return "🔥 Excellent! You're doing great! 💪"
    elif percentage >= 70:
        return "📚 Good! But you can improve!"
    elif percentage >= 60:
        return "🚀 Needs improvement! Work harder!"
    else:
        return "❌ You failed! Better luck next time! 😢"
