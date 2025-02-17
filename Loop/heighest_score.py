# import random


student_scores = [150, 200, 300, 400, 500,670, 800, 1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800, 3000, 3200, 3400, 3600, 3800, 4000, 4200, 4400, 4600, 4800, 5000, 5200, 5400, 5600, 5800, 6000, 6200, 6400, 6600, 6800, 7000, 7200, 7400, 7600, 7800, 8000, 8200, 8400, 8600, 8800, 9000, 9200, 9400, 9600, 9800, 10000]
# print(sum(student_scores))
# print(max(student_scores)

total_sum = 0
# for score in student_scores:
#     total_sum += score
# print(total_sum)
max_score = student_scores[0]
min_score = student_scores[0]
for score in student_scores:
    if score > max_score:
        max_score = score
    elif score < min_score:
        min_score = score
print(f"The highest score in the class is: {max_score}")
print(f"The lowest score in the class is: {min_score}")
average_score = total_sum / len(student_scores)
print(f"The average score in the class is: {average_score:.2f}")
total =0
for number in range(1,101):
    
    total += number
print(total)

#  genarate password
