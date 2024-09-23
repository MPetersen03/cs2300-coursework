#mpetersen_p1.py

#creates first matrix
def create_mat1():
    rows = 8 # Petersen
    columns = 5 # Mason

    mat1 = [[0] * columns for _ in range(rows)]

    value = 1

    for column in range(columns):
        for row in range(rows):
            mat1[row][column] = value
            value += 1

    return mat1

# creates second matrix
def create_mat2():
    rows = 8 # Petersen
    columns = 5 # Mason

    mat2 = [[0] * columns for _ in range(rows)]

    value = 2

    for row in range(rows):
        for column in range(columns):
            mat2[row][column] = value
            value += 3

    return mat2

# creates third matrix
def create_mat3():
    rows = 2
    columns = 4

    mat3 = [[0] * columns for _ in range(rows)]

    value = 10

    for column in range(columns):
        for row in range(rows):
            mat3[row][column] = value
            value -= 2

    return mat3

# creates fourth matrix
def create_mat4():
    rows = 4
    columns = 2

    mat4 = [[0] * columns for _ in range(rows)]

    value = -6
    
    for row in range(rows):
        for column in range(columns):
            mat4[row][column] = value
            value += 1.5

    return mat4

# write a matrix to txt file
def write_matrix_to_file(matrix, filename):
  
    with open(filename, 'w') as f:
        for row in matrix:
            f.write(' '.join(map(str, row)) + '\n')



def main():
    first_name = "Mason"
    last_name = "Petersen"

    first_name_length = len(first_name) # 5
    last_name_length = len(last_name) # 8



    mat1 = create_mat1()
    mat2 = create_mat2()
    mat3 = create_mat3()
    mat4 = create_mat4()

    write_matrix_to_file(mat1, "mpetersen_mat1.txt")
    write_matrix_to_file(mat2, "mpetersen_mat2.txt")
    write_matrix_to_file(mat3, "mpetersen_mat3.txt")
    write_matrix_to_file(mat4, "mpetersen_mat4.txt")

    print(f"{first_name} = {first_name_length}")
    print(f"{last_name} = {last_name_length}")

if __name__ == "__main__":
    main()