import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


# Define a function to compute color histogram features  
# Pass the color_space flag as 3-letter all caps string
# like 'HSV' or 'LUV' etc.
# KEEP IN MIND IF YOU DECIDE TO USE THIS FUNCTION LATER
# IN YOUR PROJECT THAT IF YOU READ THE IMAGE WITH 
# cv2.imread() INSTEAD YOU START WITH BGR COLOR!
def bin_spatial(img, color_space='RGB', size=(32, 32)):
    colour_dict = { 'RGB':'RGB',
                    'BGR':cv2.COLOR_BGR2RGB,
                    'HLS':cv2.COLOR_BGR2HLS,
                    'HSV':cv2.COLOR_BGR2HSV,
                    'LUV':cv2.COLOR_BGR2LUV,
                    'YUV': cv2.COLOR_RGB2YUV,
                    'YCrCb': cv2.COLOR_RGB2YCrCb
                    }
    
    # If someother Colour Space
    if color_space.upper() != 'RGB':
        method = colour_dict.get(color_space, 'RGB')
        img = cv2.cvtColor(img, method)
    else:
        img = np.copy(img)

    small_img = cv2.resize(img, size)
    feature_vec = small_img.ravel()
    # Return the feature vector
    return feature_vec

if __name__ == "__main__":    
    # You can also read cutout2, 3, 4 etc. to see other examples
    image = mpimg.imread('cutout1.jpg')
    feature_vec = bin_spatial(image, color_space='HSV', size=(32, 32))

    # Plot features
    plt.plot(feature_vec)
    plt.title('Spatially Binned Features')


##
## Solution
##
# Define a function to compute color histogram features  
# Pass the color_space flag as 3-letter all caps string
# like 'HSV' or 'LUV' etc.
# def bin_spatial(img, color_space='RGB', size=(32, 32)):
#     # Convert image to new color space (if specified)
#     if color_space != 'RGB':
#         if color_space == 'HSV':
#             feature_image = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
#         elif color_space == 'LUV':
#             feature_image = cv2.cvtColor(img, cv2.COLOR_RGB2LUV)
#         elif color_space == 'HLS':
#             feature_image = cv2.cvtColor(img, cv2.COLOR_RGB2HLS)
#         elif color_space == 'YUV':
#             feature_image = cv2.cvtColor(img, cv2.COLOR_RGB2YUV)
#         elif color_space == 'YCrCb':
#             feature_image = cv2.cvtColor(img, cv2.COLOR_RGB2YCrCb)
#     else: feature_image = np.copy(img)             
#     # Use cv2.resize().ravel() to create the feature vector
#     features = cv2.resize(feature_image, size).ravel() 
#     # Return the feature vector
#     return features