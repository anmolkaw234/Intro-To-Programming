def read_file(file_name):
    yearbook = {}
    with open(file_name, 'r') as f:
        current_student = None
        for line in f:
            line = line.strip()
            if line == '':
                continue
            if ':' in line:
                current_student = line[:-1]
                yearbook[current_student] = {}
            else:
                name, signature = line.split(',')
                yearbook[current_student][name.strip()] = int(signature.strip())
    return yearbook

def find_max_min(yearbook):
    max_signatures = []
    min_signatures = []
    max_count = 0
    min_count = float('inf')
    for student, signatures in yearbook.items():
        count = sum(signatures.values())
        if count > max_count:
            max_signatures = [student]
            max_count = count
        elif count == max_count:
            max_signatures.append(student)
        if count < min_count:
            min_signatures = [student]
            min_count = count
        elif count == min_count:
            min_signatures.append(student)
    print("Students with most signatures:", max_signatures)
    print("Students with least signatures:", min_signatures)

yearbook = read_file("input.txt")
find_max_min(yearbook)















