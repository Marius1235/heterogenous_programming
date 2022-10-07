from PIL import Image
import numpy as np 


'''
The grayscale_converter function that applies the formula:

greyscale = 0.2989*R + 0.5870*G + 0.1140*B 

to the image array provided. 


inputs: 
    i. img_arr : a 2D array of an image with its r,g,b values next to each other
    shape: (512,1536)

    ii. arr_to_save : a 2D array to which we will write the result of the greyscale-conversion
    shape: (512,512) 

'''

def grayscale_converter(img_arr, arr_to_save):

    for i in range(512):
        for j in range(0,512):

            offset = j*3
            
            temp_array = img_arr[i][offset:offset+3]

            arr_to_save[i][j] = 0.2989*temp_array[0] + 0.5870*temp_array[1] + 0.1140*temp_array[2]

    return arr_to_save



'''
A solution that more closely resembles how we would go about solving this
problem if we had to use CUDA.
We are still only using numpy arrays here.
'''
def solution():
        
    image = Image.open("./lenna.png")

    # Lets take a look at the image using image.show()
    image.show()

    # Converting image to numpy arrays 
    arr = np.asarray(image)

    # The image has been transformed into 3D numpy arrays
    # The shape is : (512,512,3)
    # There are a total of 512x512 pixels in this image. 
    # Each pixel further has 3 values : the red-green-blue values.
    print(arr.shape)

    # We want to flatten these 3D arrays into 2D array so its easier to work with
    new_arr = arr.reshape(len(arr), -1)
    print(new_arr.shape)

    # The new shape is (512,1536). 512 * 3 = 1536 
    # The red-green-blue values are now placed next to each other

    # arr[0][0] and new_arr[0][:3] are the same
    # The array has been adequately flattened by one dimension 

    # We will create a 2D array of zero values which we will then write our result to
    
    # NOTE: This is not the most efficient way of solving this problem in numpy but this
    # is a more accurate reflection of how we allocate and write to arrays in CUDA.
    zeros = np.zeros((512,512))

    # We use the greyscale_converter function to 
    # transform the 2D array of size (512,1536) into size (512,512)
    # using the "luminosity method" : https://www.tutorialspoint.com/dip/grayscale_to_rgb_conversion.htm
    
    final_arr = grayscale_converter(new_arr, zeros)

    print(final_arr.shape)

    modified_img_new = Image.fromarray(final_arr)

    modified_img_new.show()


solution()





'''
The following solution shows the best way of converting to greyscale
Using numpy's built-in dot product method.
'''
def efficent_solution():        
    image = Image.open("./lenna.png")

    image.show()

    arr = np.asarray(image)

    def grayscale_converter(arr):
        return np.dot(arr[...,:3], [0.2989, 0.5870, 0.1140])

    new_arr = grayscale_converter(arr)

    modified_img = Image.fromarray(new_arr)

    modified_img.show()

efficent_solution()