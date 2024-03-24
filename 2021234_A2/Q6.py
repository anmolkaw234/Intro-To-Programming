def compute_grades(marks_file, weights):
  
  with open('IPgrades.txt', 'w') as out_file:
    
    with open(marks_file, 'r') as in_file:
      
      for line in in_file:
        
        items = line.split(',')
        
        roll_no = items[0]
        
        total_marks = 0
        weight_sum = 0
        
        for i, (max_marks, weight) in enumerate(weights):
          
          mark = int(items[i + 1])
          
          normalized_mark = (mark / max_marks) * weight
          
          total_marks += normalized_mark
          
          weight_sum += weight
        
        weighted_sum = total_marks / weight_sum
        
        normalized_weighted_sum = weighted_sum * 100
        
        if normalized_weighted_sum >= 80:
          grade = 'A'
        elif normalized_weighted_sum >= 70:
          grade = 'A-'
        elif normalized_weighted_sum >= 60:
          grade = 'B'
        elif normalized_weighted_sum >= 50:
          grade = 'B-'
        elif normalized_weighted_sum >= 40:
          grade = 'C'
        elif normalized_weighted_sum >= 35:
          grade = 'C-'
        elif normalized_weighted_sum >= 30:
          grade = 'D'
        else:
          grade = 'F'
        
        out_file.write(f"{roll_no},{normalized_weighted_sum:.2f},{grade}\n")


compute_grades('IPmarks.txt', [(10, 5), (20, 5), (100, 15), (40, 10)])

