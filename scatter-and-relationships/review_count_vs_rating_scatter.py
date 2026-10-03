import matplotlib.pyplot as plt

review_count = [15, 30, 45, 120, 200, 250, 310, 400, 450, 500]
rating_score = [2.1, 2.8, 3.2, 3.5, 3.9, 4.1, 4.0, 4.6, 4.8, 4.9]

plt.scatter(review_count, rating_score, color='green', marker='o')

plt.title('Rating and Total number of Reviews')
plt.ylabel('Rating (1-5 stars)')
plt.xlabel('Total number of reviews')

plt.show()