import matplotlib.pyplot as plt

study_hours = [1, 2, 2.5, 3, 4, 4.5, 5, 6, 7, 8]
exam_score = [50, 55, 60, 62, 70, 72, 78, 85, 88, 95]

plt.scatter(study_hours, exam_score, color='green', marker='o')

plt.title('Study Hours vs Exam Score')
plt.xlabel('Hours Studied')
plt.ylabel('Exam Score (%)')

plt.grid(True)

plt.show()