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

        # TODO: Loop through each pixel 
            
            # TODO : find the correct "offset" to iterate over 3 values in a row at a time 

            # TODO: retrieve the 3 red, green and blue values related to a pixel             

            # TODO: Compute the grayscale value from the red,green and blue values 
            #       using the formula: 0.2989*R + 0.5870*G + 0.1140*B

            # TODO: Write this new value in the arr_to_save in the correct position
            
    return arr_to_save



'''
A solution that more closely resembles how we would go about solving this
problem if we had to use CUDA (which we will do in the next classes).
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

