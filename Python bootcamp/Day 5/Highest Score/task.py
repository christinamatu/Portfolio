
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score

print(max_score)
# Is 150 greater than zero? Yes, so 150 becomes the new score.
# Is 142 greater than 150? No, so the loop will go to the next number which is 185.