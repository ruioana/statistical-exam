grades = [100, 98, 90, 40, 85, 100, 75, 70, 90, 65, 90, 75, 55.5]

#print all grades 

def print_grades(grades_input):
  for grade in grades_input:
    print (grade)

# sum grades

def grades_sum(scores):
  total = 0
  for score in scores: 
    total += score
  return total
    
#get the average of grades

def grades_average(grades_input):
  sum_of_grades = grades_sum(grades_input)
  average = sum_of_grades / float(len(grades_input))
  return average

#get the variance of grades

def grades_variance(grades):
    variance = 0
    for number in grades:
        variance += (grades_average(grades) - number) ** 2
    return variance / len(grades)

#get the standard deviation of grades

def grades_std_deviation(variance):
  return variance ** 0.5

variance = grades_variance(grades)

#print all the work :) 

for grade in grades:
  print (grade)
print (grades_sum(grades))
print (grades_average(grades))
print (grades_variance(grades))
print (grades_std_deviation(variance))