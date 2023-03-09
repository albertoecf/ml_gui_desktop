## Image Classifier

This is a desktop application that utilizes a Convolutional Neural Network (CNN) to classify images into defined categories. In this example, we are categorizing images of hamburgers and boxes.

The main libraries used in this project are Tkinter (for building the GUI), Keras (for building and training the CNN), and Scikit-learn (for data preprocessing and model evaluation).

The CNN model was trained on a dataset of images of hamburgers and boxes, and achieved high accuracy in distinguishing between the two classes

## Use case

This application can be used in various scenarios such as in online orders where the user orders a product and receives a different product than what was specified. This implementation may not seem very useful (who would be interested in distinguishing a box from a hamburger?). But it builds the architecture for more sophisticated implementations.

## Features

This application allows users to:
* Load an image from their computer system
* View the image
* Rate the image


## Dependencies
The main libraries used in this project are:

* Tkinter
* Keras
* scikit-learn

### Running the application

To run the application, simply run the gui_image_classifier.py file. This will launch a GUI where users can upload their images and classify them

## Example 

Instantiate desktop app

<img width="368" alt="Captura de pantalla 2022-12-31 a las 11 32 34" src="https://user-images.githubusercontent.com/81099969/210133565-720f041d-02bf-4fc5-83ce-580873e7c5e7.png">

Upload local image : 

<img width="1209" alt="Captura de pantalla 2022-12-31 a las 11 34 37" src="https://user-images.githubusercontent.com/81099969/210133603-e46a6821-bce2-438c-a040-a39810312673.png">

Run and Predict class : 

<img width="574" alt="Captura de pantalla 2022-12-31 a las 11 35 09" src="https://user-images.githubusercontent.com/81099969/210133611-9d523c9a-96ef-423d-8a47-753e4e1895c7.png">
