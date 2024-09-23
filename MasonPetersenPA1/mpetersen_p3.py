
import numpy as np

# Could not get numpy to work, email was sent regarding this issue

def read_mat_from_txt(filename):
    

def add_mats(mat_a, mat_b):
    

def write_mat_to_txt(matrix, filename):
    
    

def main():
   

    
    mat_a_name = input("Enter the first matrix name (Mat1, Mat2, Mat3, Mat4): ")
    mat_b_name = input("Enter the second matrix name (Mat1, Mat2, Mat3, Mat4): ")

    filename_a = f"mpetersen_{mat_a_name.lower()}.txt"
    filename_b = f"mpetersen_{mat_b_name.lower()}.txt"
    output_filename = f"mpetersen_p3_outA{mat_a_name[-1]}{mat_b_name[-1]}.txt"

    
    mat_a = read_mat_from_txt(filename_a)
    mat_b = read_mat_from_txt(filename_b)

    
    result_matrix = add_mats(mat_a, mat_b)

    
    write_mat_to_txt(result_matrix, output_filename)
    

if __name__ == "__main__":
    main()

