# mpetersen_p2.py


# read in a matrix from a txt file
def read_mat_from_txt(filename):
    with open(filename, 'r') as f:
        return [list(map(int, line.split())) for line in f.readlines()]

# adds to matrixs to each other
def add_mats(mat_a, mat_b):
    
    if len(mat_a) != len(mat_b) or len(mat_a[0]) != len(mat_b[0]):
        raise ValueError("Matrix Dimentions dont match")
    
    added_mat = [[0] * len(mat_a[0]) for _ in range(len(mat_a))]
    for i in range(len(mat_a)):
        for j in range(len(mat_a[0])):
            added_mat[i][j] = mat_a[i][j] + mat_b[i][j]

    return added_mat;

# writes an added matrix to a txt file
def write_mat_to_txt(matrix, filename):
    
    with open(filename, 'w') as f:
        for row in matrix:
            f.write(' '.join(map(str, row)) + '\n')

def main():

    mat_a_name = input("Enter the first matrix name (Mat1, Mat2, Mat3, Mat4): ")
    mat_b_name = input("Enter the second matrix name (Mat1, Mat2, Mat3, Mat4): ")

    filename_a = f"mpetersen_{mat_a_name.lower()}.txt"
    filename_b = f"mpetersen_{mat_b_name.lower()}.txt"
    output_filename = f"mpetersen_p2_out{mat_a_name[-1]}{mat_b_name[-1]}.txt"

    mat_a = read_mat_from_txt(filename_a)
    mat_b = read_mat_from_txt(filename_b)

    try:
        result_matrix = add_mats(mat_a, mat_b)
    except ValueError as e:
        print(e)
        return

    write_mat_to_txt(result_matrix, output_filename)

  

if __name__ == "__main__":
    main()


