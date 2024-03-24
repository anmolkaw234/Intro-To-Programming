
GRADES = {"A+": 10, "A": 10, "A-": 9, "B": 8, "B-": 7, "C": 6, "C-": 5, "D": 4, "F": 2}

def process_input(input_str):
  
  course_info = input_str.split()
  
  
  if len(course_info) != 3:
    print("Error: Incorrect number of inputs")
    return None
  if not course_info[0].isalnum():
    print("Error: Improper course number")
    return None
  if not course_info[1].isdigit() or int(course_info[1]) not in [0, 1, 2, 4]:
    print("Error: Incorrect number of credits")
    return None
  if course_info[2] not in GRADES:
    print("Error: Incorrect grade")
    return None
  
  
  return (course_info[0], int(course_info[1]), GRADES[course_info[2]])

def compute_sgpa(courses):
  
  total_credits = 0
  total_grade_points = 0
  
  
  for course in courses:
    course_no, credits, grade = course
    total_credits += credits
    total_grade_points += credits * grade
  
  
  return total_grade_points / total_credits

def main():
  
  courses = []

  
  while True:
    
    input_str = input()

    
    if input_str == "":
      break

    
    processed_input = process_input(input_str)
    if processed_input is not None:
      courses.append(processed_input)

  
  courses.sort()
  
  
  for course in courses:
    course_no, credits, grade = course
    print("{}: {}".format(course_no, grade))
  print("SGPA: {:.2f}".format(compute_sgpa(courses)))


main()
