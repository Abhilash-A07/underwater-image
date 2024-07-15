# Underwater Image Enhancement Using Deep Learning
Engineering Final year project
PROBLEM STATEMENT:
The sharpness and contrast of the images captured in underwater suffer from poor color contrast and poor visibility. Moreover, the quality of underwater images deteriorates due to the physical properties of the aquatic medium, light scattering, reflection, and becomes more and less visible as water depth increases. To overcome the problems we have planned to implement an efficient system using deep learning.

* ABSTRACT *
In recent years, signal and image processing based on fractional calculus has attracted extensive attention. Aiming at the serious problem of gray-scale loss in the existing pseudo color methods in high gray-scale image enhancement, a pseudo color enhancement algorithm suitable for Dynamic heterogeneous feature fusion neural network is proposed, and the traditional jet, HSV and rainbow coding are improved. Firstly, bit depth quantization is performed on the high-level gray image. Secondly, color enhancement is realized by using the constructed high gray-scale enhancement algorithm. Then, combined with the convolution neural network, the compact learning method is used to extract the features of the multi-scale image, and the jump connection is used to prevent the gradient dispersion and overcome the fog blur effect of the underwater image. The style cost function is used to learn the correlation between various channels of color image, improve the color correction ability of the model, and overcome the problem of color distortion of underwater image. The results show that compared with traditional image enhancement methods, the proposed method has better comprehensive performance in subjective vision and objective indicators, and has advantages in dealing with underwater image enhancement. While improving the brightness of the image, the problem of color distortion and brightness blocking of the enhanced image is solved. The texture information of the image is effectively restored. The brightness distribution of the enhanced image can well restore the brightness distribution of the real shooting environment, which verifies that the algorithm has higher robustness

* OBJECTIVES *
  To build an efficient model to reconstruct the underwater images without damage.
 	avoid the noise while reconstructing the underwater images.  	To improve accuracy of training model and reconstruction model.
 	To enhance image quality using deep learning model.
 	The goal of image enhancement is to improve the usefulness of an image for a given task such as providing a more subjectively pleasing image for human viewing.

* METHADOLOGY *
  System Architecture
![image](https://github.com/user-attachments/assets/cfb0c129-9527-4f24-a669-15e3dd9e9306)

* SYSTEM REQUIREMENTS AND SPECIFICATION *
  
  1 Functional Requirements
This section describes the functional requirements of the system for those requirements which are expressed in natural language style.
1.	Create a desktop application using Tkinter framework.
2.	User should load the dataset.
3.	Once user load dataset images system will preprocess.
4.	System will extract the image features and train the model using CNN.
5.	Save trained model in system.
6.	User loads a underwater image as input.
7.	System will preprocess and extract image features.
8.	System will automatically enhance image quality without missing data content.
9.	Application should efficiently improve underwater image quality using Deep learning algorithm.
2 Non-Functional Requirements
These are requirements that are not functional in nature, that is, these are constraints within which the system must work.
 	The program must be self-contained so that it can easily be moved from one Computer to another. It is assumed that network connection will be available on the computer on which the program resides.
 	Capacity, scalability, and availability:
The system shall always achieve 100 per cent availability.
The system shall be scalable to support additional clients and volunteers.
 	Maintainability:
The system should be optimized for supportability, or ease of maintenance as far as possible. This may be achieved through the use of documentation of coding standards Naming conventions, class libraries and abstraction.

HARDWARE REQUIREMENTS
  Processor Type	:lntel CoreTM 	 
  Speed	: 2.4 GHZ
  	  GB RAM
  Hard disk	 	   80 GB HDD
SOFTWARE REQUIREMENTS
  Operating System	   Windows 64-bit
  Technology	   Python
  IDE	   Python1DLE
  Tools	• Anaconda, Node JS, Etherium
  Python Version	   Python 3.7

* SYSTEM DESIGN *

![image](https://github.com/user-attachments/assets/830f416f-4dff-4387-a0b6-864defea0922)

* IMPLEMENATATION OF OUR PROJECT *

  6.1 Modules
We have split this project into following modules:
 	Data collection
 	Data Preprocess and feature Extraction
 	Building Training of Model
 	Image Enhancement
Data Collection:
In this module we are collecting the good quality images from kaggle.com which contains more than 1500 images in .jpg format with the various size.
Data Preprocess and Feature Extraction:
In this module we are passing raw dataset as input our system will resize the image into 256x256 size using the opencv then our system will extract the image features like color, texture, color format.
Pseudo Code:
Step 1: For 	to length of dataset
Step 1: For 	to 8
Step 2: Read j image from dataset
Step 3: Resize the image into 256x256
Step 4: Apply Wavelet Transform mechanism to transform the image to the numerical array
Step 5: Extract features of the image like color, texture, color pattern, End fo
Step 6: Combine features
Building Training of Model:
•	The proposed CNN has 5 types of layers which are shown in system architecture with 5 different colors.
•	Deep convolution neural network
•	Applied to learning the high-frequency part of image information.
•	It consists of four parts, including convolution layer for
•	Learning low-level features, which contains two convolution
•	Layers; improved dense blocks for learning high-level
•	Features including 12 IDBs; the fusion layer used to fuse the
•	Intensive features of learning; reconstructed blocks for generating
•	High frequency features, including an upper sampling
•	Layer and a convolution layer.
Pseudo Code:
Procedure Training()
Input: Image Dataset
Output: Trained model
Begin:
Stepl: Read the dataset
Step 2: Apply CNN model
Step3: Train using fit function
Step 4: Save trained model.
End
•	The proposed CNN has 5 types of layers which are shown in system architecture with 5 different colors.
•	Deep convolution neural network
•	Applied to learning the high-frequency part of image information.
•	It consists of four parts, including convolution layer for
•	Learning low-level features, which contains two convolution
•	Layers; improved dense blocks for learning high-level
•	Features including 12 IDBs; the fusion layer used to fuse the
•	Intensive features of learning; reconstructed blocks for generating
•	High frequency features, including an upper sampling
•	Layer and a convolution layer.
Pseudo Code:
Procedure Training()
Input: Image Dataset
Output: Trained model
Begin:
Stepl: Read the dataset
Step 2: Apply CNN model
Step3: Train using fit function
Step 4: Save trained model.
End
•	The proposed CNN has 5 types of layers which are shown in system architecture with 5 different colors.
•	Deep convolution neural network
•	Applied to learning the high-frequency part of image information.
•	It consists of four parts, including convolution layer for
•	Learning low-level features, which contains two convolution
•	Layers; improved dense blocks for learning high-level
•	Features including 12 IDBs; the fusion layer used to fuse the
•	Intensive features of learning; reconstructed blocks for generating
•	High frequency features, including an upper sampling
•	Layer and a convolution layer.
Pseudo Code:
Procedure Training()
Input: Image Dataset
Output: Trained model
Begin:
Stepl: Read the dataset
Step 2: Apply CNN model
Step3: Train using fit function
Step 4: Save trained model.
End

-----> PERFORMANCE ANALYSIS
![image](https://github.com/user-attachments/assets/4a808c01-e5cc-4c1d-811e-0f9d281978e7)

-------> OUTPUT --------
Home Page
![image](https://github.com/user-attachments/assets/4d829c5a-3e2e-4377-b6e0-1d58decceaf2)
Select image
![image](https://github.com/user-attachments/assets/ec39f1d7-9181-4a76-86b6-1deaf1bff3d4)
Enhanced Image
![image](https://github.com/user-attachments/assets/a3137d22-9754-41ba-bcd4-8219f0881e07)

CONCLUSION & FUTURE ENHANCEMENT
Conclusion:
Aiming at the problems of low illumination images, this project proposes a low illumination enhancement method based on attention mechanism, residual dense blocks and generation of counter measure. Firstly, the method uses to generate a global exposure attention map to guide the subsequent modules to enhance the illumination. Secondly, different levels of features extracted by CRM and cardm are fused to obtain more detailed information. A generative countermeasure network is proposed to transform the underwater image into the image of underwater environment as truly as possible. The result shows that the underwater image synthesized by the model can effectively train the underwater image enhancement model, and provides a new idea for expanding the underwater image data set. A novel underwater image enhancement model based on MWCNN and style cost function is proposed.
Future Enhancement:
Image Restoration Techniques: Explore advanced image restoration techniques specifically designed for underwater images. This can involve the removal of noise, correction of color distortion, and enhancement of fine details to improve the overall visual quality.





